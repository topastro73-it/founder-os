# Admin & Controllo di Gestione Skill

Skill per gestire l'amministrazione operativa e il controllo di gestione
di una startup italiana. Estende il CFO Agent con la parte operativa
che il commercialista non copre proattivamente.

## Contesto: startup italiana

{{COMPANY_NAME}} è una società italiana (SRL innovativa).
Questo comporta obblighi specifici: IVA, INPS, bilancio civilistico,
dichiarazioni fiscali, e opportunità specifiche (credito R&D, regime
startup innovativa, incentivi).

## Aree coperte

### 1. Scadenzario fiscale e amministrativo
### 2. Fatturazione e incassi
### 3. Cash management operativo
### 4. Controllo di gestione
### 5. Adempimenti societari
### 6. Incentivi e agevolazioni
### 7. Gestione fornitori e costi

---

## Comandi disponibili

### `/admin scadenzario`
Mostra tutte le scadenze admin/fiscali prossime.

**Processo**:
1. Leggi `company/finance/scadenzario.md`
2. Filtra: prossimi 30 giorni
3. Classifica per urgenza
4. Segnala: scadenze passate non marcate come completate

**Output format**:
```markdown
# 📅 Scadenzario — {data}

## 🔴 Scadute (non completate!)
| Scadenza | Data | Tipo | Importo stimato | Owner |
|----------|------|------|----------------|-------|

## 🟡 Prossimi 7 giorni
| Scadenza | Data | Tipo | Importo stimato | Owner |
|----------|------|------|----------------|-------|

## 🟢 Prossimi 30 giorni
| Scadenza | Data | Tipo | Importo stimato | Owner |
|----------|------|------|----------------|-------|

## Prossimo trimestre
| Scadenza | Data | Tipo | Note |
|----------|------|------|------|
```

### `/admin cashflow`
Analisi cashflow operativo: entrate attese, uscite previste, saldo proiettato.

**Processo**:
1. Carica `company/finance/cashflow.md`
2. Entrate: fatture emesse (quando incassiamo?), revenue ricorrente
3. Uscite: stipendi, fornitori, tasse, SaaS subscription, affitto, altro
4. Proiezione: saldo conto prossimi 3 mesi settimana per settimana
5. Alert: se il saldo proiettato scende sotto soglia critica

**Output**: `docs/reports/cashflow-{date}.md`

### `/admin fatture-status`
Stato della fatturazione: emesse, da emettere, incassate, scadute.

**Processo**:
1. Leggi `company/finance/fatturazione.md`
2. Mostra:
   - Fatture da emettere (revenue maturato non fatturato)
   - Fatture emesse in attesa di pagamento (con scadenza)
   - Fatture scadute (non pagate oltre i termini)
   - Fatture incassate nel mese
3. Calcola: DSO (Days Sales Outstanding), aging analysis
4. Alert: fatture scadute da 30+ giorni

**Output format**:
```markdown
## 💶 Fatturazione — {data}

### Da emettere
| Cliente/Partner | Periodo | Importo | Da emettere entro |
|----------------|---------|---------|------------------|

### In attesa di pagamento
| N. Fattura | Cliente | Importo | Emessa | Scadenza | Giorni |
|-----------|---------|---------|--------|----------|--------|

### Scadute ⚠️
| N. Fattura | Cliente | Importo | Scadenza | Giorni ritardo |
|-----------|---------|---------|----------|---------------|

### Incassate questo mese
| N. Fattura | Cliente | Importo | Incassata il |
|-----------|---------|---------|-------------|

### Riepilogo
- Fatturato mese: €—
- Da incassare: €—
- Scaduto: €—
- DSO medio: — giorni
```

### `/admin costi-ricorrenti`
Mappa tutti i costi ricorrenti: SaaS, infrastruttura, servizi, stipendi.

**Processo**:
1. Leggi `company/finance/costi-ricorrenti.md`
2. Categorizza: infra/cloud, tool SaaS, servizi professionali, stipendi, affitto, altro
3. Per ogni costo: importo mensile, annuale, data rinnovo, possibilità di taglio
4. Calcola: burn rate operativo dettagliato
5. Identifica: costi ottimizzabili, contratti in scadenza, duplicazioni

**Output**: `docs/reports/costi-ricorrenti-{date}.md`

### `/admin controllo-gestione`
Report di controllo di gestione: budget vs actual, margini per linea.

**Processo**:
1. Confronta budget (dal CFO) vs actual (dai dati operativi)
2. Analisi per centro di costo: R&D, Sales & Marketing, G&A, Infra
3. Margine per partner: revenue da partner - costi diretti allocati
4. Variance analysis: dove spendiamo più/meno del previsto
5. Proponi azioni correttive

