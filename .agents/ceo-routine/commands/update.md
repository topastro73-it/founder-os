# Command: update

## Trigger
`/routine update [topic] [valore]` oppure "Aggiorna [metrica] a [valore]"

## Esempi
- `/routine update mrr 4800` → aggiorna MRR in kpis.md
- `/routine update clienti-attivi 6` → aggiorna clienti attivi in kpis.md
- `/routine update burn-rate 15000` → aggiorna burn rate in kpis.md
- `/routine update runway 18` → aggiorna runway in kpis.md
- `/routine update pipeline 85000` → aggiorna pipeline value in kpis.md

## Topic supportati

| Topic | Campo in kpis.md | Sezione |
|-------|-----------------|---------|
| `mrr` | MRR | Revenue |
| `arr` | ARR | Revenue |
| `acv` | ACV medio | Revenue |
| `nrr` | NRR | Revenue |
| `clienti-attivi` | Clienti attivi | Growth |
| `partner-attivazione` | Partner in attivazione | Growth |
| `new-logos` | New logos/mese | Growth |
| `churn` | Churn rate | Growth |
| `conversion` | Trial → Paid conversion | Growth |
| `pipeline` | Pipeline value | Sales |
| `win-rate` | Win rate | Sales |
| `sales-cycle` | Sales cycle (days) | Sales |
| `cac` | CAC | Sales |
| `wau` | WAU | Product |
| `nps` | NPS | Product |
| `uptime` | Uptime | Product |
| `burn-rate` | Burn rate | Financial |
| `runway` | Runway | Financial |

## Processo

1. Identifica il topic e il valore dal comando
2. Leggi `company/metrics/kpis.md`
3. Aggiorna il campo corrispondente con il nuovo valore
4. Aggiorna trend (confronto con valore precedente)
5. Conferma l'aggiornamento al CEO
6. Se il valore e critico (runway < 9 mesi, churn > 5%), segnala

## Output
Aggiorna `company/metrics/kpis.md`
Commit: `[routine] update: {topic} = {valore}`
