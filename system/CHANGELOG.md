# founder-os Changelog

Registro di tutte le modifiche significative all'architettura, alle logiche e alle regole del sistema founder-os.

**Formato versioni:**
- `MAJOR` — breaking change (agent rimosso, regola incompatibile, ristrutturazione del sistema)
- `MINOR` — nuova funzionalità (nuovo agent, nuova skill, nuova regola, nuovo workflow)
- `PATCH` — correzione o aggiornamento minore (fix command, typo in regola critica, aggiustamento behavior)

**Come si aggiorna**: vedi `.skills/system-admin/SKILL.md` — comando `/system changelog`.
**Come si crea un checkpoint**: `/system checkpoint` — crea git tag + entry in questo file.
**Come si fa rollback**: `/system rollback <versione>` — ripristina solo i file di sistema.

---

## v1.1.3 — 2026-06-21 — Guardrail anti-deriva learnings (close + start)

### feat | detector candidati learning non promossi (close Step 0.3.E + start Step 3b) | .agents/ceo-routine/commands/close.md, .agents/ceo-routine/commands/start.md, system/protocols/learnings.md
**What**: Guardrail bidirezionale. **Al close** (Phase 0, Step 0.3.E + blocco recap Step 0.4) e **allo start**
(Step 3b): scansiona le wiki-session degli ultimi 30 giorni, estrae i candidati nelle sezioni
`## Learnings proposed` / `## Proposed learning (candidate)` e li ri-flagga al CEO finché non sono **promossi** a
`LRN-XXX` o esplicitamente scartati (`→ scartato {data}`). Documentato in `system/protocols/learnings.md`
(sezione "Guardrail anti-deriva").
**Why**: la proposta di un candidato da sola non lo "consuma"; se la promozione viene saltata ai close i learning
restano sepolti nelle wiki e `learnings.md` smette di crescere pur in presenza di pattern nuovi. Ora serve una
decisione esplicita (promuovi / scarta), a inizio o fine sessione.
**Impact**: PATCH — additivo alle routine esistenti, nessun breaking change.

---

## v1.1.2 — 2026-06-06

### feat | nuova skill: agent-creator | .skills/agent-creator/
**What**: Aggiunta skill `agent-creator` — guida conversazionale per creare nuovi agenti senza conoscenze tecniche. Claude conduce un'intervista in 9 domande (una alla volta), genera `AGENT.md`, `COMMANDS.md`, cartella `commands/`, aggiorna `AGENTS.md` e `CHANGELOG.md`, committa.
**Why**: Complementare a `skill-creator` — abbassa la barriera per estendere il sistema con nuovi ruoli senza toccare file o terminale.
**Impact**: MINOR — nuova skill standalone, nessun breaking change.

---

## v1.1.1 — 2026-06-06

### feat | nuova skill: skill-creator | .skills/skill-creator/
**What**: Aggiunta skill `skill-creator` — guida conversazionale per creare nuove skill senza conoscenze tecniche. Claude conduce un'intervista in 7 domande (una alla volta), genera `SKILL.md`, aggiorna `SKILLS.md` e `CHANGELOG.md`, committa.
**Why**: Abbassa la barriera per utenti non tecnici che vogliono estendere il sistema senza toccare file o terminale.
**Impact**: MINOR — nuova skill standalone, nessun breaking change.

---

## v1.1.0 — Sales CRM-in-repo: account↔opportunità, cockpit, aging, funnel

### feat | opportunity management: cockpit commerciale nel repo | .skills/ | .agents/sales | scripts/ | company/customers/
**What**: Aggiunto un sistema CRM-leggero versionato nel repo, con il repo come source of truth della pipeline (un CRM esterno resta opzionale).
- **Modello dati**: livello **Opportunità** separato dall'**Account** (1 account → N trattative). `company/customers/opportunities/` + `TEMPLATE.md`; account template ristrutturato con indice Opportunità.
- **Skill** `.skills/opportunity-management/SKILL.md` (owner Sales): modello, tassonomia 6 stage + probabilità, regole aging a fasce, board, drill-down, pattern funnel. In `SKILLS.md`.
- **Comandi Sales**: `/sales board` (lancia lo script generatore) e `/sales opportunity` (drill-down/update); `pipeline-review` legge le opportunità. `COMMANDS.md` + `AGENT.md` aggiornati (8→10 comandi).
- **Script** `scripts/generate-pipeline.py`: genera `PIPELINE.md` da `opportunities/*.md` + `pipeline-config.yaml` (target, segmenti, soglie aging). Aging calcolato live; colonna + subtotali per segmento; nessuna dipendenza esterna (yaml fallback).
- **Config** `company/customers/pipeline-config.yaml`: target weighted, stage→prob, segmenti, soglie aging — personalizzabile via /setup.
- **Aging proattivo** agganciato a `ceo-routine/start`, `customer-success/alert-check`, CoS `daily-briefing` + `weekly-digest` (fasce 🟡/🟠/🔴).
- **Funnel di prospecting**: template `company/customers/target-funnel.md` + playbook "importa e consolida da fonti sparse".
- **Dedup wiki**: `system/protocols/wiki.md` — entity partner = sola narrativa, account = SoT.
- **Esempio**: `examples/acme-demo/customers/` con 5 account + 6 opportunità + `PIPELINE.md` generato.
**Why**: dare a founder/Direttore Commerciale una vista d'insieme sempre disponibile (dove sono ferme le trattative e perché) con drill-down, senza dipendere da un CRM esterno scollegato.
**Scope**: additivo. Nessun agente rimosso. Output rules CLAUDE.md aggiornate.

---

## v1.0.0 — Initial public release

### feat | founder-os | sistema completo
**What**: Prima release pubblica di **founder-os** — un "sistema operativo" agentico per gestire una
startup B2B SaaS come se fosse codice. Include:
- 10 agenti (CEO, PM, CTO, Marketing, Sales, Chief of Staff, CFO, HR, Legal, CEO Routine) con comandi e template.
- ~28 skill riutilizzabili (operative + di contesto).
- 5 workflow cross-agente.
- Protocolli di sistema: spec lifecycle, persistent memory, wiki, learnings, system changelog, privacy tiers.
- Wizard di onboarding `/setup` per configurare la propria azienda passo-passo.
- Integrazioni opzionali (ClickUp, Gmail, Fatture in Cloud) via MCP, configurabili con le proprie credenziali.

**Why**: Rendere il sistema riutilizzabile da qualsiasi founder, partendo da template vuoti e una demo.
**Scope**: intero repository.

---

> Le prossime entry verranno aggiunte automaticamente dagli agenti a ogni modifica di sistema.
