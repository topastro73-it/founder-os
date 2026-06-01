# Persistent Memory Protocol

Durante ogni conversazione, intercetta i dati di business concreti emersi e chiedi al CEO se salvarli nel file appropriato.

## Cosa intercettare

| Tipo | Esempio | File di destinazione |
|------|---------|---------------------|
| Numero/metrica | "Il MRR è 5.200€" | `company/metrics/kpis.md` |
| Decisione presa | "Andiamo con l'opzione A" | `decisions/YYYY-MM-DD-slug.md` |
| Info partner | "Acme ha onboardato 20 clienti" | `company/customers/partners/{slug}.md` |
| Info deal/prospect | "Partner X: meeting la settimana prossima" | `company/customers/` |
| Cambio strategia | "Focus ora sul mercato francese" | `company/strategy/vision.md` |
| Info pricing | "Prezzo base sale a €X" | `company/finance/pricing.md` |
| Info team | "Assunto Marco come CTO" | `.agents/_shared/TEAM.md` |
| Stato spec/feature | "Bulk import è in produzione" | `company/product/specs/` + `roadmap.md` |
| Scadenza | "Deliverable D2.1 scade il 15 aprile" | `company/finance/scadenzario.md` |
| Costo/fattura | "AWS costa €300/mese" | `company/finance/costi-ricorrenti.md` |
| Info competitor | "Acme ha lanciato feature simile" | `company/competitors/` |
| OKR progress | "Siamo al 60% sul KR2" | `company/strategy/` |

## Come chiedere

Alla fine della risposta, in modo conciso:

```
💾 Dati da salvare:
- MRR marzo: €5.200 → `company/metrics/kpis.md`
- Acme: +8 clienti, -2 churn → `company/customers/partners/acme.md`

Salvo tutto, scegli quali, o no?
```

## Regole

- **Chiedi SEMPRE** prima di salvare — mai agire senza conferma del CEO
- **Raggruppa** — una sola domanda alla fine, non una per dato
- **Indica il file** — il CEO deve sapere dove finisce il dato
- Se il CEO dice "salva tutto" → salva tutto e conferma con ✅ e lista file aggiornati
- Se il CEO dice "no" → non insistere, procedi
- **Non chiedere** per ipotesi, esplorazioni o dati già salvati
- **Non chiedere** durante la routine giornaliera/settimanale (i dati vengono raccolti nel flusso)

## Privacy

Applica sempre le regole di `CLAUDE.md` § 20-21:
- Dati RESTRICTED (IBAN, CF, p.IVA, dati salari) → mai in `MEMORY.md` o wiki
- Nomi cliente in narrative: usa iniziali + ruolo
