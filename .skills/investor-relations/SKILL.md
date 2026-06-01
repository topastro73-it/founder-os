# Investor Relations Skill

Gestione relazione investitori, fundraising readiness, board governance. Usata da CEO, CFO, Legal.

## Principi

1. **Trasparenza costruttiva**: condividi i dati reali, inquadra i problemi come opportunità con piano d'azione
2. **Narrativa coerente**: ogni touchpoint con un investitore rinforza la stessa storia (vision → traction → ask)
3. **Preparazione > improvvisazione**: mai andare a una call senza brief, mai inviare dati senza context
4. **Compliance**: disclaimer legale su ogni analisi di term sheet o clausola contrattuale

---

## Comandi

| Comando | Descrizione | Output |
|---------|------------|--------|
| `data-room` | Checklist completa data room per fundraising | Report con gap analysis |
| `pitch-prep` | Preparazione call con investitore specifico | Brief in `docs/investor-updates/` |
| `term-sheet-review` | Analisi clausole term sheet con benchmark | Analisi in `docs/investor-updates/` |
| `board-prep` | Preparazione board meeting | Deck outline in `docs/investor-updates/` |
| `cap-table` | Genera/aggiorna cap table | `company/finance/cap-table.md` |
| `investor-crm` | Traccia relazioni e pipeline investitori | `company/finance/investor-pipeline.md` |

---

## Comando: data-room

### Processo

1. Scansiona il repo per verificare la presenza di ogni documento richiesto
2. Per ogni categoria, segna: presente / parziale / mancante
3. Genera report con priorità di completamento

### Checklist Data Room

#### 1. Company Overview
| Documento | Path atteso | Verifica |
|-----------|------------|---------|
| Pitch deck aggiornato | `docs/investor-updates/pitch-deck-*.md` | Scansiona |
| One-pager / Executive summary | `docs/investor-updates/exec-summary.md` | Scansiona |
| Company profile | `.agents/_shared/COMPANY.md` | Sempre presente |
| Vision e strategia | `company/strategy/vision.md` | Scansiona |
| OKR correnti | `company/strategy/okr-*.md` | Scansiona |

#### 2. Financials
| Documento | Path atteso | Verifica |
|-----------|------------|---------|
| Financial model / proiezioni | `company/finance/financial-model.md` | Scansiona |
| Pricing attuale | `company/finance/pricing.md` | Scansiona |
| KPI dashboard | `company/metrics/kpis.md` | Scansiona |
| Cap table | `company/finance/cap-table.md` | Scansiona |
| Burn rate e runway | In `company/metrics/kpis.md` | Verifica dati compilati |
| MRR / ARR storico | In `company/metrics/kpis.md` | Verifica dati compilati |

#### 3. Product
| Documento | Path atteso | Verifica |
|-----------|------------|---------|
| Roadmap | `company/product/roadmap.md` | Scansiona |
| Specs / PRD principali | `company/product/specs/*.md` | Conta e verifica status |
| Backlog | `company/product/backlog.md` | Scansiona |
| Architecture overview | `docs/internal-memos/architecture-*.md` | Scansiona |
| Demo / screenshot | `docs/marketing/demo-*` | Scansiona |

#### 4. Market
| Documento | Path atteso | Verifica |
|-----------|------------|---------|
| Segmenti clienti | `company/customers/segments.md` | Scansiona |
| Competitor analysis / battlecards | `company/competitors/battlecards/*.md` | Conta |
| TAM/SAM/SOM | `company/strategy/market-sizing.md` | Scansiona |
| Case study / testimonial | `docs/marketing/case-study-*.md` | Scansiona |

#### 5. Team
| Documento | Path atteso | Verifica |
|-----------|------------|---------|
| Team overview | `.agents/_shared/TEAM.md` | Sempre presente |
| Organigramma | `company/team/org-chart.md` | Scansiona |
| Hiring plan | `company/team/hiring-plan.md` | Scansiona |

#### 6. Legal
| Documento | Path atteso | Verifica |
|-----------|------------|---------|
| Statuto / atto costitutivo | `docs/legal/statuto.md` o `.pdf` | Scansiona |
| Certificazioni (ISO, altri) | In `.agents/_shared/COMPANY.md` | Verifica sezione |
| Privacy policy / GDPR | `docs/legal/privacy-*.md` | Scansiona |
| Contratti tipo partner | `docs/legal/contract-template-*.md` | Scansiona |
| IP ownership / brevetti | `docs/legal/ip-*.md` | Scansiona |

