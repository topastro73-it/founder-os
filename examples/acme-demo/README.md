# 📦 Demo: Acme

> **Questo è un esempio fittizio.** "Acme" non esiste: serve a mostrarti come appare un
> founder-os già compilato. Nessun dato reale.
>
> **This is a fictional example.** "Acme" is made up — it shows you what a filled-in
> founder-os looks like. No real data.

## Come usarlo / How to use

- **Leggilo** per capire il livello di dettaglio atteso in ogni file.
- **Copia** i contenuti che ti servono nei file reali (`.agents/_shared/`, `company/`) e adattali.
- Oppure lancia `/setup` e usa Acme come riferimento mentre rispondi.

## Cosa fa Acme (the fictional company)

**Acme** — *the customer-onboarding automation platform for B2B SaaS companies.*
Acme aiuta i team Customer Success a far raggiungere ai nuovi clienti il "primo valore" più in fretta,
automatizzando i playbook di onboarding e misurando il time-to-value.

## File inclusi

| File | Corrisponde a |
|------|---------------|
| `COMPANY.md` | `.agents/_shared/COMPANY.md` |
| `TEAM.md` | `.agents/_shared/TEAM.md` |
| `vision.md` | `company/strategy/vision.md` |
| `segments.md` | `company/customers/segments.md` |
| `roadmap.md` | `company/product/roadmap.md` |
| `kpis.md` | `company/metrics/kpis.md` |
| `customers/pipeline-config.yaml` | `company/customers/pipeline-config.yaml` |
| `customers/partners/*.md` | `company/customers/partners/*.md` (account: Globex, Hooli, Initech, Umbrella, Wayne) |
| `customers/opportunities/*.md` | `company/customers/opportunities/*.md` (6 trattative) |
| `customers/PIPELINE.md` | `company/customers/PIPELINE.md` (cockpit **generato**) |
| `customers/target-funnel.md` | `company/customers/{canale}-funnel.md` |

### Cockpit commerciale (CRM-in-repo)

`customers/` mostra il sistema **account ↔ opportunità ↔ cockpit** con aging e segmenti. Per rigenerare il board:

```
python scripts/generate-pipeline.py --base examples/acme-demo/customers --date 2026-06-05
```

(In uso reale: `python scripts/generate-pipeline.py` senza argomenti, con la data di oggi.) Vedi `.skills/opportunity-management/SKILL.md`.
