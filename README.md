# 🏢 founder-os

> Run your B2B SaaS startup like code. An agentic operating system you run inside [Claude Code](https://claude.com/claude-code).
>
> Gestisci la tua startup B2B SaaS come se fosse codice. Un sistema operativo agentico che vive dentro Claude Code.

---

## 🇬🇧 English

**founder-os** turns your repository into the single source of truth for your company. Instead of scattered docs, you get a team of AI agents — CEO, Product, CTO, Marketing, Sales, CFO, HR, Legal, Chief of Staff — that read shared company context, execute structured commands, write traceable outputs, and commit them to git.

Everything is plain Markdown. Every action produces a file. Every file is versioned.

### Quick Start

1. **Clone** this repo and open it in [Claude Code](https://claude.com/claude-code) (CLI, desktop, or IDE extension).
2. Run the setup wizard:
   ```
   /setup
   ```
   It asks ~10 questions and fills in your company identity, team, vision, segments, roadmap, KPIs, and routine cadence — one step at a time.
3. Start working:
   ```
   /routine start        # your guided daily/weekly session
   /pm write-spec        # invoke the Product Manager
   /sales pipeline-review # invoke Sales
   ```

> Not sure what good looks like? See [`examples/acme-demo/`](examples/acme-demo/) — a fully filled-in fictional company you can read or copy from.

### What's inside

| Layer | What |
|-------|------|
| **10 agents** (`.agents/`) | CEO, Product Manager, CTO, Marketing, Sales, Chief of Staff, CFO, HR, Legal, + a CEO Routine "entry point". Each has a persona, commands, and templates. |
| **~28 skills** (`.skills/`) | Reusable competencies: pricing, B2B SaaS playbook, presentations, writing, compliance, plus optional integrations (ClickUp, Gmail, Fatture in Cloud). |
| **5 workflows** (`.workflows/`) | Multi-agent processes: feature lifecycle, product launch, quarterly planning, incident response, customer escalation. |
| **System protocols** (`system/`) | Spec lifecycle, persistent memory, wiki, learnings, changelog, privacy tiers. |
| **Company state** (`company/`) | Your live data: strategy, product, metrics, customers, finance, compliance. Starts as templates. |

### How it works

```
You: "/pm write-spec"
  → Claude reads .agents/product-manager/AGENT.md and becomes the PM
  → loads shared context (.agents/_shared/) + relevant company/ data
  → executes the command, writes output to the right folder
  → commits:  [pm] spec: <description>
```

The rules that govern all of this live in [`CLAUDE.md`](CLAUDE.md).

### License
MIT — see [`LICENSE`](LICENSE). Use it, fork it, make it yours.

---

## 🇮🇹 Italiano

**founder-os** trasforma il tuo repository nel single source of truth dell'azienda. Al posto di documenti sparsi, hai un team di agenti AI — CEO, Product, CTO, Marketing, Sales, CFO, HR, Legal, Chief of Staff — che leggono il contesto condiviso, eseguono comandi strutturati, producono output tracciabili e li committano su git.

Tutto è Markdown. Ogni azione genera un file. Ogni file è versionato.

### Avvio rapido

1. **Clona** questo repo e aprilo in [Claude Code](https://claude.com/claude-code).
2. Lancia il wizard di setup:
   ```
   /setup
   ```
   Ti fa ~10 domande e compila identità azienda, team, vision, segmenti, roadmap, KPI e cadenza — un passo alla volta.
3. Inizia a lavorare:
   ```
   /routine start         # la tua sessione guidata
   /pm write-spec         # invoca il Product Manager
   /sales pipeline-review # invoca Sales
   ```

> Vuoi vedere un esempio già compilato? Guarda [`examples/acme-demo/`](examples/acme-demo/).

### Primi file (se preferisci compilare a mano invece di `/setup`)

1. ⭐ `.agents/_shared/COMPANY.md` — Chi sei
2. ⭐ `company/strategy/vision.md` — Dove vai
3. `.agents/_shared/TEAM.md` — Il team
4. `company/customers/segments.md` — Per chi lavori
5. `company/metrics/kpis.md` — Come stai andando

### Licenza
MIT — vedi [`LICENSE`](LICENSE).

---

<sub>Built with Claude Code. Originally extracted and fully anonymized from a real seed-stage B2B SaaS operating system.</sub>
