# Skill: Skill Creator

## Identità

Guida conversazionale per creare una nuova skill nel sistema.
Non richiede conoscenze tecniche: Claude conduce un'intervista, l'utente risponde in linguaggio naturale, Claude genera tutti i file.

**Attivazione**: l'utente dice qualcosa come "voglio creare una skill", "ho bisogno di una nuova skill", "aggiungi una skill per X", o invoca `/create-skill`.

---

## Come funziona

Claude conduce un'intervista in sequenza. Fa **una domanda alla volta**, in italiano semplice. Alla fine genera tutto automaticamente.

Non serve sapere cosa sia un "slug", un "path" o un "comando" — Claude traduce le risposte in struttura tecnica.

---

## Flow dell'intervista

### Step 1 — Scoperta

Prima di fare domande, Claude legge:
- `.skills/SKILLS.md` — per capire le skill esistenti ed evitare duplicati
- `.agents/AGENTS.md` — per conoscere gli agenti disponibili come owner

Poi spiega brevemente all'utente cosa sta per fare e inizia con la prima domanda.

---

### Step 2 — Intervista (7 domande, una alla volta)

**D1. A cosa serve questa skill?**
> "Descrivi con parole tue cosa deve fare questa skill. Non importa la forma — anche un paragrafo va bene."

→ Claude estrae: scopo, verbi chiave, dominio

---

**D2. Chi la usa principalmente?**
> "Chi nella tua azienda userà questa skill? (es. il founder, il team sales, chi gestisce i clienti, chi si occupa di finanza...)"

→ Claude mappa su agenti esistenti in `.agents/`. Se l'utente nomina un ruolo non mappato, Claude chiede di confermare l'agente più vicino.

---

**D3. Cosa fa in concreto?**
> "Dimmi le 2-5 azioni principali che questa skill deve saper fare. Esempi: 'prepara un report', 'manda un'email', 'calcola un punteggio', 'genera un documento'."

