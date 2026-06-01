# Command: burn-analysis

## Trigger
`Come CFO, analizza il burn rate` oppure "Quanto runway abbiamo?"

## Processo
1. Carica metriche: MRR, costi mensili, cash in bank
2. Calcola: burn rate netto, gross burn, runway in mesi
3. Modella 3 scenari: current trajectory, optimistic (+30% growth), pessimistic (-20% growth + higher churn)
4. Identifica: quando serve il prossimo round, quanto raccogliere, a che condizioni

## Output
Salva in: `docs/reports/burn-analysis-{YYYY-MM-DD}.md`
Commit: `[cfo] analysis: burn rate and runway`
