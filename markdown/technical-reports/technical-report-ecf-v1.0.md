# Technical Report: Electronic Fiscal Voucher (e-CF) v1.0

> **Original**: Informe Técnico Comprobante Fiscal Electrónico v1.0  
> **Source**: [Informe Técnico e-CF v1.0.pdf](file:///home/romulo/visual/ecf/ecf-docs/Informe%20y%20Descripci%C3%B3n%20T%C3%A9cnica/Informe%20T%C3%A9cnico%20e-CF%20v1.0.pdf)  
> **Pages**: 52

---

## Overview

This document serves as the primary technical guide for the DGII e-CF system, providing essential logic for XML generation, tax calculation accuracy, and structural integrity.

---

## Actors in the System

| Actor | Description |
|-------|-------------|
| **Electronic Issuer** | Emisor Electrónico - entity that issues e-CFs |
| **Electronic Receptor** | Receptor Electrónico - entity that receives e-CFs electronically |
| **Non-Electronic Receptor** | Receptor No Electrónico - receives printed representation only |

---

## Web Services Overview (Section 4)

The DGII provides the following REST API services for e-CF operations:

| Service | Description |
|---------|-------------|
| **4.1 Autenticación** | Token generation via signed seed (1-hour validity) |
| **4.2 Recepción e-CF** | Submit e-CF XML, returns `TrackId` |
| **4.3 Recepción RFCE** | Submit consumer invoice summary (< RD$250k) |
| **4.4 Recepción Aprobación Comercial** | Submit ACECF (acceptance/rejection) to DGII |
| **4.5 Consulta Resultado e-CF** | Query e-CF status by `TrackId` (for issuers) |
| **4.6 Consulta Estado e-CF** | Query e-CF validity (for receivers) |
| **4.7 Consulta TrackId e-CF** | Get all TrackIds for an e-NCF |
| **4.8 Consulta Directorio** | Lookup receiver's service URLs |
| **4.9 Consulta Estatus Servicios** | Check DGII service availability |
| **4.10 Anulación e-NCF** | Cancel unused e-NCF sequences |

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

### Section D: Descuentos o Recargos — Conditional

Global discounts or charges applied to the entire invoice.

### Section E: Paginación — Optional

### Section E: Paginación — Optional

Required **only** when the printed representation exceeds one page. It must appear on all pages except the last one (which contains the global totals).

| Element | Description |
|---------|-------------|
| `PaginaNo` | Sequential page number (starts at 1) |
| `SubtotalGravadoPagina` | Sum of taxed amounts on this page |
| `SubtotalExentoPagina` | Sum of exempt items on this page |
| `SubtotalItbisPagina` | Sum of ITBIS on this page |
| `SubtotalImpuestoAdicionalPagina` | Sum of ISC + Other Taxes on this page |
| `MontoTotalPagina` | Grand total for items on this page |

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

### Notification Requirement
The issuer **must immediately notify** DGII of the contingency state via:
1.  **Office Virtual (OFV)**: Contingency Module
2.  **Contact Center**: Notification of situation and type

### Contingency Types (Tipos de Contingencia)

| Type | Definition | End Condition |
|------|------------|---------------|
| **Total Contingency** | System failure affecting **all** operations/branches. | Ends when DGII receives the first e-CF or user notifies resolution. |
| **Partial Contingency** | System failure affecting **some** branches/POS, while others operate normally. | Ends when user notifies resolution for those specific branches. |

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
