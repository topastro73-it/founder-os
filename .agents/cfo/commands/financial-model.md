# Command: financial-model

## Trigger
`Come CFO, crea il modello finanziario` oppure "Fammi il P&L"

## Processo
1. Carica metriche correnti da `company/metrics/kpis.md`
2. Definisci assunzioni: growth rate, churn, ACV, costi, hiring plan
3. Costruisci P&L a 12-24 mesi: Revenue, COGS, Gross Margin, OpEx (per categoria), EBITDA, Cash Flow
4. Calcola unit economics: CAC, LTV, LTV/CAC, Payback period
5. Includi sensitivity analysis su variabili chiave
6. Se richiesto, genera file `.xlsx` con formula trasparenti

## Output
Salva in: `company/finance/financial-model.md`
Se Excel: `company/finance/financial-model-{date}.xlsx`
Commit: `[cfo] model: financial model update`
