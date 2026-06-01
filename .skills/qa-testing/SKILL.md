# QA & Testing Skill

Skill per supportare il CTO nella pianificazione e gestione del testing.
Genera test plan, test case, test report da PRD e spec esistenti.
Non esegue test automaticamente — prepara tutto perché il team li esegua.

## Contesto prodotto

Il prodotto può avere più livelli di utenti — i test devono coprire tutti i ruoli rilevanti:

```
Admin / Operatore          → Gestione account, dashboard, configurazione
Utente standard            → Funzionalità core del prodotto
End-customer (se presente) → Dashboard, report, notifiche
```

Ogni feature va testata dalla prospettiva di tutti gli utenti impattati.

## Comandi disponibili

### `/qa test-plan [spec]`
Genera test plan completo da una PRD.

**Processo**:
1. Leggi la PRD da `company/product/specs/prd-{slug}.md`
2. Estrai tutte le user stories e acceptance criteria
3. Genera test plan strutturato:

```markdown
# Test Plan: {Feature Name}

**PRD**: company/product/specs/prd-{slug}.md
**Versione**: 1.0
**Data**: {YYYY-MM-DD}
**Owner**: CTO / QA

## Scope
- **In scope**: [cosa testiamo]
- **Out of scope**: [cosa NON testiamo in questo ciclo]
- **Ambienti**: [staging / pre-prod / prod]

## Test Strategy
- **Functional testing**: tutti i flussi utente dalle user stories
- **Edge case testing**: input invalidi, limiti, casi limite
- **Integration testing**: interazioni con altri moduli/servizi
- **Security testing**: autenticazione, autorizzazione, input sanitization
- **Performance testing**: [se applicabile — carico, response time]
- **Regression testing**: feature esistenti che potrebbero essere impattate

## Risorse necessarie
- **Dati di test**: [dataset necessari — account fake, CSV di test, etc.]
- **Account di test**: [ruoli necessari — admin, operatore, utente standard]
- **Ambienti**: [staging configurato con X]
- **Tool**: [Postman, Cypress, manuale, etc.]

## Criteri di accettazione per il rilascio
- [ ] Tutti i test case critici passati
- [ ] Nessun bug P0/P1 aperto
- [ ] Test di regressione passati
- [ ] Performance entro i limiti definiti
- [ ] Security check completato

## Timeline
| Fase | Durata stimata | Chi |
|------|---------------|-----|
| Preparazione test data | [tempo] | [chi] |
| Esecuzione test funzionali | [tempo] | [chi] |
| Fix bug trovati | [tempo] | [chi] |
| Re-test dopo fix | [tempo] | [chi] |
| Regression test | [tempo] | [chi] |
| Sign-off | [tempo] | CTO |
```

**Output**: `company/product/testing/test-plan-{slug}.md`

---

### `/qa test-cases [spec]`
Genera test case dettagliati da una PRD.

**Processo**:
1. Leggi la PRD e gli acceptance criteria
2. Per ogni acceptance criteria genera 1+ test case
3. Per ogni user story aggiungi: happy path, sad path, edge case
4. Per ogni livello utente impattato: test specifici

**Formato test case**:

```markdown
# Test Cases: {Feature Name}

**PRD**: company/product/specs/prd-{slug}.md
**Totale test case**: {N}
**Critici**: {N} | **Alti**: {N} | **Medi**: {N} | **Bassi**: {N}

---

## TC-001: {Titolo descrittivo}

- **User Story**: US-{N}
- **Priorità**: Critico / Alto / Medio / Basso
- **Livello utente**: Admin / Operatore / End-customer
- **Tipo**: Funzionale / Edge case / Security / Performance
- **Pre-condizioni**: [stato iniziale necessario]
- **Test data**: [dati specifici necessari]

| Step | Azione | Input | Risultato atteso |
|------|--------|-------|-----------------|
| 1 | [cosa fare] | [con quali dati] | [cosa deve succedere] |
| 2 | [cosa fare] | [con quali dati] | [cosa deve succedere] |
| 3 | [cosa fare] | [con quali dati] | [cosa deve succedere] |

- **Post-condizioni**: [stato finale atteso]
- **Note**: [info aggiuntive, workaround noti, etc.]

---

## TC-002: {Titolo — caso negativo}

- **User Story**: US-{N}
- **Priorità**: Alto
- **Livello utente**: Admin
- **Tipo**: Edge case
- **Pre-condizioni**: [stato iniziale]

| Step | Azione | Input | Risultato atteso |
|------|--------|-------|-----------------|
| 1 | [azione con input invalido] | [dato errato] | [messaggio errore appropriato] |
| 2 | [verificare] | | [nessun dato corrotto] |

---

## TC-003: {Titolo — sicurezza}
...
```

Classifica ogni test case per priorità:
- **Critico**: se fallisce, la feature non può andare in produzione
- **Alto**: funzionalità core, deve passare
- **Medio**: funzionalità secondaria, può essere workaround
- **Basso**: nice-to-have, cosmetico

