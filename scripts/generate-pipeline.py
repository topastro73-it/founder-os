#!/usr/bin/env python3
"""
generate-pipeline.py — genera il cockpit commerciale (PIPELINE.md) dalle opportunità.

Legge:  {base}/pipeline-config.yaml  +  {base}/opportunities/*.md
Scrive: {base}/PIPELINE.md

Uso:
    python scripts/generate-pipeline.py                  # base = company/customers
    python scripts/generate-pipeline.py --base examples/acme-demo/customers
    python scripts/generate-pipeline.py --date 2026-06-05   # data di riferimento per l'aging (default: oggi)

Nessuna dipendenza esterna richiesta (parser YAML minimale incorporato; usa PyYAML se presente).
Metodologia: .skills/opportunity-management/SKILL.md
"""
import argparse, datetime, glob, os, re, sys

# ---------- config ----------
DEFAULTS = {
    "currency_symbol": "€",
    "weighted_target": 500000,
    "stages": {"discovery": 20, "technical-alignment": 30, "proposal-sent": 40,
               "negotiation": 60, "contract-sent": 80, "won": 100, "lost": 0},
    "segments": {},
    "aging": {"attention_days": 7, "warning_days": 14, "critical_days": 21},
}

def load_config(path):
    cfg = {k: (v.copy() if isinstance(v, dict) else v) for k, v in DEFAULTS.items()}
    if not os.path.exists(path):
        return cfg
    text = open(path, encoding="utf-8").read()
    try:
        import yaml  # optional
        data = yaml.safe_load(text) or {}
    except Exception:
        data = _mini_yaml(text)
    for k, v in (data or {}).items():
        if isinstance(v, dict) and isinstance(cfg.get(k), dict):
            cfg[k].update(v)
        else:
            cfg[k] = v
    return cfg

def _mini_yaml(text):
    """Parser minimale: scalari top-level + dict annidati a 2 spazi (key: value)."""
    out, cur = {}, None
    for raw in text.splitlines():
        line = raw.split("#", 1)[0].rstrip()
        if not line.strip():
            continue
        if re.match(r"^[^\s].*:\s*$", line):          # "key:" -> nested dict
            cur = line.strip()[:-1]; out[cur] = {}
        elif re.match(r"^[^\s].*:", line):             # "key: value" top level
            k, v = line.split(":", 1); out[k.strip()] = _val(v.strip()); cur = None
        elif re.match(r"^\s+\S", line) and cur:        # nested "  key: value"
            k, v = line.strip().split(":", 1); out[cur][k.strip()] = _val(v.strip())
    return out

def _val(s):
    s = s.strip().strip('"').strip("'")
    if re.fullmatch(r"-?\d+", s): return int(s)
    return s

# ---------- frontmatter ----------
def parse_fm(path):
    t = open(path, encoding="utf-8").read()
    m = re.search(r"^---\n(.*?)\n---", t, re.S)
    if not m: return None
    body = m.group(1); d = {}
    for line in body.splitlines():
        mm = re.match(r"^([a-z0-9\-]+):\s*(.*)$", line)
        if mm:
            d[mm.group(1)] = mm.group(2).split("#")[0].strip().strip('"').strip()
    d["_high"] = bool(re.search(r'severity:\s*"?high', body))
    d["_file"] = os.path.basename(path)
    return d

def num(x):
    try: return float(x)
    except (TypeError, ValueError): return 0.0

# ---------- aging ----------
def days_between(ref, ds):
    try:
        y, m, dd = map(int, ds.split("-")[:3])
        return (ref - datetime.date(y, m, dd)).days
    except Exception:
        return None

def aging(o, ref, th):
    if o.get("stage") in ("won", "lost"): return None
    g = days_between(ref, o.get("last-activity", ""))
    nsd = days_between(ref, o.get("next-step-due", ""))
    blocked = o.get("status-flag") == "blocked"
    A, W, C = th["attention_days"], th["warning_days"], th["critical_days"]
    crit = (g is not None and g >= C) or o["_high"] or (nsd is not None and nsd > W)
    warn = (g is not None and W <= g < C) or (nsd is not None and A < nsd <= W) or (blocked and g is not None and g > A)
    att = (g is not None and A <= g < W) or (nsd is not None and 0 < nsd <= A)
    return "🔴" if crit else ("🟠" if warn else ("🟡" if att else "🟢"))

