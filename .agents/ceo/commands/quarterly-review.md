# Command: quarterly-review

## Trigger
`/ceo quarterly-review` oppure "Fai il review del trimestre"

## Processo

1. **Carica contesto**
   - `company/strategy/okrs/` — OKR del trimestre
   - `company/metrics/kpis.md` — Metriche
   - `company/product/roadmap.md` — Cosa abbiamo consegnato
   - `decisions/` — Decisioni prese nel trimestre
   - `docs/` — Documenti generati nel trimestre

2. **Analizza risultati**
   - OKR: per ogni KR, a che punto siamo? (0-100%)
   - Metriche: trend positivi e negativi
   - Prodotto: cosa è stato consegnato vs pianificato
   - Team: come stiamo, cosa abbiamo imparato

3. **Genera review strutturato**
   - Executive summary (3-5 righe)
   - OKR scorecard
   - Wins del trimestre
   - Misses e lesson learned
   - Decisioni chiave prese
   - Outlook per il prossimo trimestre
   - Rischi e opportunità

## Output
Salva in: `docs/reports/quarterly-review-{YYYY-QN}.md`
Commit: `[ceo] review: Q{N} quarterly review`
