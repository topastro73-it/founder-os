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
