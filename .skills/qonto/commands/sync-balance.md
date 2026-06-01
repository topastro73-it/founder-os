# Qonto Command: sync-balance

Legge i saldi correnti dei conti Qonto e aggiorna `company/finance/cashflow.md`.

## Agenti autorizzati

CFO, CEO, Chief of Staff

## Invocazione

```
/cfo qonto sync-balance
```

## Processo

### Passo 1 — Leggi saldi via script

```bash
python3 scripts/qonto_sync.py balance
```

Lo script chiama `GET /v2/organization` e estrae per ogni `bank_accounts[]`:
- `name` → nome conto
- `iban` → IBAN
- `balance` → saldo corrente
- `authorized_balance` → saldo autorizzato (al netto di operazioni pendenti)
- `updated_at` → data ultimo aggiornamento

### Passo 2 — Aggiorna cashflow.md

Riscrivi la sezione `## Saldo corrente`:

```markdown
| Conto | Saldo | Data verifica |
|-------|-------|---------------|
| Conto principale (Qonto) | €X.XXX,XX | 2026-03-23 |
| Marketing (Qonto) | €XXX,XX | 2026-03-23 |
| **Totale disponibile** | **€X.XXX,XX** | |
```

### Passo 3 — Aggiorna KPIs

Se il saldo totale differisce significativamente dalla "Cassa stimata" in `company/metrics/kpis.md`, aggiorna il valore.

### Passo 4 — Commit

```bash
git add company/finance/cashflow.md
git commit -m "[cfo] qonto: sync saldi — €X.XXX totale disponibile"
```

## Note

- Il saldo Qonto riflette i movimenti contabilizzati, non le operazioni in attesa di settlement
- Qonto non e' l'unico conto — verificare se ci sono altri conti bancari (es. BPM) non su Qonto
