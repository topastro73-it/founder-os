# Command: build-vs-buy

## Trigger
`/cto build-vs-buy [capability]` oppure "Meglio costruire o comprare [capability]?"

## Processo
1. Valuta importanza strategica (core vs non-core capability)
2. Analizza expertise interna e capacità disponibile
3. Calcola TCO a 3 anni per BUILD vs BUY vs PARTNER:
   - Build: sviluppo + manutenzione + opportunity cost
   - Buy: licenza + integrazione + vendor lock-in risk
   - Partner: revenue share + integrazione + dipendenza
4. Valuta rischi per ogni opzione
5. Raccomanda BUILD / BUY / PARTNER con piano di implementazione

## Output
Salva in: `docs/reports/build-vs-buy-{slug}.md`
Commit: `[cto] analysis: build-vs-buy for {capability}`
