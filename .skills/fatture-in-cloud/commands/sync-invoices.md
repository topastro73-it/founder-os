# FIC Command: sync-invoices

Sincronizza le fatture emesse da Fatture in Cloud e aggiorna `company/finance/fatturazione.md`.

## Agenti autorizzati

CFO, CEO, Chief of Staff

## Invocazione

```
/cfo fatture-in-cloud sync-invoices
/cfo fatture-in-cloud sync-invoices 2026      # anno specifico
/cfo fatture-in-cloud sync-invoices 2026-01   # mese specifico
```

## Processo

### Passo 1 — Esegui il sync via script

```bash
python3 scripts/fic_sync.py invoices --year 2026
```

Lo script chiama:

```
GET /c/{company_id}/issued_documents
  ?type=invoice
  &date_from=2026-01-01
  &date_to=2026-12-31
  &per_page=50
  &page=1
```

Pagina automaticamente finché non ha tutti i documenti.

Per ogni fattura estrae:
- `number` + `number_suffix` → numero fattura
- `date` → data emissione
- `entity.name` → cliente
- `subject` → descrizione
- `amount_net` → imponibile
- `amount_vat` → IVA
- `gross_amount` → totale lordo
- `payment_status` → `not_paid` | `partial` | `paid`
- `due_date` → scadenza (da `payments_list[].due_date` se assente nel documento)
- Data incasso effettivo da `payments_list[]` dove `status = paid`

### Passo 2 — Aggiorna fatturazione.md

Riscrivi la tabella `## Fatture emesse {anno}` in `company/finance/fatturazione.md`:

```markdown
| N. | Data emissione | Cliente | Descrizione | Imponibile | IVA | Totale | Scadenza | Stato | Incassata il |
|----|----------------|---------|-------------|-----------|-----|--------|----------|-------|-------------|
| 1/2026 | 2026-01-15 | Acme Corp | Canone Jan | €8.000 | €1.760 | €9.760 | 2026-02-14 | ✅ Incassata | 2026-02-10 |
| 2/2026 | 2026-01-31 | Partner X | Canone Jan | €3.000 | €660 | €3.660 | 2026-03-01 | ⚠️ Scaduta | — |
```

Mapping `payment_status` → icona:
| FIC status | Icona |
|-----------|-------|
| `paid` | ✅ Incassata |
| `not_paid` + scadenza futura | ⏳ Attesa |
| `not_paid` + scadenza passata | ⚠️ Scaduta |
| `partial` | 🔶 Parziale |

### Passo 3 — Aggiorna riepilogo mensile

Popola la tabella `## Riepilogo mensile {anno}`:
- `Fatturato` = somma `gross_amount` per mese
- `Incassato` = somma `gross_amount` dove `payment_status = paid` per mese di incasso
- `Scaduto` = somma `gross_amount` dove `not_paid` e `due_date` passata
- `DSO` = media giorni tra emissione e incasso (solo fatture pagate)

### Passo 4 — Aggiorna aging

Popola `## Aging Analysis`:
- 0–30 giorni: `due_date` tra oggi e -30gg, `not_paid`
- 31–60 giorni: `due_date` tra -31 e -60gg, `not_paid`
- 61–90 giorni: `due_date` tra -61 e -90gg, `not_paid`
- 90+ giorni: `due_date` oltre -90gg, `not_paid`

### Passo 5 — Commit

```bash
git add company/finance/fatturazione.md
git commit -m "[cfo] fatture-in-cloud: sync invoices YYYY-MM-DD — N fatture, €X fatturato"
```

## Guardrails

- MAI cancellare fatture già presenti nel file — solo aggiornare e aggiungere
- Se `gross_amount` è negativo → è una nota di credito, marcala con `NC` nel numero
- Fatture con `payment_status = partial`: mostrare importo residuo nella colonna Note
- Se lo script fallisce per credenziali mancanti, bloccarsi e chiedere `FIC_ACCESS_TOKEN`
