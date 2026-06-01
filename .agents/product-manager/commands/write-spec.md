# Command: write-spec

## Trigger
`/pm write-spec [feature]` oppure "Scrivi la spec per [feature]"

## Processo

0. **Spec Status Check** ← Regola globale 9 (CLAUDE.md)
   - Leggi `company/product/specs/INDEX.md` + frontmatter di ogni spec
   - Identifica spec stale e chiedi conferma al CEO prima di procedere
   - Aggiorna frontmatter e INDEX, poi continua

1. **Carica contesto**
   - Evaluation precedente (se esiste) da `company/product/specs/evaluation-*.md`
   - `company/strategy/vision.md` per allineamento
   - `company/customers/segments.md` per le personas

2. **Genera PRD** con il template PRD, includendo:
   - Problem statement chiaro
   - User personas coinvolte
   - User stories in formato "As a... I want... So that..."
   - Acceptance criteria in formato "Given/When/Then"
   - **Data Model** (se la feature introduce nuove entità) — in linguaggio funzionale, MAI tecnico. Vedi regole nel template PRD.
   - Requisiti funzionali e non-funzionali
   - **In scope** (cosa è esplicitamente incluso)
   - Out of scope (cosa NON include)
   - Metriche di successo
   - Dipendenze e rischi
   - **Acceptance Criteria (Spec-level)** — criteri verificabili per l'intera iniziativa
   - **Implementation Status** — tabella deliverable con status/owner/ClickUp ref
   - **Decisions Made** — decisioni di design locali alla spec
   - **Deferred / Follow-up** — item rimandati a future iterazioni

3. **Definisci scope** in T-shirt size con razionale

## Output
Salva in: `company/product/specs/prd-{slug}.md`
Commit: `[pm] spec: PRD for {feature-name}`

## Handoff
→ CTO per stima tecnica e feasibility review
