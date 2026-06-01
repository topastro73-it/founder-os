# Skills — Index

Competenze riutilizzabili disponibili a **tutti gli agenti**. Ogni skill ha comandi, template, e contesto specifico nel suo `SKILL.md`.

Sono organizzate in due categorie:
- **Skill operative**: con comandi eseguibili e integrazione con sistemi esterni (ClickUp, Gmail, Stripe, ecc.)
- **Skill di contesto**: framework e guide lette come background per informare le decisioni

---

## Skill operative (con comandi eseguibili)

| Skill | Owner primario | Path | Usata da | Integrazione |
|-------|----------------|------|----------|--------------|
| **ClickUp** | PM | `.skills/clickup/SKILL.md` | PM, CTO, Chief of Staff | ClickUp API — gestione task, epic, roadmap |
| **Gmail** | Chief of Staff | `.skills/gmail/SKILL.md` | **Tutti gli agenti** | Gmail API — mailbox CEO, brief, tracking |
| **Customer Success** | Sales | `.skills/customer-success/SKILL.md` | Sales (owner), CEO, Chief of Staff | Gestione churn, NPS, expansion, QBR |
| **Partner Onboarding** | Sales | `.skills/partner-onboarding/SKILL.md` | Sales, PM, Chief of Staff | Onboarding partner, schede, timeline |
| **Data & Metrics** | CFO | `.skills/data-metrics/SKILL.md` | CEO, CFO, PM, Chief of Staff | KPI, dashboard, reporting |
| **Investor Relations** | CFO | `.skills/investor-relations/SKILL.md` | CEO, CFO, Legal | Investor updates, pitch prep, cap table |
| **Content Library** | Marketing | `.skills/content-library/SKILL.md` | Marketing, Sales, CEO, Chief of Staff | Asset index, templates, reuse |
| **Outbound & ABM** | Sales | `.skills/outbound-abm/SKILL.md` | Sales (owner), Marketing, CEO | Campaign planning, targeting, sequencing |
| **Financial Import** | CFO | `.skills/financial-import/SKILL.md` | CFO, CEO, Chief of Staff | Import finanze, bilanci, forecasting |
| **Audit & Compliance** | Legal | `.skills/audit-compliance/SKILL.md` | Legal (owner), CTO, CEO, Chief of Staff, HR, Sales | NIS2, GDPR, ISO27001, audit trail |
| **Admin & Controllo** | CFO | `.skills/admin-controllo/SKILL.md` | CFO (owner), CEO, Chief of Staff | Accessi, permessi, governance |
| **Fatture in Cloud** | CFO | `.skills/fatture-in-cloud/SKILL.md` | CFO (owner), CEO, Chief of Staff | Integrazione FiC per fatturazione |
| **Qonto** | CFO | `.skills/qonto/SKILL.md` | CFO (owner), CEO, Chief of Staff | Conto bancario, transazioni, reconciliazione |
| **ERP** | CFO | `.skills/erp/SKILL.md` | CFO (owner), CEO, Chief of Staff | Integrazione ERP per ordini, inventario |
| **Stripe** | CFO | `.skills/stripe/SKILL.md` | CFO (owner), CEO, Chief of Staff, Sales | Pagamenti, subscription, payout |
| **Business Analysis** | PM | `.skills/business-analysis/SKILL.md` | PM (owner), CEO, Chief of Staff | Requirements, gap analysis, functional spec |
| **NotebookLM** | CEO | `.skills/notebooklm/SKILL.md` | CEO, PM, CTO, Chief of Staff, Sales, Legal | AI-powered document analysis, insights |
| **Personal Todo** | CEO | `.skills/personal-todo/SKILL.md` | CEO (owner), CEO Routine | To-do list personale del CEO — add, list, done, review |
| **System Admin** | CEO | `.skills/system-admin/SKILL.md` | CEO (owner), tutti gli agenti | Changelog, checkpoint e rollback del sistema founder-os |
| **QA & Testing** | CTO | `.skills/qa-testing/SKILL.md` | CTO (owner), PM | Test plan, test case, test report, smoke/security test |

---

## Skill di contesto (framework e guide)

Lette come background per informare le decisioni; non hanno comandi eseguibili.

