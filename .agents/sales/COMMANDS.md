# Sales — Available Commands

Elenco completo dei comandi disponibili per il Sales Agent.

### `/sales deal-review [prospect]`
Analizza un deal: positioning, rischi, strategia di chiusura.
→ Leggi: `commands/deal-review.md`
→ Output: `docs/reports/deal-review-{prospect}.md`

### `/sales proposal-generate [prospect]`
Genera proposta commerciale personalizzata.
→ Leggi: `commands/proposal-generate.md`
→ Output: `docs/proposals/proposal-{prospect}.md`

### `/sales objection-handler [objection]`
Genera risposta strutturata a un'obiezione ricorrente.
→ Leggi: `commands/objection-handler.md`
→ Output: `docs/internal-memos/objection-{slug}.md`

### `/sales board`
Rigenera il cockpit commerciale: vista sinottica di tutte le opportunità, bloccati & aging in cima, per segmento/stage/owner.
→ Leggi: `commands/board.md` · Skill: `.skills/opportunity-management/SKILL.md`
→ Esegue: `python scripts/generate-pipeline.py` → Output: `company/customers/PIPELINE.md`

### `/sales opportunity [opp-slug]`
Drill-down e aggiornamento di una trattativa: crea/sposta stage/logga attività/gestisci blocker.
→ Leggi: `commands/opportunity.md` · Skill: `.skills/opportunity-management/SKILL.md`
→ Output: `company/customers/opportunities/{opp-slug}.md`

### `/sales pipeline-review`
Analizza la pipeline corrente (report narrativo): health, rischi, velocity, forecast. Legge le opportunità strutturate del repo.
→ Leggi: `commands/pipeline-review.md`
→ Output: `docs/reports/pipeline-review-{date}.md`

### `/sales pricing-quote [prospect]`
Genera quotazione personalizzata.
→ Leggi: `commands/pricing-quote.md`
→ Output: `docs/proposals/quote-{prospect}.md`

### `/sales competitive-battlecard [competitor]`
Genera/aggiorna battlecard per uso in call di vendita.
→ Leggi: `commands/competitive-battlecard.md`
→ Output: `company/competitors/battlecards/{competitor}.md`

### `/sales customer-health [partner]`
Analizza lo stato di salute di un partner/cliente.
→ Skill: `.skills/customer-success/SKILL.md`
→ Output: `docs/reports/partner-health-{slug}.md`

### `/sales outbound-sequence [target]`
Genera una sequenza outbound personalizzata per un target.
→ Skill: `.skills/outbound-abm/SKILL.md`
→ Output: `docs/marketing/sequences/sequence-{slug}.md`
