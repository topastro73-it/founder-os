# Skill: Gmail Reading

## Scopo

Fornire a tutti gli agenti accesso contestuale alle email aziendali tramite Gmail MCP.
Le email sono **solo contesto** — non vengono archiviate nel repo, non vengono inoltrate intere, non contengono dati sensibili in documenti pubblici.

## Quando ogni agente la usa

| Agente | Uso principale | Query tipiche |
|--------|---------------|---------------|
| **Chief of Staff** | Daily briefing, email senza risposta, escalation | `is:unread newer_than:1d`, `is:unread older_than:2d -label:sent` |
| **CEO** | Email da investitori, board, partner strategici | `from:investor OR from:vc newer_than:7d`, `subject:term sheet OR subject:follow-up` |
| **PM** | Feature request da clienti, bug report, feedback | `from:customer subject:feature OR subject:request newer_than:14d`, `label:feedback` |
| **CTO** | Alert di sistema, incident, email da fornitori infrastruttura | `subject:alert OR subject:incident OR subject:downtime newer_than:1d`, `from:pagerduty OR from:aws` |
| **Sales** | Risposta a proposte, follow-up prospect, email deal | `subject:proposal OR subject:quote newer_than:7d`, `from:[prospect-domain]` |
| **CFO** | Fatture, bonifici, email da banca e commercialista | `subject:fattura OR subject:invoice newer_than:30d`, `from:commercialista OR from:banca` |
| **Legal** | Contratti, NDA, email legali | `subject:contratto OR subject:NDA OR subject:agreement newer_than:30d`, `label:legal` |
| **HR** | Candidati, colloqui, offerte di lavoro | `subject:candidatura OR subject:application newer_than:14d`, `label:recruiting` |
| **Marketing** | Press inquiry, partnership, richieste di co-marketing | `subject:press OR subject:partnership newer_than:14d` |

## Query Gmail utili per tutti gli agenti

```
# Email urgenti non lette
is:unread is:important newer_than:1d

# Email senza risposta da più di 48h (richiede attenzione)
is:unread older_than:2d -from:me -label:newsletter

# Email da un dominio specifico
from:@dominio.com newer_than:30d

# Thread in corso (non risolti)
is:unread label:inbox -label:automated

# Cerca per topic specifico
subject:"[topic]" OR body:"[keyword]" newer_than:14d
```

## Regole di sicurezza (OBBLIGATORIE)

1. **Mai archiviare email nel repo** — Le email sono contesto temporaneo, non documenti aziendali.
2. **Solo summary, non testo integrale** — Quando usi il contenuto di un'email in un documento, scrivi una sintesi, mai citare verbatim.
3. **Mai dati sensibili in file pubblici** — Importi, dati personali, contenuti di NDA/contratti non vanno in `docs/` o `company/`.
4. **Mai il corpo dell'email in commit** — I commit message descrivono l'azione, non citano le email.
5. **Informazioni PII (candidati, dipendenti)** — Mai fuori da conversazioni private con HR.
6. **Credenziali e token** — Se un'email contiene password, token o link di reset, non copiarle da nessuna parte.

## Come invocare

```
# Carica il tool Gmail MCP prima di ogni operazione
# Usa gmail_search_messages per cercare
# Usa gmail_read_thread per leggere un thread specifico
# Sintetizza il contenuto, non copiarlo

Esempio:
- gmail_search_messages(query="from:cliente@example.com newer_than:7d")
- Leggi i thread rilevanti con gmail_read_thread
- Estrai solo: mittente, data, topic, azione richiesta (sì/no), urgenza
```

## Output strutturato

Quando usi email come contesto, usa sempre questo formato:

```
**Email da [nome/ruolo]** — [data]
Topic: [una riga]
Azione richiesta: [sì/no — se sì, cosa]
Urgenza: [alta/media/bassa]
```

## Integrazione con comandi

- `email-scan.md` — CoS: scansione daily per briefing
- `email-context.md` — Tutti gli agenti: contesto email su topic specifico
