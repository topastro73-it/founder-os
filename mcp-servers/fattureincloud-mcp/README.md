# Fatture in Cloud MCP Server

Server MCP per l'integrazione con Fatture in Cloud API v2.
Fornisce accesso in sola lettura a fatture, clienti, fornitori, prodotti e impostazioni aziendali.

## Setup

```bash
pip install -r requirements.txt
```

## Configurazione

Imposta le variabili d'ambiente:

```bash
export FIC_ACCESS_TOKEN="<bearer token da FIC → Impostazioni → API>"
export FIC_COMPANY_ID="<ID azienda>"
```

## Uso standalone (stdio)

```bash
python server.py
```

## Uso con Claude Code / Cowork

Aggiungi al tuo `.claude/settings.json`:

```json
{
  "mcpServers": {
    "fattureincloud": {
      "command": "python",
      "args": ["path/to/server.py"],
      "env": {
        "FIC_ACCESS_TOKEN": "...",
        "FIC_COMPANY_ID": "..."
      }
    }
  }
}
```

## Tool disponibili

| Tool | Descrizione |
|------|------------|
| `fic_list_companies` | Lista aziende accessibili |
| `fic_get_company_info` | Info azienda (nome, P.IVA, indirizzo) |
| `fic_list_invoices` | Fatture emesse con filtri per tipo, anno, query |
| `fic_get_invoice` | Dettaglio singola fattura |
| `fic_list_clients` | Anagrafica clienti |
| `fic_list_suppliers` | Anagrafica fornitori |
| `fic_list_products` | Prodotti e servizi |
| `fic_list_received_documents` | Fatture passive / spese |
| `fic_list_payment_accounts` | Conti di pagamento |
| `fic_list_payment_methods` | Metodi di pagamento |
| `fic_list_vat_types` | Aliquote IVA |
| `fic_get_tax_profile` | Profilo fiscale |

Tutti i tool supportano output in formato `markdown` (default) o `json`.
