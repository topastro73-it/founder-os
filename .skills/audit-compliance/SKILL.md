# Audit & Compliance Skill

Skill per gestire la compliance aziendale, la readiness a certificazioni,
e l'audit continuo della postura di sicurezza di {{COMPANY_NAME}}.

## Perché è importante

La compliance è un **prerequisito di business** per qualsiasi azienda B2B SaaS che tratta dati di clienti aziendali o opera in settori regolamentati:
1. I clienti enterprise e i partner di canale richiedono certificazioni nel procurement
2. I clienti finali si aspettano fornitori affidabili e certificati
3. Alcune normative (es. NIS2, GDPR) si applicano direttamente come fornitore di servizi digitali

La compliance non è un costo — è un **abilitatore di vendita e un requisito di fiducia**.

## Framework coperti

> ⚙️ **Configura questa tabella** con i framework rilevanti per la TUA azienda e il loro stato reale.
> Sotto trovi esempi comuni nel B2B SaaS — rimuovi quelli non applicabili e imposta il `Status`
> in base alla tua situazione (`Non applicabile` / `Da valutare` / `In corso` / `Compliant` / `Certificati`).
> NON dichiarare "Certificati" un framework che non hai effettivamente certificato.

| Framework | Quando serve (esempio) | Priorità | Status |
|-----------|------------------------|----------|--------|
| **GDPR** | Se tratti dati personali di clienti UE | Critica | {{GDPR_STATUS}} |
| **SOC 2 Type II** | Credibilità enterprise, mercato US/UK | Alta | {{SOC2_STATUS}} |
| **ISO 27001** | Spesso richiesto nel procurement enterprise | Media | {{ISO27001_STATUS}} |
| **NIS2** | Se rientri tra i soggetti EU obbligati | Media | {{NIS2_STATUS}} |

---

## Comandi disponibili

### `/audit compliance-status`
Dashboard dello stato di compliance su tutti i framework.

**Processo**:
1. Leggi `company/compliance/status.md` per lo stato corrente
2. Per ogni framework attivo: quanti requisiti mappati, quanti soddisfatti, quanti gap
3. Genera dashboard con semafori

**Output format**:
```markdown
# Compliance Dashboard — {data}

## Overview
| Framework | Requisiti | Soddisfatti | Gap | Compliance % | Status |
|-----------|----------|------------|-----|-------------|--------|
| NIS2 | 45 | 38 | 7 | 84% | giallo |
| GDPR | 30 | 28 | 2 | 93% | verde |
| ISO 27001 | 114 | 67 | 47 | 59% | rosso |
| SOC 2 | 64 | 30 | 34 | 47% | rosso |

## Gap critici (bloccano certificazione)
1. [Gap] — Framework: [quale] — Effort: [S/M/L] — Owner: [ruolo]

## Gap importanti (da risolvere entro [data])
1. [Gap] — Framework: [quale] — Effort: [S/M/L]

## Prossimi milestone
- [Data]: [milestone]

## Raccomandazioni
1. [Azione prioritaria]
```

**Output**: `docs/reports/compliance-status-{date}.md`

---

### `/audit gap-analysis [framework]`
Analisi gap dettagliata per un framework specifico.

**Processo**:
1. Carica requisiti del framework da `company/compliance/frameworks/`
2. Per ogni requisito: stato (compliant / partial / non-compliant / N/A)
3. Per ogni gap: cosa manca, effort per colmarlo, owner, priorità
4. Genera roadmap di remediation

**Output**: `docs/reports/gap-analysis-{framework}-{date}.md`

---

### `/audit nis2-readiness`
Verifica specifica readiness NIS2.

**Processo**:
1. Verifica i 10 requisiti chiave NIS2:
   - [ ] Risk management policy documentata e approvata dal management
   - [ ] Incident response plan con notifica 24h/72h
   - [ ] Business continuity e disaster recovery plan testato
   - [ ] Supply chain security (valutazione fornitori)
   - [ ] Vulnerability management e patching policy
   - [ ] Crittografia e encryption policy
   - [ ] Access control e autenticazione (MFA)
   - [ ] Network security e monitoring
   - [ ] Training sicurezza per management e dipendenti
   - [ ] Audit e testing periodici documentati
2. Per ogni requisito: stato, evidenza disponibile, gap
3. Valuta: siamo pronti per un audit? Se no, cosa manca?
4. Timeline per raggiungere readiness

**Output**: `docs/reports/nis2-readiness-{date}.md`

---

