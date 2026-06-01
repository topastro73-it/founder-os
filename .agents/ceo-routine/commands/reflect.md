# Command: reflect

## Trigger
`/routine reflect` oppure "Facciamo una riflessione" oppure "Ho bisogno di pensare alla strategia"

## Processo

1. **Carica contesto strategico**
   - `company/strategy/vision.md`
   - `company/strategy/okrs/` (se esistono)
   - `company/metrics/kpis.md`
   - `company/customers/segments.md`
   - `company/competitors/battlecards/`
   - Ultimi `decisions/`

2. **Genera 5 domande strategiche** personalizzate sullo stato attuale dell'azienda

Le domande devono essere:
- **Non ovvie** — non chiedere cose che il CEO gia sa
- **Provocatorie** — sfidano assunzioni implicite
- **Azionabili** — la risposta porta a una decisione concreta
- **Basate sui dati** — ancorate a metriche o fatti nel repo

### Categorie di domande

| Categoria | Tipo di domanda |
|-----------|----------------|
| **Product-Market Fit** | Stiamo risolvendo il problema giusto? Il feedback lo conferma? |
| **Go-to-Market** | Il nostro canale funziona? Il CAC e sostenibile? |
| **Competition** | Qualcuno sta facendo la nostra cosa meglio di noi? |
| **Team** | Abbiamo le persone giuste nei ruoli giusti? |
| **Finance** | I numeri raccontano la storia che pensiamo? |
| **Timing** | Stiamo andando abbastanza veloci? Troppo veloci su cose sbagliate? |

3. **Output**

```
RIFLESSIONE STRATEGICA — {data}

Prenditi 15 minuti. Niente Slack, niente email. Solo queste domande.

1. [Domanda — con contesto specifico dall'azienda]
   Perche te lo chiedo: [motivo basato su dati]

2. [Domanda]
   Perche te lo chiedo: [motivo]

3. [Domanda]
   Perche te lo chiedo: [motivo]

4. [Domanda]
   Perche te lo chiedo: [motivo]

5. [Domanda]
   Perche te lo chiedo: [motivo]

Rispondi quando sei pronto. Le tue risposte guideranno le priorita delle prossime settimane.
```

4. **Dopo le risposte del CEO**
   - Sintetizza i takeaway chiave
   - Se emergono decisioni → suggerisci di formalizzarle in `decisions/`
   - Se emergono cambi di priorita → suggerisci aggiornamento OKR o roadmap
   - Registra la riflessione nel cadence log

## Output
Interazione diretta.
Se emergono decisioni: suggerisci handoff a CEO `strategic-decision`.
Commit: `[routine] reflect: strategic reflection {YYYY-MM-DD}`
