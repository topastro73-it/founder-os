# ClickUp Command: sync-spec

Sincronizza una PRD/spec con ClickUp: crea 1 task Epic + N subtask/task collegati dagli acceptance criteria.

## Agenti autorizzati

PM, CTO

## Input richiesto

```
/pm clickup sync-spec company/product/specs/{nome-spec}.md
```

Opzionalmente per sincronizzare solo una sezione specifica:
```
/pm clickup sync-spec company/product/specs/{nome-spec}.md --section 6.6
```

## Fase 1: PREPARE

### 1.1 Leggi la spec

Carica il file spec indicato. Estrai:

- **Titolo feature** → diventa il nome del task Epic
- **Obiettivo / Problem Statement** → diventa la descrizione del task Epic
- **User Stories** (formato: "As a [ruolo], I want [azione], So that [beneficio]") → diventano task nella list Feature
- **Acceptance Criteria** per ogni story → diventano subtask del task story
- **Priority** indicata nella spec → mappa su ClickUp priority (`urgent`/`high`/`normal`/`low`)
- **Milestone/Target** → inserito nella descrizione del task (non come tag)

### 1.2 Verifica se l'Epic esiste già

Cerca task esistenti con tag `from-founder-os` e `spec:{slug}` nella list Epic:

```
clickup_filter_tasks(tags: ["from-founder-os", "spec:{slug}"], list_ids: ["{{CLICKUP_LIST_ID}}"], workspace_id: "{{CLICKUP_TEAM_ID}}")
```

Se esiste: proponi UPDATE (non duplicare).
Se non esiste: proponi CREATE.

### 1.3 Struttura da generare

```
Epic (in list "Epic" {{CLICKUP_LIST_ID}}): [Titolo Feature]
  └── description autoconsistente (vedi regola sotto)

Task (in list "Feature" {{CLICKUP_LIST_ID}}): [User Story 1]
  ├── description autoconsistente (vedi regola sotto)
  └── linked all'Epic (dependency: waiting_on)

Task (in list "Feature" {{CLICKUP_LIST_ID}}): [User Story 2]
  ├── description autoconsistente
  └── linked all'Epic
```

**Nota**: se la spec ha una sola feature/story senza epic-level separation, creare un singolo Task nella list Feature (non Epic) con subtask per gli acceptance criteria.

### Regola fondamentale: descrizioni autoconsistenti

**Ogni descrizione di task (Epic, Feature, Subtask) deve essere completamente autosufficiente.**

Il dev che prende il task non deve: cercare la PRD, chiedere al PM, leggere altri file, o fare domande per capire cosa sviluppare. Deve solo aprire il task e avere tutto il contesto necessario per iniziare a lavorare.

**Regola 1 — Solo approccio funzionale, zero dettagli tecnici/architetturali.**
Le descrizioni descrivono il comportamento atteso dal punto di vista dell'utente e del prodotto. Non menzionare: nomi di campi DB, nomi di tabelle, nomi di endpoint, scelte architetturali, stack tecnologico. Queste sono decisioni del dev/CTO, non del PM. Se c'è una dipendenza tecnica, descrivila funzionalmente ("questa feature richiede che il dato X sia già disponibile nel sistema") senza specificare come è implementata.

**Regola 2 — I dati critici stanno dentro il task, non in link esterni.**
Se il task ha bisogno di dati specifici per essere completato (es. pesi di uno scoring, regole di calcolo, soglie, logiche di classificazione), quei dati vanno copiati dentro la descrizione del task. Non scrivere "i dettagli sono nella spec sezione X.Y" — il dev non deve aprire altri file. Il link alla spec è solo un riferimento aggiuntivo facoltativo, non un sostituto del contenuto.

**Struttura obbligatoria per ogni task Epic:**

```markdown
## Contesto
[Spiega perché questa feature esiste nel prodotto: quale problema risolve, per quale utente, in quale parte del flywheel si inserisce (opzionale: la fase del tuo funnel/flywheel, se ne usi uno)]

## Obiettivo
[Cosa deve essere vero quando questa epic è completata — da punto di vista utente e business]

## Utenti coinvolti
[Chi usa questa feature: es. utente finale, operatore interno, partner / rivenditore]

## Scope
[Cosa è IN scope. Cosa è esplicitamente OUT scope.]

## Dipendenze funzionali
[Quali altre funzionalità devono essere già operative perché questa epic possa essere sviluppata — descritte funzionalmente, non tecnicamente]

## Link spec (opzionale)
[company/product/specs/{nome}.md]
```

