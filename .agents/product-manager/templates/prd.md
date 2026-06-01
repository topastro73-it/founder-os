---
status: draft
date: {YYYY-MM-DD}
last-updated: {YYYY-MM-DD}
last-status-check: {YYYY-MM-DD}
decision: build
clickup-epic:
clickup-doc:
review-date:
---

# PRD: {Feature Name}

**Data**: {YYYY-MM-DD}
**Autore**: Product Manager
**Stato**: Draft | In Review | Approved | In Development | Shipped
**Versione**: 1.0

## Problem Statement

### Cosa
[Quale problema stiamo risolvendo?]

### Per chi
[Quale persona/segmento ne beneficia?]

### Perché ora
[Perché è importante risolverlo adesso?]

### Impatto se non facciamo nulla
[Cosa succede se non lo facciamo?]

## Goals & Success Metrics

| Metrica | Attuale | Target | Come misuriamo |
|---------|---------|--------|---------------|
| [Metrica 1] | — | — | [Tool/metodo] |
| [Metrica 2] | — | — | [Tool/metodo] |

## User Personas

### Persona 1: {Nome/Ruolo}
- **Chi è**: [Descrizione]
- **Pain point**: [Problema specifico]
- **Job-to-be-done**: [Cosa vuole ottenere]

## User Stories

### Story 1: {Titolo}
**As a** [persona],
**I want** [azione],
**So that** [beneficio].

**Acceptance Criteria:**
- **Given** [contesto], **When** [azione], **Then** [risultato atteso]
- **Given** [contesto], **When** [azione], **Then** [risultato atteso]

### Story 2: {Titolo}
**As a** [persona],
**I want** [azione],
**So that** [beneficio].

**Acceptance Criteria:**
- **Given** [contesto], **When** [azione], **Then** [risultato atteso]

## Data Model (optional — include if the feature introduces new entities)

Describe the data model in **functional language**, not technical schema language. The PRD defines *what data exists and how it behaves* — not *how to implement it in code or database*.

**Rules**:
- Describe fields in plain language: "has a unique identifier", "has a name (text, max 100 characters)", "has a price (number, required)"
- Do NOT use technical naming conventions (snake_case, camelCase) — use plain English field names. The engineering team will choose the actual naming convention.
- Do NOT use database jargon: no "FK", "foreign key", "UUID", "boolean", "enum", "datetime", "nullable", "index", "varchar". Instead say: "links to a Category", "yes/no flag", "one of: monthly, annual, one-time", "date and time", "optional".
- DO describe relationships in plain terms: "each service belongs to exactly one category", "a partner can have many services", "links to the original Global service it was copied from".
- DO describe constraints and rules: "required", "optional", "unique", "immutable after creation", "max 100 characters".
- DO describe valid values: "one of: monthly, annual, one-time, per-device, per-user" (not "enum").
- DO describe computed/automatic fields: "set automatically by the system", "updated when the record is modified".

**Example — GOOD**:
> A **Service** has:
> - A unique identifier (set automatically, never changes even if the service is edited)
> - A name (text, max 100 characters, required)
> - A category (required, links to exactly one Category)
> - A short description (text, max 280 characters, required)
> - A price (number, required, must be greater than zero)
> - A price type (required, one of: monthly, one-time, annual, per-device, per-user)
> - A currency (default: EUR)
> - An active/archived flag (yes/no, default: active)
> - A display order (number, for manual sorting)
> - An origin indicator (one of: included from Global, duplicated from Global, custom)

**Example — BAD** (too technical, reads like a database schema):
> | Field | Type | Notes |
> | `service_id` | string (UUID) | Immutable. FK to downstream modules. |
> | `is_active` | boolean | Default: true |
> | `partner_id` | string (FK) | Null for Global catalog items |

## Functional Requirements

1. [Requisito funzionale]
2. [Requisito funzionale]

## Non-Functional Requirements

- **Performance**: [Requisiti di performance]
- **Security**: [Requisiti di sicurezza]
- **Scalability**: [Requisiti di scala]
- **Accessibility**: [Requisiti di accessibilità]

## In Scope
- [Cosa è esplicitamente incluso in questa versione]
- [Boundary chiaro per il dev team]

## Out of Scope
- [Cosa NON è incluso in questa versione]
- [Cosa rimandiamo a future iterazioni]

## Dependencies
- [Dipendenza tecnica o di business]

## Risks
| Rischio | Probabilità | Impatto | Mitigation |
|---------|------------|---------|------------|
| [Rischio] | H/M/L | H/M/L | [Piano] |

## Effort Estimate
- **T-shirt size**: [XS/S/M/L/XL]
- **Razionale**: [Perché questa stima]
- ⚠️ Da validare con CTO per stima tecnica dettagliata

## Open Questions
- [ ] [Domanda ancora da risolvere]

## Acceptance Criteria (Spec-level)
Criteri di accettazione per l'intera iniziativa (non per singola story):
- [ ] [Criterio verificabile che definisce "questa epic è completata"]
- [ ] [Criterio verificabile]

## Implementation Status
| Deliverable / Requirement | Status | Owner | ClickUp Ref | Notes |
|---|---|---|---|---|
| [deliverable-1] | Not Started | [name] | [EPIC-ID / TASK-ID] | — |
| [deliverable-2] | In Progress | [name] | [TASK-ID] | [note] |

Status values: `Not Started` · `In Progress` · `Done` · `Blocked` · `Deferred`

## Decisions Made
| Date | Decision | Rationale | Owner |
|---|---|---|---|
| YYYY-MM-DD | [decisione presa] | [perché] | [chi ha deciso] |

Nota: decisioni strategiche/cross-spec vanno in `decisions/`. Qui solo decisioni di design locali alla spec.

## Deferred / Follow-up
- [Item esplicitamente rimandato a iterazione futura — diverso da Out of Scope]
- [Item che era in scope ma è stato deprioritizzato durante lo sviluppo]
