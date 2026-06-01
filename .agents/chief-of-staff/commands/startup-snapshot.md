# Command: startup-snapshot

## Trigger
`/cos startup-snapshot` oppure "Dammi la foto della startup" oppure "Come stiamo?"

## Processo

1. **Carica tutte le fonti**
   - `.agents/_shared/COMPANY.md` — identità e posizionamento
   - `company/strategy/vision.md` — direzione strategica
   - `company/strategy/okrs/` — OKR correnti e progress
   - `company/product/roadmap.md` + `backlog.md` + `specs/` — stato prodotto
   - `company/metrics/kpis.md` + `funnel.md` — metriche chiave
   - `company/customers/segments.md` — chi sono i clienti, deal attivi
   - `company/competitors/` — landscape competitivo
   - `decisions/` — tutte le decisioni: ordina per data, estrai le più recenti
   - `docs/reports/` — report recenti di tutti gli agenti
   - `.agents/_shared/TEAM.md` — chi fa cosa

2. **Costruisci lo snapshot in sezioni**

   ### 1. Chi siamo (2-3 righe)
   Prodotto, mercato target, stadio attuale.

   ### 2. Strategia & OKR
   - Obiettivi del quarter corrente
   - Progress per ogni KR (% o stato qualitativo se metriche non disponibili)
   - Delta rispetto al piano

   ### 3. Prodotto — stato attuale
   - Cosa è in produzione oggi
   - Cosa è in sviluppo (Q corrente)
   - Prossimo lancio previsto
   - Rischio slittamento più critico

   ### 4. Metriche chiave
   - MRR / ARR (se disponibile)
   - Trial attivi, conversion rate
   - Partner / canale attivi
   - KPI di prodotto rilevanti

   ### 5. Sales & Pipeline
   - Deal attivi con stato
   - Trial in corso e loro stato
   - Prossima opportunità commerciale

   ### 6. Marketing
   - Attività in corso
   - Content/campagne attive
   - Positioning vs competitor principale

   ### 7. Team
   - Chi c'è, cosa sta facendo
   - Gap di hiring aperti (se presenti)

   ### 8. Top 5 rischi
   Ordinati per probabilità × impatto. Per ognuno: descrizione, piano di mitigazione.

   ### 9. Top 5 priorità immediate
   Le 5 cose più importanti su cui il team deve focalizzarsi questa settimana/questo mese.

   ### 10. Decisioni recenti
   Ultime 3-5 decisioni registrate nel repo con data e sintesi.

3. **Tono e formato**
   - Documento esecutivo, leggibile in 5 minuti
   - Usa semafori 🟢🟡🔴 per stato di ogni sezione
   - Evidenzia in grassetto i punti che richiedono attenzione del CEO

## Output
Salva in: `docs/reports/startup-snapshot-{YYYY-MM-DD}.md`
Commit: `[cos] report: startup snapshot {YYYY-MM-DD}`
