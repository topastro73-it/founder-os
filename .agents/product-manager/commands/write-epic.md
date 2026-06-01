# Command: write-epic

## Trigger
`/pm write-epic [epic]` oppure "Scrivi l'epic per [epic]"

## Processo

0. **Spec Status Check** \u2190 Regola globale 9 (CLAUDE.md)
   - Leggi `company/product/specs/INDEX.md` + frontmatter di ogni spec
   - Identifica spec stale e chiedi conferma al CEO prima di procedere
   - Aggiorna frontmatter e INDEX, poi continua

1. **Carica contesto**
   - `company/strategy/vision.md` per allineamento strategico
   - `company/product/roadmap.md` per posizionamento nella roadmap
   - `company/customers/segments.md` per gli utenti coinvolti
   - PRD esistenti correlate da `company/product/specs/prd-*.md`

2. **Genera Epic** con il template Epic, includendo:
   - **Perch\u00e9**: problema di business/prodotto e posizione nel flywheel (opzionale: la fase del tuo funnel/flywheel, se ne usi uno)
   - **Outcome atteso**: una frase dal punto di vista utente e business
   - **Utenti coinvolti**: quale dei livelli utente rilevanti (es. Partner, Venditore, Cliente finale)
   - **Scope**: in scope e out of scope espliciti
   - **Feature tasks**: lista dei task/user story con priorit\u00e0 e link a spec esistenti
   - **Dipendenze funzionali**: cosa deve essere gi\u00e0 operativo (funzionale, non tecnico)
   - **Vincoli**: compliance, UX, performance, deadline
   - **Definition of Done**: criteri di completamento epic-level

3. **Collega PRD esistenti**: se ci sono spec gi\u00e0 scritte per i task inclusi, linkale nella tabella Feature tasks

## Output
Salva in: `company/product/specs/epic-{slug}.md`
Commit: `[pm] epic: {epic-name}`

## Handoff
\u2192 CTO per validazione dipendenze tecniche e stima effort complessiva
\u2192 CoS per tracking operativo dell'epic
