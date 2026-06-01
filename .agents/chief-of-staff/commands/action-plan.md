# Command: action-plan

## Trigger
`/cos action-plan` oppure "Dammi il piano operativo" oppure "Cosa dobbiamo fare?"

## Processo

1. **Scansiona le fonti di azioni aperte**
   - `decisions/` — tutti i file: estrai i blocchi `## Follow-up` con checkbox `[ ]` non completate
   - `company/product/specs/` — estrai action items e domande aperte da ogni PRD
   - `docs/reports/` — estrai action items da tech review, roadmap review, report CTO/PM
   - `company/product/roadmap.md` — feature in ritardo, dipendenze a rischio
   - `company/product/backlog.md` — item bloccati o senza owner

2. **Classifica ogni azione**
   - **Owner**: chi deve agire (@ceo, @cto, @pm, @marketing, @sales)
   - **Deadline**: data esplicita o inferita dal contesto
   - **Priorità**:
     - P0 = blocca lancio, decisione aperta, scadenza imminente (≤7 giorni)
     - P1 = impatta Q corrente, nessun blocco immediato ma urgente (≤30 giorni)
     - P2 = importante ma non urgente, può aspettare il prossimo sprint

3. **Costruisci sezione "Decisioni che aspettano il CEO"**
   - Elenca ogni punto che richiede esplicitamente l'approvazione o l'azione del CEO
   - Per ognuno: contesto in 1 riga, opzioni se disponibili, raccomandazione

4. **Genera il documento strutturato**
   - Sezione P0: azioni critiche con tabella owner/deadline
   - Sezione P1: azioni importanti
   - Sezione P2: backlog operativo
   - Sezione CEO: decisioni pendenti che richiedono il founder
   - Sezione "Nessun owner": azioni senza responsabile assegnato (da delegare)

5. **Indica handoff se necessario**
   - Se un'azione P0 è bloccata su un agente specifico, segnalalo con il comando da invocare

## Output
Salva in: `docs/reports/action-plan-{YYYY-MM-DD}.md`
Commit: `[cos] report: action plan {YYYY-MM-DD}`
