# 📊 KPI — Metriche Chiave

> Come stai andando. Compilabile via `/setup`; aggiornata nelle routine settimanali/mensili.
> Aggiorna i valori `{{...}}` con i tuoi numeri reali.

## Snapshot attuale

| Metrica | Valore | Trend | Aggiornato |
|---------|--------|-------|-----------|
| MRR | {{MRR}} | — | {{DATE}} |
| ARR | {{ARR}} | — | {{DATE}} |
| Clienti attivi | {{ACTIVE_CUSTOMERS}} | — | {{DATE}} |
| Churn mensile | {{CHURN}} | — | {{DATE}} |
| NRR | {{NRR}} | — | {{DATE}} |
| CAC | {{CAC}} | — | {{DATE}} |
| LTV | {{LTV}} | — | {{DATE}} |
| Burn mensile | {{BURN}} | — | {{DATE}} |
| Runway (mesi) | {{RUNWAY}} | — | {{DATE}} |

## Funnel (mese corrente)

| Stadio | Valore |
|--------|--------|
| Lead | {{LEADS}} |
| Qualified | {{QUALIFIED}} |
| Demo/Trial | {{TRIALS}} |
| Closed Won | {{CLOSED_WON}} |

## Soglie di alert (vedi PRINCIPLES.md)
- Runway < 9 mesi → escalation CFO → CEO (fundraising).
- Churn > soglia → review Customer Success.
