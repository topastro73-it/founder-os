# Command: pipeline-review

## Trigger
`/sales pipeline-review`

## Skill
`.skills/opportunity-management/SKILL.md`

## Processo
1. Scansiona `company/customers/opportunities/*.md` (repo = source of truth della pipeline; CRM esterno opzionale via `crm-id`).
2. Calcola health: coverage vs target (`pipeline-config.yaml › weighted_target`), distribuzione per stage e per segmento, conversion rate e velocity (da `opened`/`expected-close` e Timeline).
3. Incrocia con `company/metrics/funnel.md` / `kpis.md` per coerenza.
4. Identifica deal a rischio (aging 🔴🟠, blocker high, next-step scaduti) e deal accelerabili.
5. Flag gap: pipeline sufficiente per il target? Dove si concentra il rischio (stage / owner / segmento)?
6. Proponi azioni concrete per migliorare il forecast.

## Differenza dal board
- `/sales board` → cockpit sinottico, stato istantaneo (`PIPELINE.md`, generato da script).
- `/sales pipeline-review` → **report narrativo** di analisi, datato.

## Output
Salva in: `docs/reports/pipeline-review-{YYYY-MM-DD}.md`
Commit: `[sales] review: pipeline analysis`
