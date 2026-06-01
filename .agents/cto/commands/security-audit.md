# Command: security-audit

## Trigger
`/cto security-audit`

## Processo
1. Review aree: autenticazione, autorizzazione, data protection, infrastruttura, dipendenze
2. Per ogni area: stato attuale, rischi identificati, severità (Critical/High/Medium/Low)
3. Proponi remediation plan prioritizzato per severità
4. Stima effort per ogni remediation

## Output
Salva in: `docs/reports/security-audit-{YYYY-MM-DD}.md`
Commit: `[cto] security: audit report`
