# Command: personal review

## Trigger
`/personal review`

Eseguito tipicamente ogni venerdì (fine settimana) o lunedì (inizio settimana).
Può essere chiamato manualmente in qualsiasi momento.

## Processo

### Step 1 — Leggi lo stato attuale
Leggi `personal/todo.md` e conta task per sezione.

### Step 2 — Mostra il riepilogo

```
📋 Personal Review — {YYYY-MM-DD}

Stato attuale:
  🔥 Oggi:          {N} task aperti, {N} completati
  📅 Questa settimana: {N} task aperti, {N} completati
  🗂 In lista:      {N} task
  ✅ Fatto recente: {N} task (completati negli ultimi 7gg)
```

### Step 3 — Proponi azioni

**A. Oggi → Questa settimana** (se ci sono task non completati in `Oggi`):
```
🔄 Task non completati oggi ({N}):
  • "{task 1}"
  • "{task 2}"
  → Sposto in "Questa settimana"? [sì/no]
```

**B. Pulizia "Fatto di recente"** (task con data > 7 giorni fa):
```
🧹 Task completati da più di 7 giorni ({N}):
  • [x] "{task completato}"
  → Rimuovo dall'elenco? [sì/no]
```

**C. Prioritizzazione settimana prossima**:
```
📅 In lista ci sono {N} task. Vuoi promoverne qualcuno in "Questa settimana"?
  • "{task 1}"
  • "{task 2}"
  → Indica i numeri o "nessuno"
```

### Step 4 — Applica le modifiche confermate

Solo dopo risposta esplicita del CEO:
- Sposta i task indicati
- Rimuove i completati vecchi
- Aggiorna `_Last updated: YYYY-MM-DD_`
- Salva il file

### Step 5 — Committa

```
[personal] review: weekly cleanup {YYYY-MM-DD}
```

### Step 6 — Mostra il risultato finale

```
✅ Review completata:
  Spostati in settimana: {N} task
  Rimossi (vecchi): {N} task
  Nuovi in settimana: {N} task

Todo aggiornata → personal/todo.md
```