→ Claude crea la lista dei comandi. Per ogni azione, chiede:
- Come si chiama (Claude suggerisce un nome slug, l'utente approva o corregge)
- Cosa produce in output (documento, report, dati, email...)

Se l'utente non sa cosa rispondere a "cosa produce", Claude suggerisce l'output più naturale per quell'azione.

---

**D4. Ha bisogno di dati o strumenti esterni?**
> "Per fare queste cose, la skill deve accedere a qualcosa di specifico? (es. un CRM, un foglio Excel, un'API, un'altra skill già esistente, dati in una cartella...)"

→ Claude identifica dipendenze. Se nessuna: passa avanti.

---

**D5. Dove vanno salvati i risultati?**
> "Quando la skill produce qualcosa, dove vuoi trovarlo? (es. in una cartella documenti, in una sezione report, nel profilo di un cliente...)"

→ Claude mappa su path esistenti da `CLAUDE.md` (tabella output rules). Se il path non esiste, propone di crearlo o di usarne uno simile.

---

**D6. Ci sono regole o vincoli importanti?**
> "C'è qualcosa che questa skill non deve mai fare, o qualche regola che deve sempre rispettare? (es. 'non mandare mai email senza approvazione', 'usare sempre il template X', 'non toccare i dati di produzione')"

→ Se nessuna: passa avanti.

---

**D7. Tipo di skill**
Claude valuta in autonomia in base alle risposte se è una skill **operativa** (ha comandi eseguibili, integrazione con sistemi) o **di contesto** (framework, guide, background). Mostra la sua valutazione e chiede conferma:

> "In base a quello che mi hai detto, questa mi sembra una skill **operativa** — ha comandi che producono output concreti. Confermi, o è più una guida/framework di riferimento?"

---

### Step 3 — Riepilogo e conferma

Claude mostra un riepilogo strutturato di tutto prima di creare i file:

```
📋 Riepilogo skill "{Nome}"

Scopo: ...
Tipo: operativa / di contesto
Owner: ...
Usata da: ...

Comandi:
  • {comando-1} → {output} → salvato in {path}
  • {comando-2} → {output} → salvato in {path}

Dipendenze: ...
Regole: ...
```

Poi chiede:
> "Va bene così? Posso procedere a creare i file, oppure vuoi cambiare qualcosa?"

Se l'utente vuole correggere: Claude aggiorna il punto specifico e mostra il riepilogo aggiornato.

---

### Step 4 — Generazione automatica

Dopo conferma, Claude crea:

1. **`.skills/{slug}/SKILL.md`** — usando il template sotto
2. **Aggiorna `.skills/SKILLS.md`** — aggiunge la riga nella tabella corretta (operativa o contesto)
3. **Aggiorna `system/CHANGELOG.md`** — entry `feat: nuova skill {nome}` con data e categoria MINOR
4. **Commit** — `[system] feat: nuova skill {slug}`

Comunica all'utente cosa ha creato, dove trovare i file, e come invocare la skill.

---

## Template generato: skill operativa

```markdown
# Skill: {Nome}

## Identità

{Scopo in 2-3 frasi, linguaggio chiaro}
Usata da: {agenti}.

---

## Comandi

| Comando | Descrizione | Output |
|---------|------------|--------|
| `{comando}` | {cosa fa} | {cosa produce} — salvato in `{path}` |

---

## Comando: {comando}

### Input
- {parametri necessari, opzionali}

### Processo
1. {step 1}
2. {step 2}
3. ...

### Output
{descrizione output + path di destinazione}

---

## Regole
{vincoli e regole emerse nell'intervista — ometti la sezione se vuota}

## Dipendenze
{altre skill, MCP tool, API — ometti la sezione se vuota}
```

---

## Template generato: skill di contesto

```markdown
# Skill: {Nome}

{Scopo in 2-3 frasi. Quando usarla e perché.}
Usata da: {agenti} come background per informare le decisioni su {dominio}.

---

## {Sezione 1 — framework/concetto principale}

{contenuto}

---

## {Sezione 2}

{contenuto}

---

## Quando applicarla

{situazioni specifiche in cui questa skill è rilevante}
```

---

## Comportamento di Claude durante l'intervista

- **Una domanda alla volta** — non fare liste di domande
- **Adatta il linguaggio** all'utente: se usa termini tecnici, Claude può usarli; se parla in modo operativo/business, Claude resta su quel registro
- **Suggerisci sempre** un'opzione di default che l'utente può accettare o modificare — non lasciare mai l'utente di fronte a una domanda aperta senza un punto di partenza
- **Traduci in tecnico** in silenzio: l'utente non vede slug, path, frontmatter — vede solo nomi e concetti
- **Se una risposta è ambigua**, riformula con un esempio e chiedi conferma: "Vuoi dire che il comando produce un file da aprire, oppure aggiorna dei dati già esistenti?"
- **Mai bloccarsi** su una domanda: se l'utente non sa rispondere, Claude sceglie il default più ragionevole e va avanti

---

## Esempio di conversazione

> **Utente**: voglio creare una skill per gestire le interviste agli utenti

> **Claude**: Perfetto. Ho visto che non esiste ancora una skill per questo, quindi la creo da zero.
>
> Prima domanda: **a cosa serve esattamente questa skill?** Descrivi cosa deve fare — anche in modo informale va benissimo.

> **Utente**: quando facciamo interviste con i clienti o potenziali clienti, voglio avere un posto dove raccogliere i risultati, estrarre i temi principali, e capire cosa emerge di ricorrente

> **Claude**: Chiaro. Chi nella tua azienda userà questa skill principalmente — tu come founder, qualcuno del team prodotto, il team sales, o tutti?

> **Utente**: soprattutto io e chi gestisce il prodotto

> **Claude**: Perfetto, la associo a te (CEO) e al PM.
>
> Prossima domanda: **cosa deve fare concretamente?** Dimmi le azioni principali — puoi elencarle o descriverle come vuoi. Per esempio: "raccogliere i dati di un'intervista", "fare un report riassuntivo", "trovare i temi ricorrenti"...

*(e così via)*
