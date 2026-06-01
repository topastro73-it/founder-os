# ClickUp Command: sync-ceo-actions

Sincronizza decisioni pendenti, azioni da fare e follow-up sulla lista personale ClickUp del CEO.

## Agenti autorizzati

- Chief of Staff

## Input richiesto

```
/cos sync-ceo-actions
/cos sync-ceo-actions [fonte]
```

Fonti opzionali: `daily-briefing`, `action-plan`, `follow-up-tracker`, `decision-review`, `status-check`. Se non specificata, scansiona tutte le fonti.

## Lista target

```yaml
list_id: "{{CLICKUP_CEO_PERSONAL_LIST_ID}}"
list_name: Personal List
space: "{{CLICKUP_SPACE_NAME}}"
```

---

## Fase 1: PREPARE

### Step 1 — Scansiona le fonti

Leggi e analizza le seguenti fonti dal repo per estrarre item azionabili per il CEO:

| Fonte | File | Cosa cercare |
|-------|------|--------------|
| Decisioni pendenti | `decisions/*.md` | Decisioni con `status: open` o `status: pending` |
| Follow-up scaduti | `decisions/*.md`, `docs/reports/follow-ups-*.md` | Checkbox aperti `- [ ]` con owner CEO o senza owner |
| Azioni P0/P1 | `docs/reports/action-plan-*.md` | Azioni con owner CEO o che richiedono approvazione CEO |
| Spec stale | `company/product/specs/INDEX.md` | Spec con status check scaduto (vedi protocollo in CLAUDE.md) |
| Briefing urgenze | `docs/reports/briefing-*.md` (più recente) | Item marcati come urgenti/P0 |
| Roadmap blocchi | `company/product/roadmap.md` | Item bloccati che richiedono decisione CEO |

### Step 2 — Controlla duplicati su ClickUp

Prima di proporre la creazione di un task, cerca nella lista CEO Personal se esiste già un task con nome simile:

```
clickup_filter_tasks(list_id: "{{CLICKUP_CEO_PERSONAL_LIST_ID}}")
```

Se un task con lo stesso titolo (o molto simile) esiste già:
- Se è `open` / `to do` / `in progress` → **SKIP** (già presente)
- Se è `closed` / `done` → **CREATE** nuovo (la decisione/azione è ricorrente o nuova)

### Step 3 — Classifica ogni item

Ogni item estratto viene classificato con:

| Campo | Regola |
|-------|--------|
| **Tipo** | `decision` · `action` · `follow-up` · `review` · `blocker` |
| **Priority** | `urgent` se P0 o scaduto, `high` se P1 o prossimi 3gg, `normal` altrimenti |
| **Due date** | Data deadline se presente nella fonte, altrimenti vuoto |
| **Tag** | `from-founder-os` + `ceo-action` + tag tipo (es. `decision`, `follow-up`) |

### Step 4 — Genera file di approvazione

Salva in `company/product/clickup-pending/YYYY-MM-DD-sync-ceo-actions.md`:

```markdown
---
command: sync-ceo-actions
date: YYYY-MM-DD
status: pending-approval
source: [lista fonti scansionate]
---

# ClickUp Sync — CEO Actions — Approvazione richiesta

Data: YYYY-MM-DD
Lista target: CEO Personal ({{CLICKUP_CEO_PERSONAL_LIST_ID}})

## Azioni proposte

| # | Tipo | Titolo | Priority | Due | Fonte | Azione |
|---|------|--------|----------|-----|-------|--------|
| 1 | decision | "Decidere pricing tier Enterprise" | urgent | 2026-03-25 | decisions/2026-03-20-pricing.md | CREATE |
| 2 | follow-up | "Review spec bulk-import (scaduta)" | high | — | specs/INDEX.md | CREATE |
| 3 | action | "Approvare sprint planning Q2" | normal | 2026-03-28 | reports/action-plan.md | SKIP (già in ClickUp) |

## Riepilogo

- CREATE: N task
- SKIP: N task (già presenti)
- Totale fonti scansionate: N

## Conferma

Rivedi le azioni sopra, poi esegui:
`/cos clickup approve company/product/clickup-pending/YYYY-MM-DD-sync-ceo-actions.md`
```

**Commit**: `[cos] clickup: prepare sync-ceo-actions — N azioni proposte`

---

## Fase 2: APPROVE

L'utente rivede e conferma:
```
/cos clickup approve company/product/clickup-pending/YYYY-MM-DD-sync-ceo-actions.md
```

L'utente può modificare il file prima di approvare (rimuovere righe, cambiare priority, aggiungere due date).

---

## Fase 3: EXECUTE

### Per ogni riga con azione CREATE

Crea il task nella lista CEO Personal:

```
clickup_create_task(
  list_id: "{{CLICKUP_CEO_PERSONAL_LIST_ID}}",
  name: "[TIPO] Titolo",
  markdown_description: "## Contesto\n\n{descrizione dal repo}\n\n---\n\n## Fonte\n\n{path file sorgente}\n\n---\n\n## Azione richiesta\n\n{cosa deve fare il CEO}",
  priority: {priority mappata},
  due_date: {timestamp se presente},
  tags: ["from-founder-os", "ceo-action", "{tipo}"]
)
```

**Formato nome task**: `[DECISION] Titolo`, `[ACTION] Titolo`, `[FOLLOW-UP] Titolo`, `[REVIEW] Titolo`, `[BLOCKER] Titolo`

**Formato descrizione** (usa `markdown_description` con newline reali):

```markdown
## Contesto

Breve contesto estratto dalla fonte (2-3 righe max).

---

## Fonte

`decisions/2026-03-20-pricing.md`

---

## Azione richiesta

- [ ] Cosa deve fare il CEO concretamente
```

