# Command: prioritize-backlog

## Trigger
`/pm prioritize-backlog` oppure "Prioritizza il backlog"

## Processo
0. **Spec Status Check** ← Regola globale 9 (CLAUDE.md)
   - Leggi `company/product/specs/INDEX.md` + frontmatter di ogni spec
   - Identifica spec stale e chiedi conferma al CEO prima di procedere
   - Aggiorna frontmatter e INDEX, poi continua
1. Carica `company/product/backlog.md`
2. Per ogni item, applica RICE scoring:
   - **Reach**: quanti clienti/utenti impattati (numero)
   - **Impact**: quanto migliora l'esperienza (3=Massive, 2=High, 1=Medium, 0.5=Low, 0.25=Minimal)
   - **Confidence**: quanto siamo sicuri delle stime (100%/80%/50%)
   - **Effort**: person-weeks stimati
   - **Score = (R × I × C) / E**
3. Applica Strategic Fit overlay per validazione
4. Proponi 3 tier: Must-do / Should-do / Nice-to-have
5. Identifica dipendenze e sequenza consigliata

## Output
Aggiorna: `company/product/backlog.md` con scoring e tier
Commit: `[pm] backlog: re-prioritized with RICE scoring`
