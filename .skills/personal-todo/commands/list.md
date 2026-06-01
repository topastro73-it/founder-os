# Command: personal list

## Trigger
`/personal list`
`/personal` (senza argomenti)

## Processo

1. **Leggi** `personal/todo.md`
2. **Conta** i task aperti per sezione (`- [ ]`) e completati (`- [x]`)
3. **Mostra** il contenuto formattato:

```
📋 Personal Todo — {YYYY-MM-DD}

🔥 Oggi ({N} task)
  • [ ] Task A
  • [ ] Task B

📅 Questa settimana ({N} task)
  • [ ] Task C

🗂 In lista ({N} task)
  • [ ] Task D

✅ Fatto di recente ({N} task)
  • [x] Task E (completato)
```

4. Se una sezione è vuota, mostrala comunque con `(nessun task)`
5. Se il file è completamente vuoto o non esiste, mostra:
   ```
   📋 Personal Todo — vuota. Aggiungi con: /personal add "task" [oggi|settimana|lista]
   ```

## Output

Solo visualizzazione — nessuna modifica al file, nessun commit.
