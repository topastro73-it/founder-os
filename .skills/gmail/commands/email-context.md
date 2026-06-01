# Command: email-context

## Agente
Tutti gli agenti

## Trigger
Quando un agente ha bisogno di contesto email su un topic specifico prima di agire.

Esempi di invocazione:
- "cerca le email di Acme Corp sulla proposta"
- "trova le email di feedback sulla feature X"
- "c'è stato qualcosa via email sull'incident di ieri?"
- "cerca email da [candidato] per il colloquio"

## Scopo

Fornire contesto email inline a qualsiasi agente **senza generare file**.
L'output è contesto temporaneo per la conversazione corrente, non viene committato.

## Processo

### Step 1 — Ricevi il topic

L'agente specifica:
- **Topic**: di cosa si tratta (es. "proposta Acme Corp", "feature bulk import", "incident database")
- **Mittente o dominio** (opzionale): se si cerca email da una persona o azienda specifica
- **Finestra temporale** (opzionale, default: 30 giorni)

### Step 2 — Costruisci la query Gmail

Componi la query in base al contesto:

```
# Per topic generico
subject:"[keyword]" OR body:"[keyword]" newer_than:30d

# Per mittente specifico
from:[email-o-dominio] newer_than:30d

# Per combinazione
from:[dominio] subject:"[keyword]" newer_than:14d

# Per thread aperti su un topic
subject:"[keyword]" is:unread

# Per email inviate (per vedere se abbiamo già risposto)
from:me subject:"[keyword]" newer_than:30d
```

### Step 3 — Leggi i thread rilevanti

Per ogni email trovata, leggi il thread con `gmail_read_thread`.
Priorità: thread più recenti e thread con scambi multipli (segno di conversazione attiva).

### Step 4 — Sintetizza il contesto

Restituisci una sintesi strutturata:

```markdown
**Contesto email — [topic]**

Thread trovati: N (ultimi 30 giorni)

**[Data] — [Mittente] → [Destinatario]**
Oggetto: [subject]
Sintesi: [1-2 righe su cosa dice]
Status: [in attesa di risposta / risposto / risolto]

[ripeti per ogni thread rilevante]

**Takeaway**
- [Cosa è rilevante per l'azione corrente dell'agente]
- [Eventuali impegni presi via email non ancora riflessi nel repo]
- [Azioni aperte che emergono dal thread]
```

## Regole di sicurezza

- Mai copiare il testo integrale dell'email — solo sintesi
- Se l'email contiene importi, condizioni contrattuali, dati personali: descrivili genericamente ("c'è una proposta economica", "è stato condiviso un contratto") senza riportare i valori
- Questo comando non genera file — il contesto resta nella conversazione
- Se il contesto è rilevante per una decisione, l'agente lo integra nel documento che sta producendo, non l'email stessa

## Esempi d'uso per agente

**PM**
```
email-context topic="feature bulk import" from="@cliente.com" days=60
```
→ Contesto per scrivere una spec basata su feedback reale

**Sales**
```
email-context topic="proposta Enterprise" from="acme.com" days=14
```
→ Capire a che punto è il deal prima di fare un follow-up

**CTO**
```
email-context topic="incident database" days=7
```
→ Verificare se ci sono state segnalazioni via email prima di scrivere il post-mortem

**CFO**
```
email-context topic="fattura Q1" from="fornitore.com" days=90
```
→ Verificare status fatture prima di chiusura trimestrale

**Legal**
```
email-context topic="NDA Acme" from="legal@acme.com" days=30
```
→ Trovare l'ultimo draft scambiato prima di finalizzare

**HR**
```
email-context topic="colloquio" from="candidato@email.com" days=14
```
→ Recuperare contesto colloquio prima di fare un'offerta