# ---------- render ----------
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", default="company/customers")
    ap.add_argument("--date", default=None, help="YYYY-MM-DD (default: oggi)")
    args = ap.parse_args()
    ref = datetime.date.today() if not args.date else datetime.date(*map(int, args.date.split("-")))
    cfg = load_config(os.path.join(args.base, "pipeline-config.yaml"))
    cur = cfg["currency_symbol"]; target = cfg["weighted_target"]
    seglbl = cfg["segments"]; th = cfg["aging"]
    stage_order = [s for s in cfg["stages"] if s not in ("won", "lost")]
    money = lambda n: cur + format(int(round(n)), ",d").replace(",", ".")

    files = [f for f in glob.glob(os.path.join(args.base, "opportunities", "*.md")) if not f.endswith("TEMPLATE.md")]
    opps = [o for o in (parse_fm(f) for f in files) if o]
    openo = [o for o in opps if o.get("stage") not in ("won", "lost")]
    won = [o for o in opps if o.get("stage") == "won"]
    gross = sum(num(o.get("value-gross")) for o in openo)
    weighted = sum(num(o.get("value-weighted")) for o in openo)
    fas = {"🔴": 0, "🟠": 0, "🟡": 0, "🟢": 0}
    for o in openo:
        a = aging(o, ref, th)
        if a: fas[a] += 1
    L = lambda o: f"[{o['_file'][:-3]}](opportunities/{o['_file']})"
    owner = lambda o: o.get("owner-sales") or "— (no owner)"
    sl = lambda o: seglbl.get(o.get("segment", ""), o.get("segment", "") or "—")
    cov = round(weighted / target * 100) if target else 0
    rank = {"🔴": 0, "🟠": 1, "🟡": 2, "🟢": 3}
    rows = sorted(openo, key=lambda o: (rank.get(aging(o, ref, th), 9),
                                        -(days_between(ref, o.get("last-activity", "")) or 0)))

    out = []
    out.append("<!-- COCKPIT generato da scripts/generate-pipeline.py. Snapshot; verità nel frontmatter opportunità. Tier 🟡 INTERNAL. -->\n")
    out.append("# 📊 Pipeline — Cockpit Commerciale\n")
    out.append(f"> Rigenerato **{ref.isoformat()}** · Fonte `{args.base}/opportunities/*.md` (repo = source of truth) · Target weighted {money(target)}\n")
    out.append("## Summary\n\n| | |\n|---|---|")
    out.append(f"| Opportunità aperte | **{len(openo)}** |")
    out.append(f"| Valore lordo (open) | **{money(gross)}** |")
    out.append(f"| Valore weighted (open) | **{money(weighted)}** |")
    out.append(f"| Coverage vs target | **{cov}%** |")
    out.append(f"| 🔴 / 🟠 / 🟡 / 🟢 | **{fas['🔴']} / {fas['🟠']} / {fas['🟡']} / {fas['🟢']}** |")
    out.append(f"| Vinte (won) tracciate | {len(won)} |\n")

    segs = [s for s in seglbl] + [s for s in {o.get("segment", "") for o in openo} if s and s not in seglbl]
    if any(o.get("segment") for o in openo):
        out.append("## Per segmento (open)\n\n| Segmento | Deal | Lordo | Weighted | 🔴 |\n|----------|------|-------|----------|----|")
        for s in segs:
            g = [x for x in openo if x.get("segment") == s]
            if g:
                out.append(f"| {seglbl.get(s, s)} | {len(g)} | {money(sum(num(x.get('value-gross')) for x in g))} | "
                           f"{money(sum(num(x.get('value-weighted')) for x in g))} | {sum(1 for x in g if aging(x, ref, th)=='🔴')} |")
        out.append("")

    out.append("## 🔴🟠🟡 Bloccati & Aging — *la vista del Direttore Commerciale*\n")
    out.append("| Fascia | Opportunità | Segmento | Account | Stage | Valore (w) | Owner | Giorni | Next step |")
    out.append("|--------|-------------|----------|---------|-------|-----------|-------|--------|-----------|")
    for o in rows:
        a = aging(o, ref, th)
        if a in ("🔴", "🟠", "🟡"):
            w = num(o.get("value-weighted")); wv = money(w) if w else f"{cur} —"
            g = days_between(ref, o.get("last-activity", "")); ns = (o.get("next-step", "") or "")[:48]
            out.append(f"| {a} | {L(o)} | {sl(o)} | {o.get('account','')} | {o.get('stage','')} | {wv} | {owner(o)} | "
                       f"{g if g is not None else '—'} | {ns} |")
    greens = [o for o in rows if aging(o, ref, th) == "🟢"]
    if greens:
        out.append("\n*🟢 In movimento:* " + ", ".join(f"{L(o)} ({sl(o)})" for o in greens))

    out.append("\n## Per owner (open)\n\n| Owner | Deal | Weighted | 🔴 |\n|-------|------|----------|----|")
    byo = {}
    for o in openo:
        k = owner(o); byo.setdefault(k, [0, 0.0, 0]); byo[k][0] += 1; byo[k][1] += num(o.get("value-weighted"))
        if aging(o, ref, th) == "🔴": byo[k][2] += 1
    for k, v in sorted(byo.items(), key=lambda x: -x[1][1]):
        out.append(f"| {k} | {v[0]} | {money(v[1])} | {v[2]} |")

    out.append("\n## Per stage (open)\n")
    for sid in stage_order:
        g = [x for x in openo if x.get("stage") == sid]
        if g:
            out.append(f"- **{sid}** ({cfg['stages'][sid]}%): {len(g)} deal · weighted "
                       f"{money(sum(num(x.get('value-weighted')) for x in g))}")
    if won:
        out.append("\n## Won tracciati\n" + ", ".join(f"{L(o)} ({money(num(o.get('value-gross')))})" for o in won))
    out.append("\n\n*Drill-down: file opportunità o `/sales opportunity {slug}`. Funnel di prospecting: `target-funnel.md`.*\n")

    dest = os.path.join(args.base, "PIPELINE.md")
    open(dest, "w", encoding="utf-8").write("\n".join(out))
    print(f"OK → {dest} | open {len(openo)} | gross {money(gross)} | weighted {money(weighted)} | "
          f"coverage {cov}% | fasce {fas} | won {len(won)}")
    if weighted > gross:
        print("⚠️  weighted > gross: controlla i value-gross (forse mancano o hanno commenti inline non numerici).", file=sys.stderr)

if __name__ == "__main__":
    main()
