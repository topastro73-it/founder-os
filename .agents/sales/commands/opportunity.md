# Command: opportunity

## Trigger
`/sales opportunity [opp-slug]` o linguaggio naturale:
- "sposta globex-platform a contract-sent"
- "logga la call di oggi su initech-expansion"
- "blocca hooli-pilot su accesso dati, severity high"
- "apri una nuova opportunità expansion su initech"
- "chiudi vinta wayne-deal"

## Skill
`.skills/opportunity-management/SKILL.md` (sezione 4.1)

## Processo
1. Identifica l'opportunità (`opp-slug`) o creala da `company/customers/opportunities/TEMPLATE.md`.
2. Applica l'operazione:
   - **Crea**: compila frontmatter, `opened` e `last-activity` = oggi, aggiungi riga nell'indice Opportunità dell'account.
   - **Sposta stage**: aggiorna `stage`, **ricalcola** `probability` e `value-weighted` (mappa in `pipeline-config.yaml`), `last-activity` = oggi, voce in Timeline.
   - **Logga attività**: `last-activity` = oggi, voce in Timeline (link a feedback/sessione se esistono).
   - **Blocker**: aggiungi/aggiorna/risolvi entry in `blockers:` (what/owner/since/due/severity); `status-flag: blocked` se ≥1 aperto.
   - **Next step**: aggiorna `next-step` e `next-step-due`.
   - **Chiudi**: `stage` e `status-flag` = won|lost, svuota blocker aperti, registra esito.
3. Se manca un dato chiave (valore, owner, expected-close), chiedilo invece di inventarlo.
4. Mostra lo stato aggiornato (frontmatter sintetico + aging ricalcolato).
5. Suggerisci/esegui `/sales board` per riflettere la modifica nel cockpit.

## Drill-down in lettura
Senza operazione (solo `opp-slug`): mostra la scheda completa — stato, aging, blocker, timeline, next step.

## Output
`company/customers/opportunities/{opp-slug}.md` (+ indice in `company/customers/partners/{account}.md`)
Commit: `[sales] opportunity: {opp-slug} — {azione}`