### `/audit gdpr-check`
Verifica compliance GDPR.

**Processo**:
1. Verifica requisiti chiave:
   - [ ] Registro dei trattamenti aggiornato
   - [ ] Privacy policy e cookie policy aggiornate
   - [ ] DPA firmati con tutti i processor
   - [ ] Processo per gestire richieste diritti interessati (DSAR)
   - [ ] DPIA per trattamenti ad alto rischio
   - [ ] DPO nominato (se necessario)
   - [ ] Notifica data breach entro 72h procedura
   - [ ] Privacy by design integrata nello sviluppo
   - [ ] Formazione dipendenti su privacy
   - [ ] Trasferimenti extra-UE gestiti (SCC, adequacy)
2. Gap e remediation plan
3. Disclaimer: validare con DPO/avvocato

**Output**: `docs/reports/gdpr-check-{date}.md`

---

### `/audit iso27001-roadmap`
Genera roadmap per mantenimento/rinnovo certificazione ISO 27001.

**Processo**:
1. Mappa i 93 controlli dell'Annex A (ISO 27001:2022)
2. Per ogni controllo: stato corrente, gap, effort
3. Identifica: cosa abbiamo già, cosa manca, cosa è parziale
4. Genera roadmap:
   - Fase 1: ISMS review (policy, scope, risk assessment)
   - Fase 2: Aggiornamento controlli
   - Fase 3: Audit interno
   - Fase 4: Audit esterno di sorveglianza/rinnovo
5. Timeline e budget stimato

**Output**: `docs/reports/iso27001-roadmap-{date}.md`

---

### `/audit soc2-readiness`
Valuta readiness per SOC 2 Type II.

**Processo**:
1. Verifica i 5 Trust Service Criteria:
   - Security (obbligatorio)
   - Availability
   - Processing Integrity
   - Confidentiality
   - Privacy
2. Per ogni criterio: controlli in place, gap, evidenze
3. Stima: timeline per Type I (point-in-time) e Type II (periodo osservazione)

**Output**: `docs/reports/soc2-readiness-{date}.md`

---

### `/audit policy-review`
Revisiona tutte le policy aziendali per completezza e aggiornamento.

**Processo**:
1. Inventario policy in `company/compliance/policies/`:
   - Information Security Policy
   - Acceptable Use Policy
   - Incident Response Policy
   - Business Continuity Policy
   - Data Classification Policy
   - Access Control Policy
   - Encryption Policy
   - Vendor Management Policy
   - Change Management Policy
   - HR Security Policy (onboarding/offboarding)
2. Per ogni policy: esiste? È aggiornata? È approvata? È comunicata?
3. Identifica policy mancanti o stale
4. Proponi piano di creazione/aggiornamento

**Output**: `docs/reports/policy-review-{date}.md`

---

### `/audit evidence-check`
Verifica che le evidenze di compliance siano raccolte e aggiornate.

**Processo**:
1. Per ogni framework attivo, verifica le evidenze richieste:
   - Log di sistema e monitoring
   - Report di vulnerability scan
   - Record di formazione dipendenti
   - Verbali di approvazione management
   - Report di audit precedenti
   - Test di disaster recovery
   - Registri di incidenti
   - Valutazioni fornitori
2. Per ogni evidenza: esiste? È aggiornata? È archiviata correttamente?
3. Alert per evidenze mancanti o scadute

**Output**: `docs/reports/evidence-check-{date}.md`

---

### `/audit vendor-assessment [vendor]`
Valutazione della postura di sicurezza di un fornitore.

**Processo**:
1. Questionario fornitore: certificazioni, policy, incident history, DPA
2. Risk rating: Critical / High / Medium / Low
3. Raccomandazione: approvare / approvare con condizioni / rifiutare
4. DPA necessario? Clausole specifiche?

**Output**: `company/compliance/vendors/{vendor}.md`

---

## Struttura nel repo

```
company/compliance/
├── status.md                        # Dashboard stato compliance
├── frameworks/
│   ├── nis2-requirements.md         # Requisiti NIS2 mappati
│   ├── gdpr-requirements.md         # Requisiti GDPR mappati
│   ├── iso27001-controls.md         # Controlli ISO 27001 mappati
│   └── soc2-criteria.md             # Criteri SOC 2 mappati
├── policies/
│   ├── information-security.md
│   ├── incident-response.md
│   ├── business-continuity.md
│   ├── access-control.md
│   ├── encryption.md
│   ├── vendor-management.md
│   ├── data-classification.md
│   ├── acceptable-use.md
│   ├── change-management.md
│   └── hr-security.md
├── vendors/
│   └── {vendor-slug}.md             # Valutazioni fornitori
├── audits/
│   └── {date}-{type}.md             # Record di audit
└── evidence/
    └── README.md                    # Dove trovare le evidenze
```

