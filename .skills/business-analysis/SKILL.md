# Business Analysis & Functional Analysis Skill

Skill per il PM che lo trasforma in un Business Analyst.
Quando si affronta un nuovo tema, il PM NON scrive subito una spec.
Prima conduce un'analisi funzionale interattiva: fa domande,
capisce il dominio, mappa l'AS-IS, e solo poi propone il TO-BE.

## Principio fondamentale

```
MAI scrivere una spec senza aver prima capito:
1. Come funziona OGGI (AS-IS)
2. PERCHÉ funziona così
3. Cosa NON funziona e perché
4. Cosa DOVREBBE cambiare e per chi

Le domande vengono PRIMA delle soluzioni. Sempre.
```

## Come funziona

Quando il CEO dice "voglio analizzare [tema]" o "dobbiamo capire come gestire [processo]",
il PM entra in **modalità Business Analyst**:

1. Non propone soluzioni
2. Fa domande per capire il dominio
3. Documenta le risposte in tempo reale
4. Costruisce progressivamente il modello funzionale
5. Solo alla fine propone la spec

Il processo è **conversazionale e iterativo** — non un questionario rigido.

---

## Comandi disponibili

### `/pm analyze [topic]`
Avvia un'analisi funzionale interattiva su un tema.

**Processo — Fase 1: DOMAIN UNDERSTANDING**

Il PM inizia con domande aperte per capire il perimetro:

```
📊 Analisi funzionale: {topic}

Iniziamo a capire il dominio. Rispondimi con il livello di dettaglio 
che vuoi — posso approfondire ogni punto.

1. PANORAMICA
   - Cos'è [topic] nel contesto della tua azienda?
   - Chi sono gli attori coinvolti? (utenti, sistemi, partner)
   - Dove si colloca nel flusso di lavoro attuale?

2. STATO ATTUALE (AS-IS)
   - Come viene gestito oggi?
   - Con quali strumenti? (manuale, Excel, tool, piattaforma)
   - Da chi? (ruolo, persona)
   - Con quale frequenza?

Rispondimi e approfondisco da lì.
```

**Processo — Fase 2: DEEP DIVE**

In base alle risposte, il PM approfondisce con domande mirate.
Non fa tutte le domande insieme — procede per strati:

**Strato dati**:
- Quali dati/entità sono coinvolti?
- Che campi ha ogni entità? Che valori possono avere?
- Da dove vengono i dati? Chi li inserisce?
- Come sono collegati tra loro? (relazioni)
- Ci sono dati calcolati o derivati?
- Qual è il volume? (quanti record, quante volte al giorno/mese)

**Strato processi**:
- Quali sono i passaggi del processo dall'inizio alla fine?
- Ci sono approvazioni o passaggi di stato?
- Ci sono condizioni/regole business? ("se X allora Y")
- Cosa succede quando qualcosa va storto? (eccezioni, errori)
- Ci sono deadline o SLA?
- Chi viene notificato e quando?

**Strato utenti**:
- Chi fa cosa in questo processo?
- Quali sono i permessi? Chi può vedere/modificare cosa?
- Qual è l'esperienza utente oggi? Dove si blocca? Cosa è confuso?
- Quali sono i workaround che usano? (indizio di problemi)

**Strato integrazioni**:
- Quali altri sistemi sono coinvolti?
- Come comunicano? (API, export CSV, manuale, email)
- Ci sono sincronizzazioni? In tempo reale o batch?
- Cosa succede quando un sistema è offline?

**Strato regole business**:
- Ci sono regole di validazione? (es. "il campo X è obbligatorio se Y")
- Ci sono calcoli? (es. "il prezzo = base × quantità × sconto")
- Ci sono stati e transizioni? (es. "da bozza a approvato a attivo")
- Ci sono limiti? (es. "max 100 record per utente")
- Ci sono eccezioni alle regole? (es. "tranne per i clienti Tier 1")

**Processo — Fase 3: PAIN POINTS & GAPS**

