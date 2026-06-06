---
partner-name: "{Nome Account}"
slug: "{slug}"
type: ""            # tipo account (allinea ai tuoi segmenti / segments.md)
tier: ""            # tier relazione (es. Attract | Engage | Scale | Enterprise)
status: "prospect"  # prospect | onboarding | active | at-risk | churned
contract-date: ""
contract-renewal: ""
onboarding-phase: ""
onboarding-start: ""
health-score: null
last-health-check: null
last-metrics-update: null
owner-sales: ""
owner-pm: ""
contact-name: ""
contact-role: ""
contact-email: ""
---

# {Nome Account}

<!--
QUESTO È L'ACCOUNT (anagrafica + relazione + successo post-vendita).
Lo stato VIVO delle trattative NON vive qui: vive in company/customers/opportunities/{opp-slug}.md.
La sezione "Opportunità" è un INDICE che linka quei file.
La narrativa storica di lungo periodo vive in wiki/entities/partners/{slug}.md.
-->

## Overview

| Campo | Valore |
|-------|--------|
| Tipo | {tipo} |
| Tier | {tier} |
| Status | {prospect / onboarding / active / at-risk / churned} |
| Contratto | {data firma} → {data rinnovo} |
| Owner Sales | {nome} |
| Contatto principale | {nome}, {ruolo} — {email} |

## Opportunità

<!-- Indice generato da company/customers/opportunities/ (filtra per account == {slug}). -->

| Opportunità | Tipo | Stage | Valore (lordo / weighted) | Status | Aging | Owner |
|-------------|------|-------|---------------------------|--------|-------|-------|
| [{opp-slug}](../opportunities/{opp-slug}.md) | {type} | {stage} | € — / € — | {status-flag} | {🟢/🟡/🟠/🔴} | {owner} |

## Metriche Correnti (account / post-sale)

| Metrica | Valore | Data aggiornamento |
|---------|--------|--------------------|
| {metrica 1} | — | — |
| Revenue mensile generato | € — | — |
| NPS / Soddisfazione | — | — |

## Health Score (account attivo)

| Data | Score | Fascia | Note |
|------|-------|--------|------|
| — | — | — | Baseline da stabilire dopo go-live |

## Note account

<!-- Solo note su ANAGRAFICA / relazione (cambio referente, rinnovo, escalation).
La cronologia delle trattative va nelle opportunità; la storia narrativa nella wiki entity. -->

### YYYY-MM-DD — {Tipo nota}
{Contenuto}
