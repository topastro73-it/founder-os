# System Changelog Protocol

Ogni volta che un agente modifica file di sistema (`.agents/`, `.skills/`, `.workflows/`, `CLAUDE.md`, `system/protocols/`), deve aggiungere una entry in `system/CHANGELOG.md` **nello stesso commit** della modifica.

## Cosa tracciare

- Nuova skill o agente creato → `feat`
- Behavior modificato in agente/skill esistente → `change`
- Correzione a un comando o regola → `fix`
- Agent/skill rimossa o regola incompatibile → `breaking`
- Riorganizzazione strutturale senza cambio di comportamento → `refactor`

## Versioning

- Incrementa **MINOR** per `feat`
- Incrementa **PATCH** per `change` / `fix` / `refactor`
- Incrementa **MAJOR** per `breaking`

Leggi la versione corrente da `git tag --sort=-v:refname | grep "^v" | head -1`.

## Checkpoint

Dopo cambiamenti MINOR o MAJOR, suggerisci al CEO `/system checkpoint` per creare il git tag corrispondente.

## Rollback

`/system rollback <versione>` ripristina SOLO `.agents/`, `.skills/`, `.workflows/`, `CLAUDE.md`, `system/learnings.md`, `system/protocols/` — mai i dati business.

Vedi `.skills/system-admin/SKILL.md` per il dettaglio completo.
