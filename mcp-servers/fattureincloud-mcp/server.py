"""
Fatture in Cloud MCP Server
============================
MCP server for Fatture in Cloud API v2.
Provides read access to invoices, clients, products, payments, and company info.

Auth: OAuth2 Bearer token via environment variables.
Base URL: https://api-v2.fattureincloud.it
"""

import json
import os
from datetime import datetime, timezone
from enum import Enum
from typing import Optional, List

import httpx
from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel, Field, ConfigDict

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
API_BASE_URL = "https://api-v2.fattureincloud.it"
ACCESS_TOKEN = os.environ.get("FIC_ACCESS_TOKEN", "")
COMPANY_ID = os.environ.get("FIC_COMPANY_ID", "")

mcp = FastMCP("fattureincloud_mcp")

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

class ResponseFormat(str, Enum):
    MARKDOWN = "markdown"
    JSON = "json"


def _headers() -> dict:
    return {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Accept": "application/json",
    }


async def _api_get(path: str, params: Optional[dict] = None) -> dict:
    """Generic GET request to FIC API v2."""
    url = f"{API_BASE_URL}/c/{COMPANY_ID}/{path}"
    async with httpx.AsyncClient(timeout=30.0) as client:
        resp = await client.get(url, headers=_headers(), params=params or {})
        resp.raise_for_status()
        return resp.json()


async def _api_get_no_company(path: str, params: Optional[dict] = None) -> dict:
    """GET request without company_id prefix (e.g. /companies)."""
    url = f"{API_BASE_URL}/{path}"
    async with httpx.AsyncClient(timeout=30.0) as client:
        resp = await client.get(url, headers=_headers(), params=params or {})
        resp.raise_for_status()
        return resp.json()


async def _api_post(path: str, body: dict) -> dict:
    """Generic POST request to FIC API v2."""
    url = f"{API_BASE_URL}/c/{COMPANY_ID}/{path}"
    headers = {**_headers(), "Content-Type": "application/json"}
    async with httpx.AsyncClient(timeout=30.0) as client:
        resp = await client.post(url, headers=headers, json=body)
        resp.raise_for_status()
        return resp.json()


async def _get_vat_id(vat_percent: float) -> Optional[int]:
    """Look up the FIC vat_type id for a given percentage (e.g. 22 → id)."""
    try:
        data = await _api_get("settings/vat_types")
        for v in data.get("data", []):
            if float(v.get("value", -1)) == float(vat_percent) and not v.get("is_disabled", False):
                return v["id"]
    except Exception:
        pass
    return None


def _handle_api_error(e: Exception) -> str:
    if isinstance(e, httpx.HTTPStatusError):
        status = e.response.status_code
        if status == 401:
            return "Errore: Token non valido o scaduto. Verificare FIC_ACCESS_TOKEN."
        if status == 403:
            return "Errore: Accesso negato. Permessi insufficienti per questa risorsa."
        if status == 404:
            return "Errore: Risorsa non trovata. Verificare l'ID."
        if status == 429:
            retry = e.response.headers.get("Retry-After", "qualche secondo")
            return f"Errore: Rate limit superato. Riprovare tra {retry}."
        try:
            body = e.response.json()
            detail = body.get("error", body.get("message", str(body)))
        except Exception:
            detail = e.response.text[:300]
        return f"Errore API ({status}): {detail}"
    if isinstance(e, httpx.TimeoutException):
        return "Errore: Timeout nella richiesta. Riprovare."
    return f"Errore: {type(e).__name__} — {e}"


def _ts_to_date(ts: Optional[str]) -> str:
    """Convert ISO date string to human-readable."""
    if not ts:
        return "—"
    try:
        dt = datetime.fromisoformat(ts.replace("Z", "+00:00"))
        return dt.strftime("%d/%m/%Y")
    except Exception:
        return str(ts)


def _format_amount(amount) -> str:
    """Format a numeric amount as EUR."""
    if amount is None:
        return "—"
    return f"€{float(amount):,.2f}"


