# Command: system rollback

## Trigger
`/system rollback v{VERSIONE}`
`/system rollback list` — elenca i checkpoint disponibili

## Scopo

Ripristina i **soli file di sistema** a una versione precedente, senza toccare i dati business.

**File ripristinati** (sistema):
- `CLAUDE.md`
- `.agents/` (tutto il contenuto)
- `.skills/` (tutto il contenuto)
- `.workflows/` (tutto il contenuto)
- `system/learnings.md` (solo questo file — non il CHANGELOG)

**File preservati** (dati, mai toccati):
- `company/`
- `docs/`
- `decisions/`
- `wiki/`
- `personal/`
- `inbox/`
- `system/CHANGELOG.md` (il changelog resta sempre attuale)

---

## Processo

### Step 0 — `/system rollback list`

Se l'utente chiede la lista dei checkpoint disponibili:
```bash
git tag --sort=-v:refname | grep "^v"
```
Mostra con data e descrizione del tag:
```bash
git for-each-ref --sort=-creatordate --format='%(refname:short) | %(creatordate:short) | %(subject)' refs/tags | grep "^v"
```

Output formattato:
```
📋 Checkpoint disponibili:
  v1.1.0 | 2026-05-06 | Personal todo system
  v1.0.0 | 2026-05-01 | Sistema baseline
```

---

### Step 1 — Verifica esistenza del tag
```bash
git tag | grep "^v{VERSIONE}$"
```
Se non esiste:
```
⚠️ Checkpoint v{VERSIONE} non trovato.
   Checkpoint disponibili: /system rollback list
```
Fermati.

### Step 2 — Mostra il diff di sistema tra ora e il checkpoint

Mostra cosa cambierebbe nel rollback:
```bash
git diff v{VERSIONE}..HEAD -- CLAUDE.md .agents/ .skills/ .workflows/ system/learnings.md --stat
```

Output al CEO:
```
🔄 Rollback v{VERSIONE} — cosa cambierebbe:

File di sistema che verrebbero ripristinati:
{lista file modificati con +/- righe}

File aggiunti dopo v{VERSIONE} (verranno rimossi):
{lista nuovi file}

File eliminati dopo v{VERSIONE} (verranno ripristinati):
{lista file rimossi}

Dati business: INVARIATI (company/, docs/, decisions/, wiki/, personal/)
```

### Step 3 — Chiedi conferma esplicita

```
⚠️ ROLLBACK SISTEMA — Questa operazione è reversibile (il branch resta su HEAD).

Vuoi procedere con il rollback dei file di sistema a v{VERSIONE}?
Digita "confermo rollback v{VERSIONE}" per procedere.
```

**Non procedere** con nessun'altra risposta. Il rollback richiede conferma testuale esplicita.

### Step 4 — Crea un tag di sicurezza sulla versione attuale

Prima di fare qualsiasi cosa, preserva lo stato attuale:
```bash
git tag -a pre-rollback-$(date +%Y%m%d-%H%M) -m "pre-rollback snapshot before rolling back to v{VERSIONE}"
```

### Step 5 — Ripristina i file di sistema

```bash
git checkout v{VERSIONE} -- CLAUDE.md .agents/ .skills/ .workflows/ system/learnings.md
```

### Step 6 — Aggiungi una entry al CHANGELOG (NON ripristinato)

Il `system/CHANGELOG.md` resta sempre aggiornato. Aggiungi:

```markdown
## v{VERSIONE-CORRENTE+PATCH} — {YYYY-MM-DD}

### change | system rollback
**What**: Rollback del sistema a v{VERSIONE}
**Why**: {motivo fornito dal CEO, o "ripristino manuale richiesto"}
**Rolled back to**: v{VERSIONE} (commit {SHA del tag})
**Pre-rollback snapshot**: tag `pre-rollback-{timestamp}`
**Files**: CLAUDE.md, .agents/, .skills/, .workflows/, system/learnings.md
```

### Step 7 — Commit del rollback

```bash
git add CLAUDE.md .agents/ .skills/ .workflows/ system/learnings.md system/CHANGELOG.md
git commit -m "[system] rollback: v{VERSIONE-CORRENTE} → v{VERSIONE}"
```

### Step 8 — Conferma finale

```
✅ Rollback completato — {YYYY-MM-DD HH:MM}

Sistema ripristinato a: v{VERSIONE}
Snapshot pre-rollback: tag pre-rollback-{timestamp} (puoi tornare avanti con /system rollback pre-rollback-XXX)

File ripristinati:
  ✅ CLAUDE.md
  ✅ .agents/ ({N} file)
  ✅ .skills/ ({N} file)
  ✅ .workflows/ ({N} file)
  ✅ system/learnings.md

Invariati:
  🔒 company/, docs/, decisions/, wiki/, personal/

Changelog aggiornato: system/CHANGELOG.md → v{VERSIONE-CORRENTE+PATCH}
```

---

## Note di sicurezza

- Il rollback è sempre **reversibile** — il tag `pre-rollback-{timestamp}` ti permette di tornare avanti
- Il CHANGELOG non viene mai ripristinato — mantiene sempre la storia completa
- I dati business non vengono mai toccati
- Se hai dubbi su cosa farà il rollback, fermati allo Step 2 e leggi il diff
