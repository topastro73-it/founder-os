# Skill: NotebookLM

## Scopo

Fornire agli agenti accesso a knowledge base documentali su Google NotebookLM tramite MCP.
NotebookLM permette di caricare documenti (PDF, siti web, YouTube, Google Docs) e interrogarli con risposte grounded, citation-backed e zero-hallucination via Gemini.

Casi d'uso principali:
- **Ricerca documentale**: interrogare specifiche, normative, documentazione tecnica caricata su NotebookLM
- **Due diligence**: analisi di documenti investitori, contratti, report di mercato
- **Sintesi cross-documento**: risposte che combinano informazioni da più fonti caricate
- **Preparazione meeting**: briefing basati su documenti rilevanti

## Quando ogni agente la usa

| Agente | Uso principale | Notebook tipici |
|--------|---------------|-----------------|
| **CEO** | Due diligence investitori, ricerca mercato, preparazione board | Market research, investor docs, board materials |
| **PM** | Specifiche tecniche, documentazione competitor, standard di settore | Product docs, competitor analysis, industry standards |
| **CTO** | Documentazione tecnica, architettura, RFC | Technical docs, architecture specs, security standards |
| **Chief of Staff** | Report cross-funzionali, policy aziendali, materiali strategici | Company policies, strategic docs, meeting notes |
| **Sales** | Documentazione prospect, case study, materiali RFP | Prospect research, case studies, RFP materials |
| **Legal** | Normative, contratti tipo, compliance frameworks | Regulations (NIS2, GDPR), contract templates, compliance docs |

## Tool MCP disponibili

### Lettura (read-only, nessuna approvazione richiesta)

| Tool | Uso |
|------|-----|
| `ask_question` | Interroga il notebook selezionato — risposte grounded con citazioni |
| `get_health` | Verifica stato del server MCP |
| `list_notebooks` | Lista tutti i notebook salvati nella library locale |
| `select_notebook` | Seleziona il notebook attivo per le query |
| `get_notebook` | Dettagli del notebook corrente |
| `search_notebooks` | Cerca notebook per tag o keyword |
| `get_library_stats` | Statistiche di utilizzo della library (solo profilo full) |

### Scrittura (con approvazione)

| Tool | Uso |
|------|-----|
| `setup_auth` | Autenticazione Google via browser — eseguire una sola volta |
| `list_sessions` | Mostra sessioni di autenticazione attive |
| `add_notebook` | Salva un link NotebookLM nella library locale con tag e descrizione |
| `update_notebook` | Modifica metadata di un notebook (tag, descrizione) |
| `remove_notebook` | Rimuovi un notebook dalla library (solo profilo full) |

## Workflow: SELECT → ASK → USE

### 1. SELECT — Scegli il notebook

```
list_notebooks          → vedi tutti i notebook disponibili
search_notebooks        → cerca per tag/keyword
select_notebook         → attiva il notebook per le query
```

### 2. ASK — Interroga

```
ask_question            → fai la domanda al notebook attivo
                          Le risposte includono citazioni dai documenti sorgente
```

### 3. USE — Usa il risultato

- Sintetizza la risposta nel contesto dell'agente
- **Mai copiare risposte integrali** — usa summary e insight chiave
- Cita la fonte: "Da NotebookLM [nome notebook]: ..."

## Profili di configurazione

| Profilo | Tool disponibili | Uso consigliato |
|---------|-----------------|-----------------|
| `minimal` | 5 tool (solo query) | Consultazione rapida, read-only |
| `standard` | 10 tool (query + library) | Uso quotidiano — **profilo consigliato** |
| `full` | 16 tool (tutto incluso admin) | Setup iniziale e manutenzione |

Configurazione:
```bash
npx notebooklm-mcp config set profile standard
```

## Setup iniziale

1. **Autenticazione**: eseguire `setup_auth` — si apre Chrome per login Google
2. **Creare notebook su notebooklm.google.com**: caricare i documenti desiderati
3. **Aggiungere alla library**: `add_notebook` con link, tag e descrizione
4. **Testare**: `select_notebook` → `ask_question`

**Raccomandazione**: usare un account Google dedicato per l'automazione.

## Regole di sicurezza (OBBLIGATORIE)

1. **Mai salvare risposte integrali nel repo** — Solo summary e insight chiave
2. **Mai dati sensibili in file committati** — Importi, dati personali, contenuti NDA restano nel notebook
3. **Citare la fonte** — Quando usi info da NotebookLM, indica il notebook di origine
4. **Account dedicato** — Usare un account Google separato dall'account personale/aziendale principale
5. **Non caricare credenziali su NotebookLM** — I notebook possono essere condivisi, non caricare file con token/password

## Dove vivono i dati

| Dato | Posizione |
|------|-----------|
| Notebook e documenti | notebooklm.google.com (cloud Google) |
| Library locale (metadata) | `~/.config/notebooklm-mcp/` |
| Configurazione MCP | `~/Library/Application Support/Claude/claude_desktop_config.json` |
| Output usati dagli agenti | Sintetizzati nei documenti del repo (mai raw) |

## Integrazione CEO Cadence

### Giornaliero
- Non richiesto di default

### Settimanale
- Consultazione notebook di mercato/competitor per weekly review

### Mensile
- Due diligence su documenti investitori pre-board
- Review normative e compliance (NIS2, GDPR) se ci sono aggiornamenti

## MCP Graceful Degradation

Se il server NotebookLM MCP non è disponibile (auth scaduta, Chrome non presente, rete):
- **Segnala** al CEO quale funzionalità manca
- **Prosegui** con i dati disponibili nel repo
- **Non bloccare** il lavoro — i notebook sono contesto aggiuntivo, non fonte primaria