**Output**: `docs/reports/controllo-gestione-{period}.md`

### `/admin incentivi-check`
Verifica incentivi e agevolazioni disponibili per startup innovative italiane.

**Processo**:
1. Verifica requisiti per:
   - **Credito d'imposta R&D** (ricerca e sviluppo)
   - **Patent box** (se applicabile)
   - **Regime startup innovativa** (agevolazioni fiscali, societarie, lavoristiche)
   - **Smart&Start Italia** o altri bandi MISE/Invitalia
   - **Bandi regionali** (Lombardia)
   - **Incentivi assunzione** (under 36, Sud, donne, NEET)
   - **Credito formazione 4.0**
   - **Sabatini** (per investimenti in beni strumentali)
2. Per ogni incentivo: siamo eligible? Lo stiamo usando? Quanto potremmo ottenere?
3. Deadline per richieste/rendicontazioni
4. ⚠️ Disclaimer: validare con commercialista

**Output**: `docs/reports/incentivi-check-{date}.md`

### `/admin vendor-costs [vendor]`
Analisi costo di un fornitore: storico, contratto, alternative, ottimizzazione.

**Processo**:
1. Quanto spendiamo? Storico degli ultimi 12 mesi
2. Il contratto: durata, rinnovo, clausole di uscita, aumenti previsti
3. Ci sono alternative più economiche?
4. Possiamo rinegoziare?

**Output**: `docs/reports/vendor-cost-{vendor}.md`

### `/admin adempimenti-societari`
Checklist adempimenti societari annuali.

**Processo**:
1. Verifica stato:
   - [ ] Bilancio approvato e depositato (entro 120gg da chiusura esercizio)
   - [ ] Dichiarazione dei redditi (IRES/IRAP)
   - [ ] Dichiarazione IVA annuale
   - [ ] Comunicazione titolare effettivo
   - [ ] Diritto annuale Camera di Commercio
   - [ ] Mantenimento requisiti startup innovativa (se applicabile)
   - [ ] Aggiornamento visura camerale
   - [ ] Verbali assemblea/CDA
   - [ ] Libro soci aggiornato
2. Per ogni adempimento: scadenza, stato, owner (tu / commercialista)

**Output**: `docs/reports/adempimenti-{anno}.md`

---

## Struttura dati nel repo

```
company/finance/
├── financial-model.md          # (già esistente - CFO)
├── pricing.md                  # (già esistente)
├── cap-table.md                # (già esistente - IR)
├── investor-pipeline.md        # (già esistente - IR)
├── scadenzario.md              # Scadenze fiscali e admin
├── cashflow.md                 # Cashflow operativo
├── fatturazione.md             # Registro fatture
├── costi-ricorrenti.md         # Mappa costi fissi
├── incentivi.md                # Incentivi e agevolazioni attive
```

---

## Integrazione nei workflow

### CEO Decision Cadence

**Giornaliero**:
- Alert se scadenza fiscale/admin nei prossimi 3 giorni
- Alert se fattura scaduta da 30+ giorni non incassata

**Settimanale**:
- "Fatture: €[X] da incassare, di cui €[Y] scadute"
- "Cashflow prossime 4 settimane: €[saldo proiettato]"
- Scadenze della prossima settimana

**Mensile**:
- Controllo di gestione: budget vs actual
- Costi ricorrenti: rinnovi in arrivo, ottimizzazioni possibili
- "Hai verificato gli incentivi disponibili? Ultimo check: [data]"
- Cashflow a 3 mesi

### CEO Routine Agent

Quando il Routine Agent fa il check giornaliero, legge anche lo scadenzario:
- "Dopodomani scade l'F24 — il commercialista lo ha preparato?"
- "La fattura a Partner X di febbraio non è ancora stata emessa — la emettiamo?"

### CFO Agent

Il CFO usa questi dati per:
- `financial-model`: burn rate dettagliato da costi-ricorrenti
- `burn-analysis`: cashflow operativo come input
- `scenario-analysis`: impatto di nuove assunzioni o fornitori

---

## Regole

- **SEMPRE** segnalare scadenze fiscali con anticipo (7 giorni per mensili, 30 per annuali)
- **MAI** dare consulenza fiscale specifica — rimandare al commercialista per interpretazioni
- **SEMPRE** proporre azioni concrete: "Emetti la fattura", "Chiedi al commercialista"
- Lo scadenzario è la fonte di verità — se non è aggiornato, il sistema lo segnala
- Le fatture scadute sono un problema di cash, non solo di ordine — trattarle come urgenze
- Per gli incentivi: segnalare l'opportunità, il commercialista valida
