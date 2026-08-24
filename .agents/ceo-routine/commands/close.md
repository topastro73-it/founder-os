# Comando: close

## Scopo
Chiudere la sessione di lavoro: generare la pagina wiki della sessione, aggiornare le pagine entita, committare e pushare tutte le modifiche del repo verso il remote, con risoluzione automatica dei conflitti git.

Invocazione: `/routine close` oppure `/close` da qualsiasi agente.
Trigger alternativi: "chiudi", "fine", "stop", "basta per oggi".

---

## Procedura di esecuzione

### Phase 0 — Retrospective Reconciliation (ultimi 7 giorni)

**Scopo**: prima di generare la wiki della sessione corrente, leggere le sessioni wiki e i learnings degli ultimi giorni e **applicarli** alla sessione corrente — chiudere il loop su promesse, domande aperte, e learnings rilevanti.

#### Step 0.1 — Leggi le ultime sessioni wiki

Scansiona `wiki/sessions/` e seleziona i file con data (dal filename `YYYY-MM-DD-{slug}.md`) degli ultimi 7 giorni (escludendo la sessione corrente se già scritta).

Per ogni file estrai dal frontmatter e dal contenuto:
- **Promesse con deadline** (sezione `## Promises`)
- **Domande aperte** (sezione `## Open questions`)
- **Decisioni prese** (sezione `## Decisions` — per back-reference)
- **Entità toccate** (frontmatter `entities:`)
- **Learnings applicati o segnalati** (riferimenti `LRN-XXX`)

Se non esistono sessioni wiki negli ultimi 7 giorni, salta al Step 0.4.

#### Step 0.2 — Carica i learnings attivi

Leggi `system/learnings.md` ed estrai tutti i learnings con `Status: active`. Costruisci una mappa `tag → LRN-ID` per il matching successivo.

#### Step 0.3 — Riconcilia con la sessione corrente

Confronta lo stato passato con quanto emerso nella sessione corrente:

**A. Promesse scadute o in scadenza**
Per ogni promessa estratta dalle ultime 7 sessioni:
- Se `due` ≤ oggi:
  - **Promessa onorata in questa sessione?** (cerca evidenze nella conversazione: file modificati, decisioni prese, output prodotti)
    - Se SÌ → marca la promessa come done nel wiki originale: aggiorna `- [ ]` → `- [x]` nel file `wiki/sessions/{originale}.md` E aggiungi nota: `(completed in [[{session-corrente}]] on YYYY-MM-DD)`
    - Se NO → riportala in URGENZE del prossimo briefing E nelle **Promises** della sessione corrente con flag `⚠️ carried over from {data-originale} ({N} giorni di ritardo)`

**B. Domande aperte non ancora risolte**
Per ogni domanda dalle ultime 7 sessioni:
- **Risolta in questa sessione?** (cerca evidenze: decisione presa, dato fornito, ipotesi confermata)
  - Se SÌ → aggiungi alla sessione corrente sezione **Resolved from previous sessions**: `- "{domanda}" (originaria di [[{session-orig}]]) → {risposta}` E aggiorna il wiki originale: marca la checkbox `- [x]` con back-reference
  - Se NO → resta aperta. Riportala nelle **Open questions** della sessione corrente per non perderla

**C. Learnings applicabili**
Per ogni learning attivo, verifica:
- **Era rilevante per questa sessione?** (matching tag con i temi della conversazione corrente)
  - Se è stato segnalato ed applicato → incrementa `Applied: N times` nel file `system/learnings.md` e aggiungi nel contesto: `(used in {session-slug} YYYY-MM-DD)`
  - Se era applicabile ma NON è stato segnalato → flagga al CEO: `⚠️ LRN-XXX era applicabile in questa sessione ma non è stato segnalato. Vuoi che lo marchi come applicato comunque o lo lascio invariato?`

**D. Entità con cambiamenti**
Per ogni entità toccata nelle ultime 7 sessioni e ancora attiva:
- Verifica se la sessione corrente ha generato nuovi update per quella entità
- Se SÌ → l'aggiornamento entity (Step 4 di Phase 1) deve referenziare la timeline esistente
- Se l'entità è cambiata di stato (es. partner da `onboarding` a `active`, feature da `in-development` a `shipped`) → aggiorna anche il "Current state" della entity page

**E. Candidati learning non promossi** (guardrail anti-deriva)

Per evitare che i learning proposti restino sepolti nelle wiki-session senza mai diventare `LRN-XXX` (la proposta da sola non basta: se il passo di promozione viene saltato ai close, `learnings.md` smette di crescere pur in presenza di pattern nuovi):

