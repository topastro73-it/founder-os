# CEO Routine — Available Commands

Elenco completo dei comandi disponibili per il CEO Routine Agent.

### `/routine start` (o nessun agente)
Avvia la routine del giorno (giornaliera/settimanale/mensile).
→ Leggi: `commands/start.md`
→ Output: routine interattiva + update a `company/ceo-cadence.md`

### `/routine priorities`
Mostra le 3 priorita senza routine completa.
→ Leggi: `commands/priorities.md`
→ Output: lista priorita in chat

### `/routine pending`
Mostra tutto cio che aspetta il CEO.
→ Leggi: `commands/pending.md`
→ Output: lista item in sospeso

### `/routine update`
Aggiorna un dato velocemente.
→ Leggi: `commands/update.md`
→ Uso: `/routine update metrics` oppure `/routine update spec-state`

### `/routine skip`
Segna un item come saltato consapevolmente.
→ Leggi: `commands/skip.md`
→ Uso: `/routine skip [item]`

### `/routine reflect`
Riflessione strategica guidata.
→ Leggi: `commands/reflect.md`
→ Output: sessione di riflessione strutturata

### `/routine process-signals`
Converte export Gemini/Perplexity da `docs/intelligence/inbox/` in segnali strutturati pronti per il briefing.
→ Leggi: `commands/process-signals.md`
→ Output: segnali processati nel briefing

### `/routine close` (o `/close`)
Genera wiki sessione, aggiorna entita, committa e pusha (funziona da qualsiasi macchina, risolve conflitti automaticamente).
→ Leggi: `commands/close.md`
→ Output: commit, push, wiki session in `wiki/sessions/{YYYY-MM-DD}-{slug}.md`
