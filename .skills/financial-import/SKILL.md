# Financial Import Skill

Importazione e analisi dei dati finanziari. Supporta due modalità:
1. **ERP API** (preferita) — dati live via `.skills/erp/SKILL.md` e `scripts/erp_sync.py`
2. **JSON file** (fallback) — export statico `{{COMPANY_NAME}}_PRODUCTION.json`

Usata da CFO, CEO, Chief of Staff.

## Quando usare questa skill

- **Se l'ERP API è disponibile** (`ERP_API_URL` configurata): usa `python3 scripts/erp_sync.py sync-all` per dati live. Vedi `.skills/erp/SKILL.md` per dettagli.
- **Se il CEO fornisce un file JSON** di export finanziario: usa il processo manuale descritto sotto.

## Comandi

| Comando | Descrizione | Output |
|---------|------------|--------|
| `import-financials` | Importa JSON finanziario, analizza, aggiorna KPI | Aggiorna `company/metrics/kpis.md` + report |

---

## Comando: import-financials

### Trigger
Quando il CEO fornisce un file JSON di export finanziario, o dice "aggiorna i dati finanziari", "importa i numeri", o simili.

### Input
- File JSON allegato dall'utente (formato export finanziario)

### Processo

#### Passo 1 — Parsing del JSON

Il JSON ha questa struttura top-level:

```
{
  "version", "timestamp", "settings",
  "financials",      // Array principale — CUORE dei dati
  "deals",           // Pipeline CRM
  "accounts",        // Aziende clienti/prospect
  "contacts",        // Persone fisiche
  "orders",          // Ordini a fornitori
  "users",           // Utenti sistema
  "contracts",       // Contratti attivi
  "invoices",        // Fatture emesse
  "payments",        // Pagamenti ricevuti
  "funding_rounds",  // Round di investimento
  "cash_balances"    // Saldo cassa per mese
}
```

#### Passo 2 — Data Dictionary (come interpretare i dati)

##### Il motore finanziario: `financials[]`

Ogni record ha **3 livelli di valore**:
- `plannedValue` — Forecast/budget (positivo = ricavo, negativo = costo)
- `bookingValue` — Ordinato/fatturato (contrattualizzato)
- `actualValue` — Cassa (effettivamente incassato/pagato)

**Date chiave**:
- `bookingDate` — Data firma contratto / ordine
- `plannedCashInDate` — Scadenza pagamento prevista
- `actualCashInDate` — Data effettivo incasso/pagamento
- `competenceDate` — Data inizio competenza del servizio (FONDAMENTALE per MRR)

**Classificazione**:
- `status`: `Pipeline` | `Unpaid` | `Paid` | `Lost`
- `pnl`: Categoria P&L (`Subscription Revenue`, `COGS`, `R&D`, `S&M`, `G&A`, etc.)
- `capexOpex`: `CAPEX` | `OPEX`
- `frequency`: Durata servizio in mesi (1 = mensile, 12 = annuale)
- `resource`: Nome cliente/fornitore

##### Calcolo MRR

1. Prendi `financials[]` dove `status` NON e' `Pipeline` o `Lost`
2. Filtra dove `pnl` contiene "Subscription"
3. Per ogni record, calcola `endDate = competenceDate + frequency` (mesi)
4. Se il mese analizzato cade tra `competenceDate` e `endDate`, il record genera MRR
5. Valore MRR: usa campo `mrr` se presente, altrimenti `bookingValue / frequency`

##### Calcolo crediti da incassare

`bookingValue - actualValue` per ogni record di ricavo con `status = Unpaid`

##### Calcolo burn rate

Filtra `financials[]` dove `plannedValue < 0`, raggruppa per mese (`actualMonth`, `actualYear`)

##### Calcolo backlog (fatturato non ancora fatturato)

`contracts[].totalAmount` - somma `invoices[]` collegate via `contractId`

#### Passo 3 — Regole specifiche aziendali

**CRITICO — Periodicita compensi**:
- Alcuni collaboratori hanno stipendio mensile; altri hanno compensi trimestrali o a progetto
- Per il burn rate medio: annualizza ogni persona in base alla frequenza reale dei pagamenti, NON assumere che siano tutti mensili
- Identifica la periodicita guardando il campo `frequency` e la distanza tra `competenceDate` successive per la stessa `resource`