| Skill | Owner primario | Path | Usata da | Uso |
|-------|----------------|------|----------|-----|
| **Pricing** | PM | `.skills/pricing/SKILL.md` | PM, CFO, Sales | Modelli prezzi, tiers, bundling, packaging |
| **Presentations** | CEO | `.skills/presentations/SKILL.md` | CEO, CFO, Marketing | Pitch deck, board deck, investor update |
| **Spreadsheets** | CFO | `.skills/spreadsheets/SKILL.md` | CFO, PM, Sales | Template finanziari, dashboard, modeling |
| **Analysis** | PM | `.skills/analysis/SKILL.md` | PM, CTO, CFO | Metodologie analisi, evaluation framework |
| **B2B SaaS** | PM | `.skills/b2b-saas/SKILL.md` | PM, Sales | SaaS playbook, GTM, CAC/LTV, retention |
| **Writing** | Marketing | `.skills/writing/SKILL.md` | Marketing, CEO, Sales | Tone, voice, messaging, copywriting |
| **Communication** | HR | `.skills/communication/SKILL.md` | HR, CEO | Comunicazione interna, change management |
| **Naming Strategist** | Marketing | `.skills/naming-strategist/SKILL.md` | Marketing, CEO, PM | Brief → long-list → short-list scored per nominare aziende, prodotti, feature, podcast, newsletter, sezioni, eventi |

---

## Come usare una skill

**Quando un agente invoca una skill**:

1. **Leggi** il file `SKILL.md` della skill
2. **Carica il contesto** (template, integrazione, dati aziendali)
3. **Esegui il comando** specifico (per skill operative)
4. **Salva l'output** nella location corretta
5. **Committa** con messaggio `[agente] azione: descrizione`

Esempio workflow:
```
User: "/pm write-spec"
    ↓
PM Agent: "/pm" invocato
    ↓
Read .agents/product-manager/AGENT.md
    ↓
Read .agents/product-manager/commands/write-spec.md
    ↓
Write-spec command references Business Analysis skill
    ↓
Read .skills/business-analysis/SKILL.md (per framework)
    ↓
Execute spec writing, save to company/product/specs/
    ↓
Commit [pm] spec: PRD per feature X
```

---

## Skill interne vs Plugin Cowork

Questa sessione include plugin generici (sales, marketing, legal, finance, ecc.) che offrono funzionalità simili alle skill interne.

**Regola**:
- **Skill interne** (in `.skills/`): hanno contesto specifico di {{COMPANY_NAME}} (ICP, pricing tiers, partner model, team). **Usale SEMPRE quando disponibili.**
- **Plugin Cowork**: usali come fallback per task generici non coperti dalle skill interne, o per funzionalità che le skill interne non offrono (es. brand-voice, design, enterprise-search)
- In caso di dubbio: **skill interna prima, plugin dopo**.

---

## Contesti di uso comune

### PM scrive una spec di prodotto
1. Read `.agents/product-manager/commands/write-spec.md`
2. Read `.skills/business-analysis/SKILL.md` (requirements framework)
3. Read `.skills/analysis/SKILL.md` (evaluation criteria)
4. Read `.skills/pricing/SKILL.md` (impact su pricing)
5. Write spec in `company/product/specs/prd-*.md`

### Sales prepara una proposta
1. Read `.agents/sales/commands/proposal.md`
2. Read `.skills/content-library/SKILL.md` (battlecard, template)
3. Read `.skills/outbound-abm/SKILL.md` (target account strategy)
4. Save to `docs/proposals/`

### CFO fa reporting financiero
1. Read `.agents/cfo/commands/monthly-report.md`
2. Read `.skills/data-metrics/SKILL.md` (KPI, dashboard)
3. Read `.skills/investor-relations/SKILL.md` (investor messaging)
4. Sync with `.skills/financial-import/SKILL.md` se dati esterni
5. Save to `docs/reports/`

---

## Note

- Ogni skill è **self-contained** nel suo `.skills/{slug}/` folder
- Template, command details, integration setup sono nel `SKILL.md`
- Learnings e best practices dai learnings (`system/learnings.md`) si applicano proattivamente
- Skill di contesto vengono **lette in background** prima di decision-making, non richiedono invocazione esplicita
