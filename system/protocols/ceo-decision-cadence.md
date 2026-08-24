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

## Cadence Log Freshness Check

**Perché esiste**: l'aggiornamento di `ceo-cadence.md` (data ultimo check per ritmo + riga in "Log
risposte recenti") era specificato **solo** nello Step 8 di `start.md`, cioè in mezzo a un'interazione
lunga col CEO. Una scrittura obbligatoria collocata così non è affidabile: se la sessione prosegue su
altro, quello step non scatta, e nessun errore lo segnala — il cadence log resta fermo mentre il resto
del sistema (wiki, decisioni, learnings) continua ad accumulare attività reale, e nessuno se ne accorge
finché qualcuno non lo nota per caso.

**Fix, due livelli**:

1. **Scrittura affidabile**: l'aggiornamento di `ceo-cadence.md` è ora un passo esplicito di
   `/routine close` (Phase 1, insieme alla generazione della wiki), non solo dell'interazione di
   `start`. Il close è il punto che il CEO invoca comunque per chiudere la giornata — agganciarsi lì è
   più affidabile che dipendere da uno step in mezzo a una conversazione lunga.
2. **Rete di sicurezza a `start`**: a ogni apertura di sessione, prima del briefing, confronta la data
   più recente in `ceo-cadence.md` (qualunque ritmo) con la data del file più recente in
   `wiki/sessions/`. Se la wiki è più avanti di **oltre 5 giorni** rispetto al cadence log, il cadence
   log è stale: mostralo al CEO in una riga (`⚠️ Cadence log fermo al {data}, ultima sessione reale
   {data-wiki} — lo riallineo a oggi?`) e, se conferma, aggiorna solo le date correnti (non backfillare
   la storia persa a meno che il CEO lo chieda esplicitamente).
