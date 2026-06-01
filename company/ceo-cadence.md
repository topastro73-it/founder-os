# CEO Decision Cadence — Tracking

> Aggiornato automaticamente dal sistema dopo ogni check.
> Usato dal CEO Routine Agent (`.agents/ceo-routine/AGENT.md`) come fonte di verità per determinare il ritmo.
> NON modificare manualmente (a parte la prima configurazione via `/setup`).

## Ultimo check per ritmo

| Ritmo | Ultima data | Note |
|-------|-------------|------|
| Giornaliero | — | Mai eseguito |
| Settimanale | — | Mai eseguito |
| Mensile | — | Mai eseguito |

## Routine Agent Status

| Campo | Valore |
|-------|--------|
| Ultima sessione routine | — |
| Tipo ultima routine | — |
| Promesse aperte | Vedi `company/ceo-routine.md` |
| Dati pendenti | Vedi `company/ceo-routine.md` |

## Admin & Finance nel Cadence

**Giornaliero**:
- Se c'è una scadenza fiscale/admin nei prossimi 3 giorni → alert
- Se c'è una fattura scaduta da 30+ giorni non incassata → alert

**Settimanale**:
- "Fatture: €[X] da incassare, di cui €[Y] scadute"
- "Cashflow prossime 4 settimane: €[saldo proiettato]"
- Scadenze fiscali/admin della prossima settimana

**Mensile**:
- Controllo di gestione: budget vs actual
- Costi ricorrenti: rinnovi in arrivo, ottimizzazioni possibili

## Log risposte recenti

> Vuoto. Le sessioni verranno loggate qui dal sistema.
