# ERP Integration Skill

Integrazione bidirezionale con il sistema ERP via MCP Server e REST API.
Consente di leggere, scrivere e sincronizzare dati finanziari, CRM, fatture, contratti e KPI.

## Modalità di accesso

### Opzione 1 — MCP Server ERP (consigliata)

Server MCP custom ospitato su GitHub, eseguito via `npx tsx`.
Già configurato in `.mcp.json`:

```json
{
  "erp": {
    "command": "npx",
    "args": ["tsx", "https://github.com/{{ORG}}/{{ERP_MCP_REPO}}"],
    "env": {
      "DB_FILE_PATH": "${ERP_DB_URL}"
    }
  }
}
```

**Prerequisiti**: Node.js 18+ e `npx` disponibile nel PATH.
Il database viene caricato dal file linkato in `DB_FILE_PATH`.

Quando il MCP è attivo, gli agenti possono interrogare l'ERP direttamente senza script Python intermedi.

### Opzione 2 — Script sync (fallback)

Se il MCP non è disponibile, usare lo script Python: `scripts/erp_sync.py`
Richiede: `ERP_API_URL` e opzionalmente `ERP_AUTH_TOKEN` come env var.

## Quando usare questa skill

- Quando serve accesso ai dati finanziari live (non dal JSON statico)
- Per sincronizzare fatture, cashflow, KPI dall'ERP
- Per scrivere/aggiornare record sull'ERP (upsert, bulk)
- Per fare snapshot/backup dei dati ERP

## API Reference

**Base URL**: configurata in `ERP_API_URL` (env var) o esposta dal MCP server ERP
**Auth**: opzionale via `ERP_AUTH_TOKEN` (Bearer token)

### Entità disponibili

| Entità | Chiave primaria | Descrizione |
|--------|----------------|-------------|
| `financials` | `id` | Transazioni P&L (cuore del sistema) |
| `deals` | `id` | Opportunità CRM |
| `accounts` | `id` | Aziende CRM |
| `contacts` | `id` | Contatti CRM |
| `orders` | `id` | Ordini Fornitori |
| `users` | `id` | Utenti |
| `contracts` | `id` | Contratti |
| `invoices` | `id` | Fatture |
| `payments` | `id` | Pagamenti Fatture |
| `funding_rounds` | `id` | Round di Finanziamento |
| `settings` | `key` | Impostazioni e KPI |
| `cash_balances` | `month` (YYYY-MM) | Saldi di Cassa Mensili |

### Endpoint

| Azione | Metodo | URL | Note |
|--------|--------|-----|------|
| Leggi tutti | `GET` | `/api/:store` | Array JSON |
| Leggi uno | `GET` | `/api/:store/:id` | Oggetto JSON |
| Crea/Aggiorna | `POST` | `/api/:store` | Upsert (deve avere `id`) |
| Bulk upsert | `POST` | `/api/:store/bulk` | Array di oggetti |
| Elimina uno | `DELETE` | `/api/:store/:id` | `{"success": true}` |
| Bulk delete | `POST` | `/api/:store/bulk-delete` | `{"ids": [...]}` |
| Svuota entità | `DELETE` | `/api/:store` | ⚠️ Cancella TUTTO |

### Note tecniche

- **Date**: formato ISO 8601 (es. `2026-03-23T08:45:10.000Z`)
- **Valori**: sempre netti (imponibile) nei campi principali (`netAmount`, `plannedValue`). Il lordo si calcola aggiungendo `taxRate` o `tax`
- **Content-Type**: `application/json` per tutte le richieste POST/PUT

## Comandi

| Comando | Descrizione | Output |
|---------|------------|--------|
| `sync-all` | Sincronizza tutto: fatture, cashflow, KPI | File markdown in `company/` |
| `sync-invoices` | Sincronizza fatture dall'ERP | `company/finance/fatturazione-erp.md` |
| `sync-cashflow` | Sincronizza saldi cassa dall'ERP | `company/finance/cashflow-erp.md` |
| `sync-kpis` | Calcola KPI dai financials ERP | `company/metrics/kpis-erp.md` |
| `pull` | Scarica entità come JSON | `company/finance/erp-data/*.json` |
| `snapshot` | Backup completo di tutte le entità | `company/finance/erp-data/snapshot-YYYY-MM-DD.json` |
| `push` | Carica JSON su un'entità ERP | Upsert sull'ERP |