# ---------------------------------------------------------------------------
# Tool: List Companies
# ---------------------------------------------------------------------------

class ListCompaniesInput(BaseModel):
    """Input for listing user companies."""
    model_config = ConfigDict(extra="forbid")
    response_format: ResponseFormat = Field(
        default=ResponseFormat.MARKDOWN,
        description="Output: 'markdown' o 'json'"
    )


@mcp.tool(
    name="fic_list_companies",
    annotations={
        "title": "Lista aziende Fatture in Cloud",
        "readOnlyHint": True,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": True,
    },
)
async def fic_list_companies(params: ListCompaniesInput) -> str:
    """Elenca tutte le aziende accessibili con il token corrente.
    Utile per trovare il company_id corretto.
    """
    try:
        data = await _api_get_no_company("user/companies")
        companies = data.get("data", data.get("companies", []))
        if params.response_format == ResponseFormat.JSON:
            return json.dumps({"companies": companies}, indent=2, ensure_ascii=False)
        lines = ["# Aziende Fatture in Cloud\n"]
        for c in companies:
            cid = c.get("id", "?")
            name = c.get("name", "N/A")
            tax = c.get("tax_code", c.get("vat_number", ""))
            lines.append(f"- **{name}** (ID: {cid}) — P.IVA/CF: {tax}")
        return "\n".join(lines)
    except Exception as e:
        return _handle_api_error(e)


# ---------------------------------------------------------------------------
# Tool: Company Info
# ---------------------------------------------------------------------------

class CompanyInfoInput(BaseModel):
    model_config = ConfigDict(extra="forbid")
    response_format: ResponseFormat = Field(default=ResponseFormat.MARKDOWN)


@mcp.tool(
    name="fic_get_company_info",
    annotations={
        "title": "Info azienda Fatture in Cloud",
        "readOnlyHint": True,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": True,
    },
)
async def fic_get_company_info(params: CompanyInfoInput) -> str:
    """Recupera le informazioni dell'azienda configurata (nome, P.IVA, indirizzo, ecc.)."""
    try:
        data = await _api_get("company/info")
        info = data.get("data", data)
        if params.response_format == ResponseFormat.JSON:
            return json.dumps(info, indent=2, ensure_ascii=False)
        lines = [
            "# Info Azienda\n",
            f"**Nome**: {info.get('name', 'N/A')}",
            f"**P.IVA**: {info.get('vat_number', 'N/A')}",
            f"**CF**: {info.get('tax_code', 'N/A')}",
            f"**Indirizzo**: {info.get('address_street', '')} {info.get('address_postal_code', '')} {info.get('address_city', '')} ({info.get('address_province', '')})",
            f"**Email**: {info.get('email', 'N/A')}",
            f"**Telefono**: {info.get('phone', 'N/A')}",
        ]
        return "\n".join(lines)
    except Exception as e:
        return _handle_api_error(e)


# ---------------------------------------------------------------------------
# Tool: List Issued Documents (Invoices)
# ---------------------------------------------------------------------------

class ListInvoicesInput(BaseModel):
    """Input per la lista fatture emesse."""
    model_config = ConfigDict(extra="forbid")
    doc_type: Optional[str] = Field(
        default="invoice",
        description="Tipo documento: 'invoice', 'credit_note', 'receipt', 'order', 'quote', 'proforma', 'delivery_note'. Default: 'invoice'."
    )
    year: Optional[int] = Field(
        default=None,
        description="Anno di filtraggio (es. 2026). Se omesso, restituisce i più recenti."
    )
    page: Optional[int] = Field(default=1, description="Pagina (default: 1)", ge=1)
    per_page: Optional[int] = Field(default=50, description="Risultati per pagina (default: 50, max: 100)", ge=1, le=100)
    q: Optional[str] = Field(
        default=None,
        description="Filtro SQL-like (es. \"entity.name = 'ACME'\" oppure \"date >= '2026-01-01'\")"
    )
    sort: Optional[str] = Field(
        default="-date",
        description="Ordinamento (es. '-date' per data decrescente, 'number' per numero crescente)"
    )
    response_format: ResponseFormat = Field(default=ResponseFormat.MARKDOWN)


