# Command: setup

## Trigger
`/setup` · `/onboarding setup` · oppure proposto dal CEO Routine Agent quando il sistema non è inizializzato.

## Obiettivo
Portare il founder da repo vuoto a sistema configurato, un passo alla volta. Al termine il sistema
"conosce" l'azienda e gli agenti possono lavorare con contesto reale.

## Regole di conduzione
- **Una domanda alla volta.** Attendi la risposta prima di procedere.
- Dopo ogni step: **scrivi il file** sostituendo i `{{PLACEHOLDER}}`, mostra un riepilogo di 1-2 righe, **committa** (`[onboarding] setup: <step-name>`), poi passa allo step successivo.
- Accetta sempre **"salta"** → lascia i `{{...}}` e segna lo step come da completare.
- Se un file ha ancora `{{...}}` dopo il setup, va bene: il founder può rilanciare `/setup` per finirlo.
- Lingua: rispondi nella lingua del founder (default italiano).

## Step 0 — Benvenuto & rilevamento macchina
1. Saluta brevemente e spiega che farai ~10 domande per configurare il sistema (5 min).
2. Rileva la macchina: `scutil --get LocalHostName`. Registra nome/host/model in `company/config/machines.md` (sostituisci i `{{...}}`). Model ID: `sysctl -n hw.model`. RAM: opzionale.
3. Chiedi il **nome del founder** → userai questo per `{{FOUNDER_NAME}}`/`{{CEO_NAME}}`.

## Step 1 — Identità azienda → `.agents/_shared/COMPANY.md`
Chiedi in sequenza (una alla volta), poi compila il file:
- Nome azienda → `{{COMPANY_NAME}}`
- One-liner (cosa fate, in una frase) → `{{ONE_LINER}}`
- Mission (perché esistete) → `{{MISSION}}`
- Cosa vende il prodotto / per chi / problema risolto → `{{PRODUCT_*}}`
- Modello di business + pricing tiers → `{{BUSINESS_MODEL}}`, `{{TIER_*}}`
- Stage (pre-seed/seed/...) + MRR/ARR attuale → `{{STAGE}}`, `{{CURRENT_REVENUE}}`
Lascia vuote (o "salta") le sezioni Dati Legali/Funding se il founder non vuole inserirle ora (🔴 RESTRICTED).

## Step 2 — Team → `.agents/_shared/TEAM.md`
- Founder/CEO già noto (Step 0).
- Chiedi se ci sono altre persone nel team (nome + ruolo). Aggiungi una riga per persona.
- Spiega che gli agenti AI coprono i ruoli non ancora assunti.

## Step 3 — Glossario / termini custom → `.agents/_shared/GLOSSARY.md`
- Chiedi se l'azienda usa termini propri (nome del modello, come chiamate clienti/segmenti, principi fondanti).
- Aggiungili nella sezione "Custom Terms". Se non ce ne sono, salta.

## Step 4 — Vision & strategia → `company/strategy/vision.md`
- North Star, vision 3-5 anni, posizionamento, scommesse strategiche attuali, anti-goal.

## Step 5 — Segmenti clienti → `company/customers/segments.md`
- ICP primario (chi, dimensione, ruolo buyer, pain, trigger), segmenti, anti-ICP.

## Step 6 — Roadmap & KPI iniziali → `company/product/roadmap.md` + `company/metrics/kpis.md`
- 1-3 iniziative "Now". KPI di partenza che il founder conosce (MRR, clienti, runway). Il resto resta `{{...}}` da aggiornare nelle routine.

## Step 7 — Cadenza CEO → `company/ceo-cadence.md` + `company/ceo-routine.md`
- Chiedi il ritmo preferito di routine: **giornaliero / settimanale / mensile**. Scrivilo in `{{CADENCE}}` (`ceo-routine.md`).
- Non toccare il "Log risposte recenti" (resta vuoto).

## Step 8 — Integrazioni → `.env`
- Spiega quali integrazioni opzionali esistono (ClickUp, Gmail, Fatture in Cloud) via `.mcp.json`.
- Chiedi quali vuole collegare ora. Per ognuna: guida a copiare `.env.example` → `.env` e dove prendere le chiavi (i link sono nei commenti di `.env.example`).
- **NON** committare mai `.env` (è in `.gitignore`). Se il founder non vuole integrazioni ora, salta: il sistema funziona comunque coi file locali (MCP Graceful Degradation, `CLAUDE.md` §14).

## Step 9 — Principi (opzionale) → `.agents/_shared/PRINCIPLES.md`
- I principi di default sono già generici e validi. Chiedi solo se vuole aggiungere un principio fondante proprio (es. "Customer Backward"). Se no, salta.

## Step 10 — Finalizzazione
1. Crea il marker file `.founder-os-initialized` con data e nome founder:
   ```
   initialized: YYYY-MM-DD
   founder: {{FOUNDER_NAME}}
   founder-os-version: 1.0.0
   ```
2. Esegui un check: `grep -rl "{{" .agents/_shared company/strategy/vision.md company/customers/segments.md` → elenca al founder i file con placeholder ancora da compilare ("potrai finirli con `/setup` quando vuoi").
3. Committa: `[onboarding] setup: complete`.
4. **Handoff**: "✅ Setup completo. Prova ora:
   - `/routine start` → la tua prima sessione guidata
   - `/ceo` `/pm` `/sales` ... → invoca un agente
   - `examples/acme-demo/` → un esempio già compilato da cui prendere spunto"

## Note
- Se invocato su un sistema **già inizializzato**, chiedi se vuole (a) rivedere/aggiornare una sezione specifica, o (b) ricominciare da capo.
- Rispetta sempre i Privacy Tiers: i dati 🔴 RESTRICTED restano in `company/legal/` e `company/finance/`, mai nei briefing o nei commit message.
