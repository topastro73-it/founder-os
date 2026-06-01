# Command: personal add

## Trigger
`/personal add [testo del task] [oggi|settimana|lista]`

Esempi:
- `/personal add "Chiamare dentista" oggi`
- `/personal add "Rinnovare passaporto" settimana`
- `/personal add "Leggere libro X"` ← default: lista

## Processo

1. **Leggi** `personal/todo.md` per caricare il contenuto attuale
2. **Determina la sezione** di destinazione:
   - `oggi` → `## 🔥 Oggi`
   - `settimana` → `## 📅 Questa settimana`
   - `lista` (default, se non specificato) → `## 🗂 In lista`
3. **Aggiungi** il task come nuova riga `- [ ] {testo}` nella sezione corretta
   - Se l'utente ha specificato una deadline, usa il formato: `- [ ] {testo} [📅 YYYY-MM-DD]`
4. **Aggiorna** la riga `_Last updated: YYYY-MM-DD_` con la data odierna
5. **Salva** `personal/todo.md`
6. **Committa**:
   ```
   [personal] add: {testo task breve}
   ```

## Output

Conferma breve:
```
✅ Aggiunto in {sezione}: "{testo del task}"
```

Nessuna altra elaborazione — semplicità è la priorità.