@mcp.tool(
    name="fic_list_invoices",
    annotations={
        "title": "Lista fatture emesse",
        "readOnlyHint": True,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": True,
    },
)
async def fic_list_invoices(params: ListInvoicesInput) -> str:
    """Elenca le fatture emesse (o altri documenti) con paginazione e filtri.
    Supporta filtri per tipo, anno, query SQL-like.
    """
    try:
        api_params: dict = {
            "type": params.doc_type or "invoice",
            "page": params.page,
            "per_page": params.per_page,
            "sort": params.sort or "-date",
        }
        # Build query filter
        q_parts = []
        if params.q:
            q_parts.append(params.q)
        if params.year:
            q_parts.append(f"date >= '{params.year}-01-01' and date <= '{params.year}-12-31'")
        if q_parts:
            api_params["q"] = " and ".join(q_parts)

        data = await _api_get("issued_documents", api_params)
        docs = data.get("data", [])
        pagination = data.get("pagination", {})

        if params.response_format == ResponseFormat.JSON:
            return json.dumps({"documents": docs, "pagination": pagination}, indent=2, ensure_ascii=False, default=str)

        total = pagination.get("total_items", pagination.get("total", "?"))
        current_page = pagination.get("current_page", params.page)
        total_pages = pagination.get("total_pages", "?")

        lines = [f"# Fatture emesse ({params.doc_type})\n"]
        lines.append(f"Pagina {current_page}/{total_pages} — Totale: {total} documenti\n")
        lines.append("| # | Data | Cliente | Importo | Stato | Pagato |")
        lines.append("|---|------|---------|---------|-------|--------|")

        for doc in docs:
            num = doc.get("number", "?")
            date = _ts_to_date(doc.get("date"))
            entity = doc.get("entity", {})
            client_name = entity.get("name", "N/A") if isinstance(entity, dict) else "N/A"
            amount = _format_amount(doc.get("amount_net", doc.get("amount_gross")))
            status = doc.get("status", "—")
            is_paid = "Si" if doc.get("is_marked", False) else "No"
            lines.append(f"| {num} | {date} | {client_name} | {amount} | {status} | {is_paid} |")

        # Totale importi
        amounts = [float(doc.get("amount_net", 0) or 0) for doc in docs]
        total_amount = sum(amounts)
        lines.append(f"\n**Totale pagina**: {_format_amount(total_amount)}")

        if int(current_page) < int(total_pages) if str(total_pages).isdigit() else False:
            lines.append(f"\n*Usa page={int(current_page)+1} per la pagina successiva.*")

        return "\n".join(lines)
    except Exception as e:
        return _handle_api_error(e)


# ---------------------------------------------------------------------------
# Tool: Get Single Invoice
# ---------------------------------------------------------------------------

class GetInvoiceInput(BaseModel):
    model_config = ConfigDict(extra="forbid")
    document_id: int = Field(..., description="ID del documento Fatture in Cloud")
    response_format: ResponseFormat = Field(default=ResponseFormat.MARKDOWN)