- Scansiona le wiki-session **degli ultimi 30 giorni** (finestra estesa rispetto ai 7 della retrospective, perché un candidato può restare appeso a lungo) cercando le sezioni `## Learnings proposed`, `## Proposed learning (candidate)` o righe con "candidate learning".
- Per ogni candidato trovato, verifica se è **già stato promosso**: cerca in `system/learnings.md` un LRN con concetto/fonte corrispondente, **oppure** una nota `→ promosso … come LRN-XXX` nella sessione originale.
- Se **non** promosso → riportalo nel recap (Step 0.4) sotto "🧠 Candidati learning mai promossi".
- Su conferma del CEO → promuovilo come nuovo `LRN-XXX` (riusa Step 6b), incrementa il frontmatter di `learnings.md` (`total`/`active`/`updated` + tag), e annota nella sessione originale `→ promosso {oggi} come LRN-XXX`. Aggiungi la entry in `system/CHANGELOG.md` se il batch tocca anche protocolli/agenti.
- Se il CEO dice "no/più tardi" → lascia il candidato dov'è (non insistere), ma resterà flaggato ai close successivi finché non è promosso o esplicitamente scartato (aggiungi `→ scartato {oggi}` nella sessione per silenziarlo).

#### Step 0.4 — Mostra al CEO il recap retrospective

```
🔄 Retrospective check — ultimi 7 giorni

✅ Chiuse in questa sessione
- Promessa "{X}" (da {data}, {N}gg ritardo) → completata
- Domanda "{Y}" (da {data}) → risolta: {risposta breve}

⚠️ Ancora aperte (riportate avanti)
- Promessa "{Z}" (da {data}, {N}gg ritardo) — carried over
- Domanda "{W}" (da {data}) — ancora da decidere

🧠 Learnings applicati in questa sessione
- LRN-{XXX} ({titolo breve}) — Applied counter: {N+1}

⚡ Learnings applicabili NON segnalati
- LRN-{YYY} ({titolo breve}) — vuoi marcarli come applicati?

🧠 Candidati learning mai promossi (da sessioni precedenti, ultimi 30gg)
- "{candidato}" (proposto in [[{session-orig}]] il {data}) — promuovo come LRN nuovo? [sì/scarta/più tardi]

📂 Entità aggiornate dal retrospective
- {entity-slug}: stato {old} → {new}

Procedo con la generazione della wiki sessione?
```

Aspetta conferma del CEO. Se il CEO dice "vai" o "ok", procedi con Phase 1. Se vuole correzioni manuali (es. "no, quella promessa l'ho già fatta ieri"), aggiusta prima di procedere.

#### Step 0.5 — Applica le correzioni ai file

Solo dopo conferma del CEO:
- Aggiorna i wiki delle ultime sessioni (`- [ ]` → `- [x]` con back-reference)
- Incrementa contatori `Applied: N` in `system/learnings.md`
- Aggiorna `Current state` nelle entity pages

Tutti questi cambiamenti finiranno nel commit della Phase 2 (insieme alla nuova wiki sessione).

---

### Phase 1 — Session Wiki Generation

#### Step 1 — Rileggi la conversazione della sessione
Analizza l'intera conversazione corrente e estrai:
- **Decisioni prese**: qualsiasi "decidiamo", "andiamo con", "approvato", scelta esplicita
- **Dati emersi**: numeri, metriche, info business menzionati o aggiornati
- **Ragionamenti chiave**: il "perche" dietro le decisioni (la parte piu preziosa)
- **Domande rimaste aperte**: cose da investigare, decidere, verificare
- **Promesse fatte**: "lo faccio domani", "entro venerdi", qualsiasi impegno con deadline
- **File creati o modificati**: lista dai commit della sessione
- **Agenti utilizzati**: quali agenti sono stati invocati

#### Step 2 — Genera titolo automatico
- Max 5 parole, descrittivo del focus della sessione
- Esempi: "Pricing review + Partner X onboarding", "Bulk import spec approval", "Monthly retrospective April"

#### Step 3 — Genera la pagina wiki sessione
Crea il file `wiki/sessions/{YYYY-MM-DD}-{slug}.md` con questo formato:

