# Command: process-signals

**Invocazione**: `/routine process-signals`
**Agente**: CEO Routine
**Scopo**: Converte i file grezzi in `docs/intelligence/inbox/` in segnali strutturati con frontmatter, pronti per il briefing e il RAG.

---

## Flusso

### Step 1 — Scansiona inbox

Leggi il contenuto di `docs/intelligence/inbox/`. Se vuoto (o solo `.gitkeep`), rispondi:

> 📭 Nessun file in inbox. Droppа i tuoi export da Gemini o Perplexity in `docs/intelligence/inbox/` e riprova.

### Step 2 — Per ogni file trovato

Per ciascun file (`.md`, `.txt`, `.pdf`, o altro):

1. **Leggi il contenuto** del file
2. **Estrai automaticamente** (se deducibile dal testo):
   - `source`: `gemini` o `perplexity` (dal nome file o dal contenuto)
   - `category`: `market-news`, `competitor`, o `mixed`
   - `date`: data dell'output (dal testo o dalla data di modifica del file)
   - `title`: titolo sintetico (max 8 parole)
   - `tags`: 3-5 tag rilevanti dal contenuto (es. market-trend, product-launch, pricing, competitor)
   - `entities.competitors`: competitor menzionati
   - `entities.frameworks`: framework o standard menzionati (es. ISO 27001, GDPR, SOC 2)

3. **Se non deducibile**, chiedi al CEO in un'unica domanda:
   > ⚙️ Per il file `{filename}`:
   > - Source (gemini / perplexity)?
   > - Category (market-news / competitor / mixed)?
   > - Tag principali (3-5, separati da virgola)?

4. **Genera il file strutturato** in `docs/intelligence/signals/`:

**Filename**: `{YYYY-MM-DD}-{source}-{slug}.md`
dove `{slug}` è il titolo in kebab-case (max 5 parole).

**Formato**:
```markdown
---
type: intelligence
source: gemini | perplexity
category: market-news | competitor | mixed
date: YYYY-MM-DD
title: "{titolo sintetico}"
tags: [tag1, tag2, tag3]
status: new
entities:
  competitors: []
  frameworks: []
---

# {Titolo}

{Corpo del segnale — mantieni il testo originale dell'export, eventualmente riassunto se >1000 parole}

---
*Fonte: {source} — {data}*
```

5. **Sposta il file originale** in `docs/intelligence/inbox/processed/` (crea la cartella se non esiste)

### Step 3 — Aggiorna index.md

Aggiungi una riga nella tabella di `docs/intelligence/index.md`:

```
| {YYYY-MM-DD} | {source} | {category} | [{titolo}](signals/{filename}.md) | new |
```

Rimuovi la riga placeholder `| — | — | — | Nessun segnale ancora | — |` se presente.

### Step 4 — Summary

Mostra al CEO:

> ✅ **{N} segnali processati**
>
> | File | Titolo | Source | Categoria |
> |------|--------|--------|-----------|
> | ... | ... | ... | ... |
>
> I segnali appariranno nel prossimo `/routine start` sotto "📡 Segnali dal mercato".

---

## Commit

```
[routine] intelligence: process {N} signals from inbox
```

---

## Note

- Il corpo del segnale va mantenuto in lingua originale dell'export (italiano o inglese)
- Se il file è un PDF, estrai il testo disponibile; se non leggibile, chiedi al CEO di esportarlo come testo
- Non inventare informazioni non presenti nel file originale
- I segnali con `status: new` vengono mostrati nel briefing di `/routine start`
- Dopo la review del CEO in `/routine close`, lo status viene aggiornato a `reviewed`
