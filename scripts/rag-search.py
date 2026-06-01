#!/usr/bin/env python3
"""
RAG Search - Search the indexed files.
No external dependencies.

Usage:
  python3 scripts/rag-search.py "partner pricing"        # keyword search
  python3 scripts/rag-search.py --tag NIS2               # search by tag
  python3 scripts/rag-search.py --related product/specs/prd-bulk-import.md
  python3 scripts/rag-search.py --context "billing partner"  # combined context search
  python3 scripts/rag-search.py --json ...               # JSON output
"""

import json
import sys
import argparse
from pathlib import Path
from collections import defaultdict

REPO_ROOT = Path(__file__).resolve().parent.parent
INDEX_DIR = REPO_ROOT / "system" / "rag"


def load_indices():
    """Load the JSON indices."""
    indices = {}
    for name in ["tag-index", "text-index", "graph"]:
        path = INDEX_DIR / f"{name}.json"
        if path.exists():
            with open(path, encoding="utf-8") as f:
                indices[name] = json.load(f)
        else:
            indices[name] = {}
    return indices


def search_tags(tag_index, query):
    """Search by tag (substring match)."""
    results = []
    query_lower = query.lower().strip()

    for tag, paths in tag_index.items():
        if query_lower in tag.lower():
            for path in paths:
                results.append({"path": path, "match": f"tag:{tag}", "score": 10})

    return results


def search_text(text_index, query):
    """Search by keyword in the text index."""
    results = defaultdict(lambda: {"score": 0, "matches": []})
    query_words = [w for w in query.lower().split() if w]

    for word in query_words:
        for keyword, entries in text_index.items():
            if word == keyword or (len(word) >= 4 and word in keyword) or (len(keyword) >= 4 and keyword in word):
                for entry in entries:
                    path = entry["path"]
                    weight = 3 if word == keyword else 1
                    results[path]["score"] += entry["count"] * weight
                    results[path]["matches"].append(keyword)

    return [
        {"path": path, "match": ", ".join(sorted(set(info["matches"]))[:5]), "score": info["score"]}
        for path, info in results.items()
    ]


def search_related(graph, file_path):
    """Find related files in the graph."""
    results = []

    if not graph.get("edges"):
        return results

    seen = set()
    for edge in graph["edges"]:
        if edge["from"] == file_path and edge["to"] not in seen:
            results.append({"path": edge["to"], "match": f"related ({edge['type']})", "score": 8})
            seen.add(edge["to"])
        elif edge["to"] == file_path and edge["from"] not in seen:
            results.append({"path": edge["from"], "match": f"related ({edge['type']})", "score": 8})
            seen.add(edge["from"])

    return results


def search_entities(tag_index, query):
    """Search by entity (partner, feature, framework)."""
    results = []
    query_lower = query.lower()

    for tag, paths in tag_index.items():
        if tag.startswith("entity:") and query_lower in tag:
            for path in paths:
                results.append({"path": path, "match": tag, "score": 12})

    return results


def context_search(indices, query):
    """Combined search: tags + text + entities. Returns most relevant files."""
    all_results = []

    all_results.extend(search_tags(indices["tag-index"], query))
    all_results.extend(search_text(indices["text-index"], query))
    all_results.extend(search_entities(indices["tag-index"], query))

    # Aggregate by file (sum scores)
    by_file = defaultdict(lambda: {"score": 0, "matches": set()})
    for r in all_results:
        by_file[r["path"]]["score"] += r["score"]
        by_file[r["path"]]["matches"].add(r["match"])

    sorted_results = sorted(by_file.items(), key=lambda x: -x[1]["score"])[:10]

    return [
        {"path": path, "score": info["score"], "matches": sorted(list(info["matches"]))}
        for path, info in sorted_results
    ]


def format_results(results, json_output=False):
    """Format results for output."""
    if json_output:
        print(json.dumps(results, indent=2, ensure_ascii=False))
        return

    if not results:
        print("No results found.")
        return

    print(f"\nFound {len(results)} relevant files:\n")
    for i, r in enumerate(results, 1):
        matches = r.get("matches")
        if isinstance(matches, list):
            match_str = ", ".join(matches[:5])
        else:
            match_str = r.get("match", "")
        print(f"  {i}. {r['path']}")
        print(f"     Score: {r['score']} | Match: {match_str}")
    print()


def main():
    parser = argparse.ArgumentParser(description="RAG Search - search the indexed repo")
    parser.add_argument("query", nargs="*", help="Text to search for")
    parser.add_argument("--tag", help="Search by specific tag")
    parser.add_argument("--related", help="Find files related to a specific file")
    parser.add_argument("--context", help="Combined context search (tags + text + entities)")
    parser.add_argument("--json", action="store_true", help="JSON output")

    args = parser.parse_args()

    if not (INDEX_DIR / "tag-index.json").exists():
        print("Indices not found. Run first: python3 scripts/rag-index.py", file=sys.stderr)
        sys.exit(1)

    indices = load_indices()

    if args.tag:
        results = search_tags(indices["tag-index"], args.tag)
        format_results(results, args.json)
    elif args.related:
        results = search_related(indices["graph"], args.related)
        format_results(results, args.json)
    elif args.context:
        results = context_search(indices, args.context)
        format_results(results, args.json)
    elif args.query:
        query = " ".join(args.query)
        results = context_search(indices, query)
        format_results(results, args.json)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
