#!/usr/bin/env python3
"""
RAG Indexer - Indexes all .md files in the repo.
Generates 3 indices: tag, full-text, relationship graph.
No external dependencies - only Python standard library.

Usage: python3 scripts/rag-index.py
Output: system/rag/tag-index.json, text-index.json, graph.json, summary.md
"""

import os
import json
import re
import sys
from pathlib import Path
from collections import defaultdict
from datetime import datetime

# Config
REPO_ROOT = Path(__file__).resolve().parent.parent
INDEX_DIR = REPO_ROOT / "system" / "rag"
EXCLUDED_DIRS = {
    ".git", ".obsidian", "node_modules", ".env", ".venv", "venv",
    "system/rag", ".claude", ".vscode", ".github",
}
EXCLUDED_FILES = {"README.md"}


def parse_frontmatter(content):
    """Extract YAML frontmatter from markdown content. Minimal parser, no dependencies."""
    if not content.startswith("---"):
        return {}, content

    end = content.find("\n---", 3)
    if end == -1:
        return {}, content

    fm_text = content[3:end].strip()
    body = content[end + 4:].strip()

    fm = {}
    current_key = None
    current_list = None
    current_dict = None
    current_dict_key = None

    for raw_line in fm_text.split("\n"):
        line = raw_line.rstrip()
        if not line or line.lstrip().startswith("#"):
            continue

        # Nested dict list item: "  - value" under a dict key
        if line.startswith("  - ") and current_key and current_dict is None:
            if current_list is None:
                current_list = []
                fm[current_key] = current_list
            current_list.append(line[4:].strip().strip("'\""))
            continue

        # Dict nested key: "  key: [values]" or "  key: value"
        if line.startswith("  ") and not line.startswith("  - ") and current_key and isinstance(fm.get(current_key), dict):
            sub = line.strip()
            if ":" in sub:
                k, _, v = sub.partition(":")
                k = k.strip()
                v = v.strip()
                if v.startswith("[") and v.endswith("]"):
                    fm[current_key][k] = [x.strip().strip("'\"") for x in v[1:-1].split(",") if x.strip()]
                elif v:
                    fm[current_key][k] = v.strip("'\"")
                else:
                    fm[current_key][k] = None
            continue

        # Top-level "key:" with nothing after (next lines are list or dict)
        if ":" in line and not line.startswith(" "):
            key, _, value = line.partition(":")
            key = key.strip()
            value = value.strip()
            current_key = key
            current_list = None
            current_dict = None

            if value:
                if value.startswith("[") and value.endswith("]"):
                    fm[key] = [v.strip().strip("'\"") for v in value[1:-1].split(",") if v.strip()]
                else:
                    fm[key] = value.strip("'\"")
            else:
                # Could be list or dict - peek next lines via placeholder
                fm[key] = {}  # assume dict; if we hit list items, convert

    return fm, body


def extract_wikilinks(content):
    """Extract [[wikilinks]] from content."""
    return re.findall(r'\[\[([^\]]+)\]\]', content)


# Stopwords (Italian + English basics)
STOPWORDS = {
    'il', 'lo', 'la', 'le', 'gli', 'un', 'una', 'uno', 'di', 'da', 'in', 'a',
    'con', 'su', 'per', 'tra', 'fra', 'del', 'della', 'delle', 'dei', 'degli',
    'al', 'alla', 'alle', 'ai', 'nel', 'nella', 'nelle', 'nei', 'che', 'non',
    'come', 'sono', 'essere', 'questo', 'questa', 'questi', 'queste', 'anche',
    'piu', 'ogni', 'solo', 'puo', 'deve', 'fatto', 'fare', 'quando', 'dove',
    'cosa', 'quale', 'quali', 'tutto', 'tutti', 'molto', 'sempre', 'prima',
    'dopo', 'perche', 'senza', 'proprio', 'altro', 'altri',
    'the', 'an', 'is', 'are', 'was', 'were', 'be', 'been', 'being',
    'have', 'has', 'had', 'does', 'did', 'will', 'would', 'could',
    'should', 'may', 'might', 'must', 'shall', 'can', 'need',
    'to', 'of', 'for', 'on', 'with', 'at', 'by', 'from', 'as',
    'into', 'through', 'during', 'before', 'after', 'above', 'below',
    'and', 'but', 'or', 'nor', 'not', 'so', 'yet', 'both', 'either',
    'this', 'that', 'these', 'those', 'what', 'which', 'who', 'whom',
    'here', 'there', 'then', 'than', 'just', 'also', 'some', 'any',
    'all', 'each', 'every', 'other', 'such', 'only', 'own', 'same',
    'about', 'against', 'between', 'up', 'down', 'out', 'off', 'over',
    'under', 'again', 'further', 'once', 'more', 'most', 'very',
}


