# CLICKUP_CONFIG.md — Configurazione Integrazione ClickUp

Questo file contiene la configurazione dell'integrazione ClickUp per il progetto.
L'integrazione avviene tramite MCP (Model Context Protocol) — nessuna API key da gestire manualmente.

## Workspace

```yaml
workspace_id: "{{CLICKUP_TEAM_ID}}"
workspace_name: "{{COMPANY_NAME}}"
```

## Space: Product Engineering

```yaml
space_id: "{{CLICKUP_SPACE_ID}}"
space_name: Product Engineering
```

### Folder e List

| Folder | Folder ID | List | List ID | Uso |
|--------|-----------|------|---------|-----|
| Delivery Board | {{FOLDER_ID_DELIVERY}} | Feature | {{LIST_ID_FEATURE}} | Task di sviluppo feature |
| Delivery Board | {{FOLDER_ID_DELIVERY}} | Bug | {{LIST_ID_BUG}} | Bug report e fix |
| Delivery Board | {{FOLDER_ID_DELIVERY}} | Tech-debt | {{LIST_ID_TECHDEBT}} | Debito tecnico |
| Delivery Board | {{FOLDER_ID_DELIVERY}} | Bug submission form | {{LIST_ID_BUGFORM}} | Form per bug submission |
| Delivery Board | {{FOLDER_ID_DELIVERY}} | War Room | {{LIST_ID_WARROOM}} | Urgenze e incidenti |
| Product Roadmap | {{FOLDER_ID_ROADMAP}} | Epic | {{LIST_ID_EPIC}} | Epic di roadmap |
| Product Roadmap | {{FOLDER_ID_ROADMAP}} | Release Planning | {{LIST_ID_RELEASE}} | Pianificazione release |
| — | — | 01 - Internal Projects | {{LIST_ID_INTERNAL}} | Progetti interni |
| — | — | CEO Personal | {{LIST_ID_CEO}} | Lista personale CEO (decisioni, azioni, follow-up) |

---

## Lifecycle di un task

```
Backlog → Triage → Approved → In Progress → In Review → Done → Archived
```

### Mapping folder/list per fase

| Fase | Dove |
|------|------|
| Roadmap/Epic planning | Product Roadmap → Epic |
| Sviluppo attivo | Delivery Board → Feature / Bug / Tech-debt |
| Release tracking | Product Roadmap → Release Planning |
| Urgenze | Delivery Board → War Room |

---

## Mapping Issue Types

| founder-os Concetto | ClickUp List | Note |
|--------------------|-------------|------|
| Feature / Iniziativa | Product Roadmap → Epic | Task parent |
| User Story | Delivery Board → Feature | Subtask dell'Epic o task standalone |
| Bug / Defect | Delivery Board → Bug | Separato da Feature |
| Task tecnico / Tech debt | Delivery Board → Tech-debt | No user value diretto |
| Research spike | Delivery Board → Tech-debt | Con tag: `spike` |

---

## Mapping Priority

| founder-os Label | ClickUp Priority | Quando usarla |
|-----------------|-----------------|---------------|
| P0 - Critical | `urgent` | Blocca produzione o cliente live |
| P1 - High | `high` | Blocca sprint goal o feature core |
| P2 - Medium | `normal` | Importante ma non urgente |
| P3 - Low | `low` | Nice to have, prossimi sprint |

---

## Tag Convention

| Tag | Significato |
|-----|------------|
| `from-founder-os` | Task creato/gestito dall'OS — sempre presente |
| `Q1-2026`, `Q2-2026` | Trimestre target dalla roadmap |
| `spec:{slug}` | Collegato a una PRD specifica |
| `blocked` | Bloccato da dipendenza esterna |
| `spike` | Research/esplorazione tecnica |
| `tech-debt` | Debito tecnico da ripagare |
| `customer-request` | Richiesta diretta di un cliente |

---

## Mapping Utenti (Assignee)

Per risolvere nomi in user ID usare il tool `clickup_resolve_assignees`:

```
clickup_resolve_assignees(assignees: ["Mario Rossi", "il CTO"], workspace_id: "{{CLICKUP_TEAM_ID}}")
```

Oppure usare `clickup_find_member_by_name` per un singolo utente.

---

## Note operative

- **MCP**: l'integrazione usa tool MCP, non API dirette — nessun `.env` o script bash
- **workspace_id**: passare SEMPRE il valore configurato in `{{CLICKUP_TEAM_ID}}` a ogni chiamata tool ClickUp
- **Rate limit**: ClickUp ha rate limit — in caso di errore 429, attendere e riprovare
- **Tag**: i tag devono già esistere nello space; crearli manualmente da ClickUp UI se mancano
