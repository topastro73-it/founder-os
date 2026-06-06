# Customer Success Skill

Monitoraggio salute clienti/partner, prevenzione churn, espansione account. Usata da CEO, Sales, Chief of Staff.

## Health Score Model

Ogni cliente/partner ha un **Health Score** (0–100) calcolato su 5 indicatori pesati:

| # | Indicatore | Peso | Fonte dati | Come si misura |
|---|-----------|------|-----------|----------------|
| 1 | **Utenti Onboarded** | 25% | Piattaforma | N. utenti/clienti finali registrati vs target contrattuale. Score: (actual / target) * 100, cap 100 |
| 2 | **Utenti Attivi** (30gg) | 25% | Piattaforma | Utenti con almeno 1 azione o login negli ultimi 30 giorni. Score: (attivi / onboarded) * 100 |
| 3 | **Churn Utenti** (trimestre) | 20% | Piattaforma | % utenti/clienti finali persi nel trimestre. Score: max(0, 100 - churn% * 10). Churn 0% = 100, Churn 10% = 0 |
| 4 | **Engagement Referenti** | 15% | CRM/Piattaforma | N. attività generate (proposte, report, campagne) nel mese. Score: 0 se nessuna attivita, 50 se sporadica, 100 se regolare |
| 5 | **NPS / Soddisfazione** | 15% | Survey / Feedback | Ultimo NPS score normalizzato 0–100. Se non disponibile: stima da ticket supporto e sentiment |

### Fasce Health Score

| Fascia | Score | Significato | Azione |
|--------|-------|-------------|--------|
| **Healthy** | 80–100 | Cliente/partner attivo, utilizzo in crescita | Expansion play — upsell tier o servizi |
| **Stable** | 60–79 | Funziona ma non cresce | Engagement boost — training, co-marketing |
| **At Risk** | 40–59 | Segnali di disengagement | Intervento proattivo — call con Sales + PM |
| **Critical** | 0–39 | Churn imminente | Escalation CEO — rescue plan entro 7 giorni |

### Formula

```
Health Score = (Utenti_Onboarded * 0.25) + (Utenti_Attivi * 0.25) + (Churn_Score * 0.20) + (Engagement * 0.15) + (NPS * 0.15)
```

---

## Comandi

| Comando | Descrizione | Output |
|---------|------------|--------|
| `partner-health` | Calcola health score per un cliente/partner specifico o per tutti | Report con score, trend, alert |
| `partner-review` | Review trimestrale di un cliente/partner con raccomandazioni | Documento in `docs/reports/partner-review-{partner}-{date}.md` |
| `churn-analysis` | Analisi churn con pattern e cause | Report in `docs/reports/churn-analysis-{date}.md` |
| `partner-qbr` | Genera QBR (Quarterly Business Review) deck per cliente/partner | Documento in `docs/reports/qbr-{partner}-{quarter}.md` |
| `expansion-plan` | Piano di espansione per clienti/partner healthy/stable | Piano in `docs/reports/expansion-{partner}-{date}.md` |
| `alert-check` | Scansiona tutti i clienti/partner per alert critici | Lista alert con azioni suggerite |

---

## Comando: partner-health

### Input
- Partner/cliente slug (opzionale — se omesso, tutti i clienti/partner)

### Processo
1. Leggi scheda cliente/partner da `company/customers/partners/{slug}.md`
2. Calcola ogni indicatore con i dati disponibili
3. Calcola health score complessivo
4. Confronta con score precedente per trend
5. Genera alert se score < 60 o drop > 15 punti

### Output format
```
## Partner Health — {nome cliente/partner}

| Indicatore | Score | Dettaglio |
|-----------|-------|-----------|
| Utenti Onboarded | 85 | 34/40 target |
| Utenti Attivi | 70 | 24/34 attivi 30gg |
| Churn Utenti | 90 | 1% trimestre |
| Engagement Referenti | 60 | 8 attività/mese (sporadico) |
| NPS | 75 | Ultimo NPS: 45 |

**Health Score: 77/100 — Stable**
Trend: ↓ da 82 (ultimo check)

### Raccomandazioni
1. Engagement referenti in calo → schedulare training session
2. ...
```

---

## Comando: partner-review

### Input
- Partner/cliente slug