@mcp.tool(
    name="fic_get_invoice",
    annotations={
        "title": "Dettaglio fattura emessa",
        "readOnlyHint": True,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": True,
    },
)
async def fic_get_invoice(params: GetInvoiceInput) -> str:
    """Recupera il dettaglio completo di una singola fattura emessa per ID."""
    try:
        data = await _api_get(f"issued_documents/{params.document_id}")
        doc = data.get("data", data)

        if params.response_format == ResponseFormat.JSON:
            return json.dumps(doc, indent=2, ensure_ascii=False, default=str)

        entity = doc.get("entity", {}) or {}
        items = doc.get("items_list", []) or []
        payments = doc.get("payments_list", []) or []

        lines = [
            f"# Fattura {doc.get('number', '?')}\n",
            f"**Data**: {_ts_to_date(doc.get('date'))}",
            f"**Tipo**: {doc.get('type', '?')}",
            f"**Cliente**: {entity.get('name', 'N/A')} (ID: {entity.get('id', '?')})",
            f"**P.IVA cliente**: {entity.get('vat_number', 'N/A')}",
            f"**Stato**: {doc.get('status', '?')}",
            f"**Pagata**: {'Si' if doc.get('is_marked') else 'No'}",
            "",
            "## Righe",
            "| Descrizione | Qtà | Prezzo | IVA% | Totale |",
            "|-------------|-----|--------|------|--------|",
        ]
        for item in items:
            desc = (item.get("name") or item.get("description") or "—")[:50]
            qty = item.get("qty", 1)
            price = _format_amount(item.get("net_price"))
            vat_pct = item.get("vat", {}).get("value", "—") if isinstance(item.get("vat"), dict) else item.get("vat", "—")
            total = _format_amount(item.get("net_price", 0) * item.get("qty", 1) if item.get("net_price") else None)
            lines.append(f"| {desc} | {qty} | {price} | {vat_pct}% | {total} |")

        lines.extend([
            "",
            f"**Imponibile**: {_format_amount(doc.get('amount_net'))}",
            f"**IVA**: {_format_amount(doc.get('amount_vat'))}",
            f"**Totale lordo**: {_format_amount(doc.get('amount_gross'))}",
        ])

        if payments:
            lines.extend(["", "## Pagamenti"])
            for p in payments:
                due = _ts_to_date(p.get("due_date"))
                amount = _format_amount(p.get("amount"))
                paid = "Pagato" if p.get("status") == "paid" else p.get("status", "—")
                lines.append(f"- {due}: {amount} — {paid}")

        return "\n".join(lines)
    except Exception as e:
        return _handle_api_error(e)


# ---------------------------------------------------------------------------
# Tool: List Clients
# ---------------------------------------------------------------------------

class ListClientsInput(BaseModel):
    model_config = ConfigDict(extra="forbid")
    page: Optional[int] = Field(default=1, ge=1)
    per_page: Optional[int] = Field(default=50, ge=1, le=100)
    q: Optional[str] = Field(default=None, description="Filtro (es. \"vat_number = '12345'\")")
    sort: Optional[str] = Field(default="name", description="Ordinamento (es. 'name', '-name')")
    response_format: ResponseFormat = Field(default=ResponseFormat.MARKDOWN)


@mcp.tool(
    name="fic_list_clients",
    annotations={
        "title": "Lista clienti",
        "readOnlyHint": True,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": True,
    },
)
async def fic_list_clients(params: ListClientsInput) -> str:
    """Elenca i clienti dell'azienda con paginazione e filtri."""
    try:
        api_params = {
            "page": params.page,
            "per_page": params.per_page,
            "sort": params.sort or "name",
        }
        if params.q:
            api_params["q"] = params.q

        data = await _api_get("entities/clients", api_params)
        clients = data.get("data", [])
        pagination = data.get("pagination", {})

        if params.response_format == ResponseFormat.JSON:
            return json.dumps({"clients": clients, "pagination": pagination}, indent=2, ensure_ascii=False, default=str)

        total = pagination.get("total_items", pagination.get("total", "?"))
        lines = [f"# Clienti ({total} totali)\n"]
        lines.append("| Nome | P.IVA / CF | Email | Città |")
        lines.append("|------|-----------|-------|-------|")

        for c in clients:
            name = c.get("name", "N/A")
            vat = c.get("vat_number", c.get("tax_code", "—"))
            email = c.get("email", "—")
            city = c.get("address_city", "—")
            lines.append(f"| {name} | {vat} | {email} | {city} |")

        return "\n".join(lines)
    except Exception as e:
        return _handle_api_error(e)


# ---------------------------------------------------------------------------
# Tool: List Products
# ---------------------------------------------------------------------------