### Output format
```
## Data Room Readiness — {data}

### Summary
- Presenti: N/M documenti (X%)
- Parziali: N (dati incompleti)
- Mancanti: N

### Gap Analysis (priorità alta → bassa)

| # | Documento | Stato | Priorità | Azione suggerita | Owner |
|---|-----------|-------|----------|-----------------|-------|
| 1 | Financial model | MANCANTE | CRITICO | CFO deve creare proiezioni 3Y | CFO |
| 2 | Cap table | PARZIALE | ALTO | Completare con round attuale | CFO + Legal |
| 3 | Case study cliente | MANCANTE | MEDIO | Marketing produce case study | Marketing |

### Prossimi passi
1. [Azione con owner e deadline]
```

Salva in: `docs/investor-updates/data-room-audit-{YYYY-MM-DD}.md`
Commit: `[ceo] investor: data room readiness audit`

---

## Comando: pitch-prep

### Input
- Nome investitore / fondo
- Tipo meeting (intro call, deep dive, follow-up, partner meeting)
- Data meeting

### Processo
1. Cerca informazioni sull'investitore:
   - Portfolio: quali startup simili hanno finanziato?
   - Thesis: su quali settori/stage sono focalizzati?
   - Partner: chi sarà in call? Quale background ha?
2. Analizza fit con {{COMPANY_NAME}}:
   - Allineamento thesis-prodotto
   - Portfolio conflict (hanno già investito in aziende B2B simili / stesso mercato?)
   - Stage fit (investono in seed/pre-seed?)
3. Prepara brief con:
   - Domande probabili (top 10 basate sul profilo investitore)
   - Red flag da anticipare (metriche deboli, gap nel team, mercato)
   - Talking points personalizzati (cosa del nostro pitch risuona con la loro thesis)
   - Ask chiaro (quanto, per cosa, timeline)

### Output format
```
## Pitch Prep — {nome investitore}
Data meeting: {data} | Tipo: {tipo}

### Profilo investitore
- Fondo: {nome}
- Focus: {settori, stage, geography}
- Portfolio rilevante: {startup simili}
- Partner in call: {nome, background}

### Fit Analysis
| Dimensione | Score | Note |
|-----------|-------|------|
| Thesis alignment | Alto/Medio/Basso | {perché} |
| Stage fit | Alto/Medio/Basso | {perché} |
| Portfolio conflict | Si/No | {dettagli} |

### Top 10 domande probabili
1. {Domanda} → **Risposta suggerita**: {risposta}
2. ...

### Red flag da gestire
1. {Red flag} → **Framing**: {come presentarlo}

### Talking points personalizzati
1. {Punto che risuona con la thesis dell'investitore}

### Ask
- Importo: €{X}
- Utilizzo: {breakdown}
- Timeline: {quando chiudere}
```

Salva in: `docs/investor-updates/pitch-prep-{slug-investitore}-{YYYY-MM-DD}.md`
Commit: `[ceo] investor: pitch prep for {investitore}`

---

## Comando: term-sheet-review

### Input
- Term sheet (testo o riferimento al documento)

### Disclaimer

> ⚠️ **DISCLAIMER LEGALE**: Questa analisi è generata da un sistema AI a scopo informativo e di preparazione interna. NON costituisce consulenza legale. Prima di firmare qualsiasi term sheet o accordo vincolante, consultare SEMPRE un avvocato specializzato in venture capital e diritto societario. {{COMPANY_NAME}} non si assume responsabilità per decisioni prese sulla base di questa analisi.

Questo disclaimer DEVE essere incluso all'inizio di ogni output di `term-sheet-review`.

### Processo
1. Estrai le clausole chiave dal term sheet
2. Per ogni clausola:
   - Spiega cosa significa in termini semplici
   - Indica se è standard / favorevole / sfavorevole rispetto al benchmark di mercato
   - Suggerisci punti di negoziazione se sfavorevole
3. Genera summary con raccomandazione complessiva

### Clausole analizzate
| Clausola | Cosa controllare |
|----------|-----------------|
| Valuation (pre/post-money) | Diluizione implicita, confronto con comparables |
| Liquidation preference | 1x non-participating = standard; >1x o participating = red flag |
| Anti-dilution | Weighted average = standard; full ratchet = sfavorevole |
| Board composition | Founder majority = ideale; investor majority pre-Series A = red flag |
| Vesting | 4 anni con 1 anno cliff = standard |
| Drag-along / Tag-along | Soglie, condizioni di attivazione |
| ESOP pool | Size pre/post money, diluizione implicita |
| Pro-rata rights | Standard per lead investor |
| Information rights | Frequenza e dettaglio reporting |
| Protective provisions | Quali decisioni richiedono approvazione investitore |
| No-shop / Exclusivity | Durata (30-60gg = standard; >90gg = eccessivo) |
| Governing law | Giurisdizione applicabile |

