# Command: pricing-analysis

## Trigger
`/pm pricing-analysis [feature]` oppure "Come prezzare [feature]?"

## Processo
1. Valuta customer value (impatto economico per il cliente)
2. Determina tier di packaging: Core / Premium / Add-on / Enterprise-only
3. Analizza pricing competitor per feature simili
4. Raccomanda modello: per-seat, usage-based, flat fee
5. Suggerisci price point con razionale
6. Stima impatto su revenue e attach rate

## Output
Salva in: `docs/reports/pricing-{slug}.md`
Commit: `[pm] pricing: analysis for {feature}`
Handoff → CEO per approvazione, Sales per feedback dal campo
