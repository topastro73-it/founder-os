# Command: decision-review

## Trigger
`/cos decision-review` oppure "Audit delle decisioni" oppure "Quali decisioni vanno rivalutate?"

## Processo

1. **Carica tutte le decisioni**
   - Scansiona `decisions/*.md` — ogni file è una decisione
   - Per ogni decisione estrai:
     - ID e titolo
     - Data
     - Agente che ha deciso
     - Stato (Approvata, Pendente, Superata)
     - Review Date
     - Follow-up: lista `[ ]` aperti e `[x]` chiusi
     - Conseguenze dichiarate

2. **Classifica le decisioni in 4 categorie**

   | Categoria | Criteri |
   |-----------|---------|
   | 🔴 **Review date passata** | `Review Date` < oggi e non risulta revisione fatta |
   | 🟠 **Follow-up scaduti** | Almeno un `[ ]` con deadline passata |
   | 🟡 **Follow-up incompleti** | Almeno un `[ ]` ancora aperto (non scaduto) |
   | 🟢 **In ordine** | Review date futura, tutti i follow-up `[x]` o in corso |

3. **Per ogni decisione da rivalutare**
   - Cosa era stato deciso
   - Cosa è cambiato nel contesto (nuovo dato, nuovo agente, nuova situazione)
   - Raccomandazione: confermare, modificare, o superare con nuova decisione

4. **Identifica decisioni implicite (non formalizzate)**
   - Scansiona `docs/reports/` per frasi del tipo "abbiamo deciso", "si è scelto", "da fare"
   - Se una decisione rilevante non è in `decisions/`, segnalala come "da formalizzare"

5. **Struttura del documento**

   ```
   ## Decision Review — {data}

   ### 🔴 Review date passata
   | ID | Titolo | Review Date | Stato | Azione richiesta |

   ### 🟠 Follow-up scaduti
   | ID | Titolo | Follow-up scaduto | Owner | Azione richiesta |

   ### 🟡 Follow-up ancora aperti
   | ID | Titolo | Follow-up aperti | Owner | Deadline |

   ### 🟢 Decisioni in ordine
   | ID | Titolo | Prossima review |

   ### Decisioni implicite da formalizzare
   [lista con fonte e raccomandazione]

   ### Raccomandazioni
   [cosa fare immediatamente, chi coinvolgere]
   ```

## Output
Salva in: `docs/reports/decision-review-{YYYY-MM-DD}.md`
Commit: `[cos] report: decision review {YYYY-MM-DD}`
