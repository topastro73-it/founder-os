# Spec Lifecycle Protocol

Ogni file in `company/product/specs/` ha un frontmatter YAML con `status`. Gli agenti lo aggiornano ad ogni cambiamento di stato. Il Chief of Staff mantiene aggiornato `company/product/specs/INDEX.md`.

## Stati possibili

- `draft` — bozza iniziale
- `evaluated` — valutazione tecnica/business completata
- `approved` — approvato per sviluppo
- `in-development` — in lavorazione (ClickUp Epic aperta)
- `shipped` — rilasciato e verificato
- `deferred` — posticipato con `review-date`
- `declined` — rifiutato (stato finale)

## Regole per stato

### Regola `in-development`
Quando una spec passa a `in-development`, il CTO DEVE suggerire al CEO:
> "Vuoi che generi il test plan e i test case con `/qa test-plan`?"

Il test plan va creato PRIMA che lo sviluppo finisca.

### Regola `shipped`
Una spec passa a `shipped` **solo quando**:
- (a) TUTTI i task della Epic ClickUp associata sono in stato `Released` E
- (b) esiste un test report con verdetto GO in `company/product/testing/test-report-{slug}-cycle{N}.md`

Verificare entrambe le condizioni prima di aggiornare lo status.

### Regola `spec-reconciliation`
Prima di marcare una spec come `shipped`, l'agente DEVE leggere i task e i commenti della Epic ClickUp associata per verificare se durante lo sviluppo sono emersi cambiamenti rispetto alle specifiche originali (scope modificato, AC aggiustati, funzionalità rimosse o aggiunte, comportamenti diversi da quanto scritto).

Se ci sono divergenze, aggiorna la PRD con i dati reali prima di impostare `status: shipped`. La PRD deve riflettere il prodotto come è stato costruito, non come era pianificato.
