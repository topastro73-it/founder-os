# Skill: System Admin

## Identity

Gestione dell'architettura e della versionatura del sistema founder-os.
Questa skill traccia i cambiamenti al sistema (agenti, skill, regole, workflow), crea checkpoint ripristinabili via git tag, e permette rollback sicuri ai soli file di sistema.

---

## Componenti gestiti

**File di sistema** (tracciati da changelog e checkpoint):
```
CLAUDE.md
.agents/
.skills/
.workflows/
system/
```

**File di dati** (mai toccati dal rollback):
```
company/
docs/
decisions/
wiki/
personal/
inbox/
```

---

## Versioning scheme

| Tipo | Quando | Esempio |
|------|--------|---------|
| MAJOR (x.0.0) | Breaking change: agent rimosso, regola incompatibile, ristrutturazione sistema | v2.0.0 |
| MINOR (1.x.0) | Nuova funzionalità: nuovo agent, nuova skill, nuova regola, nuovo workflow | v1.2.0 |
| PATCH (1.0.x) | Fix/aggiornamento minore: correzione command, typo in regola critica | v1.1.1 |

**Leggi la versione corrente** dal tag git più recente:
```bash
git tag --sort=-v:refname | grep "^v" | head -1
```

**Incrementa** la versione in base al tipo di cambiamento.

---

## Comandi disponibili

| Comando | Invocazione | File |
|---------|-------------|------|
| `changelog` | `/system changelog` | `commands/changelog.md` |
| `checkpoint` | `/system checkpoint` | `commands/checkpoint.md` |
| `rollback` | `/system rollback <versione>` | `commands/rollback.md` |

---

## Regola di aggiornamento automatico

**Ogni volta che un agente modifica file di sistema** (agents, skills, CLAUDE.md, workflows), deve:

1. Aggiungere una entry in `system/CHANGELOG.md` — anche per change minori
2. Se il cambiamento è significativo (MINOR o MAJOR), suggerire `/system checkpoint` al CEO

Il changelog si aggiorna **nello stesso commit** della modifica — non dopo.

Tipi di cambio che richiedono entry:
- Nuova skill o agente creato
- Comando nuovo o rimosso da un agente/skill esistente
- Regola aggiunta/modificata/rimossa in `CLAUDE.md`
- Nuovo workflow in `.workflows/`
- Cambio di comportamento documentato (es. integrazione nuova nella routine)
