# Command: agent-activity

## Trigger
`/cos agent-activity` oppure "Cosa ha fatto ogni agente?" oppure "Report attività agenti"

## Processo

1. **Scansiona l'attività per agente tramite git log**
   - Analizza i commit con prefisso `[ceo]`, `[pm]`, `[cto]`, `[marketing]`, `[sales]`, `[cos]`
   - Per ogni commit: data, tipo di azione, file prodotto
   - Periodo di analisi: ultime 4 settimane (o da inizio repository se più recente)

2. **Per ogni agente costruisci il profilo attività**

   **File prodotti**
   - Lista file creati o modificati dall'agente (da git log + diff)
   - Categorizzati per tipo: spec, decision, report, content, proposal

   **Decisioni prese o triggerate**
   - Decisioni in `decisions/` create da quell'agente
   - Decisioni in cui l'agente era referenziato come owner di follow-up

   **Handoff inviati**
   - Sezioni "Handoff" nei documenti dell'agente: a chi, per cosa
   - Verificare se il destinatario ha raccolto l'handoff (file creato in risposta?)

   **Handoff ricevuti non ancora raccolti**
   - Un altro agente ha indicato un passaggio a questo agente
   - Non risulta output dell'agente in risposta → gap

3. **Identifica gap e silenzi**
   - Agente senza commit negli ultimi 14 giorni → segnala
   - Handoff ricevuto non raccolto → segnala con fonte
   - Follow-up assegnati a quell'agente ancora aperti → conta e lista

4. **Struttura del documento**

   ```
   ## Agent Activity Report — {data}

   ### CEO
   - Output prodotti: [lista]
   - Decisioni: [lista]
   - Handoff inviati: [lista]
   - Handoff ricevuti non raccolti: [lista]
   - Follow-up aperti: [N]

   [ripeti per PM, CTO, Marketing, Sales, CoS]

   ### Tabella riassuntiva
   | Agente | Output | Decisioni | Handoff inviati | Handoff non raccolti | Follow-up aperti |

   ### Gap identificati
   [agenti silenti, handoff in sospeso, follow-up orfani]

   ### Raccomandazioni
   [chi deve fare cosa per chiudere i gap]
   ```

## Output
Salva in: `docs/reports/agent-activity-{YYYY-MM-DD}.md`
Commit: `[cos] report: agent activity {YYYY-MM-DD}`
