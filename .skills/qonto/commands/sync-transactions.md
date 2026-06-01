# Qonto Command: sync-transactions

Scarica i movimenti bancari del mese da Qonto e produce un report.

## Agenti autorizzati

CFO, CEO, Chief of Staff

## Invocazione

```
/cfo qonto sync-transactions
/cfo qonto sync-transactions 2026-03   # mese specifico
```

## Processo

### Passo 1 — Scarica movimenti via script

```bash
python3 scripts/qonto_sync.py transactions --month 2026-03
```

Lo script chiama `GET /v2/transactions` con:
- `slug` del bank account (da organization)
- `settled_at_from` / `settled_at_to` per il periodo
- Paginazione automatica (`limit=100`, `offset`)

Per ogni transazione estrae:
- `settled_at` → data contabile
- `emitted_at` → data operazione
- `side` → `credit` (entrata) o `debit` (uscita)
- `amount` → importo
- `currency` → valuta
- `label` → descrizione/causale
- `counterparty_name` → controparte (mittente o destinatario)
- `reference` → riferimento (utile per match fatture)
- `category` → categoria Qonto
- `status` → `completed`, `pending`, `declined`

### Passo 2 — Genera report

Output come JSON strutturato + sommario:

```
Entrate:  €X.XXX (N movimenti)
Uscite:   €X.XXX (N movimenti)
Netto:    €X.XXX
```

Top 5 entrate e top 5 uscite per importo.

### Passo 3 — Aggiorna cashflow.md

Popola la sezione `## Proiezione settimanale` con i dati reali delle settimane passate e proiezioni per le future.

### Passo 4 — Commit

```bash
git add company/finance/cashflow.md
git commit -m "[cfo] qonto: sync movimenti YYYY-MM — €X entrate, €Y uscite"
```
