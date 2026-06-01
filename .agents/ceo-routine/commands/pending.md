# Command: pending

## Trigger
`/routine pending` oppure "Cosa aspetta me?" oppure "Cosa ho in sospeso?"

## Processo

1. **Scansiona tutti i backlog del CEO**:
   - `decisions/` — decisioni con status `Proposta` che richiedono approvazione CEO
   - `company/product/specs/` — spec in `evaluated` che attendono approvazione
   - `company/ceo-routine.md` — promesse aperte non completate
   - `company/ceo-routine.md` — dati richiesti e non forniti
   - `company/ceo-cadence.md` — follow-up con deadline passata
   - `company/customers/partners/` — partner con alert attivi

2. **Raggruppa per tipo e urgenza**

3. **Output**

```
TUTTO CIO CHE ASPETTA TE — {data}

DECISIONI DA PRENDERE ({N})
| # | Cosa | In attesa da | Impatto se non decidi |
|---|------|-------------|----------------------|
| 1 | [decisione] | [N] giorni | [cosa si blocca] |

PROMESSE NON MANTENUTE ({N})
| # | Cosa hai promesso | Quando | A chi |
|---|------------------|--------|-------|
| 1 | [promessa] | [data] | [persona/agente] |

DATI CHE TI HO CHIESTO ({N})
| # | Dato | Richiesto il | Serve per |
|---|------|-------------|-----------|
| 1 | [dato] | [data] | [motivo] |

FOLLOW-UP SCADUTI ({N})
| # | Follow-up | Deadline | Owner |
|---|-----------|----------|-------|
| 1 | [cosa] | [data] | Tu |

PARTNER ALERT ({N})
| Partner | Score | Alert |
|---------|-------|-------|
| [partner] | [score] | [tipo] |

Totale item in attesa: {N}

Cosa vuoi chiudere adesso?
```

## Output
Interazione diretta — nessun file generato.
