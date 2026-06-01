# ClickUp Command: update-tasks

Aggiorna task ClickUp esistenti: stato, commenti, priority, assignee. Sempre con approvazione.

## Agenti autorizzati

PM, CTO, Chief of Staff

## Input richiesto

Vari modi di invocare:

```bash
# Aggiorna singolo task
/pm clickup update-tasks abc123 --status "in progress"
/pm clickup update-tasks abc123 --priority high --assignee "Mario Rossi"
/pm clickup update-tasks abc123 --comment "Bloccata da dipendenza su def456"

# Aggiornamento batch da file
/pm clickup update-tasks --from-file company/product/clickup-updates.md

# Aggiorna tutti i task legati a una spec
/pm clickup update-tasks --from-spec company/product/specs/{nome-spec}.md
```

## Fase 1: PREPARE

### 1.1 Raccogli le modifiche

Per ogni task da aggiornare, leggi lo stato corrente:

```
clickup_get_task(task_id: "{TASK_ID}", workspace_id: "{{CLICKUP_TEAM_ID}}")
```

Confronta con le modifiche richieste.

### 1.2 Genera file di approvazione

Salva in `company/product/clickup-pending/YYYY-MM-DD-update-tasks.md`:

```markdown
# ClickUp Update — Approvazione richiesta
Data: YYYY-MM-DD

## Modifiche proposte

| # | Task ID | Campo | Valore attuale | Nuovo valore |
|---|---------|-------|---------------|-------------|
| 1 | abc123 | Status | to do | in progress |
| 2 | abc123 | Assignee | — | Mario Rossi |
| 3 | def456 | Priority | low | high |
| 4 | ghi789 | Comment | — | "Bloccata da def456, attesa mercoledì" |
| 5 | jkl012 | Status | in progress | complete |

## Note
{Motivo degli aggiornamenti se specificato}

## Conferma
Per approvare: `/pm clickup approve company/product/clickup-pending/YYYY-MM-DD-update-tasks.md`
```

## Fase 2: APPROVE

L'utente esegue:
```
/pm clickup approve company/product/clickup-pending/YYYY-MM-DD-update-tasks.md
```

## Fase 3: EXECUTE

Per ogni riga del file approvato, in ordine:

**Aggiornamento status/priority/assignee**:
```
clickup_update_task(
  task_id: "abc123",
  status: "in progress",
  priority: "high",
  workspace_id: "{{CLICKUP_TEAM_ID}}"
)
```

Per assignee, prima risolvere il nome:
```
clickup_resolve_assignees(assignees: ["Mario Rossi"], workspace_id: "{{CLICKUP_TEAM_ID}}")
```
Poi:
```
clickup_update_task(
  task_id: "abc123",
  assignees: ["{resolved_user_id}"],
  workspace_id: "{{CLICKUP_TEAM_ID}}"
)
```

**Aggiunta commento**:
```
clickup_create_task_comment(
  task_id: "abc123",
  comment_text: "Testo del commento",
  workspace_id: "{{CLICKUP_TEAM_ID}}"
)
```

### Log

```
✓ abc123: Status → in progress
✓ abc123: Assignee → Mario Rossi
✓ def456: Priority → high
✓ ghi789: Comment aggiunto
✗ jkl012: Status "complete" non disponibile — salto
```

### Post-esecuzione

1. Sposta file da `clickup-pending/` a `clickup-done/`
2. Se gli aggiornamenti derivano da una spec, aggiorna la spec con lo stato corrente
3. Committa: `[pm] clickup: update-tasks — N task aggiornati`

## Casi d'uso tipici

### Fine sprint
```
/cos clickup update-tasks --status complete abc123 def456 ghi789
```

### Assegnazione bulk
```
/pm clickup update-tasks --assignee "Mario Rossi" abc123 def456 ghi789
```

### Escalation priority
```
/pm clickup update-tasks abc123 --priority urgent --comment "Escalato da CEO — impatta demo cliente venerdì"
```
