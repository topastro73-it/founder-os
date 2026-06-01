# Spec Status Check Protocol

Prima di iniziare qualsiasi attività legata al prodotto (`evaluate-request`, `write-spec`, `prioritize-backlog`, `roadmap-review`, `sprint-planning`, `status-check`, `product-plan`, `weekly-digest`), l'agente DEVE eseguire il seguente protocollo.

## Passo 1 — Scansiona
Leggi `company/product/specs/INDEX.md` e il frontmatter `status` + `last-updated` di ogni spec.

## Passo 2 — Identifica spec stale

Soglie di staleness:

| Status | Diventa stale dopo |
|--------|-------------------|
| `draft` | 7 giorni |
| `evaluated` | 14 giorni |
| `approved` | 14 giorni |
| `in-development` | 30 giorni |
| `deferred` | alla `review-date` indicata |
| `declined` / `shipped` | Mai (stati finali) |

## Passo 3 — Se ci sono spec stale

Chiedi al CEO PRIMA di procedere:

> 📋 **Spec Status Check** — Prima di procedere, confermami lo stato di queste spec:
>
> | Spec | Stato attuale | Da quando | Aggiornamento? |
> |------|--------------|-----------|---------------|
> | prd-xyz.md | approved | 2026-02-15 | → in-development? shipped? deferred? |
>
> Dimmi per ognuna lo stato corretto e procedo.

## Passo 4 — Aggiorna

Aggiorna frontmatter (`status`, `last-updated`, `last-status-check`) e `INDEX.md` in base alla risposta del CEO.

## Passo 5 — Procedi

Procedi con il lavoro originale.

## Eccezioni (non fare il check)

- Se lo hai già fatto oggi nella stessa sessione
- Se non ci sono spec stale
- Se l'attività non riguarda il prodotto (marketing content, legal review, ecc.)
- Se il check è stato fatto nelle ultime 4 ore nella stessa sessione (anti-duplicazione)