---

## Integrazione nei workflow decisionali

### Nel CEO Decision Cadence

**Giornaliero**:
- Se c'è una scadenza compliance nei prossimi 7 giorni → alert
- Se un audit è schedulato nei prossimi 30 giorni → reminder preparazione

**Settimanale**:
- "Policy review: [N] policy non aggiornate da 6+ mesi"
- "Evidenze: [N] evidenze mancanti per [framework]"

**Mensile**:
- "Compliance dashboard: NIS2 [N]%, GDPR [N]%, ISO27001 [N]%"
- "Prossimo milestone certificazione: [cosa] — [data] — siamo pronti?"
- "Vendor assessment: [N] fornitori non valutati da 12+ mesi"

### Nel PM workflow

**Quando il PM scrive una PRD** (`/pm write-spec`):
- Step aggiuntivo: "Questa feature ha impatti sulla compliance?"
- Check: tratta dati personali? Cambia l'architettura di sicurezza? Richiede DPIA?
- Se sì: flag nel frontmatter della spec: `compliance-impact: [NIS2/GDPR/ISO27001]`
- Handoff automatico → `/audit` per impact assessment

### Nel CTO workflow

**Quando il CTO fa tech-decision o architecture-review**:
- Step aggiuntivo: "Questa decisione impatta la compliance?"
- Check: cambia encryption, access control, logging, data flow?
- Se sì: documentare impatto nell'ADR e notificare audit skill
- Verifica: la nuova architettura mantiene i controlli ISO27001 mappati?

### Nel Legal workflow

**Quando Legal rivede contratti**:
- Verifica automatica: il contratto include clausole DPA se tratta dati personali?
- Check: il fornitore è stato valutato con vendor assessment?
- Se no: flag → `/audit vendor-assessment [vendor]` prima di firmare

### Nel HR workflow

**Quando HR gestisce onboarding/offboarding**:
- Onboarding: verifica che il nuovo dipendente faccia security training
- Offboarding: verifica revoca accessi, NDA in place
- Tracking: record formazione per evidenze compliance

### Nel Marketing workflow

**Quando Marketing crea contenuti su compliance per i clienti**:
- Cross-check: "Siamo noi stessi compliant su quello che stiamo raccomandando?"
- Se no: flag — non possiamo raccomandare qualcosa che noi stessi non facciamo

### Nel Sales workflow

**Quando Sales risponde a RFP/procurement**:
- Carica automaticamente: certificazioni disponibili, policy, SOC2 report
- Identifica gap: "Il cliente richiede [certificazione] e noi non ce l'abbiamo ancora — come rispondiamo?"
- Proponi: risposta onesta con roadmap di certificazione

### Nel Chief of Staff workflow

**Nel daily-briefing e weekly-digest**:
- Include sezione "Compliance" se ci sono alert o scadenze
- Nel product-plan: evidenzia spec con `compliance-impact`
- Nel startup-snapshot: include compliance % nel section

---

## Cadenza di audit consigliata

| Attività | Frequenza | Owner | Comando |
|----------|----------|-------|---------|
| Compliance status dashboard | Mensile | CoS/Legal | `/audit compliance-status` |
| Policy review | Trimestrale | Legal | `/audit policy-review` |
| Evidence check | Trimestrale | Legal/CTO | `/audit evidence-check` |
| Vendor assessment | Annuale per vendor | Legal | `/audit vendor-assessment` |
| NIS2 readiness | Trimestrale | Legal/CTO | `/audit nis2-readiness` |
| GDPR check | Semestrale | Legal | `/audit gdpr-check` |
| Penetration test | Annuale | CTO (esterno) | Manuale |
| DR test | Semestrale | CTO | Manuale |
| Security training | Annuale | HR | Manuale |

---

## Regole

- **SEMPRE** disclaimer: "Questa analisi è un assessment interno. Per certificazioni formali serve un auditor accreditato."
- **MAI** dichiarare compliance senza evidenze documentate
- **SEMPRE** collegare ogni gap a un'azione concreta con owner e deadline
- La compliance è un processo continuo, non un progetto one-shot
- Ogni spec con impatto compliance va flaggata nel frontmatter
