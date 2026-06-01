# Command: incident-postmortem

## Trigger
`/cto incident-postmortem [incident]`

## Processo
1. Timeline dell'incidente: cosa è successo, quando, impatto
2. Root cause analysis (5 Whys)
3. Cosa ha funzionato nella response
4. Cosa non ha funzionato
5. Action items con owner e deadline
6. Tono: blameless, orientato al miglioramento

## Output
Salva in: `docs/reports/postmortem-{slug}.md`
Commit: `[cto] postmortem: {incident}`
Handoff → CEO se impatto su clienti, → Marketing se comunicazione pubblica necessaria
