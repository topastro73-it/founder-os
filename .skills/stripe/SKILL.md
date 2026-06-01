# Stripe Skill

Integrazione con Stripe via MCP connector (Cowork).
Gestisce pagamenti, fatture, clienti, subscription e prodotti.
Usata da CFO, CEO, Chief of Staff, Sales.

## Prerequisiti

Connector MCP **Stripe** installato e connesso in Cowork.
(Non servono variabili d'ambiente — l'auth è gestita dal connector.)

Verifica disponibilità: se i tool `mcp__*__list_invoices`, `mcp__*__list_customers` ecc. rispondono, Stripe è attivo.

## Tool MCP disponibili

| Tool | Descrizione | Quando usarlo |
|------|------------|---------------|
| `retrieve_balance` | Saldo Stripe corrente (available, pending, instant) | Cashflow snapshot, daily briefing |
| `list_invoices` | Lista fatture (filtro per customer, limit) | Fatturato, aging, reconciliation |
| `list_payment_intents` | Lista pagamenti (filtro per customer, limit) | Transazioni, conferma incassi |
| `list_customers` | Lista clienti Stripe | Anagrafica, segmentazione |
| `list_subscriptions` | Lista subscription attive | MRR, churn analysis |
| `list_products` | Lista prodotti/piani | Catalogo pricing |
| `list_prices` | Lista prezzi associati ai prodotti | Pricing tiers, confronti |
| `list_coupons` | Lista coupon/sconti | Promozioni attive |
| `list_disputes` | Lista dispute/chargeback | Risk management |
| `fetch_stripe_resources` | Dettaglio singolo oggetto per ID (in_, pi_, cus_, sub_, prod_, price_, ch_) | Deep dive su fattura, cliente, pagamento |
| `search_stripe_resources` | Ricerca full-text su risorse Stripe | Trova oggetti per nome, email, importo |
| `get_stripe_account_info` | Info account Stripe (business, country, capabilities) | Setup verification |
| `search_stripe_documentation` | Cerca nella documentazione Stripe | Troubleshooting, best practice |

## Comandi

| Comando | Descrizione | Output |
|---------|------------|--------|
| `stripe-snapshot` | Saldo + fatture recenti + subscription attive | Sezione in daily briefing o report |
| `stripe-invoices [anno]` | Lista fatture filtrate per anno con totali | Report in `docs/reports/` |
| `stripe-mrr` | Calcola MRR da subscription attive | Aggiorna `company/metrics/kpis.md` sezione MRR |
| `stripe-customers` | Anagrafica clienti Stripe con subscription status | Cross-ref con `company/customers/` |
| `stripe-reconcile` | Incrocia pagamenti Stripe con fatture FIC/Qonto | Identifica discrepanze |

## Agenti autorizzati

CFO (owner), CEO, Chief of Staff, Sales

## Flusso standard

```
# Daily (nel morning briefing CEO/CoS)
→ retrieve_balance per saldo corrente
→ list_invoices (limit 5) per ultime fatture

# Settimanale (lunedì, dopo sync FIC e Qonto)
→ stripe-invoices per fatturato periodo
→ stripe-reconcile per riconciliazione cross-platform

# Mensile (review finanziaria)
→ stripe-mrr per calcolo MRR/churn
→ stripe-customers per aggiornamento anagrafica
→ list_disputes per check chargeback
```

## Note importanti

- **Importi**: Stripe restituisce importi in centesimi (minor units). Dividere per 100 per EUR.
- **Timestamp**: Stripe usa Unix timestamp (secondi). Convertire con `datetime.fromtimestamp()`.
- **Valuta**: Account configurato in EUR.
- **Rate limit**: gestito dal connector MCP, nessun limite pratico per uso normale.
- **Fallback**: se il connector MCP non è disponibile, i dati più recenti sono in `company/finance/` (ultimo sync). Segnalare al CEO che Stripe MCP è offline.
- **Cross-reference**: i clienti Stripe (cus_*) vanno mappati con le schede partner in `company/customers/partners/` e con i contatti HubSpot CRM.

## Integrazione con altre skill

| Skill | Integrazione |
|-------|-------------|
| **Fatture in Cloud** | Riconcilia fatture FIC (fiscali IT) con invoice Stripe (pagamenti) |
| **Qonto** | I payout Stripe arrivano su Qonto — verifica con `qonto reconcile` |
| **Data & Metrics** | MRR, churn rate, ARPU calcolati da subscription Stripe |
| **ERP** | Stripe come sorgente dati revenue per il modulo finance ERP |
| **Customer Success** | Status pagamento cliente da Stripe informa health score |
| **Admin & Controllo** | Stripe dashboard per controllo gestione ricavi |
