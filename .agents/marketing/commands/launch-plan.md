# Command: launch-plan

## Trigger
`/marketing launch-plan [feature]` oppure "Pianifica il lancio di [feature]"

## Processo
1. Carica PRD/spec della feature da `company/product/specs/`
2. Classifica lancio: Tier 1 (major) / Tier 2 (notable) / Tier 3 (minor)
3. Per Tier 1 genera: blog post, email, social, landing page copy, sales enablement
4. Per Tier 2: blog post + email + changelog
5. Per Tier 3: changelog only
6. Timeline con milestones: pre-launch → launch day → post-launch
7. Success metrics per il lancio

## Output
Salva in: `docs/reports/launch-plan-{feature}.md`
Commit: `[marketing] launch: plan for {feature}`
Handoff → Sales per enablement