---

## Comando: sync-all

### Trigger
"sincronizza ERP", "aggiorna dati da ERP", "sync ERP"

### Processo

1. Esegui `python3 scripts/erp_sync.py sync-all`
2. Verifica che i 3 file siano stati generati
3. Commit: `[cfo] sync: ERP data update — invoices, cashflow, KPIs`

### Output
- `company/finance/fatturazione-erp.md`
- `company/finance/cashflow-erp.md`
- `company/metrics/kpis-erp.md`

---

## Comando: sync-invoices

### Trigger
"sincronizza fatture ERP", "fatture da ERP"

### Processo
1. Esegui `python3 scripts/erp_sync.py sync-invoices`
2. Il file include: fatture pagate (con metodo di pagamento), fatture da incassare (con aging)

### Output
- `company/finance/fatturazione-erp.md`

---

## Comando: sync-cashflow

### Trigger
"sincronizza cashflow ERP", "saldi ERP"

### Processo
1. Esegui `python3 scripts/erp_sync.py sync-cashflow`
2. Il file include: saldi mensili ordinati cronologicamente

### Output
- `company/finance/cashflow-erp.md`

---

## Comando: sync-kpis

### Trigger
"KPI da ERP", "dashboard ERP"

### Processo
1. Esegui `python3 scripts/erp_sync.py sync-kpis`
2. Il file include: MRR/ARR, revenue, costi per categoria, burn rate, runway, pipeline, contratti attivi, target vs actual

### Output
- `company/metrics/kpis-erp.md`

---

## Comando: pull

### Trigger
"scarica dati ERP", "pull ERP"

### Processo
1. Esegui `python3 scripts/erp_sync.py pull [entity1 entity2 ...]`
2. Se nessuna entità specificata, scarica tutte
3. Salva come JSON in `company/finance/erp-data/`

---

## Comando: snapshot

### Trigger
"backup ERP", "snapshot ERP"

### Processo
1. Esegui `python3 scripts/erp_sync.py snapshot`
2. Genera un file JSON completo con timestamp

### Output
- `company/finance/erp-data/snapshot-YYYY-MM-DD.json`

---

## Comando: push

### Trigger
"carica su ERP", "push ERP", "aggiorna ERP"

### Processo
1. Esegui `python3 scripts/erp_sync.py push ENTITY FILE`
2. Supporta sia singolo record che array (bulk)

### Guardrails
- ⚠️ **MAI** usare il comando `clear` (svuota entità) senza conferma esplicita del CEO
- ⚠️ **MAI** fare push di dati senza verifica preventiva (mostra preview prima)
- ⚠️ **MAI** sovrascrivere dati di produzione con dati demo/test

---

## Integrazione con altre skill

| Skill | Come si integra |
|-------|----------------|
| **Financial Import** | ERP è la fonte live; Financial Import gestisce il JSON statico come fallback |
| **Fatture in Cloud** | FIC è il sistema di fatturazione elettronica italiano; ERP è il sistema gestionale aggregato |
| **Qonto** | Qonto è il conto bancario; ERP aggrega i saldi in `cash_balances` |
| **Data & Metrics** | I KPI calcolati da ERP alimentano il dashboard metriche |
| **Admin & Controllo** | L'ERP fornisce i dati base per il controllo di gestione |

## Data model: financials[]

Il record `financials` è il cuore del sistema. Campi principali:

| Campo | Tipo | Descrizione |
|-------|------|-------------|
| `treatment` | string | `Cost` o `Recurring Revenue` o `Project-based` |
| `pnl` | string | Categoria P&L (`COGS`, `R&D`, `S&M`, `G&A`, `Subscription Revenue`, etc.) |
| `status` | string | `Pipeline`, `Unpaid`, `Paid`, `Lost` |
| `frequency` | int | Durata servizio in mesi (1=mensile, 12=annuale) |
| `plannedValue` | number | Forecast (positivo=ricavo, negativo=costo) |
| `bookingValue` | number | Contrattualizzato |
| `actualValue` | number | Effettivo (cassa) |
| `mrr` | number | MRR del record (se subscription) |
| `tax` | number | % IVA (22 = 22%) |
| `resource` | string | Nome cliente/fornitore |
