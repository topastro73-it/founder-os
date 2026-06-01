# Agents — Index

Elenco completo degli agenti aziendali disponibili. Ogni agente ha una personalità, contesto, skill e set di comandi specifici definiti nel suo `AGENT.md`.

## Come invocare un agente

Quando l'utente invoca un agente, tu **leggi** il suo `AGENT.md`, poi **diventi** quel ruolo — ne assumi personalità, contesto, skill e vincoli.

**Pattern di invocazione**:
- `/[slug] [comando]` — es. `/pm write-spec`, `/cto tech-decision`
- `come [Nome] ...` — es. "come Product Manager, valuta questa feature"

---

## Agenti disponibili

| Agente | Slug | Invocazione | AGENT.md | Responsabilità core |
|--------|------|------------|----------|-------------------|
| **CEO / Founder** | `ceo` | `/ceo [cmd]` | `.agents/ceo/AGENT.md` | Decisioni strategiche, investitori, visione |
| **Product Manager** | `pm` | `/pm [cmd]` | `.agents/product-manager/AGENT.md` | Spec, roadmap, backlog, evaluate-request |
| **CTO** | `cto` | `/cto [cmd]` | `.agents/cto/AGENT.md` | Tech decisions, architecture, platform |
| **Marketing** | `marketing` | `/marketing [cmd]` | `.agents/marketing/AGENT.md` | Content, campaigns, positioning, messaging |
| **Sales** | `sales` | `/sales [cmd]` | `.agents/sales/AGENT.md` | Deal pipeline, ABM, customer success, proposal |
| **Chief of Staff** | `cos` | `/cos [cmd]` | `.agents/chief-of-staff/AGENT.md` | Briefing, coordination, workflows, execution |
| **CFO** | `cfo` | `/cfo [cmd]` | `.agents/cfo/AGENT.md` | Financial planning, metrics, cap table, budget |
| **HR** | `hr` | `/hr [cmd]` | `.agents/hr/AGENT.md` | Hiring, onboarding, offboarding, culture |
| **Legal** | `legal` | `/legal [cmd]` | `.agents/legal/AGENT.md` | Contracts, compliance, audit, vendor-assessment |
| **CEO Routine** | `routine` | `/routine [cmd]` o nessun agente | `.agents/ceo-routine/AGENT.md` | Entry point, cadence, daily/weekly/monthly, start/close |
| **Onboarding** | `onboarding` | `/setup` o `/onboarding setup` | `.agents/onboarding/AGENT.md` | Setup iniziale guidato (primo avvio): configura azienda, team, vision, KPI |

---

## Workflow di invocazione

```
User: "/pm write-spec"
    ↓
1. Read .agents/product-manager/AGENT.md
2. Read .agents/_shared/ (COMPANY, PRINCIPLES, GLOSSARY, TEAM)
3. Read .agents/product-manager/commands/write-spec.md
4. Load relevant company/ data
5. Execute using templates/ if needed
6. Save output in correct location
7. Commit with [pm] action: description
8. If major decision → save to decisions/
9. If handoff needed → indicate next agent
```

---

## Shared context (leggi SEMPRE prima di ogni azione)

Questi file contengono il contesto comune a **tutti gli agenti**:

- `.agents/_shared/COMPANY.md` — Chi siamo, cosa facciamo, per chi
- `.agents/_shared/PRINCIPLES.md` — Come prendiamo decisioni
- `.agents/_shared/GLOSSARY.md` — Terminologia condivisa
- `.agents/_shared/TEAM.md` — Chi fa cosa, ruoli, contatti

---

## Dettagli per agente

Ogni agente ha:
- `AGENT.md` — personalità, contesto, skill disponibili, vincoli
- `commands/` — comandi specifici (es. `/pm write-spec`, `/cto tech-decision`)
- `templates/` — template per output (spec, decision, memo, ecc.)

Per invocare un comando specifico, leggi `commands/{comando}.md` dell'agente.

---

## CEO Routine — Ingresso primario

Quando il CEO apre una sessione **senza invocare un agente specifico**, il **CEO Routine Agent** si attiva automaticamente (`.agents/ceo-routine/AGENT.md`).

**Il Routine Agent**:
1. Identifica la macchina corrente (Machine Detection)
2. Determina il cadence (giornaliero/settimanale/mensile) da `company/ceo-cadence.md`
3. Esegue la routine (briefing, status check, decisioni urgenti)
4. Raccoglie risposte e aggiorna i dati
5. Fa handoff all'agente richiesto, se specificato

Se il CEO invoca **direttamente un agente** (es. `/pm write-spec`), il Routine Agent fa un **quick check** (max 1 domanda urgente, 30 secondi) e poi lascia lavorare.

---

## Note

- Ogni agente legge `MEMORY.md` e `system/learnings.md` al start della sessione
- Gli agenti hanno accesso alle 26 skill disponibili in `.skills/` (vedi `.skills/SKILLS.md`)
- Output rules e destination paths sono centralizzati in `CLAUDE.md`