def extract_keywords(text, min_length=4, top_n=30):
    """Extract significant keywords from text."""
    # Strip markdown syntax
    text = re.sub(r'```[\s\S]*?```', ' ', text)  # code blocks
    text = re.sub(r'`[^`]*`', ' ', text)  # inline code
    text = re.sub(r'https?://\S+', ' ', text)  # URLs
    text = re.sub(r'[#*_`\[\](){}|><=+\-/\\:;,.!?"\']', ' ', text)

    words = text.lower().split()
    keywords = [w for w in words if len(w) >= min_length and w not in STOPWORDS and w.replace("-", "").isalpha()]

    freq = defaultdict(int)
    for w in keywords:
        freq[w] += 1

    return dict(sorted(freq.items(), key=lambda x: -x[1])[:top_n])


def is_excluded(rel_path):
    """Check if a relative path should be excluded."""
    parts = rel_path.replace("\\", "/").split("/")
    for exc in EXCLUDED_DIRS:
        exc_parts = exc.split("/")
        if len(parts) >= len(exc_parts) and parts[:len(exc_parts)] == exc_parts:
            return True
        if exc in parts:
            return True
    return False


def scan_files():
    """Scan all .md files in the repo."""
    files = []
    for root, dirs, filenames in os.walk(REPO_ROOT):
        # Prune excluded dirs
        dirs[:] = [d for d in dirs if not d.startswith(".") or d in (".agents", ".skills", ".workflows")]
        dirs[:] = [d for d in dirs if d not in {"node_modules", "venv", ".venv"}]

        rel_root = os.path.relpath(root, REPO_ROOT)
        if rel_root != "." and is_excluded(rel_root):
            continue

        for fname in filenames:
            if not fname.endswith(".md") or fname in EXCLUDED_FILES:
                continue

            filepath = os.path.join(root, fname)
            rel_path = os.path.relpath(filepath, REPO_ROOT)

            if is_excluded(rel_path):
                continue

            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
            except Exception:
                continue

            frontmatter, body = parse_frontmatter(content)
            wikilinks = extract_wikilinks(content)
            keywords = extract_keywords(body)

            stat = os.stat(filepath)

            files.append({
                "path": rel_path.replace("\\", "/"),
                "frontmatter": frontmatter,
                "wikilinks": wikilinks,
                "keywords": keywords,
                "size": stat.st_size,
                "modified": datetime.fromtimestamp(stat.st_mtime).isoformat(),
                "word_count": len(body.split()),
            })

    return files


def build_tag_index(files):
    """Build tag index."""
    index = defaultdict(list)

    for f in files:
        fm = f["frontmatter"]

        tags = fm.get("tags", [])
        if isinstance(tags, str):
            tags = [tags]
        if isinstance(tags, list):
            for tag in tags:
                if isinstance(tag, str):
                    t = tag.lower().strip()
                    if t:
                        index[t].append(f["path"])

        ftype = fm.get("type", "")
        if isinstance(ftype, str) and ftype:
            index[f"type:{ftype.lower()}"].append(f["path"])

        fstatus = fm.get("status", "")
        if isinstance(fstatus, str) and fstatus:
            index[f"status:{fstatus.lower()}"].append(f["path"])

        author = fm.get("author", "")
        if isinstance(author, str) and author:
            index[f"author:{author.lower()}"].append(f["path"])

        entities = fm.get("entities", {})
        if isinstance(entities, dict):
            for entity_type, entity_list in entities.items():
                if isinstance(entity_list, list):
                    for entity in entity_list:
                        if isinstance(entity, str):
                            index[f"entity:{entity.lower()}"].append(f["path"])

    return dict(index)


