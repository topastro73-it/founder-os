# Command: prepare-meeting

## Trigger
`/cos prepare-meeting [topic]` oppure "Prepara il meeting su [topic]" oppure "Brief per la call con [persona/tema]"

## Processo

1. **Identifica il meeting**
   - Topic: cosa si discute
   - Partecipanti: chi c'è (interni: agenti/team; esterni: cliente, investor, partner)
   - Obiettivo: cosa deve uscire da questa call (decisione, allineamento, discovery, update)

2. **Carica contesto rilevante dal repo**
   In base al topic, leggi:
   - Se meeting prodotto/tech: `company/product/roadmap.md`, `specs/` rilevanti, `docs/reports/` CTO/PM
   - Se meeting commerciale: `company/customers/segments.md`, `docs/proposals/` se presente, `company/competitors/`
   - Se meeting strategico: `company/strategy/vision.md`, `company/strategy/okrs/`, decisioni recenti
   - Se meeting investor: `company/metrics/kpis.md`, `docs/investor-updates/` più recente
   - Sempre: `decisions/` — decisioni aperte rilevanti al topic

3. **Costruisci il brief**

   **Background** (cosa sappiamo già)
   - Contesto della situazione in 3-5 punti
   - Decisioni già prese sul topic (con riferimento al file)
   - Stato attuale del workstream coinvolto

   **Dati chiave**
   - Metriche rilevanti, stime, numeri dal repo
   - Ogni dato deve citare la fonte (file.md)

   **Domande aperte**
   - Cosa non è ancora stato deciso e potrebbe emergere nel meeting
   - Per ognuna: contesto e possibili risposte con pro/contro

   **Possibili outcome**
   - Lista dei 2-4 risultati possibili del meeting
   - Per ognuno: cosa significherebbe per il piano attuale

4. **Genera l'agenda**
   - Struttura in slot temporali (es. 5+10+10+5 minuti)
   - Ogni slot: argomento, owner della discussione, obiettivo dello slot (decidere / aggiornare / brainstorm)

5. **Struttura del documento**

   ```
   ## Meeting Prep — {topic} — {data}

   **Partecipanti**: [lista]
   **Obiettivo**: [1 riga]
   **Durata prevista**: [X minuti]

   ### Background
   [punti chiave dal repo]

   ### Dati chiave
   [numeri e metriche con fonte]

   ### Domande aperte
   [lista con contesto]

   ### Possibili outcome
   [lista con implicazioni]

   ### Agenda proposta
   | Slot | Argomento | Owner | Obiettivo |

   ### Post-meeting: follow-up da tracciare
   [spazio da compilare dopo il meeting con decisioni prese e azioni]
   ```

## Output
Salva in: `docs/internal-memos/meeting-prep-{slug}.md`
Commit: `[cos] memo: meeting prep {slug}`

## Nota
Il documento include una sezione "Post-meeting" vuota — da compilare manualmente o con `/cos daily-briefing` dopo la call.