**Struttura obbligatoria per ogni task Feature (User Story):**

```markdown
## Contesto
[In 2-3 righe: perché questa story esiste, in quale flusso si inserisce, cosa succede prima e dopo dal punto di vista dell'utente]

## User Story
As a [ruolo], I want [azione], so that [beneficio].

## Acceptance Criteria
- [ ] AC 1: [comportamento verificabile — scritto in termini di cosa l'utente vede/può fare]
- [ ] AC 2: ...
- [ ] AC 3: ...

## Dettagli funzionali
[Tutto ciò che il dev deve sapere per implementare correttamente: regole di business, soglie, logiche di calcolo, casi limite, comportamenti attesi in edge case. Questi dati stanno QUI, non in altri documenti.]
```

**Non è sufficiente** copiare solo il titolo della user story o incollare gli acceptance criteria senza contesto. Il dev deve capire *perché* sta costruendo questa cosa e avere *tutti i dati necessari* direttamente nel task.

### 1.4 Genera file di approvazione

Salva in `company/product/clickup-pending/YYYY-MM-DD-sync-spec-{slug}.md`:

```markdown
# ClickUp Sync — sync-spec — Approvazione richiesta
Data: YYYY-MM-DD
Spec: company/product/specs/{nome-spec}.md
Comando eseguito da: [agente]

## Struttura proposta

| # | Tipo | List | Parent | Summary | Priority | Tags |
|---|------|------|--------|---------|----------|------|
| 1 | Task (Epic) | Epic | — | "Titolo Feature" | high | from-founder-os, spec:{slug} |
| 2 | Task | Feature | linked #1 | "User Story 1" | high | from-founder-os, spec:{slug} |
| 3 | Subtask | Feature | #2 | "AC: L'utente può..." | normal | |
| 4 | Subtask | Feature | #2 | "AC: Il sistema verifica..." | normal | |
| 5 | Task | Feature | linked #1 | "User Story 2" | normal | from-founder-os, spec:{slug} |

## Tags
Tutti i task avranno tag: `from-founder-os`, `spec:{slug}`

## Note
{Eventuali note o assunzioni fatte durante l'estrazione}

## Conferma
Per approvare: `/pm clickup approve company/product/clickup-pending/YYYY-MM-DD-sync-spec-{slug}.md`
Per annullare: elimina o ignora questo file.
```

Comunica all'utente: "File di approvazione generato in `company/product/clickup-pending/YYYY-MM-DD-sync-spec-{slug}.md`. Revisa e approva per procedere."

## Fase 2: APPROVE

L'utente esegue:
```
/pm clickup approve company/product/clickup-pending/YYYY-MM-DD-sync-spec-{slug}.md
```

L'agente rilegge il file e chiede conferma finale: "Procedo a creare [N] task su ClickUp. Confermi? (sì/no)"

## Fase 3: EXECUTE

Per ogni riga del file di approvazione, in ordine:

1. **Crea task Epic** nella list Epic (`{{CLICKUP_LIST_ID}}`):
   ```
   clickup_create_task(
     name: "Titolo Feature",
     list_id: "{{CLICKUP_LIST_ID}}",
     markdown_description: "...",
     priority: "high",
     tags: ["from-founder-os", "spec:{slug}"],
     workspace_id: "{{CLICKUP_TEAM_ID}}"
   )
   ```
   Salva il task ID risultante.

2. **Crea task Feature** nella list Feature (`{{CLICKUP_LIST_ID}}`):
   ```
   clickup_create_task(
     name: "User Story 1",
     list_id: "{{CLICKUP_LIST_ID}}",
     markdown_description: "## Description\n...\n\n## Acceptance Criteria\n...",
     status: "Backlog",
     priority: "high",
     tags: ["from-founder-os", "spec:{slug}"],
     workspace_id: "{{CLICKUP_TEAM_ID}}"
   )
   ```
   Salva il task ID. **Status sempre `Backlog`** — il passaggio a To Do avviene solo durante il weekly planning.

3. **Collega task Feature all'Epic** con dependency:
   ```
   clickup_add_task_link(task_id: "{feature_task_id}", links_to: "{epic_task_id}", workspace_id: "{{CLICKUP_TEAM_ID}}")
   ```

4. **Crea subtask** (se necessari) come figli del task Feature:
   ```
   clickup_create_task(
     name: "AC: ...",
     list_id: "{{CLICKUP_LIST_ID}}",
     parent: "{feature_task_id}",
     priority: "normal",
     workspace_id: "{{CLICKUP_TEAM_ID}}"
   )
   ```

