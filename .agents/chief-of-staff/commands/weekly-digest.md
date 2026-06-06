# Command: weekly-digest

## Trigger
`/cos weekly-digest` oppure "Digest della settimana" oppure "Cosa ha fatto il team questa settimana?"

## Processo

1. **Scansiona l'attività della settimana**
   - `git log --since="7 days ago"` — tutti i commit, raggruppati per agente
   - Per ogni agente: quanti output, di che tipo, su quali topic
   - Nuovi file prodotti: specs, decisioni, report, content

2. **Output per agente**
   Per ciascuno dei 6 agenti (CEO, PM, CTO, Marketing, Sales, CoS):
   - Cosa ha prodotto questa settimana (file, decisioni)
   - Handoff inviati / ricevuti
   - Item aperti rimasti in carico
   - Gap: nessuna attività registrata = segnala

3. **Decisioni della settimana**
   - Lista le decisioni create con: ID, titolo, stato, data review
   - Evidenzia decisioni che hanno generato follow-up non ancora assegnati

4. **Follow-up scaduti questa settimana**
   - Scansiona `decisions/` per `[ ]` con deadline nella settimana passata
   - Per ognuno: cosa era previsto, chi era owner, non fatto → escalation?

5. **Spec Status Check**
   - Leggi `company/product/specs/INDEX.md` e controlla `last-updated` di ogni spec
   - Identifica spec con stato stale secondo soglie: `draft` >7gg, `evaluated` >14gg, `approved` >14gg, `in-development` >30gg
   - Includi nel digest la sezione:

   ```
   ## 📋 Spec che richiedono aggiornamento stato

   Le seguenti spec non vengono aggiornate da più di N giorni:

   | Spec | Stato | Ultimo aggiornamento | Giorni senza update |
   |------|-------|---------------------|-------------------|
   ```

   Se non ci sono spec stale, ometti la sezione.

6. **Pipeline — health & aging settimanale** (live da `company/customers/opportunities/*.md`, skill `.skills/opportunity-management/SKILL.md`)
   - Coverage weighted vs target, distribuzione per stage e per segmento, movimenti di stage della settimana.
   - Top trattative bloccate/aging (🔴🟠) con giorni fermi e blocco; opportunità senza owner.
   - Suggerisci `/sales board` se `PIPELINE.md` è stale.

7. **Outlook settimana prossima**
   - Follow-up con scadenza nei prossimi 7 giorni
   - Epic o milestone previsti per la settimana
   - Riunioni o review programmate (se tracciate nel repo)

6. **Struttura del documento**

   ```
   ## Weekly Digest — settimana del {data inizio} al {data fine}

   ### Output per agente
   [tabella o sezioni per agente]

   ### Pipeline — health & aging
   [coverage vs target, movimenti stage, top bloccati/aging, opportunità senza owner]

   ### Decisioni prese
   [lista con stato]

   ### Follow-up scaduti (non completati)
   [lista con owner e azione richiesta]

   ### Follow-up completati
   [breve lista — cosa è stato chiuso]

   ### Outlook settimana prossima
   [scadenze, milestone, priorità]
   ```

## Output
Salva in: `docs/reports/weekly-digest-{YYYY-MM-DD}.md` (data = lunedì della settimana corrente)
Commit: `[cos] digest: weekly {YYYY-MM-DD}`
