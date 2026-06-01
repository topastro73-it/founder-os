# Command: tech-decision

## Trigger
`/cto tech-decision [topic]` oppure "Decisione tecnica su [topic]"

## Processo
1. Definisci il problema tecnico e i vincoli
2. Identifica 2-3 opzioni con pro/contro per ciascuna
3. Valuta: performance, scalabilità, mantenibilità, costo, team skill, time-to-market
4. Raccomanda con razionale chiaro
5. Documenta come ADR

## Output
Salva in: `decisions/{YYYY-MM-DD}-{slug}.md` con template ADR
Commit: `[cto] adr: {topic}`
