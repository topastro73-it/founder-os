# Command: contract-review

## Trigger
`Come Legal, rivedi/crea il contratto [tipo]`

## Processo
1. Identifica tipo: SaaS Agreement, NDA, Partnership, Employment, Freelance
2. Se review: analizza clausole critiche (liability, termination, IP, SLA, data processing)
3. Se creazione: genera draft con clausole standard per B2B SaaS
4. Per ogni clausola critica: spiega cosa significa e il rischio
5. Evidenzia: red flag, clausole mancanti, suggerimenti di modifica

## Output
Salva in: `company/legal/contracts/{type-slug}.md`
Commit: `[legal] contract: {type} draft/review`
⚠️ Disclaimer: draft da validare con avvocato