**Output**: `company/product/testing/test-cases-{slug}.md`

---

### `/qa test-cases-api [endpoint]`
Genera test case specifici per API endpoint.

**Processo**:
1. Identifica l'endpoint (URL, metodo, parametri, auth)
2. Genera test case per:
   - **Happy path**: request valida → response corretta
   - **Validazione input**: campi mancanti, tipi sbagliati, valori fuori range
   - **Autenticazione**: senza token, token scaduto, token sbagliato
   - **Autorizzazione**: utente senza permessi, ruolo sbagliato
   - **Rate limiting**: troppe richieste
   - **Edge case**: payload vuoto, payload enorme, caratteri speciali, SQL injection, XSS

**Formato**:
```markdown
## API: {METHOD} {endpoint}

### TC-API-001: Happy path
- **Request**:
  - Method: POST
  - Headers: Authorization: Bearer {valid_token}
  - Body: {json valido}
- **Expected Response**:
  - Status: 200
  - Body: {struttura attesa}

### TC-API-002: Campo obbligatorio mancante
- **Request**: body senza campo "name"
- **Expected**: 400 Bad Request, messaggio "name is required"

### TC-API-003: Token non valido
- **Request**: Authorization: Bearer invalid_token
- **Expected**: 401 Unauthorized

### TC-API-004: Utente senza permessi
- **Request**: token valido ma ruolo utente standard su endpoint admin
- **Expected**: 403 Forbidden
```

**Output**: `company/product/testing/test-cases-api-{endpoint-slug}.md`

---

### `/qa regression-suite`
Genera o aggiorna la suite di test di regressione.

**Processo**:
1. Leggi tutte le feature shipped da `company/product/changelog.md`
2. Per ogni feature critica: 2-3 test case core che verificano che funziona ancora
3. Organizza per area: autenticazione, dashboard admin, funzionalità core del prodotto, API core
4. La regression suite è incrementale — cresce con ogni release

**Output**: `company/product/testing/test-plan-master-regression.md` (file esistente — aggiornamento incrementale, non creare un nuovo `regression-suite.md`)

---

### `/qa test-report [spec] [cycle]`
Genera report dei risultati di un ciclo di test.

**Processo**:
1. Chiedi al CTO/team i risultati: per ogni test case, passato/fallito/bloccato
2. Genera report:

```markdown
# Test Report: {Feature Name} — Ciclo {N}

**Data**: {YYYY-MM-DD}
**Tester**: [chi ha eseguito]
**Build/Version**: [versione testata]

## Riepilogo

| Stato | Count | % |
|-------|-------|---|
| ✅ Passato | {N} | —% |
| ❌ Fallito | {N} | —% |
| ⏸️ Bloccato | {N} | —% |
| ⭕ Non eseguito | {N} | —% |
| **Totale** | **{N}** | **100%** |

## Verdetto: GO / NO-GO / CONDIZIONALE

Motivazione: [perché sì/no/condizionale]

## Bug trovati

| ID | Titolo | Severità | Test case | Status |
|----|--------|----------|-----------|--------|
| BUG-001 | [titolo] | P0/P1/P2/P3 | TC-{N} | Aperto / Fix in corso / Risolto |

## Test falliti — dettaglio

### TC-{N}: {Titolo}
- **Risultato atteso**: [cosa doveva succedere]
- **Risultato effettivo**: [cosa è successo]
- **Screenshot/log**: [riferimento]
- **Bug collegato**: BUG-{N}

## Test bloccati — motivazione
- TC-{N}: bloccato da [motivo — ambiente, dati, bug bloccante]

## Raccomandazioni
1. [cosa fare prima del prossimo ciclo]
2. [rischi residui se andiamo in produzione]

## Sign-off
- [ ] CTO approva il rilascio
- [ ] Bug P0/P1 tutti risolti
- [ ] Regression passata
```

**Output**: `company/product/testing/test-report-{slug}-cycle{N}.md`

---

### `/qa security-test [feature]`
Genera checklist di security testing per una feature.

**Processo**:
1. Identifica le superfici di attacco della feature
2. Genera checklist per categoria:

```markdown
# Security Test Checklist: {Feature}

## Autenticazione
- [ ] Endpoint accessibile senza autenticazione → deve fallire con 401
- [ ] Token scaduto → deve fallire con 401
- [ ] Token di un altro utente → deve fallire con 403

## Autorizzazione
- [ ] Utente A accede a dati di un altro utente → deve fallire
- [ ] Utente standard accede a dashboard admin → deve fallire
- [ ] Escalation di privilegi tramite manipolazione request → deve fallire

## Input Validation
- [ ] SQL injection nei campi di testo → deve essere sanitizzato
- [ ] XSS (Cross-Site Scripting) → deve essere sanitizzato
- [ ] Path traversal nei file upload → deve essere bloccato
- [ ] Input più grande del limite → deve essere rifiutato con errore

## Dati
- [ ] PII visibile solo all'utente autorizzato
- [ ] Dati in transit crittografati (HTTPS)
- [ ] Dati sensibili non nei log
- [ ] Dati di un account non visibili a un altro account

## API
- [ ] Rate limiting attivo
- [ ] CORS configurato correttamente
- [ ] Nessun endpoint debug esposto
- [ ] Versioning API corretto
```