```
⚠️ Problemi e lacune — Cosa non funziona oggi?

- Quali sono i problemi principali con il processo attuale?
- Dove si perde tempo? Dove si fanno errori?
- Ci sono dati che dovresti avere e non hai?
- C'è qualcosa che fai manualmente e dovrebbe essere automatico?
- Cosa ti chiedono i partner/clienti che non riesci a fare?
- Se potessi cambiare UNA cosa, quale sarebbe?
```

**Processo — Fase 4: TO-BE PROPOSAL**

Solo dopo aver capito tutto, il PM propone:

```
📋 Proposta funzionale: {topic}

Basandomi su quello che mi hai raccontato, ecco come potrebbe funzionare:

AS-IS (oggi):
[riassunto di come funziona oggi]

PROBLEMI:
[lista problemi identificati]

TO-BE (proposta):
[come dovrebbe funzionare, con cambiamenti evidenziati]

IMPATTO:
[cosa cambia per chi, beneficio atteso]

Vuoi che proceda con la PRD completa?
```

**Output finale**: `company/product/analysis/analysis-{slug}.md`
Se approvato — genera PRD con `/pm write-spec`

---

### `/pm map-process [process]`
Mappa un processo esistente step by step.

**Processo**:
1. Chiedi di descrivere il processo dall'inizio alla fine
2. Per ogni step chiedi: chi, cosa fa, con quali dati, quale output, quanto tempo
3. Identifica: decisioni (diamond), loop, branch condizionali
4. Genera diagramma di flusso in formato testuale/mermaid
5. Identifica: colli di bottiglia, passaggi manuali eliminabili, punti di errore

**Output format**:
```markdown
# Process Map: {processo}

## Attori
- [Attore 1]: [ruolo nel processo]
- [Attore 2]: [ruolo]

## Flusso

### Step 1: {nome}
- **Chi**: [attore]
- **Cosa**: [azione]
- **Input**: [dati in ingresso]
- **Output**: [dati in uscita]
- **Tempo**: [quanto ci vuole]
- **Tool**: [strumento usato]
- **Note**: [problemi, workaround]

### Step 2: {nome}
...

### Decision Point: {condizione}
- Se [condizione A] → vai a Step X
- Se [condizione B] → vai a Step Y

## Diagramma (Mermaid)
```mermaid
flowchart TD
    A[Start] --> B[Step 1]
    B --> C{Decisione}
    C -->|Sì| D[Step 2a]
    C -->|No| E[Step 2b]
    D --> F[End]
    E --> F
```

## Problemi identificati
1. [Collo di bottiglia in Step X]
2. [Passaggio manuale eliminabile in Step Y]
3. [Punto di errore in Step Z]

## Suggerimenti di miglioramento
1. [Proposta]
```

**Output**: `company/product/analysis/process-{slug}.md`

### `/pm data-model [entity]`
Mappa il modello dati di un'entità o dominio.

**Processo**:
1. Chiedi: "Cos'è [entità]? Che informazioni contiene?"
2. Per ogni campo chiedi:
   - Nome del campo
   - Tipo (testo, numero, data, booleano, lista, riferimento)
   - Obbligatorio o opzionale?
   - Valori possibili (se è una lista/enum)
   - Da dove viene il valore? (inserito, calcolato, da altro sistema)
   - Chi può vederlo/modificarlo?
   - Validazioni (lunghezza, formato, range)
3. Chiedi relazioni: "A cosa è collegato? Un [entità] ha molti [altra entità]?"
4. Genera modello dati documentato

