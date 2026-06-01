# Data & Metrics Skill

Gestione fonti dati, cadenza aggiornamento, comandi interattivi per mantenere le metriche sempre fresche. Usata da CEO, CFO, PM, Chief of Staff.

## Mappa Fonti Dati

| Metrica | Fonte primaria | Fonte secondaria | Cadenza aggiornamento | Owner |
|---------|---------------|-----------------|----------------------|-------|
| **MRR / ARR** | Stripe / Fatturazione | Spreadsheet CFO | Mensile (entro il 5) | CFO |
| **Clienti attivi** | Piattaforma (tenant attivi) | CRM | Settimanale | PM |
| **Utenti/clienti onboarded** (per partner) | Piattaforma | Partner report | Settimanale | PM |
| **Utenti/clienti attivi** (30gg) | Piattaforma (login/attività) | — | Settimanale | PM |
| **Churn rate** | Piattaforma + CRM | — | Mensile | Sales |
| **Pipeline value** | CRM (HubSpot) | Sales tracker | Settimanale | Sales |
| **Win rate** | CRM | — | Mensile | Sales |
| **Sales cycle** | CRM | — | Mensile | Sales |
| **CAC** | Marketing spend / new logos | — | Mensile | CFO + Marketing |
| **NPS** | Survey tool | Feedback qualitativo | Trimestrale | PM |
| **WAU** | Piattaforma analytics | — | Settimanale | PM |
| **Burn rate** | Conto corrente / Contabilita | — | Mensile (entro il 10) | CFO |
| **Runway** | Burn rate + cash | — | Mensile | CFO |
| **LTV/CAC** | Calcolato (LTV = ACV / churn) | — | Trimestrale | CFO |
| **Partner health score** | Skill Customer Success | — | Settimanale | Sales/CoS |
| **Feature adoption** | Piattaforma analytics | — | Mensile | PM |
| **Uptime** | Monitoring (UptimeRobot etc.) | — | Continuo | CTO |

---

## Cadenza di Aggiornamento

### Settimanale (ogni lunedi)
- Clienti attivi
- Utenti/clienti onboarded / attivi (per partner)
- Pipeline value
- WAU
- Partner health score (quick)

### Mensile (entro il 10 del mese)
- MRR / ARR
- Churn rate
- Win rate, Sales cycle
- CAC
- Burn rate, Runway
- Feature adoption

### Trimestrale
- NPS survey
- LTV/CAC ratio
- Partner QBR data
- Competitive benchmark

---

## Comandi

| Comando | Descrizione | Output |
|---------|------------|--------|
| `update-metrics` | Guida interattiva per aggiornare le metriche | Aggiorna `company/metrics/kpis.md` |
| `partner-metrics` | Aggiorna metriche specifiche per partner | Aggiorna scheda partner |
| `dashboard` | Genera snapshot metriche correnti | Report sintetico |
| `freshness-check` | Verifica quali metriche sono scadute | Lista metriche da aggiornare |

---

## Comando: update-metrics

### Processo (interattivo)
1. Esegui `freshness-check` per identificare metriche scadute
2. Per ogni metrica scaduta, chiedi all'utente il valore aggiornato:
   ```
   Le seguenti metriche necessitano aggiornamento:

   1. MRR (ultimo: 2026-02-05) — Qual e il MRR attuale?
   2. Churn rate (ultimo: 2026-02-05) — Qual e il churn rate del mese?
   3. Pipeline value (ultimo: 2026-03-08) — Valore pipeline attuale?

   Rispondi con i numeri o "skip" per saltare.
   ```
3. Aggiorna `company/metrics/kpis.md` con i nuovi valori
4. Aggiorna timestamp `last-updated` per ogni metrica modificata
5. Commit: `[system] metrics: updated {lista metriche}`

### Regole
- Non inventare dati — chiedi SEMPRE all'utente
- Se l'utente non ha un dato, segnalo come "non disponibile" e suggerisci la fonte
- Registra la data di aggiornamento per ogni metrica

---

## Comando: partner-metrics

### Input
- Partner slug

### Processo
1. Leggi scheda partner da `company/customers/partners/{slug}.md`
2. Chiedi all'utente le metriche aggiornate:
   - Utenti/clienti onboarded
   - Utenti/clienti attivi (30gg)
   - Revenue generato dal partner
   - N. proposte inviate nel mese
   - Feedback/NPS
3. Aggiorna scheda partner
4. Ricalcola health score (invoca skill Customer Success)

---

## Comando: dashboard

### Output format
```
## Metrics Dashboard — {data}

### Revenue
| Metrica | Valore | vs Mese Prec | vs Target | Freshness |
|---------|--------|-------------|-----------|-----------|
| MRR | €X.XXX | +X% | X% del target | Aggiornato il DD/MM |
| ARR | €XX.XXX | — | — | Calcolato |

### Growth
| Metrica | Valore | Trend | Freshness |
|---------|--------|-------|-----------|
| Partner attivi | N | +N | DD/MM |
| Clienti/utenti totali | N | +N | DD/MM |

### Sales
| Metrica | Valore | Trend | Freshness |
|---------|--------|-------|-----------|
| Pipeline | €X.XXX | — | DD/MM |
| Win rate | X% | — | DD/MM |

### Health
| Partner | Score | Trend |
|---------|-------|-------|
| Partner A | 82 | ↑ |
| Partner B | 65 | ↓ |

Dati stale: {lista metriche con freshness > soglia}
```

---

## Comando: freshness-check

### Processo
1. Leggi `company/metrics/kpis.md` — controlla data ultimo aggiornamento di ogni metrica
2. Leggi `company/customers/partners/*.md` — controlla `last-metrics-update`
3. Confronta con la cadenza attesa (dalla mappa fonti dati sopra)
4. Genera report

### Output format
```
## Metrics Freshness Check — {data}

### Metriche SCADUTE (richiedono aggiornamento)
| Metrica | Ultimo aggiornamento | Cadenza | Scaduta da | Owner |
|---------|---------------------|---------|-----------|-------|
| MRR | 2026-02-05 | Mensile | 43 giorni | CFO |
| Pipeline value | 2026-03-08 | Settimanale | 12 giorni | Sales |

### Metriche OK
| Metrica | Ultimo aggiornamento | Prossimo aggiornamento |
|---------|---------------------|----------------------|
| Clienti attivi | 2026-03-18 | 2026-03-25 |

### Partner senza metriche aggiornate
| Partner | Ultimo aggiornamento | Scaduto da |
|---------|---------------------|-----------|
| partner-x | 2026-02-15 | 33 giorni |

Suggerimento: esegui `update-metrics` per aggiornare le metriche scadute.
```

---

## Integrazione CEO Cadence

### Giornaliero
- `freshness-check` automatico: se ci sono metriche critiche scadute (MRR, burn rate, runway), vengono segnalate nel check giornaliero

### Settimanale
- Summary freshness di tutte le metriche
- Reminder per metriche settimanali non aggiornate

### Mensile
- Freshness report completo incluso nel check mensile
- Suggerimento per metriche trimestrali in scadenza

---

## Dove vivono i dati

| Dato | Path |
|------|------|
| KPI dashboard | `company/metrics/kpis.md` |
| Schede partner (metriche) | `company/customers/partners/{slug}.md` |
| Report metriche | `docs/reports/metrics-*.md` |
| Segmenti clienti | `company/customers/segments.md` |
