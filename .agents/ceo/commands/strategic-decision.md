# Command: strategic-decision

## Trigger
`/ceo strategic-decision [topic]` oppure "Devo decidere su [topic]"

## Processo

1. **Definisci il problema** — Qual è la vera domanda? Perché è importante ora?
2. **Carica contesto rilevante** dal repo
3. **Identifica opzioni** — Almeno 2-3 alternative concrete
4. **Per ogni opzione valuta**:
   - Pro e contro
   - Effort / risorse richieste
   - Impatto su strategia, prodotto, team, finanze
   - Rischi e come mitigarli
   - Reversibilità (facile da cambiare o no?)
5. **Raccomanda** — Quale opzione e perché
6. **Definisci next steps** — Chi fa cosa, quando
7. **Definisci review date** — Quando rivalutiamo

## Output
Salva in: `decisions/{YYYY-MM-DD}-{slug}.md` usando il template standard
Commit: `[ceo] decision: {slug}`

## Nota
Se la decisione richiede input da altri agenti (es. stima CTO, analisi PM), indica il handoff necessario prima di decidere.
