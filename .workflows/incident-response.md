# Workflow: Incident Response

Quando c'è un outage o incidente tecnico.

## Fasi

### 1. Detect & Assess (CTO)
- Severità: P0 (down) / P1 (degraded) / P2 (minor impact)
- Impatto: quanti clienti, quale funzionalità

### 2. Communicate (CEO + Marketing)
- P0/P1: comunicazione immediata ai clienti impattati
- Status page update
- Internal notification

### 3. Resolve (CTO)
- Fix e deploy
- Verifica risoluzione

### 4. Post-mortem (CTO)
- `/cto incident-postmortem [incident]`
- Blameless, orientato al miglioramento
- Action items con owner e deadline

### 5. Follow-up (CEO + Sales)
- Comunicazione di chiusura ai clienti
- Se impatto significativo: call personale con clienti top
