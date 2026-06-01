# Workflow: Quarterly Planning

Pianificazione trimestrale coordinata tra tutti gli agenti.

## Timeline: 10 giorni lavorativi

### Fase 1: Strategic Direction (Day 1-2) — CEO
- `/ceo quarterly-review` (review Q precedente)
- `/ceo okr-review` (scoring OKR precedenti)
- Draft nuovi OKR in `company/strategy/okrs/YYYY-QN.md`
- **Handoff → PM + CTO**

### Fase 2: Roadmap Proposal (Day 3-5) — PM
- `/pm roadmap-review` (analisi roadmap corrente)
- `/pm prioritize-backlog` (ri-prioritizzazione con nuovi OKR)
- Proposta roadmap trimestrale
- **Handoff → CTO** per feasibility

### Fase 3: Tech Feasibility (Day 5-7) — CTO
- `/cto architecture-review` (se servono decisioni arch)
- `/cto tech-debt-review` (quanto tech debt includere)
- Annotazioni su roadmap: stime, rischi, dipendenze
- **Handoff → CEO** per approvazione

### Fase 4: Sales Alignment (Day 7-8) — Sales
- `/sales pipeline-review`
- Mapping: feature in roadmap ↔ deal in pipeline
- Gap analysis: serve qualcosa per chiudere deal?
- **Handoff → PM** per aggiustamenti finali

### Fase 5: GTM Planning (Day 8-10) — Marketing
- `/marketing content-plan` per il trimestre
- `/marketing launch-plan` per ogni feature major in roadmap
- Content calendar allineato a roadmap
- **Commit finale** di tutti i documenti

### Chiusura: CEO
- `/ceo investor-update` con piano trimestrale
- Commit finale: tutto in `company/strategy/`
