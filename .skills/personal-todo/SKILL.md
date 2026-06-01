# Skill: Personal Todo

## Identity

Gestione della to-do list personale del CEO, separata dal backlog business.
Skill operativa leggera: nessuna integrazione esterna, solo lettura/scrittura di `personal/todo.md`.

---

## Storage

**File principale**: `personal/todo.md`

### Struttura del file

```markdown
# Personal Todo

_Last updated: YYYY-MM-DD_

## 🔥 Oggi
- [ ] Task urgente

## 📅 Questa settimana
- [ ] Task importante

## 🗂 In lista
- [ ] Idea / task non urgente

## ✅ Fatto di recente
- [x] Task completato
```

### Regole di gestione

- **`Oggi`**: si svuota al `/routine close` — i task non completati passano in `Questa settimana`
- **`Questa settimana`**: si riorganizza al `/personal review` ogni venerdì/lunedì
- **`Fatto di recente`**: si pulisce dopo 7 giorni al weekly review
- **Deadline esplicita**: formato `- [ ] Task [📅 YYYY-MM-DD]`
- **Commit**: ogni modifica al todo viene committata con `[personal] add|done|move: descrizione`

---

## Comandi disponibili

| Comando | Invocazione | File |
|---------|-------------|------|
| `add` | `/personal add [testo] [oggi\|settimana\|lista]` | `commands/add.md` |
| `list` | `/personal list` | `commands/list.md` |
| `done` | `/personal done [testo o numero]` | `commands/done.md` |
| `review` | `/personal review` | `commands/review.md` |

---

## Integrazione CEO Routine

### `/routine start` — Morning Briefing
Leggi `personal/todo.md` e mostra solo la sezione `Oggi` nel briefing:
```
📋 Personal Today (N items):
• [ ] Task A
• [ ] Task B
```
Se `Oggi` è vuota, ometti il blocco silenziosamente.

### `/routine close` — Fine sessione
1. Mostra task `Oggi` non completati
2. Sposta automaticamente in `Questa settimana` (dopo conferma CEO)
3. Aggiorna `_Last updated` nel file
4. Il commit di chiusura include le modifiche a `personal/todo.md`

---

## Principi

- **Semplicità prima di tutto**: è un sostituto del Notepad, non un sistema di project management
- **Separazione netta**: i task personali non entrano mai in ClickUp o nel backlog business
- **Visibile ma non invasivo**: compare nel briefing solo se c'è qualcosa per oggi
- **Markdown puro**: leggibile in Obsidian, modificabile a mano, committabile, diffabile
