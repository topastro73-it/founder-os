# Workflow: Customer Escalation

Quando un cliente ha un problema critico o una richiesta urgente.

## Fasi

### 1. Intake (Sales)
- Documenta: cliente, problema, impatto, urgenza
- Salva in `company/customers/feedback/{customer}-escalation.md`

### 2. Triage (PM)
- È un bug? → CTO
- È una feature request? → `/pm evaluate-request` (fast track)
- È un problema di configurazione? → Support

### 3. Resolution
- **Bug critico**: CTO → hotfix → Marketing (comunicazione se necessario)
- **Feature urgente**: PM valuta con framework (no shortcut!)
- **Configurazione**: risolvi e documenta per knowledge base

### 4. Follow-up (Sales)
- Comunica risoluzione al cliente
- Documenta lesson learned
