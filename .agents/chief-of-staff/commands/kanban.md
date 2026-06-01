# Command: kanban

## Trigger
`/cos kanban` oppure "Mostrami la board" oppure "Aggiorna il kanban"

## Processo

1. **Raccogli tutti gli item attivi dalle fonti**
   - `company/product/roadmap.md` — epic con stato (In Progress, Planned, etc.)
   - `company/product/backlog.md` — item con priorità e owner
   - `decisions/` — follow-up aperti `[ ]` da ogni decisione
   - `docs/reports/` — action items da tech review e altri report
   - `company/product/specs/` — domande aperte e prerequisiti bloccanti

2. **Classifica ogni item in una colonna**

   | Colonna | Criteri |
   |---------|---------|
   | **To Do** | Approvato, owner assegnato, non ancora iniziato |
   | **In Progress** | Lavoro attivo in corso questa settimana/sprint |
   | **In Review** | Completato dal responsabile, in attesa di review o approvazione |
   | **Blocked** | Non avanza per dipendenza esterna, decisione mancante, o risorsa assente |
   | **Done** | Completato e verificato (include item recenti, non storici) |

3. **Per ogni item nella board indica**
   - **Titolo**: descrizione breve dell'azione (max 1 riga)
   - **Owner**: @agente o persona responsabile
   - **Da quando**: data in cui è entrato in quella colonna (se inferibile)
   - **Scadenza**: deadline se presente
   - **Prossimo step**: cosa deve succedere affinché l'item avanzi di colonna

4. **Aggiungi sezione "Aging alerts"**
   - Item in In Progress da più di 2 settimane senza aggiornamenti
   - Item in Blocked senza piano di sblocco
   - Item in To Do con scadenza passata

5. **Formato markdown kanban**
   Usa sezioni H2 per ogni colonna. Ogni item è una sottosezione con le informazioni richieste.

## Output
Salva in: `docs/reports/kanban-{YYYY-MM-DD}.md`
Commit: `[cos] report: kanban {YYYY-MM-DD}`

## Nota
Il kanban non è persistente — ogni esecuzione genera uno snapshot della board in quel momento.
Per tracking storico, confronta i file `kanban-{data}.md` nel tempo.
