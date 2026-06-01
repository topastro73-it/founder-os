# Command: system checkpoint

## Trigger
`/system checkpoint`
`/system checkpoint "descrizione opzionale"`

Crea un git tag sulla versione corrente e la registra come punto di ripristino sicuro.

## Processo

### Step 1 — Verifica repo pulito
```bash
git status --short
```
Se ci sono modifiche non committate, avvisa il CEO:
```
⚠️ Ci sono modifiche non committate. Committa prima di creare il checkpoint.
   File non committati: {lista}
```
Non procedere finché il repo non è clean.

### Step 2 — Determina la versione
```bash
git tag --sort=-v:refname | grep "^v" | head -1
```
La versione del checkpoint è quella più recente nel changelog (`system/CHANGELOG.md`).
Se non esiste ancora un tag per quella versione, usala. Se esiste già, è un errore — il checkpoint è già stato creato.

### Step 3 — Crea il git tag

```bash
git tag -a v{VERSIONE} -m "checkpoint: v{VERSIONE} — {YYYY-MM-DD} — {descrizione}"
```

Esempio:
```bash
git tag -a v1.1.0 -m "checkpoint: v1.1.0 — 2026-05-06 — Personal todo system"
```

### Step 4 — Aggiorna il campo Git tag nel CHANGELOG

Nel file `system/CHANGELOG.md`, trova l'entry della versione appena taggata e aggiorna:
```
**Git tag**: `v{VERSIONE}` (commit `{SHA breve}`)
```

Ottieni il SHA breve con:
```bash
git rev-parse --short HEAD
```

### Step 5 — Committa l'aggiornamento del changelog
```bash
git add system/CHANGELOG.md
git commit -m "[system] checkpoint: v{VERSIONE} — {descrizione}"
```

### Step 6 — Push del tag (opzionale, chiedi al CEO)
```
🏷️ Checkpoint v{VERSIONE} creato localmente.
   SHA: {SHA breve}
   Push del tag al remote? [sì/no]
```
Se sì:
```bash
git push origin v{VERSIONE}
```

### Step 7 — Conferma finale
```
✅ Checkpoint v{VERSIONE} creato — {YYYY-MM-DD}
   SHA: {SHA breve}
   Tag: git tag | grep v{VERSIONE}

   Per ripristinare: /system rollback v{VERSIONE}
   Per vedere tutti i checkpoint: git tag --sort=-v:refname | grep "^v"
```

## Note

- I tag git sono **immutabili** — non si sovrascrivono
- Se vuoi "spostare" un tag (es. hai committato dopo averlo creato), cancella e ricrea:
  ```bash
  git tag -d v{VERSIONE}
  git tag -a v{VERSIONE} -m "checkpoint: ..."
  ```
  Ma fallo solo prima del push — dopo il push i tag sono pubblici
- Il checkpoint crea un punto sicuro **solo sui file di sistema** — i dati business non fanno parte del rollback (vedi `rollback.md`)
