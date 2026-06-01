# Command: system changelog

## Trigger
`/system changelog` — aggiunge una nuova entry al changelog dopo una modifica al sistema
`/system changelog add` — alias esplicito

## Processo

### Step 1 — Determina la versione corrente
```bash
git tag --sort=-v:refname | grep "^v" | head -1
```
Se non esistono tag `v*`, la versione corrente è `v1.0.0`.

### Step 2 — Determina il tipo di cambiamento
Chiedi al CEO (o inferisci dal contesto della sessione):

| Tipo | Quando usarlo |
|------|--------------|
| `feat` | Nuova skill, nuovo agente, nuovo workflow, nuova regola CLAUDE.md |
| `change` | Behavior modificato in agente/skill esistente |
| `fix` | Correzione a un comando, fix typo in regola critica |
| `breaking` | Agent/skill rimossa, regola incompatibile, ristrutturazione |
| `refactor` | Riorganizzazione strutturale senza cambio di comportamento |

### Step 3 — Calcola la nuova versione
| Tipo | Incremento | Esempio (da v1.1.0) |
|------|------------|---------------------|
| `breaking` | MAJOR | v2.0.0 |
| `feat` | MINOR | v1.2.0 |
| `change`, `fix`, `refactor` | PATCH | v1.1.1 |

### Step 4 — Scrivi la entry in `system/CHANGELOG.md`

Inserisci **sopra** l'entry precedente, subito dopo la riga `---` iniziale:

```markdown
## v{NUOVA_VERSIONE} — {YYYY-MM-DD}

### {tipo} | {componente}
**What**: {cosa è cambiato — specifico e conciso}
**Why**: {perché è stato fatto — il rationale, la cosa più importante}
**Files**:
- `{file1}` — {cosa fa}
- `{file2}` — {cosa fa}

**Git tag**: `v{NUOVA_VERSIONE}` (commit `{SHA breve}` — da aggiungere dopo il checkpoint)
```

### Step 5 — Suggerisci checkpoint

Dopo aver aggiunto l'entry, chiedi:
```
📋 Entry aggiunta al changelog: v{NUOVA_VERSIONE}
   Vuoi creare anche un checkpoint git? → /system checkpoint
```

## Note

- Aggiungi sempre la entry **nello stesso commit** che introduce il cambiamento
- Il campo `Git tag` inizialmente ha `(tag pending — esegui /system checkpoint)` se il checkpoint non è ancora stato creato
- Non creare una entry per ogni commit di obsidian o routine — solo per modifiche intenzionali al sistema
