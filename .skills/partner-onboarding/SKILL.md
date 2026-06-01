# Partner Onboarding Skill

Processo strutturato 90 giorni da contratto firmato a primo revenue. Usata da Sales, PM, Chief of Staff.

## Overview

L'onboarding di un nuovo partner segue 4 fasi in 12 settimane. L'obiettivo e portare il partner dalla firma al **primo revenue generato tramite piattaforma** nel modo piu rapido e prevedibile possibile.

```
Settimana  1-2    3-4       5-8        9-12
          SETUP → ENABLEMENT → LAUNCH → OPTIMIZE
```

---

## Fase 1: SETUP (Settimana 1–2)

**Obiettivo**: Piattaforma configurata, team partner con accesso, primi clienti pilota caricati.

| # | Task | Owner | Success Criteria | Deadline |
|---|------|-------|-----------------|----------|
| 1.1 | Kickoff call con partner (allineamento aspettative, timeline, KPI) — usare `docs/presentations/poc-kickoff-deck.pptx` come asset di riferimento se il partner ha richiesto un PoC guidato pre-firma | Sales | Meeting avvenuto, note in CRM | Giorno 1 |
| 1.2 | Creazione tenant white-label (branding, logo, colori, dominio) | CTO/Engineering | Tenant attivo con branding partner | Giorno 3 |
| 1.3 | Configurazione utenti partner (admin + venditori) | CTO/Engineering | Tutti gli utenti creati e attivi | Giorno 5 |
| 1.4 | Import primi 5-10 clienti pilota | Partner + PM | Clienti caricati, primo utilizzo completato | Giorno 7 |
| 1.5 | Configurazione catalogo servizi partner | PM | Catalogo mappato sul prodotto | Giorno 10 |
| 1.6 | Test end-to-end: attivazione → report → proposta | PM + Partner | Flusso completo funzionante | Giorno 14 |

### Deliverable fase
- Tenant white-label attivo
- Almeno 5 clienti pilota attivati
- Catalogo servizi configurato

---

## Fase 2: ENABLEMENT (Settimana 3–4)

**Obiettivo**: Team commerciale del partner formato e autonomo nell'uso della piattaforma.

| # | Task | Owner | Success Criteria | Deadline |
|---|------|-------|-----------------|----------|
| 2.1 | Training venditori: come usare la piattaforma per vendere | Sales + PM | Training completato, quiz superato | Sett 3 |
| 2.2 | Training tecnico: interpretare output e report della piattaforma | PM/Pre-sales | Team tecnico autonomo | Sett 3 |
| 2.3 | Creazione materiale co-branded (pitch deck, one-pager) | Marketing + Partner | Materiale approvato dal partner | Sett 3 |
| 2.4 | Role-play sessioni di vendita (obiezioni comuni) | Sales | Almeno 2 sessioni completate | Sett 4 |
| 2.5 | Setup campagna lead gen (email template, landing) | Marketing + Partner | Campagna pronta al lancio | Sett 4 |
| 2.6 | Definizione target: lista 20-50 prospect da contattare | Partner + Sales | Lista validata e prioritizzata | Sett 4 |

### Deliverable fase
- Team venditori formato e certificato
- Materiale co-branded pronto
- Pipeline iniziale di 20-50 prospect target

---

## Fase 3: LAUNCH (Settimana 5–8)

**Obiettivo**: Prime vendite reali, pipeline attiva, partner autonomo nel ciclo commerciale.

| # | Task | Owner | Success Criteria | Deadline |
|---|------|-------|-----------------|----------|
| 3.1 | Lancio campagna outbound su lista prospect | Partner + Sales | Campagna attiva, prime risposte | Sett 5 |
| 3.2 | Primi 10+ assessment/demo gratuiti inviati | Partner | 10 prospect con report ricevuto | Sett 6 |
| 3.3 | Follow-up assessment → primo meeting commerciale | Partner + Sales | Almeno 3 meeting fissati | Sett 6-7 |
| 3.4 | Prima proposta commerciale inviata | Partner | 1+ proposta inviata tramite piattaforma | Sett 7 |
| 3.5 | Primo deal chiuso (anche piccolo) | Partner | Revenue > 0 dalla piattaforma | Sett 8 |
| 3.6 | Review mid-launch: cosa funziona, cosa no | Sales + PM + Partner | Azioni correttive identificate | Sett 6 |