### Log di esecuzione

Per ogni task creato, mostra:
```
✅ #1 — [DECISION] Decidere pricing tier Enterprise → task_id: abc123
✅ #2 — [FOLLOW-UP] Review spec bulk-import → task_id: def456
⏭️ #3 — SKIP (già presente come task xyz789)
```

### Post-esecuzione

1. Aggiorna il frontmatter del file: `status: executed`, aggiungi `executed_date` e lista task ID creati
2. Sposta il file in `company/product/clickup-done/`
3. **Commit**: `[cos] clickup: sync-ceo-actions — N task creati su CEO Personal`

---

## Sync bidirezionale: ClickUp → Repo

Quando invocato, il comando esegue anche una **sync inversa**: legge i task completati su ClickUp e aggiorna i file corrispondenti nel repo.

### Step 1 — Leggi task completati da ClickUp

Filtra i task nella lista CEO Personal con tag `from-founder-os` e status `complete` / `closed` / `done`:

```
clickup_filter_tasks(list_id: "{{CLICKUP_CEO_PERSONAL_LIST_ID}}", tags: ["from-founder-os"], statuses: ["complete", "closed", "done"])
```

### Step 2 — Per ogni task completato, identifica la fonte

Dalla descrizione del task, estrai il path della **Fonte** (campo `## Fonte` nella descrizione). Questo indica il file del repo da aggiornare.

### Step 3 — Aggiorna il repo in base al tipo di task

| Tipo task | File repo | Aggiornamento |
|-----------|-----------|---------------|
| `[DECISION]` | `decisions/*.md` | Aggiorna frontmatter: `status: decided`, aggiungi `decided-date: YYYY-MM-DD` se non presente |
| `[ACTION]` | File fonte indicato | Marca checkbox come completati `- [x]`, aggiorna `status` se presente nel frontmatter |
| `[FOLLOW-UP]` | File fonte indicato | Marca checkbox follow-up come completati `- [x]` |
| `[REVIEW]` | `company/product/specs/*.md` | Aggiorna frontmatter: `last-status-check: YYYY-MM-DD`, aggiorna `status` se il CEO ha indicato un nuovo status nel commento del task ClickUp |
| `[BLOCKER]` | File fonte indicato | Aggiorna la sezione blocchi (rimuovi/marca come risolto), aggiorna `status` se presente |

**Regole di aggiornamento PRD/spec**:
- Leggi i **commenti** del task ClickUp (`clickup_get_task_comments`) per capire l'esito (es. "approvato", "deferred", "shipped")
- Se il commento indica un cambio di status → aggiorna il frontmatter `status` della spec (es. `approved` → `in-development`, `in-development` → `shipped`)
- Aggiorna sempre `last-updated: YYYY-MM-DD` nel frontmatter
- Aggiorna `company/product/specs/INDEX.md` di conseguenza

**Regole di aggiornamento decisioni**:
- Se la decisione aveva `status: open` o `status: pending` → aggiorna a `status: decided`
- Leggi i commenti del task per estrarre l'esito della decisione e aggiungerlo al campo `outcome` se presente nel template

### Step 4 — Genera report aggiornamenti nel file di approvazione

Aggiungi una sezione al file di approvazione con gli aggiornamenti repo proposti:

```markdown
## Aggiornamenti repo da task completati

| # | Task ClickUp | File repo | Aggiornamento proposto |
|---|-------------|-----------|----------------------|
| 1 | abc123 — [DECISION] Pricing | decisions/2026-03-20-pricing.md | status: open → decided, decided-date: 2026-03-22 |
| 2 | def456 — [REVIEW] Spec bulk-import | company/product/specs/prd-bulk-import.md | status: approved → in-development, last-updated: 2026-03-22 |
| 3 | ghi789 — [FOLLOW-UP] Onboarding check | docs/reports/follow-ups-2026-03.md | 2 checkbox marcati come completati |
```

**Questi aggiornamenti repo seguono lo stesso flusso PREPARE → APPROVE → EXECUTE**: vengono eseguiti solo dopo approvazione esplicita del CEO.

### Step 5 — Esecuzione aggiornamenti repo (post-approvazione)

Dopo l'approvazione, per ogni riga nella sezione "Aggiornamenti repo":
1. Leggi il file repo
2. Applica le modifiche (frontmatter, checkbox, status)
3. Aggiorna `company/product/specs/INDEX.md` se spec modificate
4. Committa: `[cos] clickup: sync-repo-from-completed — N file aggiornati`

---

## Pulizia task completati (repo → ClickUp)

Quando invocato, il comando controlla anche i task esistenti nella lista CEO Personal con tag `from-founder-os`:
- Se la decisione è stata presa (file in `decisions/` ha `status: decided`) → segnala come completabile
- Se il follow-up è stato fatto (checkbox completati nel repo) → segnala come completabile

Questi task vengono elencati alla fine del file di approvazione come sezione opzionale:

```markdown
## Task completabili (opzionale)

| Task ID | Titolo | Motivo | Azione suggerita |
|---------|--------|--------|-----------------|
| abc123 | [DECISION] Pricing | Decisione presa il 2026-03-22 | CLOSE |
```

---

## Error handling

- Se la lista CEO Personal non è accessibile → errore chiaro, suggerisci di verificare l'ID lista
- Se `clickup_create_task` fallisce → logga l'errore, continua con i task successivi, riporta i fallimenti nel riepilogo
- Se non ci sono item da sincronizzare → genera comunque il report ma con messaggio "Nessuna azione pendente per il CEO"
