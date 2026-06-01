# Command: follow-up-tracker

## Trigger
`/cos follow-up-tracker` oppure "Traccia tutti i follow-up" oppure "Cosa è rimasto aperto?"

## Processo

1. **Scansiona tutte le fonti di follow-up**
   - `decisions/*.md` — blocchi `## Follow-up` con checkbox `[ ]` (aperti) e `[x]` (chiusi)
   - `docs/reports/*.md` — sezioni "Action Items", "Follow-up", "Next Steps" con checkbox
   - `company/product/specs/*.md` — domande aperte, prerequisiti, action items
   - `docs/reports/*cto-review*.md` — action items tecnici

2. **Per ogni follow-up aperto estrai**
   - Testo dell'azione
   - Owner (se indicato: @ceo, @cto, @pm, ecc.)
   - Deadline (se presente)
   - Fonte (file e sezione)

3. **Classifica in 4 bucket**

   | Bucket | Criteri |
   |--------|---------|
   | 🔴 **Scaduti** | Deadline passata, `[ ]` ancora aperto |
   | 🟠 **Prossimi 7 giorni** | Deadline nei prossimi 7 giorni |
   | 🟡 **Prossimi 30 giorni** | Deadline nei prossimi 8-30 giorni |
   | ⚪ **Senza scadenza** | Aperti ma senza deadline esplicita |

4. **Aggiungi sezione "Completati di recente"**
   - Follow-up con `[x]` chiusi negli ultimi 14 giorni
   - Utile per tracciare momentum e celebrare chiusure

5. **Aggiungi sezione "Senza owner"**
   - Follow-up aperti dove l'owner non è specificato
   - Questi richiedono assegnazione prima di poter essere tracked

6. **Struttura del documento**

   ```
   ## Follow-up Tracker — {data}

   ### 🔴 Scaduti ({N} item)
   | Azione | Owner | Scadenza | Fonte |

   ### 🟠 Prossimi 7 giorni ({N} item)
   | Azione | Owner | Scadenza | Fonte |

   ### 🟡 Prossimi 30 giorni ({N} item)
   | Azione | Owner | Scadenza | Fonte |

   ### ⚪ Senza scadenza ({N} item)
   | Azione | Owner | Fonte |

   ### ✅ Completati di recente
   | Azione | Owner | Data chiusura |

   ### ⚠️ Senza owner ({N} item)
   | Azione | Fonte | Azione richiesta |

   ### Raccomandazioni
   [cosa fare con gli item scaduti, chi contattare, escalation suggerite]
   ```

## Output
Salva in: `docs/reports/follow-ups-{YYYY-MM-DD}.md`
Commit: `[cos] report: follow-up tracker {YYYY-MM-DD}`
