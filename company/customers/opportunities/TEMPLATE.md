---
opp-name: "{Nome trattativa}"
opp-slug: "{account}-{tipo-o-progetto}"   # es. acme-pilot, globex-renewal
account: "{slug}"                          # FK → company/customers/partners/{slug}.md
segment: ""                                # key da company/customers/pipeline-config.yaml (es. enterprise | mid-market | smb | channel)
type: ""                                   # new-business | expansion | renewal | pilot | vendor-agreement
stage: "discovery"                         # discovery | technical-alignment | proposal-sent | negotiation | contract-sent | won | lost
probability: 20                            # derivata dallo stage (vedi pipeline-config.yaml)
value-gross: 0                             # ACV € annuo (lordo)
value-weighted: 0                          # = value-gross * probability / 100
owner-sales: ""
opened: "YYYY-MM-DD"
expected-close: "YYYY-MM-DD"
last-activity: "YYYY-MM-DD"                # base di calcolo dell'aging
next-step: ""
next-step-due: "YYYY-MM-DD"
status-flag: "active"                      # active | blocked | stalled | won | lost
blockers:                                  # STRUTTURATI — si aggregano nel board e alimentano l'aging
  - what: ""
    owner: ""
    since: "YYYY-MM-DD"
    due: "YYYY-MM-DD"
    severity: ""                           # low | med | high
compliance-impact: []                      # se rilevante per il tuo business
crm-id: ""                                 # link opzionale al CRM esterno (HubSpot/Salesforce/…)
---

# {Nome trattativa} — {Account}

> Account: [{account}](../partners/{account}.md) · Stage: **{stage}** · Valore: € {value-gross} ({probability}% → € {value-weighted})

## Contesto

{Di cosa si tratta: scope, driver d'acquisto, chi decide, perché ora. 3-6 righe.}

## Blocker (dettaglio)

<!-- Ogni voce qui corrisponde a una entry in `blockers:` nel frontmatter (fonte aggregata). -->

### {🔴/🟠/🟡} {Cosa blocca} — owner: {nome}, fermo dal {YYYY-MM-DD}
{Perché è bloccato, cosa serve per sbloccarlo, cosa è già stato tentato.}

## Timeline interazioni

<!-- Ordine cronologico inverso. Link alle fonti, non ricopiare il contenuto. -->

### YYYY-MM-DD — {tipo: call / email / meeting / decision}
{Cosa è successo in 1-2 righe.} → [feedback](../feedback/{file}.md) · [sessione](../../../wiki/sessions/{file}.md)

## Next steps

| # | Azione | Owner | Due | Status |
|---|--------|-------|-----|--------|
| 1 | {next-step} | {owner} | {YYYY-MM-DD} | open |
