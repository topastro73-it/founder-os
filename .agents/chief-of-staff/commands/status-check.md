# Command: status-check

## Trigger
`/cos status-check` oppure "Come stiamo su tutto?" oppure "Stato generale dei workstream"

## Processo

1. **Carica tutte le fonti rilevanti**
   - `company/product/roadmap.md` — stato epic Q corrente
   - `company/product/backlog.md` — backlog con priorità
   - `company/product/specs/` — PRD esistenti con loro stato
   - `decisions/` — tutte le decisioni con follow-up
   - `company/strategy/okrs/` — OKR correnti
   - `company/metrics/kpis.md` — metriche
   - `docs/reports/` — report recenti per contesto

2. **Analizza e assegna semaforo a ogni workstream**

   Semafori:
   - 🟢 On track — procede secondo piano
   - 🟡 Attenzione — rischio o ritardo identificato, gestibile
   - 🔴 Blocco — fermo, richiede intervento immediato
   - ⚫ Nessun dato — informazione non disponibile nel repo

3. **Workstream da coprire**

   **Prodotto**
   - Stato epic Q corrente (ognuno con semaforo)
   - Epic Non-Negotiable (NN): quali sono in progress, quali in ritardo
   - Dipendenze critiche non risolte

   **Decisioni**
   - Decisioni con follow-up aperti
   - Decisioni con review date passata
   - Decisioni pendenti (discusse ma non formalizzate)

   **OKR / Strategia**
   - Progress per ogni KR del quarter corrente
   - KR a rischio di non essere raggiunti

   **Operativo**
   - Action items P0 senza owner o scaduti
   - Handoff non raccolti tra agenti

4. **Struttura del documento**

   ```
   ## Status Check — {data}

   ### Prodotto
   | Epic | Stato | Semaforo | Note |

   ### Decisioni
   | ID | Titolo | Follow-up aperti | Semaforo |

   ### OKR Progress
   | KR | Target | Attuale | Semaforo |

   ### Operativo
   | Azione | Owner | Deadline | Semaforo |

   ### Sintesi esecutiva
   [3-5 righe: cosa va bene, cosa richiede intervento, cosa è bloccato]
   ```

## Output
Salva in: `docs/reports/status-{YYYY-MM-DD}.md`
Commit: `[cos] report: status check {YYYY-MM-DD}`
