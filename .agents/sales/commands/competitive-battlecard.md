# Command: competitive-battlecard

## Trigger
`/sales competitive-battlecard [competitor]`

## Processo
1. Carica analisi esistente da `company/competitors/battlecards/` se presente
2. Struttura battlecard per uso in call:
   - Overview competitor (1-2 frasi)
   - I LORO punti di forza (sii onesto)
   - I LORO punti deboli
   - I NOSTRI differenziatori chiave
   - Domande da fare al prospect per evidenziare i gap del competitor
   - Obiezioni comuni e risposte
   - Win/loss pattern: quando vinciamo e quando perdiamo
3. Tono: factual, non aggressivo. Vinci sui tuoi meriti.

## Output
Salva in: `company/competitors/battlecards/{competitor-slug}.md`
Commit: `[sales] battlecard: {competitor}`
