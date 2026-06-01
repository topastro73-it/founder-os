# Command: tech-debt-review

## Trigger
`/cto tech-debt-review`

## Processo
1. Cataloga debito tecnico noto per area (code, infra, dependencies, testing, docs)
2. Per ogni item: descrizione, impatto se non risolto, effort per risolvere, urgenza
3. Proponi piano di riduzione: quanto tempo dedicare per sprint (es. 20%)
4. Identifica quick wins vs investimenti strategici
5. Stima "interest rate" del debito: quanto ci rallenta ogni sprint?

## Output
Salva in: `docs/reports/tech-debt-{YYYY-MM-DD}.md`
Commit: `[cto] tech-debt: review and reduction plan`
