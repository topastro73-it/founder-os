# Chief of Staff — Available Commands

Elenco completo dei comandi disponibili per il Chief of Staff Agent.

### `/cos daily-briefing`
Briefing giornaliero: cosa è cambiato nelle ultime 24h, cosa richiede attenzione CEO oggi.
→ Leggi: `commands/daily-briefing.md`
→ Output: `docs/reports/briefing-{YYYY-MM-DD}.md`

### `/cos weekly-digest`
Digest settimanale: output per agente, decisioni prese, follow-up aperti/scaduti, outlook.
→ Leggi: `commands/weekly-digest.md`
→ Output: `docs/reports/weekly-digest-{YYYY-MM-DD}.md`

### `/cos status-check`
Stato di tutti i workstream: roadmap, specs, decisioni aperte, OKR progress, blocchi.
→ Leggi: `commands/status-check.md`
→ Output: `docs/reports/status-{YYYY-MM-DD}.md`

### `/cos follow-up-tracker`
Scansiona decisions/ e docs/ per checkbox aperti. Classifica: scaduti, prossimi 7gg, prossimi 30gg.
→ Leggi: `commands/follow-up-tracker.md`
→ Output: `docs/reports/follow-ups-{YYYY-MM-DD}.md`

### `/cos decision-review`
Audit decisioni: review date passate, follow-up incompleti, decisioni da rivalutare.
→ Leggi: `commands/decision-review.md`
→ Output: `docs/reports/decision-review-{YYYY-MM-DD}.md`

### `/cos agent-activity`
Report attività per agente: file prodotti, decisioni, handoff pendenti, gap.
→ Leggi: `commands/agent-activity.md`
→ Output: `docs/reports/agent-activity-{YYYY-MM-DD}.md`

### `/cos prepare-meeting [topic]`
Prepara brief e agenda per un meeting raccogliendo contesto dal repo.
→ Leggi: `commands/prepare-meeting.md`
→ Output: `docs/internal-memos/meeting-prep-{slug}.md`

### `/cos action-plan`
Piano operativo: tutte le azioni aperte per priorità P0/P1/P2 con owner e deadline.
→ Leggi: `commands/action-plan.md`
→ Output: `docs/reports/action-plan-{YYYY-MM-DD}.md`

### `/cos product-plan`
Pipeline prodotto completa: Discovery → Spec → Tech Review → Ready → In Progress → Launch.
→ Leggi: `commands/product-plan.md`
→ Output: `docs/reports/product-plan-{YYYY-MM-DD}.md`

### `/cos startup-snapshot`
Foto completa della startup: strategy, OKR, product, metrics, sales, team, risks, top 5 priorities.
→ Leggi: `commands/startup-snapshot.md`
→ Output: `docs/reports/startup-snapshot-{YYYY-MM-DD}.md`

### `/cos kanban`
Board markdown: To Do / In Progress / In Review / Blocked / Done. Con aging alerts.
→ Leggi: `commands/kanban.md`
→ Output: `docs/reports/kanban-{YYYY-MM-DD}.md`

### `/cos sync-ceo-actions`
Sincronizza decisioni pendenti, azioni, follow-up e blocchi sulla lista personale ClickUp del CEO. Scansiona repo per item azionabili e li crea come task nella lista CEO Personal.
→ Leggi: `.skills/clickup/commands/sync-ceo-actions.md`
→ Output: `company/product/clickup-pending/YYYY-MM-DD-sync-ceo-actions.md` (poi `clickup-done/`)
