# FIC Command: aging-report

Calcola l'aging dei crediti scaduti da Fatture in Cloud e aggiorna `company/metrics/kpis.md`.

## Agenti autorizzati

CFO, CEO, Chief of Staff

## Invocazione

```
/cfo fatture-in-cloud aging-report
```

## Processo

### Passo 1 — Esegui aging via script

```bash
python3 scripts/fic_sync.py aging
```

Lo script recupera tutte le fatture con `payment_status != paid` degli ultimi 24 mesi
e calcola per ognuna i giorni di scaduto: `today - due_date`.

### Passo 2 — Genera tabella aging

Per ogni fattura scaduta (giorni > 0):

| Cliente | N. Fattura | Importo | Scadenza | Giorni scaduto | Fascia |
|---------|-----------|---------|----------|---------------|--------|
| Acme Srl | 5/2026 | €4.000 | 2026-02-01 | 51gg | 31–60 |
| Partner X | 3/2026 | €10.000 | 2025-12-31 | 83gg | 61–90 |
| Cliente Y | 12/2025 | €5.000 | 2025-10-02 | 172gg | 90+ |

Fascia:
- `0–30gg` — monitoraggio
- `31–60gg` — primo sollecito
- `61–90gg` — secondo sollecito + CEO alert
- `90+gg` — escalation legale / stralcio

### Passo 3 — Aggiorna kpis.md

Nella sezione `## Financial` di `company/metrics/kpis.md`, aggiorna la riga:

```
| Crediti scaduti | €XX.XXX | ⚠️ |
```

E aggiorna il commento dettaglio con la lista per cliente e giorni:

```markdown
> **Crediti scaduti (€XX.XXX)**: Cliente A €X.XXX (Ngg), Cliente B €X.XXX (Ngg), ...
```

### Passo 4 — Alert al CEO Routine

Se ci sono crediti nella fascia 90+ giorni, aggiungi una riga in `company/ceo-cadence.md`
sezione Log risposte con alert:

```
- ⚠️ CREDITI 90+gg: [cliente] €[importo] ([Ngg]) — richiede decisione (sollecito legale / stralcio)
```

### Passo 5 — Commit

```bash
git add company/finance/fatturazione.md company/metrics/kpis.md company/ceo-cadence.md
git commit -m "[cfo] fatture-in-cloud: aging report YYYY-MM-DD — €X scaduto, N fatture"
```

## Soglie di azione

| Fascia | Azione automatica |
|--------|-----------------|
| 31–60gg | Nota nel log cadence |
| 61–90gg | Alert CEO nel prossimo daily briefing |
| 90+gg | Urgente nel daily briefing + opzioni A/B/C (sollecito legale / accordo / stralcio) |
| >€50.000 totale scaduto | Flag nella sezione Financial del weekly digest |