**Output format**:
```markdown
# Data Model: {Entità}

## Descrizione
[Cos'è questa entità nel business]

## Campi

| Campo | Tipo | Obbligatorio | Valori | Fonte | Note |
|-------|------|-------------|--------|-------|------|
| id | UUID | Sì | auto-generato | Sistema | PK |
| name | Testo | Sì | max 100 char | Utente | |
| status | Enum | Sì | draft/active/suspended | Sistema | Default: draft |
| parent_id | FK → ParentEntity | Sì | | Relazione | |
| created_at | DateTime | Sì | | Sistema | |
| score | Integer | No | 0-100 | Calcolato | Media dei check |

## Relazioni

| Relazione | Tipo | Con | Note |
|-----------|------|-----|------|
| Appartiene a | N:1 | ParentEntity | Ogni record ha un solo parent |
| Ha molti | 1:N | SubEntity | Storico delle sub-entità |

## Diagramma

```mermaid
erDiagram
    PARENT ||--o{ CHILD : "gestisce"
    CHILD ||--o{ ASSESSMENT : "ha"
    CHILD {
        uuid id PK
        string name
        enum status
        int score
    }
```

## Regole business
- Lo status può passare da draft → active solo se [condizione]
- Lo score viene ricalcolato quando [evento]
- Un record non può essere eliminato se ha elementi attivi associati
```

**Output**: `company/product/analysis/data-model-{slug}.md`

### `/pm requirements-elicitation [topic]`
Sessione di elicitazione requisiti strutturata.

**Processo**:
Il PM conduce un'intervista usando tecniche diverse in base al contesto:

**Tecnica 1: 5W+H**
- What: cosa deve fare il sistema?
- Who: chi lo usa? Chi ne beneficia?
- When: quando lo usano? Con quale frequenza?
- Where: dove lo usano? (device, contesto)
- Why: perché serve? Quale problema risolve?
- How: come dovrebbe funzionare? Come funziona oggi?

**Tecnica 2: User Journey**
- Chiedi di descrivere una giornata tipo dell'utente
- Per ogni momento: cosa fa, cosa prova, cosa vorrebbe

**Tecnica 3: Scenari "E se..."**
- "E se l'utente inserisce dati sbagliati?"
- "E se il sistema è offline?"
- "E se ci sono 1000 record invece di 10?"
- "E se il cliente vuole personalizzare X?"
- "E se l'utente non completa il processo?"

**Tecnica 4: MoSCoW**
Per ogni requisito emerso, classifica:
- **Must**: senza questo non funziona
- **Should**: importante ma possiamo vivere senza nella v1
- **Could**: nice-to-have
- **Won't**: esplicitamente fuori scope (importante da documentare)

**Output**: `company/product/analysis/requirements-{slug}.md`

### `/pm gap-analysis [area]`
Analisi gap tra stato attuale e stato desiderato.

**Processo**:
1. Documenta AS-IS (come funziona oggi)
2. Documenta TO-BE (come dovrebbe funzionare)
3. Identifica i gap specifici:

```markdown
# Gap Analysis: {area}

| # | Area | AS-IS | TO-BE | Gap | Priorità | Effort |
|---|------|-------|-------|-----|----------|--------|
| 1 | [area] | [oggi] | [domani] | [cosa manca] | Must/Should/Could | S/M/L |
```

4. Per ogni gap: proponi soluzione e impatto
5. Prioritizza i gap per valore business

**Output**: `company/product/analysis/gap-analysis-{slug}.md`

### `/pm functional-spec [topic]`
Genera specifica funzionale dettagliata (dopo l'analisi).

**Differenza PRD vs Functional Spec**:
- **PRD** = COSA costruire e PERCHÉ (business)
- **Functional Spec** = COME funziona in dettaglio (comportamento)

**Processo**:
1. Leggi l'analisi fatta (`company/product/analysis/analysis-{slug}.md`)
2. Genera specifica funzionale:

```markdown
# Functional Specification: {Feature}

**Analisi di riferimento**: company/product/analysis/analysis-{slug}.md
**PRD**: company/product/specs/prd-{slug}.md
**Data**: {YYYY-MM-DD}

## 1. Panoramica funzionale
[Come funziona la feature dal punto di vista dell'utente]

## 2. Attori e permessi
| Attore | Può | Non può |
|--------|-----|---------|

## 3. Modello dati
[Entità, campi, relazioni — dal data-model se fatto]

## 4. Flussi funzionali

### Flusso 1: {nome} (happy path)
1. L'utente [azione]
2. Il sistema [risposta]
3. L'utente [azione]
4. Il sistema [risposta]
5. Risultato: [stato finale]

### Flusso 2: {nome} (caso alternativo)
...

### Flusso 3: {nome} (gestione errore)
...

## 5. Regole business
| ID | Regola | Condizione | Azione | Eccezioni |
|----|--------|-----------|--------|-----------|
| BR-001 | [nome] | Se [condizione] | Allora [azione] | Tranne se [eccezione] |

## 6. Validazioni
| Campo | Regola | Messaggio errore |
|-------|--------|-----------------|
| email | formato email valido | "Inserisci un indirizzo email valido" |

## 7. Stati e transizioni
```mermaid
stateDiagram-v2
    [*] --> Draft
    Draft --> Active: Approvazione
    Active --> Suspended: Sospensione
    Suspended --> Active: Riattivazione
    Active --> [*]: Chiusura
```

## 8. Integrazioni
| Sistema | Direzione | Dati | Trigger | Frequenza |
|---------|----------|------|---------|-----------|

## 9. Requisiti non funzionali
- **Performance**: [tempo risposta, throughput]
- **Scalabilità**: [volumi attesi]
- **Disponibilità**: [uptime richiesto]
- **Sicurezza**: [encryption, auth, audit log]

## 10. Casi limite e eccezioni
| Caso | Cosa succede | Come gestirlo |
|------|-------------|--------------|

## 11. Impatto su funzionalità esistenti
[Cosa cambia in feature già in produzione]

## 12. Domande aperte
- [ ] [Domanda non ancora risolta]
```

**Output**: `company/product/analysis/func-spec-{slug}.md`

---

## Struttura nel repo

```
company/product/analysis/
├── analysis-{slug}.md           # Analisi funzionale interattiva
├── process-{slug}.md            # Process map
├── data-model-{slug}.md         # Modello dati
├── requirements-{slug}.md       # Requisiti elicitati
├── gap-analysis-{slug}.md       # Gap analysis
└── func-spec-{slug}.md          # Specifica funzionale dettagliata
```

## Il flusso completo: da domanda a sviluppo

```
"Voglio gestire [X]"
       │
       ▼
/pm analyze [X]          → Domande interattive, capisco il dominio
       │
       ▼
/pm map-process          → Mappo come funziona oggi (opzionale)
/pm data-model           → Mappo i dati coinvolti (opzionale)
       │
       ▼
/pm requirements-elicitation  → Elicito requisiti con MoSCoW
       │
       ▼
/pm gap-analysis         → Confronto AS-IS vs TO-BE
       │
       ▼
/pm functional-spec      → Specifica funzionale dettagliata
       │
       ▼
/pm write-spec           → PRD per lo sviluppo (già esistente)
       │
       ▼
/qa test-plan            → Test dalla spec (già esistente)
       │
       ▼
Sviluppo → Test → Release
```

Non tutti i passaggi sono necessari ogni volta.
Per un tema semplice: analyze → write-spec basta.
Per un tema complesso: tutti i passaggi.

## Regole per la modalità Business Analyst

1. **FAI DOMANDE, NON DARE RISPOSTE** — all'inizio il PM chiede, non propone
2. **UNA DOMANDA ALLA VOLTA** — non sommergere il CEO con 20 domande
3. **SEGUI IL FILO** — approfondisci quello che il CEO dice, non seguire uno script rigido
4. **DOCUMENTA IN TEMPO REALE** — ogni risposta viene catturata nel file di analisi
5. **RIPETI PER CONFERMA** — "Quindi se ho capito bene, [riassunto]. Corretto?"
6. **IDENTIFICA LE ASSUNZIONI** — "Sto assumendo che [X]. È corretto?"
7. **NON SALTARE ALL'IMPLEMENTAZIONE** — prima capire, poi proporre
8. **CERCA I WORKAROUND** — se il CEO dice "lo facciamo a mano", è un indizio di bisogno
9. **CHIEDI SEMPRE "PERCHÉ"** — spesso la prima risposta è superficiale, il vero bisogno è sotto
10. **USA IL PERSISTENT MEMORY** — alla fine di ogni sessione di analisi, proponi di salvare i dati emersi nei file appropriati

## Integrazione con il sistema

### Persistent Memory Protocol
Durante l'analisi emergono molti dati. Il PM segue il Persistent Memory Protocol:
"💾 Da questa analisi sono emersi: [dati]. Li salvo?"

### Spec Lifecycle
L'analisi funzionale può generare una spec con status `draft`.
Il file di analisi viene linkato nella spec come riferimento.

### CEO Decision Cadence
Settimanale: "Hai [N] analisi funzionali in corso non ancora tradotte in spec"
