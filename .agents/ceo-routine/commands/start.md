# Command: start

## Trigger
`/routine start` oppure il CEO apre una sessione senza invocare un agente specifico.

## Processo

-1. **Initialization Check** (primo avvio)

   Prima di tutto, verifica se il sistema è stato configurato:
   - Se **non** esiste il file `.founder-os-initialized` nella root, **oppure**
   - `.agents/_shared/COMPANY.md` contiene ancora placeholder `{{` (grep `{{` sul file)

   → il sistema **non è inizializzato**. Non eseguire la routine. Invece, proponi il setup:

   ```
   👋 Benvenuto in founder-os! Vedo che il sistema non è ancora configurato.
   Vuoi che ti guidi nel setup iniziale (~10 domande, 5 minuti)?  →  lancio `/setup`
   (Oppure puoi compilare a mano `.agents/_shared/COMPANY.md`.)
   ```

   Se il CEO accetta → fai handoff all'**Onboarding Agent** (`/setup`). Altrimenti procedi pure,
   ma avvisa che gli agenti avranno contesto limitato finché i `{{...}}` non sono compilati.
   Se il sistema **è** inizializzato → salta silenziosamente allo Step 0.

0. **Stale Session Detector** (self-healing — vedi LRN-012)

   Prima di qualsiasi altra operazione, verifica che l'ultima sessione sia stata chiusa correttamente con `/routine close`.

   **Logica**:
   - Leggi le ultime 3 entry di `company/ceo-cadence.md` sezione "Log risposte recenti" e estrai le date
   - Per ogni data `D` trovata, controlla se esiste un file `wiki/sessions/D-*.md`
   - Se manca uno o più wiki per date che hanno entry in cadence → **stale session detected**

   **Comportamento**:
   - Se nessuna sessione stale → procedi silenziosamente al Step 1
   - Se 1+ sessioni stale → mostra al CEO **prima** del briefing:

     ```
     ⚠️ Sessione/i non chiuse con `/routine close`:
       • {data} — cadence log presente, wiki/sessions/ vuoto
       • ...

     Cosa faccio prima di iniziare la giornata?
       (a) Recovery completo — genero wiki retroattivo da commit + cadence + decisioni
       (b) Recovery minimo — creo solo nota stub per non perdere riferimento
       (c) Skip — proseguo, lasciando il gap
     ```

   - Se il CEO sceglie (a) o (b):
     1. Identifica i file da cui ricostruire: `git log --since=D --until=D+1 --pretty=format:"%h %s"`, `decisions/D-*.md`, entry cadence di `D`, file modificati
     2. Genera `wiki/sessions/D-{slug-recovered}.md` seguendo il template di `close.md` Step 3, con frontmatter aggiuntivo `recovery-note:` che spiega che il wiki è stato ricostruito retroattivamente
     3. Riconcilia promesse del wiki precedente (marca `[x]` quelle chiuse durante D, riportando `(completed in [[recovered-session]])`)
     4. Incrementa contatori `Applied:` dei learning effettivamente usati
     5. Aggiorna entity pages se cambiate
     6. Aggiorna `wiki/index.md` con la nuova sessione
     7. Aggiorna i file di stato che erano stati saltati (es. partner page se la cadence dice "promesse chiuse" ma il file non riflette)
     8. Mostra al CEO il summary del recovery e chiedi conferma prima di proseguire al briefing
   - Se il CEO sceglie (c) → logga il gap nelle URGENZE del briefing odierno: `⚠️ Sessione {D} non riconciliata — wiki mancante`

   **Eccezioni** (non eseguire il check):
   - Sessioni con cadence entry ma senza decisioni/promesse/file business toccati (es. solo `[obsidian] auto-sync`) → non serve wiki
   - Date prima di 2026-04-25 (attivazione del sistema wiki — sessioni precedenti non hanno wiki by design)
   - Se il check è già stato fatto nella stessa giornata → skip silenzioso

1. **Carica contesto**
   - Leggi `company/ceo-cadence.md` per determinare il ritmo
   - Leggi `company/ceo-routine.md` per preferenze e promesse aperte
   - Leggi `company/product/specs/INDEX.md` per stato spec
   - Leggi `company/metrics/kpis.md` per freshness metriche
   - Scansiona `decisions/` per decisioni aperte
   - Scansiona `company/customers/partners/` per alert partner (health < 60)
   - **Scansiona `company/customers/opportunities/*.md` per aging trattative** (skill `.skills/opportunity-management/SKILL.md`, sezione 3): calcola l'aging live da `last-activity`/`next-step-due`/`blockers` e prepara i top 🔴🟠 (account, blocco, giorni fermi, owner, next step). Mostrali nel blocco di apertura e includi i 🔴 nelle URGENZE. Soglie da `company/customers/pipeline-config.yaml`. Segnala in evidenza le opportunità **senza owner** e quelle con weighted alto bloccate.
   - Leggi `personal/todo.md` per i task personali di oggi (sezione `🔥 Oggi`)