def build_text_index(files):
    """Build full-text keyword index."""
    index = defaultdict(list)

    for f in files:
        for keyword, count in f["keywords"].items():
            index[keyword].append({"path": f["path"], "count": count})

    for keyword in index:
        index[keyword].sort(key=lambda x: -x["count"])

    return dict(index)


def build_graph(files):
    """Build relationship graph."""
    nodes = {}
    edges = []

    # Map filename (without ext) -> path for wikilink resolution
    name_to_path = {}
    for f in files:
        name = os.path.splitext(os.path.basename(f["path"]))[0].lower()
        name_to_path[name] = f["path"]

    for f in files:
        path = f["path"]
        fm = f["frontmatter"]
        nodes[path] = {
            "type": fm.get("type", "unknown") if isinstance(fm.get("type"), str) else "unknown",
            "tags": fm.get("tags", []) if isinstance(fm.get("tags"), list) else [],
            "status": fm.get("status", "") if isinstance(fm.get("status"), str) else "",
            "word_count": f["word_count"],
            "modified": f["modified"],
        }

        # Explicit relations from frontmatter
        related = fm.get("related", [])
        if isinstance(related, list):
            for rel in related:
                if isinstance(rel, str):
                    edges.append({"from": path, "to": rel, "type": "related"})

        # Relations from wikilinks
        for link in f["wikilinks"]:
            target = name_to_path.get(link.lower())
            if target and target != path:
                edges.append({"from": path, "to": target, "type": "wikilink"})

    return {"nodes": nodes, "edges": edges}


def main():
    print("RAG Indexer - indexing repository...")

    INDEX_DIR.mkdir(parents=True, exist_ok=True)

    files = scan_files()
    print(f"  Found {len(files)} .md files")

    tag_index = build_tag_index(files)
    print(f"  Tag index: {len(tag_index)} unique tags")

    text_index = build_text_index(files)
    print(f"  Text index: {len(text_index)} unique keywords")

    graph = build_graph(files)
    print(f"  Graph: {len(graph['nodes'])} nodes, {len(graph['edges'])} edges")

    with open(INDEX_DIR / "tag-index.json", "w", encoding="utf-8") as f:
        json.dump(tag_index, f, indent=2, ensure_ascii=False)

    with open(INDEX_DIR / "text-index.json", "w", encoding="utf-8") as f:
        json.dump(text_index, f, indent=2, ensure_ascii=False)

    with open(INDEX_DIR / "graph.json", "w", encoding="utf-8") as f:
        json.dump(graph, f, indent=2, ensure_ascii=False)

    # Human-readable summary
    top_tags = sorted(
        [(k, v) for k, v in tag_index.items() if not k.startswith(("type:", "status:", "author:", "entity:"))],
        key=lambda x: -len(x[1])
    )[:20]
    by_type = sorted(
        [(k, v) for k, v in tag_index.items() if k.startswith("type:")],
        key=lambda x: -len(x[1])
    )
    by_status = sorted(
        [(k, v) for k, v in tag_index.items() if k.startswith("status:")],
        key=lambda x: -len(x[1])
    )

    summary = f"""# RAG Index Summary

**Last updated**: {datetime.now().isoformat()}
**Indexed files**: {len(files)}
**Unique tags**: {len([k for k in tag_index if not k.startswith(("type:", "status:", "author:", "entity:"))])}
**Unique keywords**: {len(text_index)}
**Graph edges**: {len(graph['edges'])}

## Top Tags
{chr(10).join(f'- `{tag}`: {len(paths)} files' for tag, paths in top_tags) or '- (none)'}

## Files by type
{chr(10).join(f'- `{tag.replace("type:", "")}`: {len(paths)} files' for tag, paths in by_type) or '- (none)'}

## Files by status
{chr(10).join(f'- `{tag.replace("status:", "")}`: {len(paths)} files' for tag, paths in by_status) or '- (none)'}
"""

    with open(INDEX_DIR / "summary.md", "w", encoding="utf-8") as f:
        f.write(summary)

    print(f"\nIndexing complete. Indices saved in {INDEX_DIR}/")


if __name__ == "__main__":
    main()
