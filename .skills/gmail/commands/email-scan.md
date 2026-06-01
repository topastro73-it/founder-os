# Command: email-scan

## Trigger
Invocato automaticamente da `/cos daily-briefing` oppure manualmente con "scan email", "controlla la posta", "ci sono email importanti?"

## Scopo
Scansiona le email delle ultime 24h, classifica per urgenza e tipo, e produce una sintesi strutturata per il briefing.

## Processo

1. **Scan urgenti** (priorità massima)
   ```
   gmail_search_messages(query="is:unread is:important newer_than:1d")
   ```
   - Classifica: azione richiesta / monitoraggio / informativo

2. **Scan senza risposta** (follow-up necessario)
   ```
   gmail_search_messages(query="is:unread older_than:2d -from:me -label:newsletter -label:automated")
   ```
   - Identifica thread aperti da 48h+ senza risposta

3. **Scan per categoria** (contesto per agenti)
   - Investitori/board: `from:investor OR subject:"term sheet" OR subject:"follow-up" newer_than:7d`
   - Clienti/partner: `from:@[partner-domain] newer_than:3d`
   - Fatture/finance: `subject:fattura OR subject:invoice newer_than:7d`
   - Legal: `subject:contratto OR subject:NDA newer_than:7d`
   - Candidati: `subject:candidatura OR subject:application newer_than:7d`

4. **Per ogni email rilevante**, leggi il thread con `gmail_read_thread` e estrai:
   - Mittente e ruolo
   - Topic (1 riga)
   - Azione richiesta (sì/no — se sì, cosa)
   - Urgenza (alta/media/bassa)
   - Agente destinatario suggerito (CEO, PM, Sales, etc.)

5. **Identifica pattern**
   - Topic ricorrenti (stesso argomento da più mittenti)
   - Thread lunghi senza risoluzione
   - Email da stakeholder chiave (investitori, partner top)

## Output

Formato da inserire nel daily-briefing:

```markdown
### Email — Ultime 24h

**Azione richiesta** ({N})
| Da | Topic | Azione | Urgenza | Per |
|----|-------|--------|---------|-----|
| [nome] | [topic] | [cosa serve] | alta/media | [agente] |

**Senza risposta da 48h+** ({N})
| Da | Topic | Giorni | Suggerimento |
|----|-------|--------|-------------|
| [nome] | [topic] | [N] | [rispondere / delegare / ignorare] |

**FYI** ({N})
- [mittente]: [topic 1 riga]
```

## Regole di sicurezza

- **Mai archiviare email nel repo** — solo sintesi nel briefing
- **Mai citare verbatim** — parafrasa sempre
- **Mai dati sensibili** — importi, dati personali, contenuti NDA restano fuori
- **Mai il corpo email nei commit** — il commit descrive l'azione, non cita email
