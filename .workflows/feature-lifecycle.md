# Workflow: Feature Lifecycle

Da richiesta cliente a feature live.

## Fasi

### 1. Request (Sales)
- **Trigger**: Cliente o prospect richiede feature
- **Agente**: Sales
- **Azione**: Documenta in `company/customers/feedback/{source}.md`
- **Output**: Feature request con contesto business
- **Handoff → PM**: `/pm evaluate-request [feature]`

### 2. Evaluate (PM)
- **Agente**: Product Manager
- **Azione**: Applica framework BUILD/CONFIGURE/CUSTOM/DECLINE
- **Output**: `company/product/specs/evaluation-{slug}.md`
- **Se DECLINE**: genera response per Sales, workflow finisce
- **Se BUILD**: Handoff → PM write-spec

### 3. Spec (PM)
- **Agente**: Product Manager
- **Azione**: Scrivi PRD completa
- **Output**: `company/product/specs/prd-{slug}.md`
- **Handoff → CTO**: per stima tecnica

### 4. Tech Review (CTO)
- **Agente**: CTO
- **Azione**: Valuta feasibility, stima effort, identifica rischi
- **Output**: Annotazioni sulla PRD + ADR se decisione architetturale
- **Handoff → PM**: per finalizzare priorità

### 5. Prioritize (PM)
- **Agente**: PM
- **Azione**: Inserisci in backlog con RICE score, assegna a sprint
- **Output**: Aggiorna `company/product/backlog.md`

### 6. Build (CTO/Dev)
- **Fuori scope agenti**: sviluppo effettivo
- **Al completamento**: Handoff → Marketing per launch

### 7. Launch (Marketing)
- **Agente**: Marketing
- **Azione**: `/marketing launch-plan [feature]`
- **Output**: Blog, email, changelog, sales enablement
- **Handoff → Sales**: enablement material

### 8. Sell (Sales)
- **Agente**: Sales
- **Azione**: Aggiorna battlecard, notifica prospect che l'avevano richiesta
- **Output**: Updated battlecard, follow-up emails
