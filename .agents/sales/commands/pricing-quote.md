# Command: pricing-quote

## Trigger
`/sales pricing-quote [prospect]`

## Processo
1. Identifica tier appropriato per il prospect
2. Calcola pricing basato su: dimensione azienda, utenti, feature necessarie
3. Applica eventuali sconti standard (annual vs monthly, multi-year)
4. Genera quotazione chiara con breakdown

## Output
Salva in: `docs/proposals/quote-{prospect-slug}.md`
Commit: `[sales] quote: {prospect}`
⚠️ Sconti oltre il 20% richiedono approvazione CEO