### Processo
1. Esegui `partner-health` per il cliente/partner
2. Analizza storico metriche (ultimi 3 mesi)
3. Identifica pattern e trend
4. Genera raccomandazioni concrete con owner e deadline

### Output
File `docs/reports/partner-review-{partner}-{YYYY-MM-DD}.md` con:
- Executive summary (3 righe)
- Health score + trend
- Metriche dettagliate con storico
- Rischi identificati
- Piano d'azione (max 5 azioni, ciascuna con owner e deadline)
- Handoff suggerito (Sales per expansion, PM per feature request, CEO per escalation)

---

## Comando: churn-analysis

### Processo
1. Scansiona tutti i clienti/partner con health score < 60
2. Identifica pattern comuni (basso onboarding, scarso engagement, etc.)
3. Calcola churn rate complessivo e per segmento
4. Genera root cause analysis

### Output
File `docs/reports/churn-analysis-{YYYY-MM-DD}.md`

---

## Comando: partner-qbr

### Input
- Partner/cliente slug
- Quarter (es. Q1-2026)

### Processo
1. Raccogli tutte le metriche del quarter
2. Genera executive summary
3. Prepara talking points per la call
4. Suggerisci expansion opportunities

### Output
File `docs/reports/qbr-{partner}-{quarter}.md` con:
- Risultati del quarter (metriche vs target)
- Wins e highlights
- Aree di miglioramento
- Piano per il prossimo quarter
- Expansion opportunity (se health > 70)

---

## Comando: expansion-plan

### Input
- Partner/cliente slug

### Prerequisito
- Health score >= 60 (Stable o Healthy)

### Processo
1. Analizza tier attuale e utilizzo feature
2. Identifica gap tra tier attuale e potenziale
3. Calcola revenue potenziale da upgrade
4. Genera piano con timeline e azioni

### Output
File `docs/reports/expansion-{partner}-{YYYY-MM-DD}.md`

---

## Comando: alert-check

### Processo
1. Scansiona `company/customers/partners/*.md`
2. Per ogni cliente/partner, calcola health score (quick mode — dati disponibili)
3. Genera alert per:
   - Score < 40 → **CRITICAL**
   - Score drop > 15 punti in 30 giorni → **WARNING**
   - Utenti attivi < 30% degli onboarded → **LOW ENGAGEMENT**
   - Nessuna attivita referenti in 30+ giorni → **DORMANT**
   - Contratto in scadenza entro 60 giorni → **RENEWAL**
4. **Aging trattative** — scansiona `company/customers/opportunities/*.md` (skill `.skills/opportunity-management/SKILL.md`, sezione 3) e genera alert per:
   - `last-activity` oltre la soglia critical, o blocker `severity: high`, o next-step scaduto oltre la soglia warning → **STALLED 🔴**
   - fermo oltre la soglia warning, o `status-flag: blocked` da oltre attention → **AGING 🟠**
   - Opportunità open **senza `owner-sales`** → **NO-OWNER** (priorità: weighted alto)

### Output format
```
## Partner Alerts — {data}

| Partner | Score | Alert | Azione suggerita |
|---------|-------|-------|-----------------|
| partner-a | 35 | CRITICAL | Rescue call entro 7gg — escalation CEO |
| partner-b | 72→55 | WARNING | Call Sales entro 14gg |
| partner-c | — | DORMANT | Nessuna attivita da 45gg — ricontattare |
```

---

## Integrazione CEO Cadence

### Giornaliero
- `alert-check` automatico: se ci sono alert CRITICAL, vengono inclusi nel check giornaliero al CEO

### Settimanale
- Summary health score di tutti i clienti/partner attivi
- Clienti/partner con score in calo significativo

### Mensile
- QBR reminder per clienti/partner con review schedulata nel mese
- Churn analysis del mese precedente
- Expansion opportunities identificate

---

## Dove vivono i dati

| Dato | Path |
|------|------|
| Schede clienti/partner | `company/customers/partners/{slug}.md` |
| Template scheda | `company/customers/partners/TEMPLATE.md` |
| Report review | `docs/reports/partner-review-*.md` |
| Report churn | `docs/reports/churn-analysis-*.md` |
| Report QBR | `docs/reports/qbr-*.md` |
| Piani espansione | `docs/reports/expansion-*.md` |
| Segmenti clienti | `company/customers/segments.md` |
| KPI | `company/metrics/kpis.md` |
