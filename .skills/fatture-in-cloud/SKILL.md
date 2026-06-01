# Fatture in Cloud Skill

Integrazione con Fatture in Cloud (TeamSystem) via API REST v2.
Sincronizza fatture emesse, pagamenti e cashflow nel repo.
Usata da CFO, CEO, Chief of Staff.

## Autenticazione — Personal Access Token (no browser)

FIC supporta **token di accesso personale** generati direttamente dalle impostazioni — nessun OAuth2, nessun flusso browser.

**Come generare il token (una sola volta)**:
1. FIC → **Impostazioni → Sviluppatore → Token di accesso**
2. Crea un nuovo token con scope: `issued_documents`, `entity.clients`, `entity.suppliers`, `products`, `settings`
3. Copia il token e aggiungilo a `~/.zshrc`:
   ```bash
   export FIC_ACCESS_TOKEN="il-tuo-token"
   export FIC_COMPANY_ID="1340993"
   ```
4. `source ~/.zshrc` e riavvia Claude Code → il MCP si avvia automaticamente

**Il token è stabile** (non scade come OAuth2) — nessuna ri-autenticazione necessaria.

---

## Modalità di accesso

### Opzione 1 — MCP Server (consigliata)

Server MCP custom in `mcp-servers/fattureincloud-mcp/server.py`.
Fornisce tool di lettura **e scrittura** direttamente accessibili dagli agenti.

**Setup** (già configurato in `.mcp.json`):
```bash
# ~/.zshrc
export FIC_ACCESS_TOKEN="il-tuo-personal-token"
export FIC_COMPANY_ID="1340993"
```

**Tool MCP disponibili**:

| Tool | Tipo | Descrizione |
|------|------|------------|
| `fic_list_companies` | read | Lista aziende accessibili |
| `fic_get_company_info` | read | Info azienda (nome, P.IVA, indirizzo) |
| `fic_list_invoices` | read | Fatture emesse con filtri per tipo, anno, query SQL-like |
| `fic_get_invoice` | read | Dettaglio singola fattura con righe e pagamenti |
| `fic_list_clients` | read | Anagrafica clienti |
| `fic_list_suppliers` | read | Anagrafica fornitori |
| `fic_list_products` | read | Prodotti e servizi |
| `fic_list_received_documents` | read | Fatture passive / spese |
| `fic_list_payment_accounts` | read | Conti di pagamento |
| `fic_list_payment_methods` | read | Metodi di pagamento |
| `fic_list_vat_types` | read | Aliquote IVA (con ID necessari per creare fatture) |
| `fic_get_tax_profile` | read | Profilo fiscale |
| `fic_create_invoice` | **write** | Crea bozza o fattura emessa |

Tutti i tool supportano output `markdown` (default) o `json`.

### Workflow creare fattura via MCP

```
1. fic_list_clients → trova entity_id del cliente
2. fic_list_vat_types → verifica id aliquota IVA (es. 22%)
3. fic_create_invoice(entity_id=..., date="YYYY-MM-DD", items=[...], is_draft=True)
4. Verifica bozza in FIC → is_draft=False per emettere
```

### Opzione 2 — Script sync (legacy)

Script Python: `scripts/fic_sync.py`
Dipendenze: `pip3 install requests python-dateutil`

## Prerequisiti

Variabili d'ambiente necessarie:

```bash
FIC_ACCESS_TOKEN=<bearer token da FIC → Impostazioni → API (OAuth2)>
FIC_COMPANY_ID=<ID azienda — visibile nell'URL dopo /c/>
```

Configurarle in `.env` locale (non committare) oppure in shell:
```bash
export FIC_ACCESS_TOKEN="..."
export FIC_COMPANY_ID="..."
```

## Comandi agente

| Comando | Descrizione | Output |
|---------|------------|--------|
| `sync-invoices` | Sincronizza fatture emesse (anno corrente) | `company/finance/fatturazione.md` |
| `aging-report` | Calcola aging crediti scaduti | Aggiorna `company/metrics/kpis.md` sezione crediti |
| `sync-cashflow` | Legge prima nota e aggiorna saldi | `company/finance/cashflow.md` |

## Agenti autorizzati

CFO (owner), CEO, Chief of Staff

## Flusso standard (settimanale)

```
# Con MCP attivo — query dirette
→ fic_list_invoices(year=2026) per fatturato anno
→ fic_list_clients() per anagrafica aggiornata
→ fic_list_received_documents(year=2026) per spese

# Oppure via comandi agente
/cfo fatture-in-cloud sync-invoices
/cfo fatture-in-cloud aging-report
```

Il CFO lo esegue ogni lunedì per mantenere i dati freschi nel cadence settimanale.

## Note API

- Base URL: `https://api-v2.fattureincloud.it`
- Auth: OAuth2 Bearer — `Authorization: Bearer {FIC_ACCESS_TOKEN}`
- Rate limit: ~1.000 req/ora, 20.000 req/mese (sliding window, HTTP 429 con Retry-After)
- Paginazione: `page` (da 1) + `per_page` (default 5, max 100)
- Query filter: parametro `q` con sintassi SQL-like (es. `date >= '2026-01-01'`)
- Docs: https://developers.fattureincloud.it/docs

## Integrazione con altre skill

| Skill | Integrazione |
|-------|-------------|
| **Stripe** | Riconcilia fatture FIC (fiscali IT) con pagamenti Stripe |
| **Qonto** | Verifica incassi bancari con `qonto reconcile` |
| **Admin & Controllo** | Dati fatturazione alimentano il controllo gestione |
| **Data & Metrics** | Revenue, aging, DSO calcolati da fatture FIC |
