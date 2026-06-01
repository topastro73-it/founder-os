# Command: okr-review

## Trigger
`/ceo okr-review` oppure "Come stanno gli OKR?"

## Processo

1. **Carica** `company/strategy/okrs/` — OKR correnti
2. **Per ogni Objective**:
   - Stato: On Track / At Risk / Off Track
   - Per ogni Key Result: progresso % e trend
   - Blockers identificati
   - Azioni correttive se necessario
3. **Genera scorecard** con overview visuale
4. **Proponi aggiustamenti** se necessario (nuovi KR, KR da droppare, target da rivedere)

## Output
Aggiorna: `company/strategy/okrs/{current-quarter}.md` (aggiungi sezione review)
Commit: `[ceo] okr: mid-quarter review` o `[ceo] okr: end-quarter scoring`
