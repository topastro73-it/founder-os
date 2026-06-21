# Learnings Protocol

Regole operative che il sistema impara dalle esperienze e applica proattivamente.

## Differenza dal wiki

Il wiki dice "il 15 marzo Partner X ha rallentato e abbiamo scoperto che era enablement". Il learning dice "quando un partner rallenta, verifica PRIMA il training venditori — nell'80% dei casi è quello".

## Dove vivono

File unico `system/learnings.md` con frontmatter YAML e formato:

```markdown
### LRN-XXX: Titolo
- **Rule**: When [situazione], [cosa fare / cosa succede].
- **Source**: Session YYYY-MM-DD — [[session-slug]]
- **Applied**: N times (contesti dove è stato usato)
- **Tags**: tag1, tag2
- **Status**: active | archived
```

## Categorie (emergono dall'uso, non sono fisse)

- Partner Management
- Sales & ABM
- Product
- Compliance & Grants
- Process & Operations

## Quando si propongono nuovi learnings

Alla fine di ogni sessione (Phase 1, Step 6b di `close.md`), il sistema analizza la conversazione e propone max 2 pattern generalizzabili. Il CEO approva, modifica o scarta. **Mai salvare senza conferma**.

## Guardrail anti-deriva (candidati non promossi)

Fallimento tipico: le sessioni continuano a **proporre** candidati nelle proprie wiki (`## Learnings proposed`, `## Proposed learning (candidate)`), ma il passo di **promozione** in `system/learnings.md` viene saltato ai close → candidati sepolti e `learnings.md` fermo pur in presenza di pattern nuovi.

Contromisura **bidirezionale** — stesso check a inizio e fine sessione (difesa in profondità):
- **Al close** (`close.md`, Phase 0, Step 0.3 punto E): prima di chiudere.
- **Allo start** (`start.md`, Step 3b): a inizio giornata, così non si aspetta il close per recuperarli.

In entrambi i casi il sistema scansiona le wiki-session degli **ultimi 30 giorni**, estrae i candidati e verifica che ognuno sia stato promosso (LRN corrispondente in `learnings.md`, oppure nota `→ promosso … come LRN-XXX` nella sessione). I candidati non promossi vengono **ri-flaggati** al CEO finché non sono promossi o esplicitamente scartati (`→ scartato {data}`). Così la proposta non basta a "consumare" il candidato: serve una decisione esplicita (promuovi / scarta), e nulla resta appeso silenziosamente.

## Quando si applicano

- Allo `/routine start`, il sistema carica i learnings in memoria (silenziosamente)
- Durante la sessione, quando un task corrisponde a un learning rilevante, il sistema interviene proattivamente: `⚡ Da esperienza passata (LRN-XXX): "{regola}". Suggerisco {azione}.`
- Max 1 learning segnalato per intervento — non sommergere
- Ogni applicazione incrementa il contatore `Applied: N times`

## Regole operative

1. **Chiedere sempre prima di salvare** — non ogni evento è una lezione, decide il CEO
2. **Applicare proattivamente** — se rilevante, mostralo senza che il CEO lo chieda
3. **Tracciare le applicazioni** — il contatore rivela quali regole sono utili
4. **Non sommergere** — max 1-2 learnings nuovi per sessione, max 1 segnalato per intervento
5. **Permettere di archiviare** — i learnings diventano obsoleti, sposta in "Archived" senza eliminare

## Cross-azienda

Un learning nato in Business A (es. partner management) può essere rilevante anche per Business B. Usa tag coerenti per far emergere connessioni cross-business.

## Privacy

Applica sempre `CLAUDE.md` § 21: anonimizza nomi cliente prima di taggare un learning cross-business. Le regole devono essere astratte ("quando un partner rallenta"), non personalizzate ("quando uno specifico partner rallenta").
