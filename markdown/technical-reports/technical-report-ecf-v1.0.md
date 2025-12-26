# Technical Report: Electronic Fiscal Voucher (e-CF) v1.0

> **Original**: Informe Técnico Comprobante Fiscal Electrónico v1.0  
> **Source**: [Informe Técnico e-CF v1.0.pdf](file:///home/romulo/visual/ecf/ecf-docs/Informe%20y%20Descripci%C3%B3n%20T%C3%A9cnica/Informe%20T%C3%A9cnico%20e-CF%20v1.0.pdf)  
> **Pages**: 52

---

## Overview

This document serves as the primary technical guide for the DGII e-CF system, providing essential logic for XML generation, tax calculation accuracy, and structural integrity.

---

## System Actors

Three primary actors interact in the Dominican Republic's electronic invoicing ecosystem:

### DGII (Dirección General de Impuestos Internos)
The regulatory authority responsible for:
- Tax administration and application per Tax Code Articles 32, 34, 35 (Law 11-92)
- e-CF validation and acceptance/rejection
- Providing web services for authentication, reception, and queries
- Maintaining the electronic taxpayer directory

### Electronic Issuer (Emisor Electrónico)
Any taxpayer **authorized by DGII** to emit electronic fiscal receipts. Requirements:
- Must possess a **digital certificate for tax processes** (INDOTEL-accredited)
- Responsible for XML generation, digital signing, and transmission
- Must implement web services for P2P communication (if also a receiver)

### Electronic Receiver (Receptor Electrónico)
Any taxpayer who receives e-CFs electronically. Key points:
- **Every electronic receiver is also an electronic issuer** (dual role requirement)
- Must implement reception web service to receive e-CFs from other issuers
- Must send Commercial Approval/Rejection (`Aprobación Comercial`) for received e-CFs
- Authorized by DGII with same digital certificate requirements

**Non-Electronic Receiver:** Not part of the e-CF system; receives only printed representation (RI) and queries validity via DGII web portal.

---

## Web Services

All communication uses **REST Web Services** with XML payloads. Base URLs:

- **Production**: `https://ecf.dgii.gov.do/ecf/`
- **Certification**: `https://ecf.dgii.gov.do/certecf/`
- **Pre-Certification (Testing)**: `https://ecf.dgii.gov.do/testecf/`

### 4.1. Authentication (Autenticación)
**Purpose**: Obtain a Bearer token (valid 1 hour) for all subsequent API calls.

**Process**:
1. Request seed: `GET /autenticacion/api/autenticacion/semilla`
2. Sign seed with your digital certificate
3. Submit signed seed: `POST /autenticacion/api/autenticacion/autenticar`
4. Receive JWT token

### 4.2. e-CF Reception (Recepción e-CF)
**Endpoint**: `POST /recepcion/api/recepcionecf`

**Purpose**: Submit e-CF XML to DGII for validation.

**Returns**: `TrackId` (unique identifier for status queries)

**Possible Responses**:
- `Aceptado` (Accepted) - e-CF is valid
- `Aceptado Condicional` (Conditionally Accepted) - Valid but with warnings
- `Rechazado` (Rejected) - Invalid, not fiscally valid
- `En Proceso` (Processing) - Validation in progress (~200ms avg)

### 4.3. RFCE Reception (Recepción RFCE)
**Endpoint**: `POST /recepcionrfce/api/recepcionrfce`

**Purpose**: Submit summary for Consumer Electronic Invoices < RD$250,000.

**Note**: Full e-CF XML is **not sent** to DGII for these invoices. Only a summary (RFCE format) is submitted. The complete e-CF must be stored locally for 10 years.

### 4.4. Commercial Approval Reception (Recepción de Aprobación Comercial)
**Endpoint**: `POST /aprobacioncomercial/api/aprobacioncomercial`

**Purpose**: Electronic receiver notifies DGII of their acceptance/rejection of a received e-CF.

**Format**: ACECF XML (signed)

### 4.5. e-CF Result Query (Consulta de Resultado) - Issuers
**Endpoint**: `GET /consultaresultado/api/consultas/estado?trackid={trackid}`

**Purpose**: Check validation status using `TrackId` from reception response.

**Use**: Poll this after submitting e-CF to check if accepted/rejected.

### 4.6. e-CF Status Query (Consulta de Estado) - Receivers
**Endpoint**: `GET /consultaestado/api/consultas/estado?rncemisor={rnc}&ncfelectronico={encf}&rnccomprador={rnc}&codigoseguridad={code}`

**Purpose**: Verify e-CF validity using visible fields (RNC, e-NCF, security code).

**Use**: Receivers can verify invoices without needing the TrackId.

### 4.7. TrackId Query (Consulta de TrackId)
**Endpoint**: `GET /consultatrackids/api/trackids/consulta?rncemisor={rnc}&encf={encf}`

**Purpose**: Get all `TrackIds` for a specific e-NCF (if resubmitted multiple times).

### 4.8. Directory Query (Consulta Directorio)
**Endpoint**: `GET /consultadirectorio/api/consultas/listado`

**Purpose**: Retrieve list of all electronic taxpayers and their web service URLs (reception, approval, optional authentication).

**Returns**: JSON/XML with `urlRecepcion`, `urlAceptacion`, `urlOpcional` for each RNC.

### 4.9. Service Status Query (Consulta Estatus Servicios)
**Endpoint**: `GET /estatusservicios/api/consultas/estatus`

**Purpose**: Check availability and maintenance windows for DGII services.

### 4.10. e-NCF Annulment (Anulación de e-NCF)
**Endpoint**: `POST /anulacionrangos/api/operaciones/anularrango`

**Purpose**: Annul unused sequence ranges or e-CFs signed but not sent.

**Format**: ANECF XML

### 4.11. Issuer-Receiver Communication (Comunicación Emisor-Receptor)
**Availability**: Pre-certification environment only

**Purpose**: DGII-provided simulator to test P2P communication (reception, approval) before going to production.

---

## Operation Models

Understanding how e-CFs flow between actors is critical for implementation.

### Model I: Electronic Issuer → Electronic Receiver

**Mandatory Steps (1-4):**
1. **Issuer → DGII**: Send e-CF XML
2. **DGII → Issuer**: Return `TrackId`
3. **Issuer → Receiver**: Send e-CF XML (P2P)
4. **Receiver → Issuer**: Send Acknowledgment of Receipt (`Acuse de Recibo` - ARECF XML)

**Optional Steps (5-6):**
5. **Receiver → Issuer**: Send Commercial Approval/Rejection (ACECF XML)
6. **Receiver → DGII**: Notify DGII of approval/rejection

**Key Points**:
- Issuer must send to **both** DGII and receiver
- Receiver must acknowledge receipt (step 4)
- Commercial approval is optional but recommended
- DGII only accepts commercial approvals for e-CFs it has already accepted

### Model II: Electronic Issuer → Non-Electronic Receiver

**Steps:**
1. **Issuer → DGII**: Send e-CF XML
2. **DGII → Issuer**: Return `TrackId`
3. **Issuer → Receiver**: Deliver **Printed Representation (RI)** only

**Receiver Responsibility**:
- Query e-CF validity on DGII website using QR code or manual entry
- Report purchase in Format 606 (Costs and Expenses)

### Model III: Consumer Invoice < RD$250,000

**Steps**:
1. **Issuer**: Generate full e-CF XML, sign, store locally (10-year retention)
2. **Issuer → DGII**: Send **summary only** (RFCE format, not full XML)
3. **DGII → Issuer**: Return validation status (Accepted/Rejected/Conditionally Accepted)
4. **Issuer → Consumer**: Deliver printed representation

**Critical Differences**:
- Full e-CF is **never sent** to DGII (only summary)
- No P2P transmission (consumers are non-electronic)
- QR code uses different URL structure (see Section 17)
- Max 10,000 line items (vs 1,000 for standard e-CFs)

---

## Corrections and Annulment

### Corrections (Using Credit/Debit Notes)

Use electronic credit notes (`Nota de Crédito Electrónica` - Type 34) or debit notes (`Nota de Débito Electrónica` - Type 33):

**Credit Note Rules**:
- **Within 30 days**: Can refund both price + ITBIS
- **After 30 days**: Can only refund price (ITBIS is NOT refundable per Regulation 293-11, Arts. 8 & 28)

**Modification Codes** (in `InformacionReferencia` section):
| Code | Purpose |
|------|------|
| 1 | Annuls the modified NCF |
| 2 | Corrects text in the modified receipt |
| 3 | Corrects amounts in the modified NCF |
| 4 | Replaces NCF emitted in contingency |

### Annulment (Using ANECF)

Use the Annulment web service (4.10) for:
- e-CFs that were **signed but never sent** (not to DGII, not to receiver)
- Unused sequence ranges

**Cannot Annul**:
- e-CFs already sent to DGII or receiver (must use credit note)
- Sequences where `secuenciaUtilizada = true` in DGII response

**Rejection Scenarios**:
If e-CF is rejected in Commercial Approval by receiver:
- Issuer must send credit note to both DGII and receiver

If e-CF is approved by receiver but rejected by DGII:
- e-CF is invalid (commercial approval also becomes invalid)
- Issuer must create new e-CF to replace the one given to receiver

---

## Actors in the System

| Actor | Description |
|-------|-------------|
| **Electronic Issuer** | Emisor Electrónico - entity that issues e-CFs |
| **Electronic Receptor** | Receptor Electrónico - entity that receives e-CFs electronically |
| **Non-Electronic Receptor** | Receptor No Electrónico - receives printed representation only |

---

## e-CF Types (Tipos de Comprobante)

| Code | Type | Description |
|------|------|-------------|
| `31` | Factura de Crédito Fiscal Electrónica | B2B Tax Credit Invoice — Allows recipient to claim tax credits/deductions |
| `32` | Factura de Consumo Electrónica | B2C Consumer Invoice — Final consumers, no tax credit |
| `33` | Nota de Débito Electrónica | Debit Note — Recovers post-sale costs (interest, freight) |
| `34` | Nota de Crédito Electrónica | Credit Note — Cancels, returns, discounts, or corrects errors |
| `41` | Comprobante de Compras Electrónico | Purchases from unregistered taxpayers (informal sector) |
| `43` | Comprobante de Gastos Menores Electrónico | Minor work-related expenses (parking, tolls, consumables) |
| `44` | Comprobante de Regímenes Especiales Electrónico | ITBIS/ISC exempt transactions under special tax regimes |
| `45` | Comprobante Gubernamental Electrónico | Sales to government entities (non-commercial) |
| `46` | Comprobante para Exportaciones Electrónico | Exports, Free Trade Zones, and Commercial Free Zones |
| `47` | Comprobante para Pagos al Exterior Electrónico | Foreign payments with full withholding (per Art. 297, 305 of Tax Code) |

---

## e-NCF Structure (Número de Comprobante Fiscal Electrónico)

The e-NCF consists of **13 alphanumeric characters**:

```
E XX NNNNNNNNNN
│ │  └── 10 digits: Sequential number (0000000001 to 9999999999)
│ └──── 2 digits: e-CF type code (31, 32, 33, etc.)
└────── 1 letter: Fixed "E" prefix for electronic series
```

**Example**: `E310000000005` (Type 31 Credit Fiscal Invoice, sequence 5)

**Validity Rules:**
- Sequences are valid from authorization date until **December 31st of the following year**
- Cannot be used after expiration date
- Unused sequences should be cancelled via the ANECF format

---

## XML Document Sections

### Section A: Encabezado (Header) — Mandatory

Contains document identification, issuer, recipient, and totals.

| Element | Description |
|---------|-------------|
| `RNCEmisor` | Issuer's RNC (tax ID) |
| `RNCReceptor` | Recipient's RNC |
| `TipoECF` | e-CF type code |
| `eNCF` | Electronic fiscal voucher number |
| `FechaEmision` | Issue date |

### Section B: Detalle de Bienes o Servicios (Items Detail) — Mandatory

Individual items or services sold.

| Element | Description |
|---------|-------------|
| `IndicadorMontoGravado` | Tax indicator (see below) |
| `NombreItem` | Item name/description |
| `CantidadItem` | Quantity |
| `PrecioUnitarioItem` | Unit price |
| `MontoItem` | Total amount for line |

**`IndicadorMontoGravado` Values:**

| Value | Meaning |
|-------|---------|
| `1` | Gravado (Taxed) |
| `2` | Exento (Exempt) |
| `3` | Tasa Cero (Zero Rate) |

### Section C: Subtotales Informativos — Optional

Informational subtotals that do not affect the main totalizers.

### Section D: Descuentos o Recargos (Discounts/Surcharges) — Conditional

Global discounts or charges applied to the entire invoice.

### Section E: Paginación — Optional

Information about pages and items per page.

---

## XML Format Requirements

### Character Escaping in ALFANUM Fields

**Critical**: The following characters have special meaning in XML and **must** be escaped:

| Character | Name | Use &#... (Decimal) | Use &#x... (Hex) |
|-----------|------|---------------------|------------------|
| `"` | quot | `&#34;` | `&#x22;` |
| `&` | amp | `&#38;` | `&#x26;` |
| `'` | apos | `&#39;` | `&#x27;` |
| `<` | lt | `&#60;` | `&#x3C;` |
| `>` | gt | `&#62;` | `&#x3E;` |

**Example**:
```xml
<!-- WRONG -->
<NombreItem>Laptop 15" & Mouse</NombreItem>

<!-- CORRECT -->
<NombreItem>Laptop 15&#34; &#38; Mouse</NombreItem>
```

### Field Obligatoriness Codes

Each field in the e-CF format has an obligatoriness code:

| Code | Meaning | When Required |
|------|---------|---------------|
| `0` | Not applicable | Field must NOT appear in this document type |
| `1` | Mandatory | Must always be present |
| `2` | Conditional | Required only if specific condition met (e.g., discounts exist) |
| `3` | Optional | May be included at issuer's discretion |

**Example**: `<DescuentoORecargo>` is **conditional (2)** - required only if global discounts/surcharges exist.

---

## Business Rules

### Rounding Rules (Section 13)

Standard rounding: if the 3rd decimal is ≥ 5, round up the 2nd decimal.

**Exceptions (more decimals allowed):**

| Field | Max Decimals |
|-------|--------------|
| `PrecioUnitarioItem` | 4 |
| `PrecioUnitarioItemOtraMoneda` | 4 |
| `TipoCambio` | 3 |
| `Subcantidad` | 3 |

### Tolerance Rules (Section 12)

| Type | Tolerance |
|------|-----------|
| **Global Tolerance** | ±0.50 DOP between sum of items and grand total |
| **Line Tolerance** | ±1 unit of price value per line in detail section |

### Line Item Calculation Formula

```
MontoItem = (PrecioUnitarioItem × CantidadItem) - MontoDescuentoItem
```

---

## Tax Calculations

### ISC (Impuesto Selectivo al Consumo) — Section 14

#### Alcoholic Beverages

| Element | Description |
|---------|-------------|
| `MontoImpuestoSelectivoConsumoEspecifico` | Based on liters of pure alcohol |
| `MontoImpuestoSelectivoConsumoAdvalorem` | Ad valorem component |

#### Cigarettes

Uses specific rates per unit/pack.

### CDT (Contribución al Desarrollo de las Telecomunicaciones) — Section 15

| Property | Value |
|----------|-------|
| **Rate** | 2% |
| **Applies to** | Telecommunications services |

### Propina Legal (Legal Tip)

| Property | Value |
|----------|-------|
| **Rate** | 10% |
| **Applies to** | Restaurants, bars, hotels |

---

## Norma General 07-07 (Section 16)

Applies to specific sectors where only a portion of the service is taxed (e.g., 90% exempt, 10% taxed).

**Implementation Requirement:**

The XML must show **two separate items** in the detail section:
1. One item with `IndicadorMontoGravado = 2` (Exempt portion)
2. One item with `IndicadorMontoGravado = 1` (Taxed portion)

---

## Printed Representation (Representación Impresa) Requirements

The printed version of an e-CF must include:

| Element | Description |
|---------|-------------|
| **Header** | Text: "Comprobante Fiscal Electrónico" |
| **Type Name** | Literal name (e.g., "FACTURA DE CONSUMO ELECTRÓNICA") |
| **QR Code** | Contains URL for DGII verification |
| **Security Code** | 6-character alphanumeric from digital signature (`CodigoSeguridad`) |
| **Legend** | Text: "Documento firmado electrónicamente" |

---

## Key XML Elements Reference

| Element | Description | Section |
|---------|-------------|---------|
| `ECF` | Root element | — |
| `Encabezado` | Header section | A |
| `Emisor` | Issuer information | A |
| `Receptor` | Recipient information | A |
| `Totales` | Total amounts | A |
| `DetalleItem` | Line item | B |
| `SubtotalInformativo` | Informational subtotal | C |
| `DescuentoORecargo` | Discount or surcharge | D |
| `CodigoSeguridad` | Security code for QR | — |
| `FirmaDigital` | Digital signature block | — |

---

## Technical Constraints

> [!IMPORTANT]
> **Line Item Limit**: e-CF documents have a maximum limit of **1,000 line items** (items in the Detalle section).

### Other Constraints
- **File Name**: Must strictly follow `[RNC]E[Type][Sequence].xml` format.
- **Encoding**: UTF-8 is mandatory.
- **Floating Point**: Max 2 decimals for monetary values (with specific exceptions for unit prices).

---

---

## Contingency Operations (Operación en Contingencia)

Defined as exceptional situations preventing normal e-CF emission.

### Scenario A: No Connection (Falta de Conectividad)
If you cannot connect to DGII Web Services:

1. Continue emitting e-CFs locally (generate, sign, and store)
2. **Queue** them for transmission
3. Send them to DGII immediately when connection is restored
4. **Printed Representation Note**: Include the legend "Consulte su validez después de 72 horas"

### Scenario B: Deferred Sending (Envío Diferido)
For batch/asynchronous transmission:

1. Generate and sign e-CFs normally
2. Queue for later transmission (within 24 hours)
3. **Printed Representation Note**: Include "Consulte su validez después de 24 horas"

### Scenario C: Technical Incapacity (Incapacidad Técnica)
If your software is down, certificates expired, or signing is broken:

1. Issue **Series B** (Paper NCF) invoices to clients
2. Keep records of all B-series issued during incapacity
3. Once resolved:
   - Generate a corresponding **Series E** (e-CF) for each Series B issued
   - **Do NOT** send this e-CF to the client (they already have the Series B)
   - Send the e-CF to **DGII only**
   - Include the Series B NCF in the **Reference Information** section with `CodigoModificacion = 4` (NCF Contingencia)

> [!WARNING]
> The taxpayer must maintain authorized B-series NCF sequences for contingency use.
> The printed document during technical incapacity will **not** have a QR code.

---

## Summary

This technical report provides the complete specification for:

1. Understanding the 10 types of e-CF documents
2. XML structure and mandatory sections
3. Tax calculation rules (ITBIS, ISC, CDT, Propina Legal)
4. Rounding and tolerance requirements
5. Printed representation requirements
