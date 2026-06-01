# Command: personal done

## Trigger
`/personal done [testo parziale o numero di riga]`

Esempi:
- `/personal done "dentista"` ← match parziale sul testo
- `/personal done 2` ← secondo task nella lista (ordine di apparizione)
- `/personal done tutto oggi` ← marca tutti i task di Oggi come completati

## Processo

1. **Leggi** `personal/todo.md`
2. **Trova** il task da completare:
   - Se argomento numerico → prendi il task in posizione N (contando solo `- [ ]` aperti)
   - Se testo → cerca match parziale case-insensitive nei task aperti
   - Se `tutto oggi` → seleziona tutti i `- [ ]` nella sezione `## 🔥 Oggi`
   - Se match ambiguo (più task corrispondono) → chiedi conferma mostrando le opzioni
3. **Sposta** il task:
   - Cambia `- [ ]` in `- [x]`
   - Rimuovilo dalla sezione corrente
   - Aggiungilo in fondo alla sezione `## ✅ Fatto di recente`
4. **Aggiorna** `_Last updated: YYYY-MM-DD_`
5. **Salva** e **committa**:
   ```
   [personal] done: {testo task breve}
   ```

## Output

```
✅ Fatto: "{testo task}"
   Spostato in → Fatto di recente
```

Se nessun task trovato:
```
⚠️ Nessun task trovato con "{argomento}". Usa /personal list per vedere i task aperti.
```
