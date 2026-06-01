# Command: write-blogpost

## Trigger
`/marketing write-blogpost [topic]` oppure "Scrivi un post su [topic]"

## Processo
1. Carica tone of voice da `.skills/writing/` (include **Anti-AI-Slop Rules** — sezione finale)
2. Identifica: target persona, keyword primaria, intent (informational/commercial)
3. Struttura: hook forte → problema → soluzione → proof → CTA
4. Scrivi in modo conversazionale, non corporate
5. Includi: meta title, meta description, H1/H2 structure, internal links suggeriti
6. **Anti-slop pass finale**: scorri Quick Checks di `.skills/writing/SKILL.md#anti-ai-slop-rules` e calcola Scoring (5 dimensioni). Se < 35/50, revisiona prima di salvare. Vale anche per la newsletter Operator's Note (sezione AgenticOS di `docs/blog-posts/`)

## Output
Salva in: `docs/blog-posts/{slug}.md`
Commit: `[marketing] content: blog post — {title}`
