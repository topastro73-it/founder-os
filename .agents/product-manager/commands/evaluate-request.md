# Command: evaluate-request

## Trigger
`/pm evaluate-request [feature]` oppure "Valuta questa richiesta: [descrizione]"

## Input richiesto
- Nome/descrizione della feature
- Cliente richiedente (se applicabile)
- Contesto business (deal size, urgenza, chi la chiede)

## Processo

0. **Spec Status Check** ← Regola globale 9 (CLAUDE.md)
   - Leggi `company/product/specs/INDEX.md` + frontmatter di ogni spec
   - Identifica spec stale e chiedi conferma al CEO prima di procedere
   - Aggiorna frontmatter e INDEX, poi continua

1. **Carica contesto**
   - `company/strategy/vision.md` per i pilastri strategici
   - `company/product/roadmap.md` per conflitti/sinergie
   - `company/customers/segments.md` per validare segmento
   - `company/product/backlog.md` per richieste simili esistenti

2. **Estrai il bisogno reale**
   - Qual è il job-to-be-done del cliente?
   - La feature richiesta è la soluzione giusta o c'è di meglio?
   - Distingui il "cosa chiedono" dal "perché lo chiedono"

3. **Applica framework di valutazione**

   **Strategic Fit** (High/Medium/Low):
   - Si allinea alla visione e ai pilastri?
   - Serve il segmento core?
   - Rafforza la differenziazione?

   **Scalability** (Scalable/Partially/Custom):
   - Si può generalizzare?
   - Richiede config customer-specific?
   - Crea debito tecnico?

   **Market Demand** (Broad/Niche/Single-customer):
   - Quanti clienti ne beneficerebbero?
   - È un pain point comune?
   - Esiste domanda di mercato?

   **Effort vs Value**:
   - Effort stimato: XS/S/M/L/XL
   - Business value: impatto su revenue/retention/acquisition
   - Opportunity cost: cosa non facciamo se facciamo questo?

4. **Genera raccomandazione**
   - **BUILD FOR PRODUCT**: High fit + Scalable + Broad demand
   - **BUILD AS CONFIGURABLE**: Medium-high fit + Partially scalable + Multi-customer
   - **CUSTOM DEVELOPMENT**: Low fit OR single-customer OR unclear value
   - **DECLINE/DEFER**: Low fit + Niche OR conflitto con integrità prodotto

5. **Check red flags** (se da sales)
   - □ Single customer request senza validazione
   - □ Timeline irrealistico
   - □ Scope creep potential
   - □ Sales commission > strategic value
   - □ Competitor matching vs customer need

## Output
Salva in: `company/product/specs/evaluation-{slug}.md`
Commit: `[pm] evaluation: {feature-name}`

## Post-evaluation handoffs
- Se DECLINE → genera response template per Sales
- Se BUILD → suggerisci `/pm write-spec` come next step
- Se richiede stima tecnica → indica handoff a CTO
- Se è una decisione strategica → indica escalation a CEO