```markdown
---
type: session
date: {YYYY-MM-DD}
title: {titolo auto-generato}
agents: [{lista agenti usati}]
duration: ~{stima durata}
entities: [{partner, feature, decisioni toccate}]
tags: [{tag rilevanti}]
decisions: [{slug decisioni prese}]
open-questions: [{slug domande aperte}]
promises:
  - what: {descrizione promessa}
    due: {YYYY-MM-DD}
related:
  - {file del repo toccati o rilevanti}
---

# Session: {data} — {titolo}

## Context
[Perche questa sessione, cosa ha portato qui]

## Decisions
[Per ogni decisione:]
### {Titolo decisione}
- **Decision**: {cosa si e deciso}
- **Rationale**: {perche}
- **Impact**: {cosa cambia}
- **File**: [[file collegato se esiste]]

## Data updates
- {metrica}: {valore} (saved in {file} ✓)
- ...

## Key reasoning
[Il contesto e il "perche" dietro le decisioni — la parte piu preziosa
che si perde nelle note tradizionali]

## Open questions
- [ ] {domanda} — {ipotesi o prossimo step}
- ...

## Promises
- [ ] {cosa} — due: {YYYY-MM-DD}
- ...

## Files touched
- {file} ({created/updated})
- ...

## Agents used
- {lista agenti}
```

#### Step 4 — Aggiorna le pagine entita
Per ogni entita toccata nella sessione (partner, feature, decisione, concetto):

1. Cerca se esiste `wiki/entities/{tipo}/{slug}.md`
2. **Se esiste** → aggiungi una voce nella sezione Timeline:
   ```markdown
   ### {YYYY-MM-DD} — [[{session-slug}]]
   - {punto 1}
   - {punto 2}
   - Action: {prossima azione se presente}
   ```
   Aggiorna anche la sezione "Current state" se i dati sono cambiati.

3. **Se non esiste** → crea la pagina entita:
   ```markdown
   ---
   type: entity
   entity_type: {partner|feature|decision|concept}
   name: {Nome}
   tags: [{tag rilevanti}]
   ---

   # {Nome}

   {Breve descrizione, 1-2 righe}

   ## Timeline (from sessions)

   ### {YYYY-MM-DD} — [[{session-slug}]]
   - {punti chiave dalla sessione}

   ## Current state
   - **Status**: {stato corrente}
   - {altri dati rilevanti}
   ```

#### Step 5 — Aggiorna wiki/index.md
Aggiungi la nuova sessione nella sezione "Recent Sessions" (mantieni le ultime 20).
Aggiungi nuove pagine entita se create.

#### Step 6 — Proponi salvataggio dati (Persistent Memory Protocol)
Se nella sessione sono emersi dati che andrebbero salvati nei file di stato del repo
(metriche in `kpis.md`, stato partner in `customers/partners/`, promesse in `ceo-routine.md`):
- Mostra al CEO cosa proponi di aggiornare
- Aspetta conferma prima di modificare file di stato

#### Step 6b — Proponi nuovi learnings
Analizza la sessione per pattern riutilizzabili:
- Un problema e stato risolto → la soluzione e generalizzabile?
- Un errore e stato evitato → perche?
- Un processo ha funzionato bene → replicabile?
- Un'assunzione era sbagliata → cosa abbiamo imparato?

Se trova potenziali learnings, proponi:
```
🧠 Possibili learnings da questa sessione:
1. "Quando [situazione], [cosa succede/cosa fare]"
   → Salvo come learning?
Salvo, modifico o scarto?
```

- Se il CEO conferma → aggiungi a `system/learnings.md` con ID incrementale (LRN-XXX), testo, categoria, fonte (sessione corrente), tag, contatore "Applied: 0 times"
- Se il CEO dice "no" → non salvare, non insistere
- Max 2 learnings proposti per sessione — solo quelli davvero generalizzabili

#### Step 6b.5 — Personal Todo cleanup

Leggi `personal/todo.md` e controlla la sezione `## 🔥 Oggi`:

- Se ci sono task `- [ ]` non completati, chiedi al CEO:
  ```
  📋 Personal Today — task non completati ({N}):
  • "{task 1}"
  • "{task 2}"
  → Sposto in "Questa settimana"? [sì/no/segna fatto]
  ```
- Se il CEO conferma → sposta i task non completati in `## 📅 Questa settimana`
- Se il CEO segna qualcuno come fatto → applicare `/personal done` su quelli indicati
- Aggiorna `_Last updated: YYYY-MM-DD_` nel file
- Le modifiche a `personal/todo.md` saranno incluse nel commit di Phase 2
- Se `Oggi` è già vuota, salta silenziosamente

#### Step 6b.7 — Aggiorna il cadence log (obbligatorio)

