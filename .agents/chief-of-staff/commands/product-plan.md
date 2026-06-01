# Command: product-plan

## Trigger
`/cos product-plan` oppure "Dove siamo sul prodotto?" oppure "Stato della pipeline prodotto"

## Processo

1. **Carica tutto company/product/**
   - `roadmap.md` — epic pianificati per quarter, priorità, effort
   - `backlog.md` — item dettagliati con stato e owner
   - `specs/` — tutti i PRD esistenti: leggi stato, domande aperte, dipendenze
   - `changelog.md` — cosa è stato già shippato

2. **Carica context tecnico**
   - `docs/reports/` — tech review CTO, stime effort riviste
   - `decisions/` — decisioni di scope che impattano la roadmap

3. **Costruisci la pipeline per ogni feature/epic**

   Per ogni item identifica la fase attuale:

   | Fase | Definizione |
   |------|-------------|
   | **Discovery** | Idea o richiesta non ancora analizzata |
   | **Spec** | PRD in scrittura o da scrivere |
   | **Tech Review** | PRD scritto, in attesa di review CTO |
   | **Ready** | Approvato da PM + CTO, pronto per sviluppo |
   | **In Progress** | In sviluppo attivo |
   | **Launch** | Shippato in produzione |

4. **Per ogni feature nel documento finale indica**
   - Fase attuale
   - Quarter target
   - Priorità (P0/P1/P2)
   - Owner engineering
   - Dipendenze critiche non risolte
   - Prossimo step concreto (chi deve fare cosa per avanzare di fase)
   - Risk flag se in ritardo o a rischio slittamento

5. **Aggiungi sezione "Dipendenze critiche non risolte"**
   - Lista delle dipendenze inter-epic che bloccano l'avanzamento
   - Indicazione dell'agente responsabile di sbloccarle

6. **Aggiungi sezione "Capacità Q corrente"**
   - Totale dev-settimane richieste vs disponibili
   - Semaforo: 🟢 ok / 🟡 attenzione / 🔴 overloaded

## Output
Salva in: `docs/reports/product-plan-{YYYY-MM-DD}.md`
Commit: `[cos] report: product plan {YYYY-MM-DD}`
