# Protocol — Meetings ingestion

> How meeting minutes (MoMs) enter the founder-OS. Mirrors the intelligence-inbox pattern
> (`docs/intelligence/` + `/routine process-signals`) but for meetings. Outputs are written in English
> (see memory: output-language-english).

## Why

Meetings produce decisions, deals, action items and reusable lessons that otherwise stay trapped in raw
notes. This protocol turns a MoM into structured founder-OS state, with a single audit trail per meeting.

## Layers it feeds (reuse, don't duplicate)

| Content in a MoM | Goes to |
|------------------|---------|
| Deal / prospect / pipeline movement | `company/customers/opportunities/{opp-slug}.md` (+ account in `partners/`) |
| Decision taken | `decisions/YYYY-MM-DD-{slug}.md` (immutable, template DEC-NNN) |
| Strategic idea (not yet decided) | `wiki/entities/concepts/{slug}.md` or a decision in `Proposta` state |
| Partner/account fact | `company/customers/partners/{slug}.md` |
| Money: grants, pricing model | `company/finance/` |
| Equity / cap-table 🔴 | `company/finance/equity.md` **only** (never elsewhere) |
| Founder commitments | `company/ceo-routine.md` "Promesse aperte" (+ opportunity next-steps) |
| Product / roadmap signal | `company/product/backlog.md` or `roadmap.md` |
| Reusable rule | propose a learning at `/routine close` → `system/learnings.md` |
| Narrative ("why") | `wiki/sessions/` + `wiki/entities/` (generated at `/routine close`) |

## Flow

1. **Drop** the raw MoM into `docs/meetings/inbox/`.
2. **Extract & fan out** — route each item to the layer above.
3. **Write the structured MoM** `docs/meetings/{YYYY-MM-DD}-{slug}.md`:
   - Frontmatter: `type: meeting`, `date`, `attendees`, `meeting-type`, `related-opportunities`,
     `related-decisions`, `tier`.
   - Sections: **Summary** · **Decisions** · **Action items** (owner · due) · **Routed-to** (links to every
     file created/updated).
   - **Store structured only** — do not commit the raw verbatim transcript (keeps the repo lean and
     PII-light). Move the raw source to `docs/meetings/inbox/processed/` (gitignored if it carries PII).
4. **Index** — add a row to `docs/meetings/index.md`.
5. **Commit** per agent area (`[sales]`, `[ceo]`, `[cfo]`, `[cos]`). No equity %, grant amounts, or PII in
   commit-message bodies.

## Privacy gate (CLAUDE.md §20-21)

- 🔴 RESTRICTED (equity, cap-table, IBAN, CF/p.IVA, salaries) → `company/finance/` or `company/legal/` only;
  never in `docs/meetings/`, `wiki/`, `system/learnings.md`, or commit messages.
- External-people PII: use the partner account contact fields; in `wiki/` use initials + role unless a
  dedicated entity page exists.
- Default tier for a MoM that mixes topics: 🟡 INTERNAL.

## See also
`system/protocols/persistent-memory.md`, `system/protocols/wiki.md`, `.skills/opportunity-management/SKILL.md`.