Aggiorna `company/ceo-cadence.md` (vedi `system/protocols/ceo-decision-cadence.md`):
- Sezione "Ultimo check per ritmo": aggiorna la data per **giornaliero** sempre; per **settimanale** se
  questa è la prima sessione della settimana (lunedì); per **mensile** se prima sessione del mese
- Sezione "Log risposte recenti": aggiungi una riga con data, tipo di routine eseguita, e un riassunto
  di una riga della sessione

Questo passo è **obbligatorio quanto la generazione della wiki** (Step 3): non deve dipendere
dall'essere ricordato durante un'interazione lunga. Se il close avviene senza aver mai eseguito lo
Step 8 di `start.md` in questa sessione (es. il CEO ha aperto lavorando già su un altro agente), esegui
comunque questo aggiornamento prima di committare. Le modifiche entrano nel commit di Phase 2.

#### Step 6c — Proponi reminder ClickUp per promesse (opzionale)
Se nella sessione sono emerse promesse con deadline:
```
📌 Promises from this session:
1. "{cosa}" — due: {YYYY-MM-DD}
Create ClickUp reminders?
```
- Se ClickUp disponibile e confermato → crea reminder via MCP ClickUp
- Se ClickUp non disponibile → salva solo in `ceo-cadence.md`

#### Step 7 — Chiedi conferma
```
📖 Wiki sessione generata: wiki/sessions/{file}.md
   Entita aggiornate: {lista}
   Dati da salvare: {lista file di stato}

   Salvo tutto e chiudo?
```

Se il CEO conferma, procedi. Se vuole aggiungere qualcosa, aspetta.

---

### Phase 2 — Git Close (dopo conferma CEO)

#### Step 8 — Identifica la macchina

```bash
scutil --get LocalHostName
```

Includi il nome macchina nel commit message.

#### Step 9 — Verifica stato repo

```bash
git -C <repo_root> status --short
git -C <repo_root> diff --stat HEAD
```

Se non ci sono modifiche (working tree pulito e nessun file wiki generato), concludi con:
> ✅ Nessuna modifica da committare. Repo gia in sync.

#### Step 10 — Stage di tutte le modifiche

```bash
git -C <repo_root> add -A
```

#### Step 11 — Costruisci il commit message
Formato:
```
[wiki] session: {titolo sessione}

Wiki: wiki/sessions/{file}.md
Entities: {lista entita aggiornate/create}

Retrospective:
- Promesse chiuse: {N}
- Domande risolte: {N}
- Learnings applicati: LRN-XXX ({N+1})
- Carried over: {N} promesse, {N} domande

Files modificati:
- <lista file staged>

Sessione chiusa.
```

Se nella sessione sono stati salvati nuovi learnings, aggiungili:
```
New learnings: LRN-XXX ({titolo})
```

Se il retrospective check non ha rilevato nulla (sessione isolata, nessuna sessione precedente negli ultimi 7gg), ometti la sezione "Retrospective".

Se nella sessione non si e generato il wiki (es. sessione brevissima senza contenuto significativo), usa il formato legacy:
```
[routine] close: <YYYY-MM-DD> [<NomeMacchina>]
```

#### Step 12 — Commit

```bash
git -C <repo_root> commit -m "<messaggio>"
```

Se il commit fallisce per repo pulito (exit 1, "nothing to commit"), salta al Step 15.

#### Step 13 — Fetch del remote per rilevare divergenze

```bash
git -C <repo_root> fetch origin
git -C <repo_root> rev-list --count HEAD..origin/v2
```

Se count = 0 → il remote non ha modifiche nuove → vai a Step 15 (push diretto).
Se count > 0 → ci sono commit sul remote non presenti in locale → vai a Step 14.

#### Step 14 — Merge automatico con gestione conflitti

```bash
git -C <repo_root> merge origin/v2 --no-edit -m "merge: auto-sync from remote [routine close]"
```

**Caso A — Merge riuscito senza conflitti**: procedi al Step 15.

**Caso B — Conflitti rilevati** (`git status` mostra file `UU`/`AA`/`DD`):

1. Identifica i file in conflitto:
   ```bash
   git -C <repo_root> diff --name-only --diff-filter=U
   ```

2. Per ogni file in conflitto, tenta risoluzione automatica:
   - **File di testo strutturati** (`.md`, `.yaml`, `.json`): applica strategia `union`
     ```bash
     git -C <repo_root> checkout --merge <file>
     ```
   - **File critici** (`CLAUDE.md`, `*.md` in `company/strategy/`, `company/product/specs/`):
     usa strategia `ours` (locale vince su file di sistema):
     ```bash
     git -C <repo_root> checkout --ours <file>
     git -C <repo_root> add <file>
     ```

