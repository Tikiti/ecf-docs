# Electronic Fiscal Voucher (e-CF) XML Format v1.0

> **Original**: Formato Comprobante Fiscal Electrónico (e-CF) V1.0  
> **Source**: [Formato Comprobante Fiscal Electrónico (e-CF) V1.0.pdf](file:///home/romulo/visual/ecf/ecf-docs/Formatos%20XML/Formato%20Comprobante%20Fiscal%20Electr%C3%B3nico%20(e-CF)%20V1.0.pdf)  
> **Pages**: 87

---

## Overview

This document defines the complete XML structure for electronic invoices in the Dominican Republic's DGII system. It covers all element definitions, data types, constraints, and validation rules.

---

## Technical Standards

| Standard | Value |
|----------|-------|
| **Encoding** | UTF-8 |
| **Format** | XML |
| **Namespace** | DGII e-CF Schema |

---

## XML Structure Sections

1. **Encabezado** (Header) - Document identification, parties, totals
2. **Detalle** (Line Items) - Individual goods/services
3. **Subtotales Informativos** - Informational subtotals
4. **Descuentos o Recargos Globales** - Global discounts/surcharges
5. **Información de Referencia** - Reference information
6. **Otros Impuestos** - Additional taxes

---

## Section 3.1: Encabezado (Header)

### 3.1.1 IdDoc (Document Identification)

| Element | Type | Max Len | Req | Description |
|---------|------|---------|-----|-------------|
| `Version` | NUM | 3 | R | Current version: `1.0` |
| `eNCF` | ALFA | 13 | R | Electronic fiscal sequence number |
| `FechaEmision` | DATE | 10 | R | Format: `DD-MM-YYYY` |
| `TipoeCF` | NUM | 2 | R | e-CF type code (31-47) |
| `TipoIngresos` | NUM | 2 | O | Income type for ISR purposes |
| `TipoPago` | NUM | 1 | O | Payment type |
| `FechaVencimiento` | DATE | 10 | O | Expiration date |

### 3.1.2 Emisor (Issuer)

| Element | Type | Max Len | Req | Description |
|---------|------|---------|-----|-------------|
| `RNCEmisor` | NUM | 9/11 | R | Issuer's RNC |
| `RazonSocialEmisor` | ALFA | 150 | R | Legal name |
| `NombreComercial` | ALFA | 150 | O | Trade name |
| `Sucursal` | ALFA | 10 | O | Branch code |
| `DireccionEmisor` | ALFA | 200 | O | Address |
| `MunicipioEmisor` | NUM | 6 | O | Municipality code |
| `ProvinciaEmisor` | NUM | 2 | O | Province code |
| `TelefonoEmisor` | ALFA | 15 | O | Phone |
| `CorreoEmisor` | ALFA | 100 | O | Email |
| `FechaEmisionNCF` | DATE | 10 | O | NCF issue date |

### 3.1.3 Comprador (Buyer)

| Element | Type | Max Len | Req | Description |
|---------|------|---------|-----|-------------|
| `RNCComprador` | NUM | 9/11 | C | Buyer's RNC (see conditions below) |
| `IdentificadorExtranjero` | ALFA | 20 | C | Foreign ID (when buyer has no RNC) |
| `RazonSocialComprador` | ALFA | 150 | C | Legal name |
| `ContactoComprador` | ALFA | 100 | O | Contact name |
| `CorreoComprador` | ALFA | 100 | O | Email |
| `DireccionComprador` | ALFA | 200 | O | Address |
| `MunicipioComprador` | NUM | 6 | O | Municipality code |
| `ProvinciaComprador` | NUM | 2 | O | Province code |

**Buyer Identification Rules:**

| e-CF Type | Condition | Requirement |
|-----------|-----------|-------------|
| `31` (Credit Fiscal) | Always | `RNCComprador` **mandatory** |
| `32` (Consumer) | Total ≥ RD$250,000 | `RNCComprador` **required** |
| `32` (Consumer) | Total < RD$250,000 | `RNCComprador` **optional** |
| `32` (Consumer) | Foreign buyer, no RNC | `IdentificadorExtranjero` required |
| `33/34` (Notes) | Modifying e-CF type 32 ≥ RD$250k | Same buyer ID as original |
| `46` (Exports/FTZ) | Resident buyer | `RNCComprador` required |
| `46` (Exports/FTZ) | Non-resident buyer | `IdentificadorExtranjero` required |

### 3.1.5 Totales

| Element | Type | Max Len | Req | Description |
|---------|------|---------|-----|-------------|
| `MontoGravadoTotal` | DEC | 18 | O | Total taxable amount |
| `MontoGravadoI1` | DEC | 18 | O | Amount at ITBIS rate 1 (18%) |
| `MontoGravadoI2` | DEC | 18 | O | Amount at ITBIS rate 2 (16%) |
| `MontoGravadoI3` | DEC | 18 | O | Amount at ITBIS rate 3 (0%) |
| `MontoExento` | DEC | 18 | O | Exempt amount |
| `ITBIS1` | DEC | 18 | O | ITBIS at 18% |
| `ITBIS2` | DEC | 18 | O | ITBIS at 16% |
| `ITBIS3` | DEC | 18 | O | ITBIS at 0% |
| `TotalITBIS` | DEC | 18 | O | Total ITBIS |
| `TotalISC` | DEC | 18 | O | Total selective consumption tax |
| `TotalOtrosImpuestos` | DEC | 18 | O | Total other taxes |
| `MontoTotal` | DEC | 18 | R | Grand total |
| `MontoNoFacturable` | DEC | 18 | O | Non-billable amounts |
| `MontoPeriodo` | DEC | 18 | O | Period amount |

---

## Section 3.2: Detalle (Line Items)

| Element | Type | Max Len | Req | Description |
|---------|------|---------|-----|-------------|
| `NumeroLinea` | NUM | 4 | R | Sequential from 1 |
| `IndicadorFacturacion` | NUM | 1 | O | Tax indicator |
| `NombreItem` | ALFA | 200 | R | Item description |
| `IndicadorBienServicio` | NUM | 1 | O | 1=Good, 2=Service |
| `CantidadItem` | DEC | 18 | R | Quantity (up to 6 decimals) |
| `UnidadMedida` | ALFA | 3 | O | Unit of measure |
| `PrecioUnitarioItem` | DEC | 18 | R | Unit price (up to 4 decimals) |
| `DescuentoMonto` | DEC | 18 | O | Discount amount |
| `TablaSubDescuento` | — | — | O | Sub-discount breakdown |
| `MontoItem` | DEC | 18 | R | Line total |

### IndicadorFacturacion Values

| Value | Meaning |
|-------|---------|
| `1` | Gravado (Taxed at standard rate) |
| `2` | Exento (Exempt) |
| `3` | Tasa Cero (Zero rate) |

---

## Section 3.3: Subtotales Informativos

Optional section for informational subtotals that don't affect main totals.

| Element | Type | Max Len | Req | Description |
|---------|------|---------|-----|-------------|
| `NumeroSubtotal` | NUM | 3 | R | Subtotal number |
| `DescripcionSubtotal` | ALFA | 100 | R | Description |
| `MontoSubtotal` | DEC | 18 | R | Amount |
| `Orden` | NUM | 3 | O | Display order |

---

## Section 3.4: Descuentos o Recargos Globales

| Element | Type | Max Len | Req | Description |
|---------|------|---------|-----|-------------|
| `NumeroDescuentoRecargo` | NUM | 3 | R | Sequence number |
| `TipoDescuentoRecargo` | NUM | 1 | R | 1=Discount, 2=Surcharge |
| `Descripcion` | ALFA | 100 | O | Description |
| `Porcentaje` | DEC | 5 | O | Percentage |
| `MontoDescuentoRecargo` | DEC | 18 | R | Amount |
| `IndicadorMontoGravado` | NUM | 1 | O | Tax indicator |

---

## Section 3.5: Paginación (Pagination)

Used for printed representation to indicate line items per page.

| Element | Type | Max Len | Req | Description |
|---------|------|---------|-----|-------------|
| `NoPagina` | NUM | 3 | 2 | Page number |
| `NoLineaDesde` | NUM | 4 | 2 | Starting line item |
| `NoLineaHasta` | NUM | 4 | 2 | Ending line item |
| `SubtotalMontoGravadoPagina` | DEC | 18 | 2 | Page subtotal (taxable) |
| `SubtotalItbisPagina` | DEC | 18 | 2 | Page subtotal (ITBIS) |

---

## Section 3.6: Información de Referencia

Used for Notes (Credit/Debit) to reference the modified e-CF(s).

| Element | Type | Max Len | Req | Description |
|---------|------|---------|-----|-------------|
| `NCFModificado` | ALFA | 13 | 1 | e-NCF of the invoice being modified |
| `RNCOtroContribuyente` | NUM | 11 | 2 | RNC if different from original buyer |
| `FechaNCFModificado` | DATE | 10 | 1 | Issue date of modified e-CF |
| `CodigoModificacion` | NUM | 2 | 1 | Modification type (see below) |

**Modification Codes:**

| Code | Description |
|------|-------------|
| `1` | Anula documento completo (Full cancellation) |
| `2` | Corrige texto (Text correction) |
| `3` | Corrige montos (Amount correction) |
| `4` | Referencia NCF contingencia (Contingency reference) |
| `5` | Sustituye e-NCF provisional (Replaces provisional) |

> [!NOTE]
> Reference Information is **mandatory** for types 33 (Debit Note) and 34 (Credit Note).

---

## Section 3.7: Firma Digital (Digital Signature)

| Element | Type | Req | Description |
|---------|------|-----|-------------|
| `FechaHoraFirma` | DATETIME | 1 | Format: DD-MM-YYYY HH:MM:SS |
| `Signature` | XML-DSig | 1 | Enveloped signature covering entire document |

See [Digital Signing Guide](../guides/digital-signing-guide.md) for implementation details.

---

## Code Tables

### Table I: e-CF Types (TipoeCF)

| Code | Description |
|------|-------------|
| `31` | Factura de Crédito Fiscal Electrónica |
| `32` | Factura de Consumo Electrónica |
| `33` | Nota de Débito Electrónica |
| `34` | Nota de Crédito Electrónica |
| `41` | Comprobante de Compras Electrónico |
| `43` | Comprobante de Gastos Menores Electrónico |
| `44` | Comprobante de Regímenes Especiales Electrónico |
| `45` | Comprobante Gubernamental Electrónico |
| `46` | Comprobante para Exportaciones Electrónico |
| `47` | Comprobante para Pagos al Exterior Electrónico |

### Table II: Payment Methods (FormaPago)

| Code | Description |
|------|-------------|
| `01` | Efectivo (Cash) |
| `02` | Cheque/Transferencia/Depósito |
| `03` | Tarjeta de Crédito/Débito |
| `04` | Compra a Crédito |

### Table III: Income Types (TipoIngresos)

| Code | Description |
|------|-------------|
| `01` | Ingresos por operaciones (Operational income) |
| `02` | Ingresos financieros (Financial income) |
| `03` | Ingresos extraordinarios (Extraordinary income) |
| `04` | Ingresos por arrendamientos (Rental income) |
| `05` | Ingresos por venta de activo depreciable (Asset sale) |
| `06` | Otros ingresos (Other income) |

### Table IV: Payment Types (TipoPago)

| Code | Description |
|------|-------------|
| `1` | Contado (Cash/Immediate) |
| `2` | Crédito (Credit) |
| `3` | Gratuito (Free/No charge) |

---

## Validation Rules

| Rule | Description |
|------|-------------|
| **E01** | `eNCF` must match issuer RNC and be from an authorized range |
| **E05** | For type `31`, `RNCComprador` is mandatory and must be valid/active |
| **E32** | For type `32` ≥ RD$250,000, buyer identification is mandatory |
| **Date** | `FechaEmision` cannot be >30 days in past from submission |
| **Total** | `MontoTotal` = sum of `MontoItem` + taxes - discounts |
| **Signature** | `RNCEmisor` must match the signer's authorized RNC |
| **Expiry** | e-NCF sequence must not be expired at submission time |

> [!CAUTION]
> **Empty Tags Are Forbidden**: Do not include empty elements like `<Field></Field>` or `<Field />`. If a value is null/empty, **omit the tag entirely**.

---

## Data Type Reference

| Type | Description |
|------|-------------|
| `ALFA` | Alphanumeric string |
| `NUM` | Numeric (integers) |
| `DEC` | Decimal number |
| `DATE` | Date in DD-MM-YYYY format |

**Requirement Codes:**
- `R` = Required
- `O` = Optional
- `C` = Conditional
