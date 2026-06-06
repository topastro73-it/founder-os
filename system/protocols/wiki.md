# Wiki Protocol

La memoria narrativa del sistema, complementare ai file di stato e ai learnings.

## Cos'è

Il wiki cattura il **perché** dietro i dati — decisioni, ragionamento, contesto, domande aperte, promesse. Non è un transcript: è il filo del ragionamento che si perderebbe altrimenti.

## Tre strati di memoria (sempre tenuti separati)

- **File di stato** (`company/`) → i numeri (MRR, pipeline, roadmap). Rispondono a "com'è la situazione?"
- **Wiki** (`wiki/`) → la storia. Rispondono a "come ci siamo arrivati? perché abbiamo deciso così?"
- **Learnings** (`system/learnings.md`) → le regole operative apprese. Rispondono a "cosa abbiamo imparato che dobbiamo ricordare?"

## Struttura

- `wiki/sessions/{YYYY-MM-DD}-{slug}.md` — una pagina per sessione, generata al close
- `wiki/entities/partners/{slug}.md` — **solo timeline narrativa** del partner (storia, "perché"). NON duplica lo stato: niente "Current state"/"Open items"/owner/stage/valore. Quei dati vivono nell'account. La pagina porta in testa un puntatore all'account SoT.
- `wiki/entities/features/{slug}.md` — storia delle feature
- `wiki/entities/decisions/{slug}.md` — evoluzione decisioni
- `wiki/entities/concepts/{slug}.md` — pensiero strategico
- `wiki/index.md` — indice delle ultime 20 sessioni + entity pages

## Quando si genera

Al `/routine close` il sistema produce automaticamente la wiki page secondo il template definito in `.agents/ceo-routine/commands/close.md` (Phase 1, Steps 1-5). Il CEO conferma prima del commit.

## Quando si legge

- Al `/routine start` il sistema mostra il blocco "Dove eravamo rimasti" estratto dall'ultima sessione wiki (decisioni, domande aperte, promesse — vedi `start.md` step 2)
- Al `/routine close` il sistema esegue la **Phase 0 — Retrospective Reconciliation** sugli ultimi 7 giorni (vedi `close.md`): rilegge tutte le sessioni wiki recenti, riconcilia promesse/domande/learnings con la sessione corrente, marca come done quanto chiuso, riporta avanti quanto resta aperto, incrementa contatori Applied dei learnings usati. Il CEO conferma il recap prima della generazione della nuova wiki.

## Regole

- Il wiki è scritto a fine sessione, mai inventato durante
- Estrai dal flusso reale della conversazione, non riassunti generici
- Le promesse con deadline scaduta vanno nelle URGENZE del briefing successivo
- Le entity pages crescono per accumulo (timeline), non si sovrascrivono
- **Account = source of truth dello stato partner** (`company/customers/partners/{slug}.md`); la entity wiki è solo narrativa e linka all'account + alle opportunità (`company/customers/opportunities/`). Mai duplicare stato/owner/blocker/valore nella wiki. Vedi `.skills/opportunity-management/SKILL.md`.
- Tutti i file wiki sono in inglese (vedi feedback memory)

## Privacy

Applica sempre le regole di `CLAUDE.md` § 20-21:
- Mai scrivere IBAN, CF, p.IVA, dati salari in wiki
- Nomi cliente finali: usa iniziali + ruolo (es. "M. Rossi, CISO Acme"), salvo entity page dedicata
- Cross-azienda: anonimizza nomi cliente prima di pubblicare learnings cross-business