### Deliverable fase
- Primo revenue generato
- Pipeline attiva con 5+ opportunita
- Partner autonomo nel ciclo assess → propose → close

---

## Fase 4: OPTIMIZE (Settimana 9–12)

**Obiettivo**: Crescita sostenibile, processi consolidati, health score > 70.

| # | Task | Owner | Success Criteria | Deadline |
|---|------|-------|-----------------|----------|
| 4.1 | Analisi conversion rate assessment → deal | PM + Sales | Report con insight e azioni | Sett 9 |
| 4.2 | Ottimizzazione catalogo servizi (basata su dati reali) | PM + Partner | Catalogo aggiornato con top seller | Sett 10 |
| 4.3 | Setup monitoraggio continuo per clienti attivi | PM/Engineering | Dashboard partner attiva | Sett 10 |
| 4.4 | Primo QBR interno (review 90 giorni) | Sales + PM | QBR completato, piano Q+1 | Sett 12 |
| 4.5 | Health score check e baseline | CoS/Sales | Health score calcolato e registrato | Sett 12 |
| 4.6 | Valutazione upsell: tier upgrade o servizi aggiuntivi | Sales | Raccomandazione con timeline | Sett 12 |

### Deliverable fase
- Health score baseline registrato (target > 70)
- Piano trimestrale successivo definito
- Decision point: espandere, mantenere, o intervento

---

## Comandi

| Comando | Descrizione | Output |
|---------|------------|--------|
| `new-partner` | Inizializza onboarding per un nuovo partner | Crea scheda partner + checklist tracking |
| `status` | Mostra stato onboarding di un partner (o tutti) | Report con fase attuale e completamento |
| `checklist` | Mostra checklist dettagliata della fase attuale | Lista task con stato e owner |

---

## Comando: new-partner

### Input
- Nome partner
- Tipo (es. Reseller / Distributore / Agenzia / System Integrator)
- Tier contrattuale (es. Starter / Growth / Scale / Enterprise)
- Data firma contratto
- Contatto principale (nome, ruolo, email)

### Processo
1. Crea file `company/customers/partners/{slug}.md` dal template
2. Compila dati iniziali
3. Imposta fase = SETUP, start date = data firma
4. Genera checklist fase 1 con deadline calcolate
5. Handoff: notifica Sales + PM per kickoff

### Output
- File partner creato in `company/customers/partners/{slug}.md`
- Commit: `[sales] onboarding: new partner {nome} — setup phase started`

---

## Comando: status

### Input
- Partner slug (opzionale — se omesso, tutti)

### Output format
```
## Onboarding Status — {data}

| Partner | Fase | Settimana | Completamento | Prossima milestone | Alert |
|---------|------|-----------|--------------|-------------------|-------|
| Partner A | LAUNCH | 6/12 | 75% | Primo deal (sett 8) | - |
| Partner B | SETUP | 2/12 | 40% | Primo utilizzo (giorno 7) | Task 1.4 in ritardo |
```

---

## Comando: checklist

### Input
- Partner slug
- Fase (opzionale — default: fase attuale)

### Output
Checklist della fase con stato di ogni task:
```
## Checklist SETUP — Partner A (Settimana 1/2)

- [x] 1.1 Kickoff call — completato 2026-03-01
- [x] 1.2 Tenant white-label — completato 2026-03-03
- [ ] 1.3 Configurazione utenti — in corso (deadline: 2026-03-05)
- [ ] 1.4 Import clienti pilota — non iniziato (deadline: 2026-03-07)
- [ ] 1.5 Catalogo servizi — non iniziato (deadline: 2026-03-10)
- [ ] 1.6 Test end-to-end — non iniziato (deadline: 2026-03-14)

Completamento: 33% | On track: Si
```

---

## Dove vivono i dati

| Dato | Path |
|------|------|
| Schede partner | `company/customers/partners/{slug}.md` |
| Template scheda | `company/customers/partners/TEMPLATE.md` |
| Segmenti clienti | `company/customers/segments.md` |
| **PoC kickoff deck** (asset pre-firma — standard per attivare il PoC guidato di un prospect) | `docs/presentations/poc-kickoff-deck.pptx` |
