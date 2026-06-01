# Command: competitive-analysis

## Trigger
`/pm competitive-analysis [competitor]` oppure "Analizza [competitor]"

## Processo
1. Carica `company/competitors/landscape.md` se esiste
2. Analizza competitor su: positioning, feature set, pricing, target market, punti di forza/debolezza
3. Mappa feature comparison matrix (noi vs loro)
4. Identifica differenziatori nostri e gap
5. Genera battlecard per Sales
6. Proponi raccomandazioni strategiche (dove investire, dove concedere)

## Output
Salva in: `company/competitors/battlecards/{competitor-slug}.md`
Commit: `[pm] competitive: {competitor} battlecard`
Handoff → Sales per enablement