**Revenue non contrattualizzata**:
- Alcuni clienti generano revenue mensile variabile ma potrebbero non avere un `contract` nel sistema
- Cercala nei `financials[]` per la `resource` specifica
- Aggiungila separatamente all'MRR adjusted

**Grant e pass-through**:
- I grant (pnl contiene "Grant") NON sono revenue operativa
- Attenzione ai costi di giroconto consortile (pnl = "Consortium pass-through") — sono costi legati all'erogazione dei grant
- Calcola sempre l'impatto netto di ogni grant: `incasso grant - costi consortili associati`

**Finanziamenti BPM**:
- I prestiti bancari (pnl contiene "Mortgage" o "Funding") NON sono revenue
- Le rate sono costi finanziari ricorrenti

#### Passo 3b — Pipeline da HubSpot (NON dal JSON)

**Decisione DEC-005 (2026-03-22)**: la pipeline commerciale si legge da **HubSpot CRM** (via MCP tool `search_crm_objects`), NON dal JSON. Il JSON ha dati pipeline stale e incompleti.

Per leggere la pipeline:
1. Chiama `get_user_details` per verificare accesso
2. Chiama `search_crm_objects` con objectType `DEAL`, properties `["dealname", "amount", "dealstage", "pipeline", "hs_deal_stage_probability", "closedate", "hubspot_owner_id"]`, sort by amount DESC, limit 200
3. Chiama `get_properties` per objectType `DEAL`, propertyNames `["dealstage"]` per ottenere il mapping stage ID → label
4. Chiama `search_owners` per mappare owner ID → nome

**Stage mapping HubSpot**:
- `12054091` = Discovery & Qualification (prob. 20%)
- `12054092` = Technical Alignment (prob. 30%)
- `12054093` = Proposal Sent (prob. 40%)
- `12054094` = Negotiation & Verbal Agreement (prob. 60%)
- `12054095` = Contract Sent (prob. 80%)
- `12054096` = Won (prob. 100%)
- `1274663529` = Lost (prob. 0%)

**Attenzione**: molti deal in Discovery hanno amount = €1 (placeholder). Filtrarli o segnarli come "valore TBD" nell'analisi.

#### Passo 4 — Analisi da produrre

1. **P&L per trimestre** — Revenue operativa vs costi, per categoria pnl (da JSON)
2. **MRR e ARR** — Da contratti attivi, con breakdown per cliente (da JSON)
3. **Burn rate** — Costi fissi mensili + costi variabili trimestrali (media mensile) (da JSON)
4. **Cash flow mensile** — Entrate vs uscite, per mese, trend (da JSON)
5. **Crediti aging** — Importo, scadenza, giorni scaduto, per cliente (da JSON)
6. **Unit economics** — ARPU, ACV medio/mediano, segmentazione clienti (da JSON)
7. **Pipeline** — Deal per stage, valore pesato, owner, deal recenti (**da HubSpot**)
8. **Concentrazione revenue** — Top clienti, HHI index, % cumulativo (da JSON)
9. **Grant status** — Incassato vs pipeline, impatto netto dopo pass-through (da JSON)
10. **Runway** — 3 scenari (base 5% growth, ottimista 8%, pessimista 2% + churn) (da JSON + HubSpot pipeline)

#### Passo 5 — Output

1. Aggiorna `company/metrics/kpis.md` con i numeri reali
2. Salva report completo in `docs/reports/burn-analysis-{YYYY-MM-DD}.md`
3. Commit: `[cfo] analysis: financial import and burn analysis from production export`

### Guardrails

- MAI trattare i compensi trimestrali come se fossero mensili
- MAI contare prestiti bancari come revenue
- MAI contare grant lordi come liquidita — sempre calcolare il netto dopo pass-through
- SEMPRE presentare 3 scenari (base, ottimista, pessimista)
- SEMPRE indicare le assunzioni dietro ogni proiezione
- SEMPRE segnalare crediti scaduti con aging > 30 giorni come rischio
