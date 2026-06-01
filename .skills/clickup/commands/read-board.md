# ClickUp Command: read-board

Legge la Delivery Board e Product Roadmap, importa lo stato in `company/product/clickup-board-current.md`.
Solo lettura — nessuna approvazione richiesta.

## Struttura della board

La Space "Product Engineering" è organizzata in due folder principali:

```
Delivery Board (folder {{CLICKUP_FOLDER_DELIVERY}})
├── Feature ({{CLICKUP_LIST_FEATURE}})     ← task di sviluppo in corso
├── Bug ({{CLICKUP_LIST_BUG}})             ← bug da fixare
├── Tech-debt ({{CLICKUP_LIST_TECHDEBT}})  ← debito tecnico
├── War Room ({{CLICKUP_LIST_WARROOM}})    ← urgenze
└── Bug submission form ({{CLICKUP_LIST_BUGFORM}})

Product Roadmap (folder {{CLICKUP_FOLDER_ROADMAP}})
├── Epic ({{CLICKUP_LIST_EPIC}})           ← epic di roadmap
└── Release Planning ({{CLICKUP_LIST_RELEASE}}) ← release
```

## Agenti autorizzati

Tutti

## Input richiesto

```bash
/pm clickup read-board              # Tutto (default)
/pm clickup read-board delivery     # Solo Delivery Board
/pm clickup read-board roadmap      # Solo Product Roadmap / Epic
/pm clickup read-board feature      # Solo list Feature
/pm clickup read-board bug          # Solo list Bug
```

## Esecuzione

### List da leggere

| List | List ID | Comando MCP |
|------|---------|------------|
| Feature | {{CLICKUP_LIST_FEATURE}} | `clickup_filter_tasks(list_ids: ["{{CLICKUP_LIST_FEATURE}}"])` |
| Bug | {{CLICKUP_LIST_BUG}} | `clickup_filter_tasks(list_ids: ["{{CLICKUP_LIST_BUG}}"])` |
| Tech-debt | {{CLICKUP_LIST_TECHDEBT}} | `clickup_filter_tasks(list_ids: ["{{CLICKUP_LIST_TECHDEBT}}"])` |
| War Room | {{CLICKUP_LIST_WARROOM}} | `clickup_filter_tasks(list_ids: ["{{CLICKUP_LIST_WARROOM}}"])` |
| Epic | {{CLICKUP_LIST_EPIC}} | `clickup_filter_tasks(list_ids: ["{{CLICKUP_LIST_EPIC}}"])` |
| Release Planning | {{CLICKUP_LIST_RELEASE}} | `clickup_filter_tasks(list_ids: ["{{CLICKUP_LIST_RELEASE}}"])` |

**Nota**: passare sempre `workspace_id: "{{CLICKUP_TEAM_ID}}"` a ogni chiamata.

### Campi da estrarre per ogni task

`id`, `name`, `status.status`, `priority`, `assignees`, `tags`, `due_date`, `url`

Per task con molti subtask, usare `detail_level: "summary"` per evitare risposte troppo grandi.

## Output: company/product/clickup-board-current.md

```markdown
# Board Product Engineering — Snapshot

> Aggiornato: YYYY-MM-DD HH:MM

---

## 🚀 Delivery Board — Feature (List {{CLICKUP_LIST_FEATURE}})

> Task di sviluppo in corso.

| ID | Summary | Assignee | Priority | Status | Due Date |
|----|---------|----------|----------|--------|----------|
| abc123 | Autenticazione SSO | mario | urgent | to test | 2026-03-25 |
| def456 | Custom domain setup | luigi | high | in progress | — |

**Totale**: N task | Per stato: To Do: X, In Progress: Y, In Review: Z, Done: W

---

## 🐛 Delivery Board — Bug (List {{CLICKUP_LIST_BUG}})

| ID | Summary | Assignee | Priority | Status | Due Date |
|----|---------|----------|----------|--------|----------|
| ... | | | | | |

**Totale**: N task

---

## 🔧 Delivery Board — Tech-debt (List {{CLICKUP_LIST_TECHDEBT}})

| ID | Summary | Priority | Status |
|----|---------|----------|--------|
| ... | | | |

**Totale**: N task

---

## 🚨 War Room (List {{CLICKUP_LIST_WARROOM}})

| ID | Summary | Assignee | Priority | Status |
|----|---------|----------|----------|--------|
| ... | | | | |

**Totale**: N task

---

## 🗺️ Product Roadmap — Epic (List {{CLICKUP_LIST_EPIC}})

| ID | Summary | Priority | Status | Tags |
|----|---------|----------|--------|------|
| ... | | | | |

**Totale**: N epic

---

## 📦 Release Planning (List {{CLICKUP_LIST_RELEASE}})

| ID | Summary | Status | Due Date |
|----|---------|--------|----------|
| ... | | | |

**Totale**: N release

---

## Riepilogo

| List | Count |
|------|-------|
| 🚀 Feature | N |
| 🐛 Bug | N |
| 🔧 Tech-debt | N |
| 🚨 War Room | N |
| 🗺️ Epic | N |
| 📦 Release | N |
| **Totale** | **N** |
```

## Post-esecuzione

Il file viene sovrascritto ad ogni lettura (è uno snapshot). Non viene committato automaticamente — è read-only.

Comunica: "Board letta. Feature: N task, Bug: N, Tech-debt: N, Epic: N."