**Output**: `company/product/testing/security-test-{slug}.md`

---

### `/qa smoke-test [release]`
Genera checklist di smoke test per una release.

**Processo**:
1. Identifica le funzionalità core del prodotto (quelle che se non funzionano, è un P0)
2. Genera checklist rapida (max 15-20 check, eseguibile in 30 minuti):

```markdown
# Smoke Test: Release {version}

**Tempo stimato**: 30 minuti
**Ambiente**: [staging/production]
**Data**: {YYYY-MM-DD}
**Tester**: [chi]

## Login & Auth
- [ ] Login admin funziona
- [ ] Login operatore funziona
- [ ] Login utente standard funziona
- [ ] Logout funziona
- [ ] Password reset funziona

## Core — Admin
- [ ] Dashboard admin si carica
- [ ] Lista utenti/account visibile
- [ ] Aggiunta nuovo account funziona

## Core — Funzionalità principale
- [ ] Flusso primario del prodotto funziona
- [ ] Output/risultato principale generato correttamente
- [ ] Export / download funziona

## Core — Utente standard
- [ ] Dashboard utente si carica
- [ ] Dati principali visibili
- [ ] Notifiche/alert visibili

## API
- [ ] Endpoint health check: 200 OK
- [ ] Endpoint core: risponde in <2s

## Risultato
- [ ] Tutti i check passati → GO
- [ ] Check falliti: [lista] → BLOCCA RELEASE
```

**Output**: `company/product/testing/smoke-test-{version}.md`

---

### `/qa test-data [spec]`
Genera specifica dei dati di test necessari.

**Processo**:
1. Leggi la PRD e i test case
2. Identifica tutti i dati necessari per eseguire i test:
   - Account di test per ogni ruolo
   - Dataset (account fake, CSV di test, dati di esempio)
   - Configurazioni (setup iniziale, moduli attivi)
   - Dati edge case (CSV malformati, nomi con caratteri speciali, etc.)
3. Proponi come crearli (script, manuale, fixture)

**Output**: `company/product/testing/test-data-{slug}.md`

---

## Struttura nel repo

```
company/product/testing/
├── test-plan-{slug}.md            # Test plan per feature
├── test-cases-{slug}.md           # Test case dettagliati
├── test-cases-api-{slug}.md       # Test case API
├── test-report-{slug}-cycle{N}.md # Report risultati
├── security-test-{slug}.md        # Security checklist
├── smoke-test-{version}.md        # Smoke test per release
├── test-data-{slug}.md            # Specifica dati di test
└── test-plan-master-regression.md # Suite regressione (incrementale)
```

## Workflow: da PRD a rilascio testato

```
1. PM scrive PRD             → company/product/specs/prd-{slug}.md
2. CTO fa tech review        → stime, rischi, architettura
3. /qa test-plan             → genera test plan dalla PRD
4. /qa test-cases            → genera test case dettagliati
5. /qa test-data             → specifica dati necessari
6. Dev implementa            → sviluppo
7. /qa smoke-test            → checklist rapida su staging
8. /qa security-test         → security checklist
9. Team esegue test          → manuale o automatizzato
10. /qa test-report          → report con risultati e verdetto
11. Se GO → release
12. /qa regression-suite     → aggiorna suite regressione
```

## Integrazione nel sistema

### Nel CTO workflow
Quando una spec passa a `status: in-development`:
- Suggerisci: "Vuoi generare il test plan e i test case?"
- Il test plan viene creato PRIMA che lo sviluppo finisca

### Nel PM workflow
Quando una spec passa a `status: shipped`:
- Verifica: "C'è un test report con verdetto GO?"
- Se no: flag — non dovrebbe essere shipped senza test

### Nel CEO Decision Cadence — Settimanale
- "Spec in development senza test plan: [lista]"
- "[N] bug P0/P1 aperti"

### Nel Chief of Staff — product-plan
Mostra colonna "Test status" per ogni spec in `in-development`:
- 📋 Test plan creato
- 🧪 In test
- ✅ Test passato (GO)
- ❌ Test fallito (NO-GO)
- ⚠️ Nessun test plan

### Integrazione project management
I bug trovati durante il testing possono essere creati come task nel tool di project management (es. ClickUp):
- Area: Product Engineering → Delivery Board → Bug
- Con riferimento al test case che li ha trovati

## Regole

- **MAI** rilasciare senza almeno lo smoke test
- **SEMPRE** generare test case da PRD, non a memoria
- **SEMPRE** includere test negativi e edge case, non solo happy path
- **SEMPRE** documentare i risultati, anche se tutto passa
- I test di sicurezza sono obbligatori per feature che toccano auth, dati, API
- La regression suite cresce con ogni release — non la ricominciare da zero
- I bug trovati in test vanno nel tool di project management con priorità e link al test case