### Log di esecuzione

Stampa a schermo ogni azione:
```
✓ CREATED Epic: abc123 — "Titolo Feature" (list: Epic)
✓ CREATED Task: def456 — "User Story 1" (list: Feature)
✓ LINKED: def456 → abc123
✓ CREATED Subtask: ghi789 — "AC: L'utente può..." (parent: def456)
✗ FAILED Subtask: "AC: Il sistema..." — Error: 400 Bad Request
```

### Post-esecuzione

1. Sposta il file da `clickup-pending/` a `company/product/clickup-done/`
2. Aggiungi al file uno stato finale:
   ```
   ## Risultato esecuzione
   Data esecuzione: YYYY-MM-DD HH:MM
   Task creati: N/M
   Epic task ID: abc123
   ```
3. Aggiorna la spec originale aggiungendo in frontmatter: `clickup-epic: "[{epic_id}](https://app.clickup.com/t/{epic_id})"` — il campo DEVE contenere l'ID e il link diretto all'epic su ClickUp. L'epic si trova nella lista Epics (`{{CLICKUP_LIST_ID}}`) della board Product Roadmap, ed è collegata ai Feature task tramite dependency di tipo `blocking` (Feature blocks Epic).
4. **Aggiorna la sezione "Implementation Status" della spec** con i task creati:
   - Per ogni task creato, aggiungi o aggiorna la riga nella tabella Implementation Status
   - Campi: Deliverable (nome task), Status (`Not Started`), Owner (assignee se presente), ClickUp Ref (task ID con link), Notes
   - Se la sezione Implementation Status non esiste nella spec, creala seguendo il template in `.agents/product-manager/templates/prd.md`
5. **Pubblica/aggiorna la spec su ClickUp Docs**:
   - Ogni spec ha un **Doc dedicato** nel Folder "Product Specs" (ID: `{{CLICKUP_LIST_ID}}`)
   - Il nome del Doc DEVE essere il titolo della spec (es. `PRD — Nome Feature`), NON un nome generico
   - Se la spec non ha ancora un Doc (campo `clickup-doc:` vuoto nel frontmatter) → crea con `clickup_create_document` (name = titolo spec, parent = `{"id": "{{CLICKUP_LIST_ID}}", "type": "5"}`, visibility = `PUBLIC`, create_page = `true`), poi aggiorna la pagina con il contenuto markdown senza frontmatter
   - Se la spec ha già un Doc (`clickup-doc:` nel frontmatter) → aggiorna la pagina esistente con `clickup_update_document_page` (content replace completo)
   - Aggiorna il frontmatter della spec con `clickup-doc: "[{doc_id}](https://app.clickup.com/{{CLICKUP_TEAM_ID}}/v/dc/{doc_id})"`
   - Questo link è quello che va nella sezione References dei task ClickUp, così il dev clicca e arriva alla spec
6. Committa: `[pm] clickup: sync-spec {nome-spec} → Epic abc123 + N tasks`

### Regola di allineamento bidirezionale Spec ↔ ClickUp

Ogni volta che un agente interagisce con task ClickUp collegati a una spec (sync-spec, update-tasks, read-board), DEVE mantenere allineata la sezione **Implementation Status** della spec sorgente:

- **Creazione task** (sync-spec) → aggiunge riga in Implementation Status con `Not Started`
- **Cambio status su ClickUp** (update-tasks) → aggiorna la colonna Status nella spec (`Not Started` → `In Progress` → `Done` → `Blocked` → `Deferred`)
- **Lettura board** (read-board) → se rileva disallineamenti tra ClickUp e la spec, segnala e propone aggiornamento
- **Task eliminato o spostato** → aggiorna la riga con nota esplicativa
- **Spec aggiornata nel repo** (write-spec, edit manuale) → ri-pubblica il contenuto sul ClickUp Doc con `clickup_update_document_page`

Questa regola garantisce che la spec sia sempre una fotografia aggiornata dello stato di implementazione, senza dover aprire ClickUp. Il ClickUp Doc è un **mirror** del repo, non il source of truth — il repo resta il source of truth.

## Error handling

- Se un task Feature fallisce: logga l'errore, continua con gli altri, segnala in summary
- Se l'Epic fallisce: interrompi tutto, non creare i task figli
- Se la list non è accessibile: blocca e chiedi di verificare la configurazione in `CLICKUP_CONFIG.md`
