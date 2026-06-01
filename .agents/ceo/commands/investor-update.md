# Command: investor-update

## Trigger
`/ceo investor-update` oppure "Prepara l'investor update mensile"

## Processo

1. **Carica contesto**
   - `company/metrics/kpis.md` — MRR, churn, pipeline, growth
   - `company/product/roadmap.md` — Cosa abbiamo rilasciato
   - `company/product/changelog.md` — Changelog recente
   - `company/customers/segments.md` — Nuovi clienti, churn
   - `company/strategy/vision.md` — Narrative corrente

2. **Genera update** seguendo il template investor-update

3. **Tono**: Onesto, conciso, confident ma non overselling. Gli investitori apprezzano trasparenza su problemi + come li stai affrontando.

## Output
Salva in: `docs/investor-updates/{YYYY-MM}-update.md`
Commit: `[ceo] update: {month} investor update`

## Template
Usa: `.agents/ceo/templates/investor-update.md`
