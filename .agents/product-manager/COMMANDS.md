# Product Manager — Available Commands

Elenco completo dei comandi disponibili per il PM Agent.

## Core Commands

### `/pm evaluate-request [feature]`
Valuta una feature request con il framework BUILD/CONFIGURE/CUSTOM/DECLINE.
→ Leggi: `commands/evaluate-request.md`
→ Output: `company/product/specs/evaluation-{slug}.md`

### `/pm write-spec [feature]`
Scrivi una PRD completa con user stories e acceptance criteria.
→ Leggi: `commands/write-spec.md`
→ Output: `company/product/specs/prd-{slug}.md`

### `/pm write-epic [epic]`
Scrivi un'Epic che raggruppa feature tasks correlati con scope, outcome e Definition of Done.
→ Leggi: `commands/write-epic.md`
→ Output: `company/product/specs/epic-{slug}.md`

### `/pm prioritize-backlog`
Applica RICE scoring al backlog e proponi priorità.
→ Leggi: `commands/prioritize-backlog.md`
→ Output: aggiorna `company/product/backlog.md`

### `/pm roadmap-review`
Analizza roadmap per allineamento strategico, gap e bilanciamento.
→ Leggi: `commands/roadmap-review.md`
→ Output: `docs/reports/roadmap-review-{date}.md`

### `/pm competitive-analysis [competitor]`
Analisi competitiva dettagliata con battlecard.
→ Leggi: `commands/competitive-analysis.md`
→ Output: `company/competitors/battlecards/{competitor}.md`

### `/pm pricing-analysis [feature]`
Valutazione pricing per una nuova feature/tier.
→ Leggi: `commands/pricing-analysis.md`
→ Output: `docs/reports/pricing-{slug}.md`

### `/pm sprint-planning`
Proponi contenuto del prossimo sprint basato su priorità e capacità.
→ Leggi: `commands/sprint-planning.md`
→ Output: `docs/reports/sprint-plan-{date}.md`

---

## Discovery Commands

### `/pm discovery-plan [topic]`
Genera piano di discovery per validare un'ipotesi di prodotto.
→ Output: `company/product/discovery/plan-{slug}.md`

### `/pm interview-guide [persona]`
Genera guida per intervista di discovery (es. buyer, utente finale, partner commerciale).
→ Output: `company/product/discovery/interview-guide-{persona}.md`

### `/pm feedback-synthesis`
Sintetizza feedback raccolti da multiple fonti in `company/customers/feedback/`.
→ Output: `docs/reports/feedback-synthesis-{date}.md`

### `/pm assumption-tracker`
Traccia e valida le assunzioni di prodotto.
→ Output: aggiorna `company/product/discovery/assumptions.md`

---

## Competitive Intelligence Commands

### `/pm competitor-track`
Aggiorna il tracking sistematico dei competitor (landscape + battlecard).
→ Output: aggiorna `company/competitors/landscape.md` + battlecard

### `/pm feature-matrix [competitors]`
Genera feature comparison matrix aggiornata.
→ Output: `company/competitors/feature-matrix-{date}.md`

### `/pm competitor-alert`
Check rapido per novità competitive.
→ Output: in chat

### `/pm win-loss-analysis`
Analisi dei deal vinti e persi vs competitor.
→ Output: `docs/reports/win-loss-{date}.md`

---

## Release Management Commands

### `/pm release-plan [version]`
Genera piano di rilascio per una versione (alpha → beta → GA → post-release).
→ Output: `company/product/releases/release-{version}.md`

### `/pm changelog-entry [version]`
Genera entry per il changelog, user-friendly e distinta per audience.
→ Output: aggiorna `company/product/changelog.md`

### `/pm versioning-decision`
Decidi il tipo di versioning bump (MAJOR/MINOR/PATCH).
→ Output: in chat

---

## Product Analytics Commands

### `/pm metrics-review`
Review delle metriche prodotto per i segmenti rilevanti (es. clienti, partner, utenti finali).
→ Output: `docs/reports/product-metrics-review-{date}.md`

### `/pm adoption-analysis [feature]`
Analisi di adozione di una feature specifica.
→ Output: `docs/reports/adoption-{feature}-{date}.md`

### `/pm cohort-analysis`
Analisi per coorte di clienti onboarded (retention 30/60/90gg).
→ Output: `docs/reports/cohort-analysis-{date}.md`

---

## Stakeholder Communication Commands

### `/pm roadmap-share [audience]`
Genera versione della roadmap per un'audience specifica (es. partner / board / team / sales).
→ Output: `docs/reports/roadmap-{audience}-{date}.md`

### `/pm release-comms [version]`
Genera comunicazioni di release per tutte le audience.
→ Output: `docs/marketing/release-comms-{version}/`

### `/pm partner-roadmap-review [partner]`
Prepara la sessione di roadmap review con un partner specifico.
→ Output: `docs/reports/partner-roadmap-review-{partner}.md`

### `/pm product-update [audience]`
Genera product update periodico per un'audience.
→ Output: `docs/reports/product-update-{audience}-{date}.md`

---

## Business Analysis Commands (da `.skills/business-analysis/SKILL.md`)

### `/pm analyze [topic]`
Avvia un'analisi funzionale interattiva. Domande aperte → deep dive per strati → pain points → proposta TO-BE.
→ Output: `company/product/analysis/analysis-{slug}.md`

### `/pm map-process [process]`
Mappa un processo esistente step by step con diagramma Mermaid.
→ Output: `company/product/analysis/process-{slug}.md`

### `/pm data-model [entity]`
Mappa il modello dati di un'entità o dominio (campi, relazioni, regole).
→ Output: `company/product/analysis/data-model-{slug}.md`

### `/pm requirements-elicitation [topic]`
Sessione di elicitazione requisiti strutturata (5W+H, User Journey, Scenari, MoSCoW).
→ Output: `company/product/analysis/requirements-{slug}.md`

### `/pm gap-analysis [area]`
Analisi gap tra AS-IS e TO-BE con priorità e effort.
→ Output: `company/product/analysis/gap-analysis-{slug}.md`

### `/pm functional-spec [topic]`
Genera specifica funzionale dettagliata (dopo l'analisi). Diversa dalla PRD: descrive il COME, non il COSA.
→ Output: `company/product/analysis/func-spec-{slug}.md`
