# Command: sprint-planning

## Trigger
`/pm sprint-planning` oppure "Pianifica il prossimo sprint"

## Processo
0. **Spec Status Check** ← Regola globale 9 (CLAUDE.md)
   - Leggi `company/product/specs/INDEX.md` + frontmatter di ogni spec
   - Identifica spec stale e chiedi conferma al CEO prima di procedere
   - Aggiorna frontmatter e INDEX, poi continua
1. Carica `company/product/backlog.md` (prioritizzato)
2. Valuta capacità disponibile (da `company/team/`)
3. Seleziona items che entrano nello sprint rispettando:
   - Priorità RICE
   - Dipendenze
   - Mix sano: feature + bug fix + tech debt
4. Per ogni item: definisci goal chiaro e definition of done
5. Identifica rischi dello sprint

## Output
Salva in: `docs/reports/sprint-plan-{YYYY-MM-DD}.md`
Commit: `[pm] sprint: planning for {date-range}`