class ListProductsInput(BaseModel):
    model_config = ConfigDict(extra="forbid")
    page: Optional[int] = Field(default=1, ge=1)
    per_page: Optional[int] = Field(default=50, ge=1, le=100)
    q: Optional[str] = Field(default=None, description="Filtro (es. \"name = 'Licenza Pro'\")")
    response_format: ResponseFormat = Field(default=ResponseFormat.MARKDOWN)


@mcp.tool(
    name="fic_list_products",
    annotations={
        "title": "Lista prodotti/servizi",
        "readOnlyHint": True,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": True,
    },
)
async def fic_list_products(params: ListProductsInput) -> str:
    """Elenca i prodotti e servizi configurati in Fatture in Cloud."""
    try:
        api_params = {"page": params.page, "per_page": params.per_page}
        if params.q:
            api_params["q"] = params.q

        data = await _api_get("products", api_params)
        products = data.get("data", [])
        pagination = data.get("pagination", {})

        if params.response_format == ResponseFormat.JSON:
            return json.dumps({"products": products, "pagination": pagination}, indent=2, ensure_ascii=False, default=str)

        lines = ["# Prodotti / Servizi\n"]
        lines.append("| Nome | Codice | Prezzo netto | IVA |")
        lines.append("|------|--------|-------------|-----|")

        for p in products:
            name = p.get("name", "N/A")
            code = p.get("code", "—")
            price = _format_amount(p.get("net_price"))
            vat = p.get("default_vat", {})
            vat_val = f"{vat.get('value', '?')}%" if isinstance(vat, dict) else "—"
            lines.append(f"| {name} | {code} | {price} | {vat_val} |")

        return "\n".join(lines)
    except Exception as e:
        return _handle_api_error(e)


# ---------------------------------------------------------------------------
# Tool: List Received Documents
# ---------------------------------------------------------------------------

class ListReceivedDocsInput(BaseModel):
    model_config = ConfigDict(extra="forbid")
    doc_type: Optional[str] = Field(
        default="expense",
        description="Tipo: 'expense', 'passive_credit_note', 'passive_delivery_note'. Default: 'expense'."
    )
    year: Optional[int] = Field(default=None, description="Anno di filtraggio")
    page: Optional[int] = Field(default=1, ge=1)
    per_page: Optional[int] = Field(default=50, ge=1, le=100)
    q: Optional[str] = Field(default=None)
    sort: Optional[str] = Field(default="-date")
    response_format: ResponseFormat = Field(default=ResponseFormat.MARKDOWN)


@mcp.tool(
    name="fic_list_received_documents",
    annotations={
        "title": "Lista documenti ricevuti (spese)",
        "readOnlyHint": True,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": True,
    },
)
async def fic_list_received_documents(params: ListReceivedDocsInput) -> str:
    """Elenca documenti ricevuti (fatture passive / spese) con paginazione e filtri."""
    try:
        api_params = {
            "type": params.doc_type or "expense",
            "page": params.page,
            "per_page": params.per_page,
            "sort": params.sort or "-date",
        }
        q_parts = []
        if params.q:
            q_parts.append(params.q)
        if params.year:
            q_parts.append(f"date >= '{params.year}-01-01' and date <= '{params.year}-12-31'")
        if q_parts:
            api_params["q"] = " and ".join(q_parts)

        data = await _api_get("received_documents", api_params)
        docs = data.get("data", [])
        pagination = data.get("pagination", {})

        if params.response_format == ResponseFormat.JSON:
            return json.dumps({"documents": docs, "pagination": pagination}, indent=2, ensure_ascii=False, default=str)

        total = pagination.get("total_items", pagination.get("total", "?"))
        lines = [f"# Documenti ricevuti — {params.doc_type} ({total} totali)\n"]
        lines.append("| Data | Fornitore | Importo | Pagato |")
        lines.append("|------|-----------|---------|--------|")

        for doc in docs:
            date = _ts_to_date(doc.get("date"))
            entity = doc.get("entity", {}) or {}
            supplier = entity.get("name", "N/A") if isinstance(entity, dict) else "N/A"
            amount = _format_amount(doc.get("amount_net", doc.get("amount_gross")))
            paid = "Si" if doc.get("is_marked") else "No"
            lines.append(f"| {date} | {supplier} | {amount} | {paid} |")

        return "\n".join(lines)
    except Exception as e:
        return _handle_api_error(e)


