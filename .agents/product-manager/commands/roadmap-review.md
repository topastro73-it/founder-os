# Command: roadmap-review

## Trigger
`/pm roadmap-review` oppure "Analizza la roadmap"

## Processo
0. **Spec Status Check** ← Regola globale 9 (CLAUDE.md)
   - Leggi `company/product/specs/INDEX.md` + frontmatter di ogni spec
   - Identifica spec stale e chiedi conferma al CEO prima di procedere
   - Aggiorna frontmatter e INDEX, poi continua
1. Carica `company/product/roadmap.md` e `company/strategy/vision.md`
2. Mappa ogni iniziativa ai pilastri strategici
3. Valuta bilanciamento: tech debt vs feature, quick win vs strategic bet, customer-driven vs vision-driven
4. Identifica gap strategici non coperti
5. Flag rischi di sequencing/dipendenze
6. Genera raccomandazioni di aggiustamento

## Output
Salva in: `docs/reports/roadmap-review-{YYYY-MM-DD}.md`
Commit: `[pm] review: roadmap analysis`
