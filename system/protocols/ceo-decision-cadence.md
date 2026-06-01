# CEO Decision Cadence Protocol

Il cadence check è responsabilità **esclusiva** del CEO Routine Agent (`.agents/ceo-routine/AGENT.md`). Nessun altro agente esegue il cadence autonomamente.

## Come funziona

- Quando il CEO apre una sessione senza invocare un agente specifico → CEO Routine si attiva automaticamente ed esegue la routine appropriata (giornaliera/settimanale/mensile)
- Quando il CEO invoca direttamente un agente (es. `/pm write-spec`) → CEO Routine fa un **quick check** (max 1 domanda urgente, 30 secondi) e poi lascia lavorare l'agente
- I ritmi, i formati e le soglie sono definiti in `.agents/ceo-routine/AGENT.md`
- Il tracking è in `company/ceo-cadence.md`

## Regole del cadence

- Il mensile INCLUDE settimanale e giornaliero
- Dopo ogni check, aggiorna `company/ceo-cadence.md` con data e log risposte
- Il CEO non deve ricordarsi di chiedere il briefing — il sistema glielo propone

## Eccezioni (non fare il check)

- Se lo hai già fatto oggi nella stessa sessione
