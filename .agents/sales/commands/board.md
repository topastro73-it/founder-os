# Command: board

## Trigger
`/sales board` · "Mostra il cockpit" · "Dove sono ferme le trattative?" · "Rigenera la pipeline"

## Skill
`.skills/opportunity-management/SKILL.md`

## Processo
1. Esegui lo script generatore:
   ```
   python scripts/generate-pipeline.py
   ```
   (Per un sottoinsieme/esempio: `--base examples/acme-demo/customers`. Per una data di riferimento dell'aging diversa da oggi: `--date YYYY-MM-DD`.)
2. Lo script legge `company/customers/pipeline-config.yaml` + `company/customers/opportunities/*.md`, calcola l'aging live e scrive `company/customers/PIPELINE.md` con: Summary, Per segmento, **🔴🟠🟡 Bloccati & Aging**, Per owner, Per stage, Won.
3. Mostra al CEO il riassunto (output dello script) ed evidenzia i top 🔴 e le opportunità senza owner.

## Note
- Il board è uno snapshot: la verità resta nel frontmatter delle opportunità. Rigeneralo dopo ogni batch di update.
- Se Python non è disponibile, in fallback puoi rigenerare il markdown leggendo le opportunità e applicando le regole della skill (sezione 3-4.2).

## Output
`company/customers/PIPELINE.md`
Commit: `[sales] board: pipeline cockpit {YYYY-MM-DD}`