# ---------------------------------------------------------------------------
# Tool: Payment Accounts & Methods
# ---------------------------------------------------------------------------

class ListSettingsInput(BaseModel):
    model_config = ConfigDict(extra="forbid")
    response_format: ResponseFormat = Field(default=ResponseFormat.MARKDOWN)


@mcp.tool(
    name="fic_list_payment_accounts",
    annotations={
        "title": "Conti di pagamento",
        "readOnlyHint": True,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": True,
    },
)
async def fic_list_payment_accounts(params: ListSettingsInput) -> str:
    """Elenca i conti di pagamento configurati (banca, cassa, PayPal, ecc.)."""
    try:
        data = await _api_get("settings/payment_accounts")
        accounts = data.get("data", [])

        if params.response_format == ResponseFormat.JSON:
            return json.dumps({"payment_accounts": accounts}, indent=2, ensure_ascii=False, default=str)

        lines = ["# Conti di pagamento\n"]
        for a in accounts:
            name = a.get("name", "N/A")
            acc_type = a.get("type", "—")
            iban = a.get("iban", "—")
            lines.append(f"- **{name}** ({acc_type}) — IBAN: {iban}")
        return "\n".join(lines)
    except Exception as e:
        return _handle_api_error(e)


@mcp.tool(
    name="fic_list_payment_methods",
    annotations={
        "title": "Metodi di pagamento",
        "readOnlyHint": True,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": True,
    },
)
async def fic_list_payment_methods(params: ListSettingsInput) -> str:
    """Elenca i metodi di pagamento configurati (bonifico, RiBa, carta, ecc.)."""
    try:
        data = await _api_get("settings/payment_methods")
        methods = data.get("data", [])

        if params.response_format == ResponseFormat.JSON:
            return json.dumps({"payment_methods": methods}, indent=2, ensure_ascii=False, default=str)

        lines = ["# Metodi di pagamento\n"]
        for m in methods:
            name = m.get("name", "N/A")
            mid = m.get("id", "?")
            lines.append(f"- **{name}** (ID: {mid})")
        return "\n".join(lines)
    except Exception as e:
        return _handle_api_error(e)


# ---------------------------------------------------------------------------
# Tool: VAT Types
# ---------------------------------------------------------------------------

@mcp.tool(
    name="fic_list_vat_types",
    annotations={
        "title": "Aliquote IVA",
        "readOnlyHint": True,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": True,
    },
)
async def fic_list_vat_types(params: ListSettingsInput) -> str:
    """Elenca le aliquote IVA configurate."""
    try:
        data = await _api_get("settings/vat_types")
        vats = data.get("data", [])

        if params.response_format == ResponseFormat.JSON:
            return json.dumps({"vat_types": vats}, indent=2, ensure_ascii=False, default=str)

        lines = ["# Aliquote IVA\n"]
        lines.append("| Descrizione | Aliquota | Detraibile |")
        lines.append("|-------------|----------|------------|")
        for v in vats:
            desc = v.get("description", v.get("value", "N/A"))
            value = v.get("value", "?")
            deductible = v.get("is_disabled", "—")
            lines.append(f"| {desc} | {value}% | {deductible} |")
        return "\n".join(lines)
    except Exception as e:
        return _handle_api_error(e)


# ---------------------------------------------------------------------------
# Tool: Suppliers (Entities)
# ---------------------------------------------------------------------------

class ListSuppliersInput(BaseModel):
    model_config = ConfigDict(extra="forbid")
    page: Optional[int] = Field(default=1, ge=1)
    per_page: Optional[int] = Field(default=50, ge=1, le=100)
    q: Optional[str] = Field(default=None)
    sort: Optional[str] = Field(default="name")
    response_format: ResponseFormat = Field(default=ResponseFormat.MARKDOWN)


