# Command: daily-briefing

## Trigger
`/cos daily-briefing` oppure "Briefing di oggi" oppure "Cosa è successo?" oppure "Cosa devo sapere oggi?"

## Processo

0. **CEO Decision Cadence Check** — SEMPRE PRIMO PASSO
   - Leggi `company/ceo-cadence.md`
   - Controlla l'ultima data di ogni ritmo (giornaliero / settimanale / mensile)
   - Determina quale ritmo attivare seguendo il **CEO Decision Cadence Protocol** in `CLAUDE.md` (regola #10)
   - Se scatta un ritmo, poni le domande del cadence al CEO PRIMA del briefing
   - Dopo le risposte del CEO: aggiorna `company/ceo-cadence.md` (data + log) e poi prosegui con il briefing
   - Se nessun ritmo scatta: "✓ Cadence check: nessuna urgenza. Procedo con il briefing."

0. **Spec Status Check** (solo se ci sono spec senza update da >2 settimane)
   - Leggi `company/product/specs/INDEX.md` e controlla `last-updated` di ogni spec
   - Se ci sono spec con `draft`/`evaluated`/`approved` stale (>7/14/14 giorni), includi nel briefing la sezione:

   ```
   ## 📋 Spec che richiedono aggiornamento stato

   Le seguenti spec non vengono aggiornate da più di N giorni:

   | Spec | Stato | Ultimo aggiornamento | Giorni senza update |
   |------|-------|---------------------|-------------------|
   | prd-xyz.md | approved | 2026-02-15 | 28 |
   ```

   Non interrompere per chiedere conferma: segnala passivamente nel briefing.

1. **Scansiona email ultime 24h** ← `.skills/gmail/commands/email-scan.md`
   - Esegui `email-scan` prima di qualsiasi altra cosa
   - Classifica in: azione richiesta / monitoraggio / informativo
   - Identifica pattern (topic ricorrenti, thread senza risposta 48h+)
   - La sezione email va all'inizio del briefing, prima dei commit git

2. **Scansiona attività recenti (ultime 24-48h)**
   - `git log --since="48 hours ago"` — commit recenti per agente e tipo
   - Per ogni commit: cosa è stato prodotto, da quale agente, quale impatto
   - Nuovi file in `decisions/`, `docs/reports/`, `company/product/specs/`

3. **Estrai segnali che richiedono attenzione CEO**
   - Follow-up con scadenza oggi o domani (da `decisions/` e `docs/reports/`)
   - Handoff non raccolti: un agente ha indicato un passaggio → verificare se è stato fatto
   - Decisioni aperte senza owner o senza data
   - Dipendenze critiche a rischio (leggi `docs/reports/` più recente del CTO/PM)

4. **Priorità per oggi**
   - Lista le 3-5 azioni più urgenti per il CEO oggi
   - Per ognuna: contesto in 1 riga, cosa serve fare, quanto tempo stimato

5. **Struttura del documento**

   ```
   ## Briefing {data}

   ### Cosa è cambiato
   [commit e output recenti, per agente]

   ### Richiede la tua attenzione oggi
   [azioni urgenti con scadenza, escalation, blocchi]

   ### Priorità CEO per oggi
   1. ...
   2. ...
   3. ...

   ### FYI — Nessuna azione richiesta
   [aggiornamenti di contesto, non urgenti]
   ```

6. **Tono**: telegrafico. Bullet point. Niente prose non necessarie.

## Output
Salva in: `docs/reports/briefing-{YYYY-MM-DD}.md`
Commit: `[cos] briefing: {YYYY-MM-DD}`
