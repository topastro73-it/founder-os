# Qonto Command: reconcile

Incrocia i movimenti Qonto con le fatture FIC per identificare fatture incassate e pagamenti non riconciliati.

## Agenti autorizzati

CFO, CEO, Chief of Staff

## Invocazione

```
/cfo qonto reconcile
/cfo qonto reconcile 2026-03   # mese specifico
```

## Prerequisiti

Eseguire prima:
- `/cfo fatture-in-cloud sync-invoices` (per avere fatture aggiornate)
- `/cfo qonto sync-transactions` (per avere movimenti aggiornati)

## Processo

### Passo 1 — Carica dati

1. Leggi `company/finance/fatturazione.md` → lista fatture con stato e importo
2. Esegui `python3 scripts/qonto_sync.py transactions --month YYYY-MM` → movimenti bancari

### Passo 2 — Matching automatico

Per ogni entrata Qonto (`side = credit`), cerca una fattura FIC corrispondente:

**Criteri di match** (in ordine di priorita):
1. **Importo esatto** — `transaction.amount == fattura.gross_amount`
2. **Importo + controparte** — importo coincide e `counterparty_name` contiene il nome cliente
3. **Riferimento fattura** — `transaction.reference` contiene il numero fattura

**Soglia di tolleranza**: ±€1 (per arrotondamenti bancari)

### Passo 3 — Genera report riconciliazione

```markdown
## Riconciliazione YYYY-MM

### Fatture matched (incassate)
| Fattura | Cliente | Importo | Data incasso Qonto | Match type |
|---------|---------|---------|-------------------|------------|
| 8/2026 | Multireti | €122.000 | 2026-03-01 | Importo esatto |

### Fatture scadute NON trovate in Qonto
| Fattura | Cliente | Importo | Scadenza | Giorni |
|---------|---------|---------|----------|--------|
| ... | ... | ... | ... | ... |

### Entrate Qonto NON matchate a fatture
| Data | Controparte | Importo | Riferimento |
|------|-------------|---------|-------------|
| ... | ... | ... | ... |
```

### Passo 4 — Aggiorna stati

Per le fatture matched:
- Aggiorna `fatturazione.md`: stato → ✅ Incassata, data incasso
- Ricalcola aging analysis
- Aggiorna crediti scaduti in `kpis.md`

### Passo 5 — Commit

```bash
git add company/finance/fatturazione.md company/metrics/kpis.md
git commit -m "[cfo] qonto: riconciliazione YYYY-MM — N fatture matched, €X incassato"
```

## Guardrails

- MAI marcare una fattura come incassata senza match Qonto — solo suggerire
- Se il match e' ambiguo (piu' fatture con lo stesso importo), chiedere conferma al CEO/CFO
- Mostrare SEMPRE le entrate non matchate — potrebbero essere anticipi, note di credito, o errori