@mcp.tool(
    name="fic_list_suppliers",
    annotations={
        "title": "Lista fornitori",
        "readOnlyHint": True,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": True,
    },
)
async def fic_list_suppliers(params: ListSuppliersInput) -> str:
    """Elenca i fornitori dell'azienda."""
    try:
        api_params = {
            "page": params.page,
            "per_page": params.per_page,
            "sort": params.sort or "name",
        }
        if params.q:
            api_params["q"] = params.q

        data = await _api_get("entities/suppliers", api_params)
        suppliers = data.get("data", [])
        pagination = data.get("pagination", {})

        if params.response_format == ResponseFormat.JSON:
            return json.dumps({"suppliers": suppliers, "pagination": pagination}, indent=2, ensure_ascii=False, default=str)

        total = pagination.get("total_items", pagination.get("total", "?"))
        lines = [f"# Fornitori ({total} totali)\n"]
        lines.append("| Nome | P.IVA / CF | Email | Città |")
        lines.append("|------|-----------|-------|-------|")

        for s in suppliers:
            name = s.get("name", "N/A")
            vat = s.get("vat_number", s.get("tax_code", "—"))
            email = s.get("email", "—")
            city = s.get("address_city", "—")
            lines.append(f"| {name} | {vat} | {email} | {city} |")

        return "\n".join(lines)
    except Exception as e:
        return _handle_api_error(e)


# ---------------------------------------------------------------------------
# Tool: Tax Profile
# ---------------------------------------------------------------------------

@mcp.tool(
    name="fic_get_tax_profile",
    annotations={
        "title": "Profilo fiscale",
        "readOnlyHint": True,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": True,
    },
)
async def fic_get_tax_profile(params: ListSettingsInput) -> str:
    """Recupera il profilo fiscale dell'azienda (regime, ritenute, ecc.)."""
    try:
        data = await _api_get("settings/tax_profile")
        profile = data.get("data", data)

        if params.response_format == ResponseFormat.JSON:
            return json.dumps(profile, indent=2, ensure_ascii=False, default=str)

        lines = ["# Profilo Fiscale\n"]
        for key, value in profile.items():
            if key.startswith("_"):
                continue
            label = key.replace("_", " ").title()
            lines.append(f"**{label}**: {value}")
        return "\n".join(lines)
    except Exception as e:
        return _handle_api_error(e)


# ---------------------------------------------------------------------------
# Tool: Create Invoice (Draft)
# ---------------------------------------------------------------------------

class InvoiceItem(BaseModel):
    model_config = ConfigDict(extra="forbid")
    description: str = Field(..., description="Descrizione della riga (es. 'Abbonamento Piano Pro - Gennaio 2026')")
    qty: float = Field(default=1.0, description="Quantità (default: 1)")
    net_price: float = Field(..., description="Prezzo unitario netto IVA esclusa (es. 54.90)")
    vat_percent: float = Field(default=22.0, description="Aliquota IVA % (default: 22). Esempi: 0, 4, 10, 22.")


class InvoicePayment(BaseModel):
    model_config = ConfigDict(extra="forbid")
    amount: float = Field(..., description="Importo rata (lordo IVA inclusa)")
    due_date: str = Field(..., description="Data scadenza in formato YYYY-MM-DD")
    payment_account_id: int = Field(default=1280625, description="ID conto di pagamento. Default: 1280625 (Stripe). Usa fic_list_payment_accounts per altri conti.")


class CreateInvoiceInput(BaseModel):
    model_config = ConfigDict(extra="forbid")
    entity_id: int = Field(..., description="ID cliente FIC (usa fic_list_clients per trovarlo). Es. DPWAY=85109787")
    entity_name: str = Field(..., description="Ragione sociale cliente (es. 'DPWAY S.R.L.')")
    date: str = Field(..., description="Data documento YYYY-MM-DD (es. '2026-03-26')")
    items: List[InvoiceItem] = Field(..., description="Righe fattura (almeno 1). Una riga per mese/periodo.")
    payments: List[InvoicePayment] = Field(..., description="Rate di pagamento. La somma deve corrispondere al totale lordo.")
    doc_type: str = Field(default="invoice", description="Tipo: 'invoice' (default), 'credit_note', 'quote', 'proforma'.")
    e_invoice: bool = Field(default=True, description="True = fattura elettronica SDI (default). False = solo PDF.")
    subject: Optional[str] = Field(default=None, description="Oggetto visibile nel documento (opzionale)")
    notes: Optional[str] = Field(default=None, description="Note a piè di documento (opzionale)")


