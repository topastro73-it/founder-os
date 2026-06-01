# Pricing Skill

Framework per decisioni di pricing in B2B SaaS. Usato da PM, CFO e Sales.

## Principi di Pricing B2B SaaS

### Value-Based Pricing
Non prezzare in base ai costi. Prezza in base al valore che il cliente ottiene.
Domanda chiave: "Quanto vale risolvere questo problema per il cliente?"

### Pricing Architecture

#### Modelli
| Modello | Quando usarlo | Pro | Contro |
|---------|-------------|-----|--------|
| **Per-seat** | Valore cresce con utenti | Prevedibile, scalabile | Limita adozione |
| **Usage-based** | Valore proporzionale all'uso | Allineato al valore | Imprevedibile per il cliente |
| **Flat fee** | Semplicità è un differenziatore | Facile da vendere | Non scala col valore |
| **Tiered** | Segmenti diversi con bisogni diversi | Segmentazione naturale | Complessità |
| **Hybrid** | Bisogno di prevedibilità + upside | Bilanciato | Più complesso da comunicare |

#### Packaging (Tiers)
| Tier | Target | Caratteristiche |
|------|--------|----------------|
| **Starter/Basic** | SMB, self-serve | Core features, limiti su volume/utenti |
| **Professional** | Mid-market | Tutte le feature, integrazioni, supporto |
| **Enterprise** | Enterprise, high-touch | Custom, SLA, dedicated support, SSO, audit |

### Framework di Decisione

#### Per nuova feature — dove la metto?
1. **Core** (inclusa in tutti i tier): se è table-stakes o se la differenziazione competitiva lo richiede
2. **Tier-gated**: se il segmento target è chiaro (es. SSO → Enterprise)
3. **Add-on**: se il valore è indipendente dal tier e misurabile separatamente
4. **Usage-based**: se il valore è direttamente proporzionale all'uso

#### Per cambio pricing
1. Analizza impatto su clienti esistenti (grandfathering?)
2. Modella impatto su revenue: ACV change × conversion change × churn change
3. Test: cosa fa il competitor? Il nostro prezzo è giustificabile?
4. Comunica: trasparenza sul perché del cambio, preavviso adeguato

### Metriche di Pricing Health
- **ACV medio**: trend e distribuzione
- **Discount rate medio**: quanto scendiamo dal listino? (target: <15%)
- **Tier distribution**: % clienti per tier (sano: 60% mid, 25% starter, 15% enterprise)
- **Upgrade rate**: % clienti che salgono di tier
- **Price sensitivity**: a che punto il prezzo blocca i deal?

### Anti-Pattern
- ❌ "Il competitor costa X, noi costiamo X-20%" → race to the bottom
- ❌ "Il cliente dice che è troppo caro" → potrebbe non essere il tuo ICP
- ❌ "Prezzo diverso per ogni cliente" → nightmare operativo
- ❌ "Free tier illimitato" → attira clienti wrong-fit
- ❌ "Discount per chiudere il deal" → senza processo = slippery slope

### Dove vivono i dati di pricing nel repo
- `company/finance/pricing.md` — Listino corrente e tier structure
- `decisions/` — Decisioni di pricing passate con razionale
- `docs/reports/pricing-*.md` — Analisi pricing (da PM e CFO)
- `docs/proposals/quote-*.md` — Quotazioni (da Sales)
