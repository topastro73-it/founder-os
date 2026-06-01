# Command: proposal-generate

## Trigger
`/sales proposal-generate [prospect]` oppure "Genera proposta per [prospect]"

## Processo
1. Carica context sul prospect (deal review se esiste, altrimenti chiedi info)
2. Carica `.agents/_shared/COMPANY.md` per value proposition
3. Personalizza: parla dei LORO problemi, non delle nostre feature
4. Struttura: Executive Summary → Problema → Soluzione → Perché noi → Pricing → Next steps
5. Includi social proof rilevante (case study, metriche, testimonial se disponibili)
6. Pricing: usa tier appropriato, chiaro e trasparente

## Output
Salva in: `docs/proposals/proposal-{prospect-slug}.md`
Commit: `[sales] proposal: {prospect}`