### Output format
```
## Term Sheet Analysis — {investitore}

⚠️ DISCLAIMER: [disclaimer completo]

### Summary
| Clausola | Status | Note |
|----------|--------|------|
| Valuation | ✅ Standard | Pre-money €Xm, diluizione Y% |
| Liquidation pref | ⚠️ Da negoziare | 1.5x participating — chiedere 1x non-participating |
| Anti-dilution | ✅ Standard | Weighted average |
| Board | 🔴 Red flag | 2 investitori su 3 — richiedere parità |

### Analisi dettagliata
[Per ogni clausola: spiegazione, benchmark, raccomandazione]

### Raccomandazione
[Procedere / Negoziare / Rifiutare — con motivazione]

### Punti di negoziazione prioritari
1. {Clausola} — {cosa chiedere} — {perché}
```

Salva in: `docs/investor-updates/term-sheet-review-{slug}-{YYYY-MM-DD}.md`
Commit: `[ceo] investor: term sheet analysis for {investitore}`

Handoff: **Legal** per review formale

---

## Comando: board-prep

### Input
- Data board meeting
- Agenda (opzionale — se non fornita, usa agenda standard)

### Processo
1. Raccogli dati aggiornati da:
   - `company/metrics/kpis.md` — KPI attuali
   - `company/product/roadmap.md` — stato roadmap
   - `company/finance/pricing.md` — pricing e revenue
   - `company/customers/partners/*.md` — stato partner
   - `decisions/` — decisioni recenti
   - `company/strategy/` — OKR e strategia
2. Identifica gap nei dati (metriche non aggiornate)
3. Genera outline del board deck

### Agenda standard board meeting
1. **KPI Update** (5 min) — MRR, ARR, churn, pipeline, runway
2. **Product Update** (10 min) — shipped, in-dev, roadmap changes
3. **Go-to-Market** (10 min) — partner pipeline, deal status, marketing highlights
4. **Financial Update** (5 min) — burn, runway, cash position
5. **Team** (5 min) — hiring, org changes
6. **Asks** (10 min) — cosa serve dal board (intro, advice, decisioni)
7. **Discussion** (15 min) — topic strategico del quarter

### Output
```
## Board Meeting Prep — {data}

### Pre-meeting checklist
- [ ] KPI aggiornati (ultimo update: {data})
- [ ] Financial update dal CFO
- [ ] Product demo/screenshot pronti
- [ ] Partner pipeline aggiornata
- [ ] Asks definiti

### Deck outline
[Sezione per sezione con dati e talking points]

### Dati mancanti
| Dato | Owner | Deadline |
|------|-------|----------|
```

Salva in: `docs/investor-updates/board-prep-{YYYY-MM-DD}.md`
Commit: `[ceo] investor: board meeting prep {data}`

---

## Comando: cap-table

### Processo
1. Leggi `company/finance/cap-table.md`
2. Se vuoto/template: chiedi all'utente i dati fondamentali:
   - Soci fondatori e % quote
   - Round precedenti (importo, valuation, quote cedute)
   - ESOP pool (se presente)
3. Calcola: fully diluted ownership, diluizione per round futuro
4. Aggiorna il file

### Output
Aggiorna `company/finance/cap-table.md`
Commit: `[cfo] finance: updated cap table`

---

## Comando: investor-crm

### Processo
1. Leggi `company/finance/investor-pipeline.md`
2. Mostra stato attuale della pipeline
3. Permetti di aggiungere/aggiornare contatti:
   - Nome fondo + partner
   - Stage (cold / warm intro / first call / deep dive / term sheet / closed)
   - Note ultimo contatto
   - Prossimo step
   - Fit score (1-5)
4. Aggiorna il file

### Output
Aggiorna `company/finance/investor-pipeline.md`
Commit: `[ceo] investor: updated investor pipeline`

---

## Integrazione CEO Cadence

### Mensile
- **Runway alert**: se runway < 9 mesi (calcolato da burn rate e cash in `company/metrics/kpis.md`), genera alert automatico:
  ```
  🚨 **RUNWAY ALERT** — Runway stimato: {N} mesi ({data esaurimento stimata}).
  Azione: avviare processo fundraising o ridurre burn. Vuoi che prepari la data room?
  ```
- Se investor pipeline ha deal in stage `deep dive` o `term sheet`, remind nel check mensile

### Settimanale
- Se ci sono meeting con investitori schedulati nella settimana, remind di preparare pitch-prep

---

## Dove vivono i dati

| Dato | Path |
|------|------|
| Cap table | `company/finance/cap-table.md` |
| Investor pipeline | `company/finance/investor-pipeline.md` |
| Pitch prep, board prep, term sheet review | `docs/investor-updates/` |
| Data room audit | `docs/investor-updates/` |
| Financial model | `company/finance/financial-model.md` |
| KPI (per runway calc) | `company/metrics/kpis.md` |
| Pricing | `company/finance/pricing.md` |
