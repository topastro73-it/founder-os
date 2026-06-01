# Command: pipeline-review

## Trigger
`/sales pipeline-review`

## Processo
1. Carica `company/metrics/funnel.md`
2. Analizza health della pipeline: coverage ratio, velocity, conversion rate per stage
3. Identifica deal a rischio e deal accelerabili
4. Proponi azioni per migliorare forecast
5. Flag gap: abbiamo abbastanza pipeline per il target?

## Output
Salva in: `docs/reports/pipeline-review-{YYYY-MM-DD}.md`
Commit: `[sales] review: pipeline analysis`