3. Crea il file di log dei conflitti:
   ```
   CONFLICTS.md  (nella root del repo)
   ```
   Contenuto:
   ```markdown
   # Conflitti rilevati — <YYYY-MM-DD HH:MM>

   Macchina: <NomeMacchina>
   Branch: v2
   Remote: origin/v2

   ## File in conflitto risolti automaticamente
   | File | Strategia usata | Note |
   |------|----------------|------|
   | <file> | ours / union | <breve nota> |

   ## File in conflitto NON risolti (richiede revisione manuale)
   | File | Motivo |
   |------|--------|
   | <file> | <motivo> |

   ## Azione richiesta
   - [ ] Revisionare i file sopra elencati
   - [ ] Cancellare questo file quando risolto
   ```

4. Se rimangono ancora marker di conflitto (`<<<<<<`), non eseguire il commit di quel file.
   Aggiungi il file a "NON risolti" in `CONFLICTS.md` e escludilo dallo stage:
   ```bash
   git -C <repo_root> checkout HEAD -- <file>
   ```

5. Committa cio che e stato risolto + `CONFLICTS.md`:
   ```bash
   git -C <repo_root> add -A
   git -C <repo_root> commit -m "[routine] close: <data> — merge con conflitti parziali [<NomeMacchina>]"
   ```

6. **Notifica al CEO** con un messaggio del tipo:
   > ⚠️ **Conflitti rilevati durante il close**
   > Ho risolto automaticamente N file (strategia: ours/union).
   > Questi file richiedono revisione manuale prima del prossimo close:
   > - `<file1>` — motivo
   > Dettagli in `CONFLICTS.md`.

#### Step 15 — Push verso il remote

```bash
git -C <repo_root> push origin v2
```

Se il push fallisce per divergenza (rejected, non-fast-forward):
```bash
git -C <repo_root> pull --rebase origin v2
git -C <repo_root> push origin v2
```

Se anche il rebase fallisce, torna allo Step 14 per i file in conflitto.

#### Step 16 — RAG Re-index (background)
Esegui in background (non blocca il close):
```bash
python3 scripts/rag-index.py
```
Se lo script non esiste o fallisce, salta silenziosamente.

#### Step 17 — Conferma finale
Mostra al CEO:
```
✅ Close completato — <YYYY-MM-DD HH:MM>
   Macchina: <NomeMacchina>
   Commit: <SHA breve>
   Files committati: <N>
   Push: ✅ origin/v2 aggiornato

📖 Wiki: wiki/sessions/{file}.md
   Entita: {N} aggiornate, {N} create

🔄 Retrospective (ultimi 7gg)
   Promesse chiuse: {N} / aperte: {N}
   Domande risolte: {N} / ancora aperte: {N}
   Learnings applicati (counter +1): {lista LRN-XXX}
   Learnings nuovi salvati: {N}

⚠️ Carried over al prossimo briefing
   {lista promesse e domande riportate avanti}

   Conflitti: nessuno / N file risolti (dettagli in CONFLICTS.md)
   RAG: re-indicizzazione in corso (background)

✨ Sessione chiusa. A domani!
```

Se il retrospective check non ha rilevato nulla, ometti i blocchi 🔄 e ⚠️.

---

## Variabili di ambiente richieste

| Variabile | Come ottenerla |
|-----------|---------------|
| `<repo_root>` | Directory del repo: default `/Users/<user>/founder-os` o path rilevato con `git rev-parse --show-toplevel` |
| `<NomeMacchina>` | Da `scutil --get LocalHostName` |
| `<YYYY-MM-DD>` | Da `date +%Y-%m-%d` |

---

## Note operative

- Questo comando e **non-distruttivo**: non fa mai `git reset --hard` ne `git push --force`
- In caso di dubbio, preferisci creare un commit e lasciare `CONFLICTS.md` piuttosto che perdere lavoro
- Se il repo non ha un remote configurato, skippa gli Step 13-15 e notifica il CEO
- Esegui sempre da `v2` — è il branch di lavoro permanente, **non si mergia mai su `main`**. Se sei su un altro branch, notifica prima di procedere
- **NON chiudere mai senza chiedere** — il CEO potrebbe voler aggiungere qualcosa
- Il titolo e auto-generato ma il CEO puo modificarlo
- Le promesse con deadline diventano reminder — proponi di creare task su ClickUp se disponibile
- Le domande aperte vengono ripresentate nella sessione successiva (via wiki context in start)
