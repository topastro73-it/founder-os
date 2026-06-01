# Qonto Skill

Integrazione con Qonto (banca online) via API v2.
Sincronizza saldi, movimenti bancari e riconcilia con i dati fatturazione.
Usata da CFO, CEO, Chief of Staff.

## Prerequisiti

Credenziali memorizzate in **macOS Keychain** (encrypted, mai nel repo).

**Setup one-time** (eseguire manualmente, una sola volta per macchina):

```bash
security add-generic-password -a "qonto" -s "QONTO_LOGIN"  -w "<qonto-login-slug>" -U
security add-generic-password -a "qonto" -s "QONTO_SECRET" -w "<secret-da-qonto>" -U
```

La secret key si recupera da Qonto → Integrazioni → API key.

Script: `scripts/qonto.sh` (wrapper) → `scripts/qonto_sync.py` (Python)
Dipendenze: `pip3 install requests`

Il wrapper bash legge le credenziali dal Keychain ed esporta le env vars al
processo Python. Niente file `.env`, niente credenziali in chiaro nel repo.

## Comandi

| Comando | Descrizione | Output |
|---------|------------|--------|
| `sync-balance` | Legge saldi conti Qonto | Aggiorna `company/finance/cashflow.md` sezione saldi |
| `sync-transactions` | Scarica movimenti del mese | Report movimenti + aggiorna cashflow |
| `reconcile` | Incrocia movimenti Qonto con fatture FIC | Identifica fatture incassate / pagamenti non riconciliati |

## Agenti autorizzati

CFO (owner), CEO, Chief of Staff

## Flusso standard

Comando wrapper (legge Keychain automaticamente):

```bash
bash scripts/qonto.sh balance                    # saldi conti
bash scripts/qonto.sh transactions --month 2026-04
bash scripts/qonto.sh reconcile --month 2026-04
```

Invocazione agente:
```
/cfo qonto sync-balance           # ogni lunedi — aggiorna saldo in cashflow.md
/cfo qonto sync-transactions      # ogni lunedi — scarica movimenti mese
/cfo qonto reconcile              # dopo sync-invoices FIC — incrocia fatture con incassi
```

## Note API

- Base URL: `https://thirdparty.qonto.com/v2`
- Auth: `Authorization: {login}:{secret}` (NO base64)
- Rate limit: 1.000 req/10s, 10.000 req/10min
- Pagination: `limit` + `offset`, max 10.000 risultati per query
- Conti: Conto principale (main) + Marketing
