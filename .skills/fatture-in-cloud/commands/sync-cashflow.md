# FIC Command: sync-cashflow

Legge la prima nota da Fatture in Cloud e aggiorna `company/finance/cashflow.md`.

## Agenti autorizzati

CFO, CEO, Chief of Staff

## Invocazione

```
/cfo fatture-in-cloud sync-cashflow
/cfo fatture-in-cloud sync-cashflow 2026-03   # mese specifico
```

## Processo

### Passo 1 — Leggi prima nota via script

```bash
python3 scripts/fic_sync.py cashflow --month 2026-03
```

Lo script chiama:

```
GET /c/{company_id}/cashbook
  ?date_from=2026-03-01
  &date_to=2026-03-31
  &kind=all
```

Ogni record prima nota ha:
- `date` → data movimento
- `description` → descrizione
- `kind` → `cashbook_in` (entrata) | `cashbook_out` (uscita)
- `amount_in` → importo entrata
- `amount_out` → importo uscita
- `entity_name` → controparte (se collegata)
- `document.id` / `document.type` → documento collegato (fattura, nota spese, etc.)

### Passo 2 — Calcola saldo conto

Somma tutte le entrate e uscite fino a oggi per ottenere il saldo corrente.
Aggiorna `## Saldo corrente` in `company/finance/cashflow.md`:

```markdown
| Conto corrente principale | €XXX.XXX | 2026-03-23 |
```

### Passo 3 — Aggiorna entrate attese

Dalla lista fatture `not_paid` (già ottenuta da `sync-invoices`), popola:

```markdown
### Fatture emesse in attesa di incasso
| N. Fattura | Cliente | Importo | Scadenza | Probabilità incasso |
| 5/2026 | Acme Srl | €4.167 | 2026-02-01 | Alta (51gg, cliente attivo) |
```

Probabilità automatica basata sull'aging:
- 0–30gg → Alta
- 31–60gg → Media
- 61–90gg → Bassa
- 90+gg → Critica

### Passo 4 — Proiezione settimanale

Calcola saldo proiettato settimana per settimana per le prossime 12 settimane:
- Entrate attese: fatture in scadenza per settimana (da FIC) + MRR ricorrente (da kpis.md)
- Uscite attese: uscite fisse da `cashflow.md` + scadenze fiscali da `scadenzario.md`

Aggiorna tabella `## Proiezione settimanale`.

### Passo 5 — Commit

```bash
git add company/finance/cashflow.md
git commit -m "[cfo] fatture-in-cloud: sync cashflow YYYY-MM-DD — saldo €X, proiezione 12 sett"
```

## Note

- Il saldo FIC riflette solo i movimenti inseriti nella prima nota — verificare con estratto conto bancario
- I movimenti bancari non riconciliati in FIC non appaiono — riconciliare prima del sync
- Se `amount_in` e `amount_out` sono entrambi 0 su un record, è una girata interna — ignora
