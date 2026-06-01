# CFO — Available Commands

Elenco completo dei comandi disponibili per il CFO Agent.

### `/cfo financial-model`
Crea o aggiorna il modello finanziario: P&L, cash flow, unit economics.
→ Leggi: `commands/financial-model.md`
→ Output: `company/finance/financial-model.md` + file `.xlsx` se richiesto

### `/cfo burn-analysis`
Analisi burn rate e runway con scenari.
→ Leggi: `commands/burn-analysis.md`
→ Output: `docs/reports/burn-analysis-{date}.md`

### `/cfo unit-economics`
Calcola e analizza unit economics: CAC, LTV, LTV/CAC, payback period.
→ Leggi: `commands/unit-economics.md`
→ Output: `docs/reports/unit-economics-{date}.md`

### `/cfo fundraising-prep`
Prepara i numeri per un round di fundraising: metriche, proiezioni, use of funds.
→ Leggi: `commands/fundraising-prep.md`
→ Output: `docs/reports/fundraising-prep-{date}.md`

### `/cfo budget-review`
Revisiona budget vs actual per il periodo corrente.
→ Leggi: `commands/budget-review.md`
→ Output: `docs/reports/budget-review-{period}.md`

### `/cfo scenario-analysis [topic]`
Modella scenari what-if: cosa succede se cresciamo del 20% vs 50%? Se assumiamo 3 persone? Se il churn raddoppia?
→ Leggi: `commands/scenario-analysis.md`
→ Output: `docs/reports/scenario-{slug}.md`

### `/cfo pricing-model`
Analizza e modella l'impatto finanziario di diverse strategie di pricing.
→ Leggi: `commands/pricing-model.md`
→ Output: `docs/reports/pricing-model-{date}.md`

### `/cfo cap-table`
Aggiorna e analizza la cap table.
→ Skill: `.skills/investor-relations/SKILL.md`
→ Output: `company/finance/cap-table.md`

### `/cfo scadenzario`
Mostra scadenze fiscali e amministrative prossime.
→ Skill: `.skills/admin-controllo/SKILL.md` (comando `/admin scadenzario`)
→ Input: `company/finance/scadenzario.md`

### `/cfo cashflow`
Analisi cashflow operativo con proiezione a 3 mesi.
→ Skill: `.skills/admin-controllo/SKILL.md` (comando `/admin cashflow`)
→ Input: `company/finance/cashflow.md`
→ Output: `docs/reports/cashflow-{date}.md`

### `/cfo fatture-status`
Stato fatturazione: emesse, da emettere, incassate, scadute.
→ Skill: `.skills/admin-controllo/SKILL.md` (comando `/admin fatture-status`)
→ Input: `company/finance/fatturazione.md`

### `/cfo costi-ricorrenti`
Mappa costi ricorrenti e burn rate operativo dettagliato.
→ Skill: `.skills/admin-controllo/SKILL.md` (comando `/admin costi-ricorrenti`)
→ Input: `company/finance/costi-ricorrenti.md`
→ Output: `docs/reports/costi-ricorrenti-{date}.md`

### `/cfo controllo-gestione`
Report controllo di gestione: budget vs actual, margini per linea.
→ Skill: `.skills/admin-controllo/SKILL.md` (comando `/admin controllo-gestione`)
→ Output: `docs/reports/controllo-gestione-{period}.md`

### `/cfo incentivi-check`
Verifica incentivi e agevolazioni per startup innovative italiane.
→ Skill: `.skills/admin-controllo/SKILL.md` (comando `/admin incentivi-check`)
→ Input: `company/finance/incentivi.md`
→ Output: `docs/reports/incentivi-check-{date}.md`

### `/cfo vendor-costs [vendor]`
Analisi costo fornitore: storico, contratto, alternative.
→ Skill: `.skills/admin-controllo/SKILL.md` (comando `/admin vendor-costs`)
→ Output: `docs/reports/vendor-cost-{vendor}.md`

### `/cfo adempimenti-societari`
Checklist adempimenti societari annuali.
→ Skill: `.skills/admin-controllo/SKILL.md` (comando `/admin adempimenti-societari`)
→ Output: `docs/reports/adempimenti-{anno}.md`
