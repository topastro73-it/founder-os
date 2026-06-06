<!--
TARGET FUNNEL — tracker consolidato del prospecting su un segmento/canale.
Pattern complementare al cockpit: il cockpit (PIPELINE.md) mostra le OPPORTUNITÀ qualificate;
questo file consolida l'intero FUNNEL di un canale (universo target → contattati → qualificati),
fondendo fonti sparse (CRM export, log chiamate, liste). Vedi playbook in fondo.
Tier: 🟡 INTERNAL. Un file per canale/segmento (rinomina, es. smb-funnel.md, channel-funnel.md).
-->

# 🗂️ Target Funnel — {nome canale/segmento}

> Consolidato il {YYYY-MM-DD} da: {fonti, es. export CRM, log attività, lista target}.
> Universo target: **{N}** · contattati: **{N}** · in questo tracker (attivi + warm): **{N}**.

**Legenda**: ✅ Won · 🟢 Attivo (deal/demo, interesse reale) · 🟡 Warm/nurture (callback datato o interesse).
I freddi e i non-interessati vanno nel footer (memoria anti-ricontatto), non nel corpo.

---

## ✅ WON — contratti attivi

| Account | Owner | Deal | Valore/MRR | Note |
|---------|-------|------|-----------|------|
| {Account} | {owner} | [{opp-slug}](opportunities/{opp-slug}.md) | € — | — |

## 🟢 ATTIVI — promossi al cockpit (deal in `opportunities/`)

| Account | Owner | Deal | Stage / € | Prossima azione |
|---------|-------|------|-----------|-----------------|
| {Account} | {owner} | [{opp-slug}](opportunities/{opp-slug}.md) | {stage} · € — | {next step} |

## 🟢 ATTIVI — qualificati (no deal formale ancora)

| Account | Owner | Ultima att. | Prossima azione |
|---------|-------|-------------|-----------------|
| {Account} | {owner} | YYYY-MM-DD | {next step} |

## 🟡 WARM / NURTURE — callback datato o interesse

| Account | Owner | Ultima att. | Prossima azione / quando |
|---------|-------|-------------|--------------------------|
| {Account} | {owner} | YYYY-MM-DD | {es. richiamare a settembre} |

---

## ⚪ Footer memoria — NON ricontattare a freddo

*Registrati per non sprecare cicli. Ricontattare solo con nuovo trigger.*

**Non interessati / chiuso**: {lista nomi}.
**Cold / canale chiuso (numero inesistente, nessuna risposta)**: {lista nomi}.

---

## 📋 Playbook — come consolidare un funnel da fonti sparse

1. **Raccogli le fonti**: export CRM (deal con stage/importo/note), log attività (chiamate/email), lista target.
2. **Join per nome account** (normalizza: rimuovi `srl/spa/inc`, minuscole). Spesso l'overlap tra fonti è basso → è proprio per questo che servono consolidate.
3. **Classifica** ogni account: Won / Attivo / Warm (callback datato) / Non-interessato / Cold. Tieni solo Won+Attivo+Warm nel corpo; gli altri nel footer-memoria.
4. **Estrai** per ogni riga: owner, ultima attività (data più recente), prossima azione + callback date, stage/€ se c'è un deal.
5. **Promuovi** al cockpit (`opportunities/`) solo gli account qualificati (deal reale o interesse forte) → entrano nel board.
6. **Riconcilia** con le opportunità già esistenti (importi reali dal CRM, contatti, storia).
