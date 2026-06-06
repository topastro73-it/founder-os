# Opportunity Management Skill

Gestione del **cockpit commerciale**: modello dati account↔opportunità, pipeline stage, aging dei blocchi, board sinottico e drill-down sul singolo deal. È la **single source of truth della metodologia** commerciale: Sales, Chief of Staff e CEO Routine si rifanno a questa skill per leggere/scrivere lo stato delle trattative.

Owner primario: **Sales**. Usata da: Sales, Chief of Staff, CEO Routine, CFO (per coverage/forecast).

> **Il repo è il source of truth della pipeline.** Un CRM esterno (HubSpot/Salesforce/…) resta opzionale; il campo `crm-id` mantiene il link ma non è la fonte.

---

## 1. Modello dati: Account vs Opportunità

| Oggetto | File | Cos'è |
|---------|------|-------|
| **Account** | `company/customers/partners/{slug}.md` | L'azienda: anagrafica, contatti, health post-vendita, onboarding, **indice** delle sue opportunità. |
| **Opportunità** | `company/customers/opportunities/{opp-slug}.md` | Una singola trattativa. Un account può averne N. Contiene lo **stato vivo**: stage, valore, blocker, aging. |
| **Board** | `company/customers/PIPELINE.md` | Vista sinottica generata. Snapshot di convenienza — la verità è il frontmatter delle opportunità. |
| **Config** | `company/customers/pipeline-config.yaml` | Target weighted, tassonomia stage→probabilità, segmenti, soglie aging. |
| **Funnel** (opzionale) | `company/customers/{canale}-funnel.md` | Tracker consolidato del prospecting su un canale (universo→contattati→qualificati). Vedi `target-funnel.md`. |

**Regole di relazione:**
- Ogni opportunità ha `account: {slug}` (FK all'account) e `segment:` (key da `pipeline-config.yaml`).
- `opp-slug` = `{account}-{progetto|tipo}` (es. `globex-platform`, `initech-expansion`).
- La narrativa di lungo periodo del partner vive in `wiki/entities/partners/{slug}.md` (timeline). L'account è il SoT di stato; la wiki entity è solo storia + link all'account.

Template: `company/customers/opportunities/TEMPLATE.md` · `company/customers/partners/TEMPLATE.md`.

---

## 2. Tassonomia stage (da `pipeline-config.yaml`)

Default a 6 stage (standard B2B) + lost. `probability` è **derivata dallo stage** (mappa in config), non si imposta a mano:

| Stage | `stage` | `probability` |
|-------|---------|---------------|
| Discovery | `discovery` | 20 |
| Technical Alignment | `technical-alignment` | 30 |
| Proposal Sent | `proposal-sent` | 40 |
| Negotiation | `negotiation` | 60 |
| Contract Sent | `contract-sent` | 80 |
| Won / Lost | `won` / `lost` | 100 / 0 |

Quando si sposta lo stage si ricalcola sempre: `probability = config.stages[stage]` e `value-weighted = round(value-gross * probability / 100)`.

---

## 3. Regole aging (calcolate live, soglie da config)

`giorni_fermo = oggi − last-activity`. Soglie da `pipeline-config.yaml › aging` (default 7/14/21):

| Fascia | Trigger |
|--------|---------|
| 🟢 OK | `giorni_fermo` < attention, nessun next-step scaduto, nessun blocker high |
| 🟡 Attention | `giorni_fermo` ≥ attention, **oppure** next-step scaduto ≤ attention |
| 🟠 Warning | `giorni_fermo` ≥ warning, oppure next-step scaduto tra attention e warning, oppure `status-flag: blocked` da > attention |
| 🔴 Critical | `giorni_fermo` ≥ critical, oppure blocker `severity: high`, oppure next-step scaduto > warning |

La fascia è la **più grave** tra quelle attivate. Won/Lost sono esclusi.

---

## 4. Comandi (via Sales agent)

| Comando | Cosa fa |
|---------|---------|
| `/sales board` | (Ri)genera `PIPELINE.md` lanciando `python scripts/generate-pipeline.py`. |
| `/sales opportunity [opp-slug]` | Drill-down: crea/aggiorna una trattativa, sposta stage, logga attività, apre/risolve blocker. |
| `/sales pipeline-review` | Report narrativo (velocity, conversion, forecast, coverage) letto dalle opportunità. |

### 4.1 `/sales opportunity` — drill-down e aggiornamento
- **Crea**: nuovo file da `opportunities/TEMPLATE.md`, `opened` e `last-activity` = oggi, aggiunge la riga nell'indice Opportunità dell'account.
- **Sposta stage**: aggiorna `stage`, ricalcola `probability` e `value-weighted`, `last-activity` = oggi, voce in Timeline.
- **Logga attività**: `last-activity` = oggi, voce in Timeline (link a feedback/sessione).
- **Blocker**: aggiungi/aggiorna/risolvi entry in `blockers:`; `status-flag: blocked` se ≥1 aperto.
- **Chiudi**: `stage`/`status-flag` = won|lost, svuota blocker, registra esito.
Dopo le modifiche: rigenera il board. Commit: `[sales] opportunity: {opp-slug} — {azione}`.

### 4.2 `/sales board` — generazione del cockpit
Lancia `python scripts/generate-pipeline.py` (base default `company/customers`). Lo script scansiona le opportunità, calcola l'aging live e scrive `PIPELINE.md` con: Summary, **Per segmento**, **🔴🟠🟡 Bloccati & Aging** (vista chiave), Per owner, Per stage, Won. Commit: `[sales] board: pipeline cockpit {data}`.

---

## 5. Integrazione con gli altri agenti
- **CEO Routine** (`/routine start`): mostra i top 🔴🟠 aging nel blocco di apertura.
- **Customer Success** (`alert-check`): aggiunge gli alert aging delle opportunità.
- **Chief of Staff** (`daily-briefing`, `weekly-digest`): sezione "Pipeline — bloccati & aging".

---

## 6. Funnel di prospecting (pattern opzionale)
Per consolidare un canale con molti target sparsi su più fonti (export CRM + log attività + liste), usa il pattern `target-funnel.md`: universo → contattati → qualificati, con footer-memoria dei non-interessati. Promuovi a `opportunities/` solo i qualificati. Playbook completo in `target-funnel.md`.

---

## 7. Dove vivono i dati

| Dato | Path |
|------|------|
| Template opportunità | `company/customers/opportunities/TEMPLATE.md` |
| Opportunità | `company/customers/opportunities/{opp-slug}.md` |
| Board / cockpit | `company/customers/PIPELINE.md` (generato da `scripts/generate-pipeline.py`) |
| Config pipeline | `company/customers/pipeline-config.yaml` |
| Account | `company/customers/partners/{slug}.md` |
| Funnel prospecting | `company/customers/{canale}-funnel.md` (template: `target-funnel.md`) |
| Timeline narrativa | `wiki/entities/partners/{slug}.md` |
| Segmenti / ICP | `company/customers/segments.md` |