2. **Wiki Context — "Dove eravamo rimasti"**
   - Trova l'ultima sessione wiki in `wiki/sessions/` (per data piu recente nel filename)
   - Se esiste, leggi il file e estrai: decisioni prese, domande aperte, promesse (con deadline)
   - Controlla promesse con deadline oggi o scadute
   - Mostra nel briefing un blocco riassuntivo di 3-5 righe:

   ```
   📖 Ultima sessione: {data} — "{titolo}"
      • Decisioni: {lista breve}
      • Aperto: {domande non risolte}
      • Promesso: {promesse con deadline, evidenzia scadute con ⚠️}
   ```

   - Se non esistono sessioni wiki, salta questo step silenziosamente
   - Se ci sono promesse scadute, includerle nelle URGENZE del daily briefing

3. **Learnings Load**
   - Leggi `system/learnings.md`
   - Carica in memoria le regole apprese (non mostrarle tutte al CEO)
   - Applicale proattivamente quando sono rilevanti durante la sessione
   - Se un learning ha tag correlati alle domande aperte dell'ultima sessione, segnala:
     `⚡ Learning LRN-XXX applicabile: "{testo regola}"`
   - Max 1 learning segnalato nello start — non sommergere

   **3b. Candidati learning non promossi** (guardrail anti-deriva — specchio di `close.md` Step 0.3.E)

   Stesso check del close, ma a inizio giornata, per non aspettare il close per recuperarli:
   - Scansiona le wiki-session degli **ultimi 30 giorni** cercando `## Learnings proposed` / `## Proposed learning (candidate)` / "candidate learning".
   - Per ogni candidato, verifica se è già promosso (LRN corrispondente in `system/learnings.md` **o** nota `→ promosso … come LRN-XXX` nella sessione). Scarta quelli con `→ scartato {data}`.
   - Se restano candidati non promossi → mostrali nel briefing (max 2, i più vecchi prima):

     ```
     🧠 Candidati learning mai promossi ({N})
        • "{candidato breve}" (da [[{session-orig}]], {N}gg fa)
        → Promuovo ora come LRN nuovo, oppure al prossimo close? [ora / close / scarta]
     ```

   - Se il CEO dice "ora" → promuovi (frontmatter `total`/`active`/`updated` + tag, entry CHANGELOG se tocca protocolli) e annota `→ promosso` nella sessione originale.
   - Se "close" → lascialo, lo ripeschi al close (Step 0.3.E). Se "scarta" → annota `→ scartato {oggi}` nella sessione per silenziarlo.
   - Se non ci sono candidati appesi, salta silenziosamente.

4. **RAG Context per domande aperte** (opzionale)
   - Se l'ultima sessione wiki ha domande aperte non risolte:
     Per ogni domanda, esegui: `python3 scripts/rag-search.py --context "[domanda]"`
   - NON mostrare risultati dettagliati — solo: "Ho contesto su [N] domande aperte"
   - L'agente usera il contesto quando il CEO chiede di lavorarci
   - Se RAG non disponibile (indici non esistono), salta silenziosamente

4b. **Intelligence Feed** (opzionale)
   - Scansiona `docs/intelligence/signals/` per file con `status: new`
   - Se presenti: mostra nel briefing il blocco seguente (max 3 segnali):

   ```
   📡 Segnali dal mercato ({N} nuovi)
      • [{data}] {source} — {titolo}
      • [{data}] {source} — {titolo}
      • ...
   ```

   - Se ci sono più di 3 segnali new, mostra i 3 più recenti e indica: "(+ N altri)"
   - I segnali rilevanti per le URGENZE del giorno vanno inclusi nelle priorità
   - Se `docs/intelligence/signals/` è vuoto o non esistono segnali new, salta silenziosamente
   - Per processare nuovi export da Gemini/Perplexity: `/routine process-signals`

5. **Determina il ritmo**
   - Se primo accesso del mese → Routine MENSILE (include settimanale + giornaliera)
   - Se primo accesso della settimana (lunedi) → Routine SETTIMANALE (include giornaliera)
   - Altrimenti → Routine GIORNALIERA

6. **Esegui la routine** secondo il formato definito in `AGENT.md`
   - Quick status (contatori)
   - Urgenze (max 3)
   - Priorita del giorno
   - **Personal Today** — se la sezione `🔥 Oggi` di `personal/todo.md` contiene task, mostra:
     ```
     📋 Personal Today (N items):
     • [ ] Task A
     • [ ] Task B
     ```
     Se `Oggi` è vuota, ometti il blocco silenziosamente.
   - Domanda del giorno
   - Se settimanale: review + spec status + metriche + piano settimana
   - Se mensile: retrospettiva + a rischio + piano mese + domande strategiche

7. **Raccogli risposte** del CEO

8. **Aggiorna**
   - `company/ceo-cadence.md` con data check e log risposte
   - `company/ceo-routine.md` con eventuali nuove promesse
   - Spec frontmatter se il CEO conferma aggiornamenti stato
   - `company/metrics/kpis.md` se il CEO fornisce dati freschi

9. **Handoff** all'agente richiesto dal CEO o suggerisci prossimo step

## Output
Interazione diretta con il CEO (nessun file generato — gli aggiornamenti vanno nei file di stato).
Commit: `[routine] daily: check {YYYY-MM-DD}` (o weekly/monthly)