@mcp.tool(
    name="fic_create_invoice",
    annotations={
        "title": "Crea fattura elettronica",
        "readOnlyHint": False,
        "destructiveHint": False,
        "idempotentHint": False,
        "openWorldHint": True,
    },
)
async def fic_create_invoice(params: CreateInvoiceInput) -> str:
    """Crea una fattura elettronica in Fatture in Cloud (sezionale numerico default).

    Note importanti:
    - La data deve essere >= all'ultima fattura emessa (sequenza numerica obbligatoria in Italia)
    - La somma dei pagamenti deve corrispondere al totale lordo (net_price * qty * 1.22 per IVA 22%)
    - Per più mesi: usa più items (una riga per mese) con più payments (una rata per mese)
    - Il conto default è Stripe (ID 1280625). Usa fic_list_payment_accounts per altri conti.

    Esempio DPWAY 2 mesi:
      items=[{desc:"Abbonamento - Gen 2026", net_price:54.90}, {desc:"... Feb 2026", net_price:54.90}]
      payments=[{amount:66.98, due_date:"2026-01-26"}, {amount:66.98, due_date:"2026-02-26"}]
    """
    try:
        # Resolve VAT ids for each item
        items_list = []
        for item in params.items:
            vat_id = await _get_vat_id(item.vat_percent)
            if vat_id is None:
                return f"Errore: aliquota IVA {item.vat_percent}% non trovata. Usa fic_list_vat_types."
            items_list.append({
                "description": item.description,
                "qty": item.qty,
                "net_price": item.net_price,
                "vat": {"id": vat_id, "value": item.vat_percent},
            })

        payments_list = [
            {
                "amount": p.amount,
                "due_date": p.due_date,
                "status": "not_paid",
                "payment_account": {"id": p.payment_account_id},
            }
            for p in params.payments
        ]

        body: dict = {
            "data": {
                "type": params.doc_type,
                "numeration": "",  # sezionale numerico default
                "date": params.date,
                "e_invoice": params.e_invoice,
                "entity": {"id": params.entity_id, "name": params.entity_name},
                "currency": {"id": "EUR", "exchange_rate": "1.00000", "symbol": "€"},
                "language": {"code": "it", "name": "Italiano"},
                "template": {"id": 10},
                "items_list": items_list,
                "payments_list": payments_list,
            }
        }
        if params.subject:
            body["data"]["subject"] = params.subject
        if params.notes:
            body["data"]["notes"] = params.notes

        result = await _api_post("issued_documents", body)
        doc = result.get("data", result)

        doc_id = doc.get("id", "?")
        doc_number = doc.get("number", "?")
        doc_date = _ts_to_date(doc.get("date"))
        entity = doc.get("entity", {}) or {}
        client_name = entity.get("name", "N/A")
        gross = _format_amount(doc.get("amount_gross"))
        net = _format_amount(doc.get("amount_net"))
        vat_amount = _format_amount(doc.get("amount_vat"))

        return (
            f"# Fattura elettronica emessa\n\n"
            f"**ID FIC**: {doc_id}  \n"
            f"**Numero**: {doc_number}  \n"
            f"**Data**: {doc_date}  \n"
            f"**Cliente**: {client_name}  \n"
            f"**Imponibile**: {net}  \n"
            f"**IVA**: {vat_amount}  \n"
            f"**Totale lordo**: {gross}  \n"
        )
    except Exception as e:
        return _handle_api_error(e)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    mcp.run(transport="stdio")
