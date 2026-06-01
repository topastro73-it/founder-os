# Content Library Skill

Catalogo centralizzato di tutti i contenuti prodotti dall'azienda. Trova, riusa, mantieni aggiornati i contenuti. Usata da Marketing, Sales, CEO, Chief of Staff.

## Principi

1. **Single source of truth**: ogni contenuto ha un path canonico nel repo
2. **Riuso > riscrittura**: adattare un contenuto esistente e sempre preferibile a crearne uno nuovo
3. **Freshness matters**: contenuto stale (>90 giorni senza update) e un liability, non un asset
4. **Per-partner view**: ogni partner dovrebbe avere contenuti personalizzati disponibili

---

## Mappa Contenuti

| Tipo | Path | Descrizione |
|------|------|-------------|
| Blog post | `docs/blog-posts/*.md` | Articoli per blog aziendale |
| Case study | `docs/marketing/case-study-*.md` | Casi d'uso e success story |
| One-pager | `docs/marketing/one-pager-*.md` | Schede prodotto sintetiche |
| Battlecard | `company/competitors/battlecards/*.md` | Analisi competitive |
| Proposal | `docs/proposals/*.md` | Proposte commerciali |
| Report | `docs/reports/*.md` | Report interni e per clienti |
| Investor update | `docs/investor-updates/*.md` | Materiale per investitori |
| Pitch deck | `docs/marketing/pitch-deck-*.md` | Presentazioni |
| Email template | `docs/marketing/email-template-*.md` | Template email |
| Social content | `docs/marketing/social-*.md` | Post LinkedIn, Twitter |
| Internal memo | `docs/internal-memos/*.md` | Comunicazioni interne |
| Release notes | `docs/release-notes/*.md` | Note di rilascio prodotto |

---

## Comandi

| Comando | Descrizione | Output |
|---------|------------|--------|
| `index` | Scansiona tutto il repo e genera indice contenuti | `docs/marketing/content-index.md` |
| `find` | Cerca contenuti per query (keyword, tipo, partner, data) | Lista risultati |
| `audit` | Analisi gap e freshness di tutti i contenuti | Report audit |
| `reuse` | Adatta contenuto esistente per nuovo contesto/partner | Nuovo file adattato |

---

## Comando: index

### Processo

1. Scansiona le seguenti directory:
   - `docs/marketing/`
   - `docs/blog-posts/`
   - `docs/proposals/`
   - `docs/reports/`
   - `docs/investor-updates/`
   - `docs/internal-memos/`
   - `docs/release-notes/`
   - `company/competitors/battlecards/`
2. Per ogni file trovato, estrai:
   - Titolo (prima riga `# ...` o nome file)
   - Tipo (dalla directory)
   - Data ultimo aggiornamento (git log o frontmatter)
   - Tag/keyword (dal frontmatter se presente, altrimenti inferiti dal contenuto)
   - Partner associato (se nel nome file o nel contenuto)
3. Genera indice strutturato per tipo e per partner
4. Salva in `docs/marketing/content-index.md`

### Output format
```markdown
# Content Index — {{COMPANY_NAME}}

> Generato automaticamente. Ultimo aggiornamento: {data}

## Per tipo

### Blog Posts ({N})
| Titolo | Data | Tag | Partner |
|--------|------|-----|---------|
| {titolo} | {data} | {tag} | {partner o —} |

### Case Study ({N})
...

### Battlecards ({N})
...

### Proposals ({N})
...

[etc.]

## Per partner

### {Nome Partner}
| Contenuto | Tipo | Data | Freshness |
|-----------|------|------|-----------|
| {titolo} | case-study | 2026-01-15 | ✅ Fresh / ⚠️ Stale |

### Contenuti generici (non partner-specific)
| Contenuto | Tipo | Data | Freshness |
|-----------|------|------|-----------|
```

Commit: `[cos] content: updated content index`

### Integrazione weekly-digest
Il Chief of Staff esegue `index` come parte del `weekly-digest`, aggiornando l'indice ad ogni digest settimanale.

---

## Comando: find

### Input
- Query di ricerca (keyword, es. "categoria-prodotto", "Partner X", "battlecard competitor")
- Filtri opzionali: tipo, partner, data range

### Processo
1. Leggi `docs/marketing/content-index.md` per ricerca rapida
2. Se serve piu dettaglio, scansiona i file effettivi con grep
3. Restituisci lista ordinata per rilevanza

### Output
```
## Content Search: "{query}"

Trovati {N} risultati:

| # | Titolo | Tipo | Path | Data | Rilevanza |
|---|--------|------|------|------|-----------|
| 1 | {titolo} | blog-post | {path} | {data} | Alta |
| 2 | {titolo} | battlecard | {path} | {data} | Media |
```

---

## Comando: audit

### Processo
1. Esegui `index` per avere la mappa completa
2. Per ogni partner attivo (da `company/customers/partners/*.md`):
   - Verifica quali tipi di contenuto esistono
   - Identifica gap (es. partner senza case study, senza proposal)
3. Per tutti i contenuti:
   - Freshness check: ultimo aggiornamento > 90 giorni = **stale**
   - Freshness check: ultimo aggiornamento > 180 giorni = **expired**
4. Identifica contenuti riutilizzabili per nuovi partner

### Output format
```
## Content Audit — {data}

### Summary
- Contenuti totali: {N}
- Fresh (<90gg): {N} ({%})
- Stale (90-180gg): {N} ({%})
- Expired (>180gg): {N} ({%})

### Gap per partner
| Partner | Case Study | Proposal | One-pager | Battlecard | Score |
|---------|-----------|----------|-----------|------------|-------|
| Partner A | ✅ | ✅ | ❌ | ✅ | 3/4 |
| Partner B | ❌ | ❌ | ❌ | ✅ | 1/4 |

### Contenuti stale (da aggiornare)
| Contenuto | Tipo | Ultimo update | Giorni | Azione |
|-----------|------|--------------|--------|--------|
| battlecard-competitor-x.md | battlecard | 2025-12-01 | 110gg | Aggiornare con dati Q1 |

### Contenuti riutilizzabili
| Contenuto originale | Adattabile per | Effort stimato |
|--------------------|---------------|---------------|
| case-study-partner-x.md | segmento verticale | Basso (cambiare nomi e numeri) |

### Raccomandazioni
1. {Azione con owner e priorita}
```

Salva in: `docs/reports/content-audit-{YYYY-MM-DD}.md`
Commit: `[marketing] audit: content library audit`

---

## Comando: reuse

### Input
- Path del contenuto originale
- Nuovo contesto (partner, segmento, evento)

### Processo
1. Leggi il contenuto originale
2. Identifica le sezioni da adattare:
   - Nomi e riferimenti specifici
   - Metriche e numeri
   - Value proposition (potrebbe variare per segmento)
   - CTA e contatti
3. Genera versione adattata
4. Salva come nuovo file con riferimento all'originale

### Output
Nuovo file nella directory appropriata con nota:
```
<!-- Adattato da: {path originale} | Data: {data} -->
```

Commit: `[marketing] content: adapted {tipo} for {contesto}`

---

## Dove vivono i dati

| Dato | Path |
|------|------|
| Content index | `docs/marketing/content-index.md` |
| Content audit | `docs/reports/content-audit-*.md` |
| Tutti i contenuti | Vedi mappa contenuti sopra |
