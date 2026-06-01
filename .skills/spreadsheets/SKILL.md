# Spreadsheets Skill

Framework per la creazione di file Excel. Usato da CFO, PM, Sales.

## Tipi di Spreadsheet Disponibili

### 1. Financial Model / P&L — Owner: CFO
- Tabs: Assumptions, Monthly P&L, Annual Summary, Unit Economics, Scenarios
- Color coding: blue = input, black = formula, green = cross-sheet reference
- Tutte le assunzioni in celle dedicate, mai hardcoded nelle formule

### 2. Pricing Calculator — Owner: CFO + Sales
- Tabs: Pricing Tiers, Quote Builder, Competitor Comparison, Discount Matrix
- Formule per calcolo automatico basato su: utenti, tier, durata contratto, add-on
- Sconti applicati automaticamente con validazione (max 20% senza approvazione)

### 3. KPI Dashboard — Owner: CFO + CEO
- Tabs: Monthly Metrics, Charts, Funnel Analysis, Cohort Analysis
- Grafici integrati per trend visualization
- Formula per calcoli automatici: growth rate m/m, churn, NRR, LTV/CAC

## Come generare i file Excel

Per generare un file `.xlsx` reale, chiedi a Claude Code:
"Genera un file Excel per [tipo] seguendo il framework in `.skills/spreadsheets/SKILL.md`"

Claude Code può generare file Excel reali con formule, formattazione e grafici.

## Best Practice Excel

### Struttura
- Prima tab = "Instructions" o "Summary" con overview
- Assunzioni separate dai calcoli
- Una tab per ogni concetto logico
- Flow left-to-right, top-to-bottom

### Formule
- Zero errori: nessun #REF!, #DIV/0!, #VALUE!, #N/A
- Usa IFERROR per proteggere da divisioni per zero
- Celle con assunzioni in blue, formule in nero
- Mai hardcoded: ogni numero modificabile è in una cella dedicata

### Formattazione
- Font consistente (Arial)
- Header con background colorato
- Numeri formattati: valuta con €, percentuali con %, separatore migliaia
- Negativi tra parentesi: (1.234) non -1.234
- Bordi leggeri per leggibilità
