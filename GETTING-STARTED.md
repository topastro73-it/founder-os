# Getting Started with founder-os

A deeper guide than the README. ~10 minutes. Bilingual: English first, Italiano sotto.

---

## 🇬🇧 English

### 1. Prerequisites
- [Claude Code](https://claude.com/claude-code) (CLI, desktop app, or IDE extension).
- Git. (Optional: a private GitHub repo if you want multi-machine sync.)

### 2. Initialize your company
Open the repo in Claude Code and run:
```
/setup
```
The **Onboarding Agent** walks you through 10 steps and writes your data into:
- `.agents/_shared/COMPANY.md` — identity, product, pricing, ICP
- `.agents/_shared/TEAM.md` — who does what
- `company/strategy/vision.md`, `company/customers/segments.md`
- `company/product/roadmap.md`, `company/metrics/kpis.md`
- `company/ceo-cadence.md` — your routine rhythm
- `company/config/machines.md` — auto-detected

You can stop and resume anytime — re-run `/setup` and it picks up the unfilled `{{placeholders}}`.

> Prefer to type it yourself? Edit `.agents/_shared/COMPANY.md` directly. Placeholders look like `{{COMPANY_NAME}}`.

### 3. Daily use
| You want to… | Run |
|--------------|-----|
| Start a guided session | `/routine start` |
| Close & commit the session | `/routine close` (or `/close`) |
| Write a product spec | `/pm write-spec` |
| Review the pipeline | `/sales pipeline-review` |
| Make an architecture decision | `/cto tech-decision` |
| Draft an investor update | `/ceo investor-update` |
| See the full list | open `.agents/AGENTS.md` |

### 4. The model
- **Agents** (`.agents/`) are roles. Invoking one makes Claude *become* that role.
- **Skills** (`.skills/`) are reusable competencies agents pull in.
- **company/** is your living state. **decisions/** is an immutable decision log. **docs/** holds generated artifacts. **wiki/** is narrative memory.
- Every rule the system follows is in `CLAUDE.md`.

### 5. Optional integrations
`founder-os` works fully offline with local files. To connect tools (ClickUp, Gmail, Fatture in Cloud), copy `.env.example` → `.env`, fill in your keys, and configure `.mcp.json`. If an integration isn't available, agents degrade gracefully and use local files.

### 6. Privacy
The system has built-in **privacy tiers** (`CLAUDE.md` §20-23). Restricted data (contracts, cap table, VAT IDs) stays in `company/legal/` and `company/finance/` and never lands in commit messages, the wiki, or public docs. Never commit `.env`.

---

## 🇮🇹 Italiano

### 1. Prerequisiti
- [Claude Code](https://claude.com/claude-code). Git. (Opzionale: repo GitHub privato per il sync multi-macchina.)

### 2. Inizializza la tua azienda
Apri il repo in Claude Code e lancia:
```
/setup
```
L'**Onboarding Agent** ti guida in 10 step e scrive i tuoi dati in `.agents/_shared/` e `company/`.
Puoi interrompere e riprendere quando vuoi: rilancia `/setup` e riparte dai `{{placeholder}}` non compilati.

> Preferisci scrivere a mano? Modifica `.agents/_shared/COMPANY.md`. I placeholder sono tipo `{{COMPANY_NAME}}`.

### 3. Uso quotidiano
| Vuoi… | Comando |
|-------|---------|
| Iniziare una sessione guidata | `/routine start` |
| Chiudere e committare | `/routine close` (o `/close`) |
| Scrivere una spec | `/pm write-spec` |
| Rivedere la pipeline | `/sales pipeline-review` |
| Decisione tecnica | `/cto tech-decision` |
| Update investitori | `/ceo investor-update` |
| Lista completa | apri `.agents/AGENTS.md` |

### 4. Il modello
- Gli **agenti** sono ruoli: invocarne uno fa "diventare" Claude quel ruolo.
- Le **skill** sono competenze riutilizzabili.
- `company/` è lo stato vivo; `decisions/` il log immutabile; `docs/` gli output; `wiki/` la memoria narrativa.
- Tutte le regole sono in `CLAUDE.md`.

### 5. Integrazioni opzionali
Funziona anche tutto offline. Per collegare strumenti, copia `.env.example` → `.env` e configura `.mcp.json`. Mai committare `.env`.

### 6. Privacy
Tier di privacy integrati (`CLAUDE.md` §20-23): i dati 🔴 RESTRICTED restano in `company/legal/` e `company/finance/`, mai nei commit o nel wiki.
