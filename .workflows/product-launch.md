# Workflow: Product Launch

Lancio coordinato di una nuova feature.

## Pre-requisiti
- PRD approvata in `company/product/specs/`
- Feature sviluppata e in staging

## Fasi

### 1. Launch Classification (PM)
- **Tier 1** (Major): New capability, market differentiator → Full launch
- **Tier 2** (Notable): Significant improvement → Blog + email + changelog
- **Tier 3** (Minor): Bug fix, small improvement → Changelog only

### 2. Launch Plan (Marketing)
- `/marketing launch-plan [feature]`
- Genera tutti gli asset necessari per il tier

### 3. Sales Enablement (Sales + Marketing)
- `/sales competitive-battlecard` — aggiorna se cambia positioning
- Talking points, demo script, FAQ

### 4. Execute Launch (Marketing)
- Pubblica content secondo timeline
- Monitor metriche di lancio

### 5. Post-Launch (PM)
- Raccogli feedback iniziale
- Monitor metriche di successo dalla PRD
- Report a 30 giorni
