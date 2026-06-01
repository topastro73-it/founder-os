# Command: priorities

## Trigger
`/routine priorities` oppure "Quali sono le mie priorita oggi?"

## Processo

1. **Carica contesto rapido**
   - `company/ceo-routine.md` — focus settimanale
   - `company/ceo-cadence.md` — ultimo log
   - `company/product/specs/INDEX.md` — spec in attesa
   - `decisions/` — decisioni aperte

2. **Calcola le 3 priorita** secondo la logica definita in AGENT.md:
   1. Decisioni bloccanti
   2. Follow-up scaduti
   3. Dati mancanti
   4. Scadenze questa settimana
   5. OKR a rischio
   6. Opportunita con finestra

3. **Output**

```
LE TUE 3 PRIORITA — {data}

1. [Priorita] — perche: [motivo] — azione: [cosa fare]
2. [Priorita] — perche: [motivo] — azione: [cosa fare]
3. [Priorita] — perche: [motivo] — azione: [cosa fare]

Cosa vuoi affrontare per primo?
```

## Output
Interazione diretta — nessun file generato.
