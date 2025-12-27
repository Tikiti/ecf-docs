# Consumer Invoice Summary (RFCE) XML Format v1.0

> **Original**: Formato Resumen Factura de Consumo Electrónica (RFCE) V1.0  
> **Source**: [Formato Resumen Factura de Consumo Electrónica (RFCE) V1.0.pdf](file:///home/romulo/visual/ecf/ecf-docs/Formatos%20XML/Formato%20Resumen%20Factura%20de%20Consumo%20Electr%C3%B3nico%20v1.0.pdf)  
> **Pages**: 12  
> **Scope**: Consumer invoices (type 32) under RD$ 250,000

---

## Overview

The RFCE (Resumen de Factura de Consumo Electrónica) is a **simplified summary format** for electronic consumption invoices (type 32) with amounts **under RD$ 250,000**. Unlike the full e-CF, it does **not** include item-by-item details.

> [!IMPORTANT]
> **Routing Rules:**
> - Consumer invoices **≥ RD$250,000** → Use full e-CF format → Send to `ecf.dgii.gov.do`
> - Consumer invoices **< RD$250,000** → Use RFCE format → Send to `fc.dgii.gov.do`

---

## API Endpoint

| Parameter | Value |
|-----------|-------|
| **Method** | `POST` |
| **Domain** | `fc.dgii.gov.do` (NOT `ecf.dgii.gov.do`) |
| **Service Path** | `{ambiente}/recepcionfc/api/recepcion/ecf` |
| **Endpoint** | `/api/recepcion/ecf` |
| **Pre-cert URL** | `https://fc.dgii.gov.do/testecf/recepcionfc/api/recepcion/ecf` |
| **Cert URL** | `https://fc.dgii.gov.do/certecf/recepcionfc/api/recepcion/ecf` |
| **Prod URL** | `https://fc.dgii.gov.do/ecf/recepcionfc/api/recepcion/ecf` |
| **Body** | Signed RFCE XML (`multipart/form-data`, field: `xml`) |
| **Response** | Immediate validation (no TrackID) |

---

## Document Structure

```xml
<RFCE>
  <Encabezado>
    <IdDoc>...</IdDoc>
    <Emisor>...</Emisor>
    <Comprador>...</Comprador>  <!-- Optional -->
    <Totales>...</Totales>
  </Encabezado>
  <CodigoSeguridadeCF>...</CodigoSeguridadeCF>
  <Signature>...</Signature>
</RFCE>
```

---

## Obligatoriedad Codes

| Code | Meaning |
|------|---------|
| `1` | **Obligatorio** (Mandatory) |
| `2` | **Condicional** (Conditional) |
| `3` | **Opcional** (Optional) |

---

## Section A: Encabezado

### A.1 IdDoc (Document Identification)

| # | Element | Description | Max | Type | Validation | Oblig |
|---|---------|-------------|-----|------|------------|-------|
| 1 | `<Version>` | Format version | 3 | ALFANUM | Fixed: `1.0` | 1 |
| 2 | `<TipoeCF>` | e-CF type code | 2 | NUM | Fixed: `32` | 1 |
| 3 | `<eNCF>` | Electronic fiscal number | 13 | ALFANUM | Valid e-NCF format | 1 |
| 4 | `<TipoIngresos>` | Income type code | 2 | NUM | Values 01-06 | 1 |
| 5 | `<TipoPago>` | Payment type | 1 | NUM | 1=Cash, 2=Credit, 3=Free | 1 |
| — | `<TablaFormasPago>` | Payment methods container | — | — | Up to 7 repetitions | 3 |
| — | `<FormaDePago>` | Payment method entry | — | — | Container for each method | 3 |
| 6 | `<FormaPago>` | Payment method code | 2 | NUM | 1-8 (see codes below) | 3 |
| 7 | `<MontoPago>` | Payment amount | 18 | NUM | ≥0, 2 decimals | 2 |

**Payment Method Codes (FormaPago):**

| Code | Description |
|------|-------------|
| 1 | Efectivo (Cash) |
| 2 | Cheque/Transferencia/Depósito |
| 3 | Tarjeta de Crédito/Débito |
| 4 | Venta a Crédito |
| 5 | Bonos o Certificados de regalo |
| 6 | Permuta |
| 7 | Nota de crédito |
| 8 | Otras Formas de pago |

> [!NOTE]
> **Footnote 1**: For each `<TablaFormasPago>` entry, fields are grouped within `<FormaDePago>` containing a `<FormaPago>` and `<MontoPago>` pair.

---

### A.2 Emisor (Issuer)

| # | Element | Description | Max | Type | Validation | Oblig |
|---|---------|-------------|-----|------|------------|-------|
| 8 | `<RNCEmisor>` | Issuer RNC | 9/11 | NUM | Valid RNC, authorized, active, no blocks | 1 |
| 9 | `<RazonSocialEmisor>` | Legal name | 150 | ALFANUM | — | 1 |
| 10 | `<FechaEmision>` | Issue date | 10 | ALFANUM | DD-MM-YYYY format | 1 |

**RNC Validation Rules:**
- a) RNC must match proper format (9 or 11 digits)
- b) RNC must be authorized as Electronic Invoicer
- c) RNC must be in "Active" status
- d) RNC must have no blocking marks

---

### A.3 Comprador (Buyer) — Optional

| # | Element | Description | Max | Type | Validation | Oblig |
|---|---------|-------------|-----|------|------------|-------|
| 11 | `<RNCComprador>` | Buyer RNC | 9/11 | NUM | — | 3 |
| 12 | `<IdentificadorExtranjero>` | Foreign ID | 20 | ALFANUM | For foreigners without RNC | 2 |
| 13 | `<RazonSocialComprador>` | Buyer name | 150 | ALFANUM | — | 3 |

> [!NOTE]
> **Footnote 2**: If `IdentificadorExtranjero` is populated, `RNCComprador` must be blank.
>
> **Footnote 3**: Conditional on buyer being a foreigner without RNC/Cédula.

---

### A.4 Totales

| # | Element | Description | Max | Type | Validation | Oblig |
|---|---------|-------------|-----|------|------------|-------|
| 14 | `<MontoGravadoTotal>` | Total taxable amount | 18 | NUM | Sum of I1+I2+I3, ≥0, 2 dec | 2 |
| 15 | `<MontoGravadoI1>` | Taxable at ITBIS 18% | 18 | NUM | ≥0, 2 decimals | 2 |
| 16 | `<MontoGravadoI2>` | Taxable at ITBIS 16% | 18 | NUM | ≥0, 2 decimals | 2 |
| 17 | `<MontoGravadoI3>` | Taxable at ITBIS 0% | 18 | NUM | ≥0, 2 decimals | 2 |
| 18 | `<MontoExento>` | Exempt amount | 18 | NUM | ≥0, 2 decimals | 2 |
| 19 | `<TotalITBIS>` | Total ITBIS | 18 | NUM | Sum of ITBIS1+2+3, ≥0 | 2 |
| 20 | `<TotalITBIS1>` | ITBIS at 18% | 18 | NUM | MontoGravadoI1 × 0.18 | 2 |
| 21 | `<TotalITBIS2>` | ITBIS at 16% | 18 | NUM | MontoGravadoI2 × 0.16 | 2 |
| 22 | `<TotalITBIS3>` | ITBIS at 0% | 18 | NUM | = 0 | 2 |
| 23 | `<MontoImpuestoAdicional>` | Additional taxes total | 18 | NUM | Sum of ISC + Others, ≥0 | 2 |

**Additional Taxes Area:**

| # | Element | Description | Max | Type | Validation | Oblig |
|---|---------|-------------|-----|------|------------|-------|
| 24 | `<TipoImpuesto>` | Tax code | 3 | NUM | Validate with Table I | 2 |
| 25 | `<MontoImpuestoSelectivoConsumoEspecifico>` | ISC Specific | 18 | NUM | >0, 2 decimals | 2 |
| 26 | `<MontoImpuestoSelectivoConsumoAdvalorem>` | ISC Ad-Valorem | 18 | NUM | >0, 2 decimals | 2 |
| 27 | `<OtrosImpuestosAdicionales>` | Other taxes | 18 | NUM | >0, 2 decimals | 2 |

**Final Totals:**

| # | Element | Description | Max | Type | Validation | Oblig |
|---|---------|-------------|-----|------|------------|-------|
| 28 | `<MontoTotal>` | Grand total | 18 | NUM | Sum of all components, ≥0 | 1 |
| 29 | `<MontoNoFacturable>` | Non-billable amounts | 18 | NUM | Can be negative | 2 |
| 30 | `<MontoPeriodo>` | Period amount | 18 | NUM | MontoTotal + MontoNoFacturable | 3 |

> [!NOTE]
> **Formula**: `MontoTotal` = `MontoGravadoTotal` + `MontoExento` + `TotalITBIS` + `MontoImpuestoAdicional`
>
> **Formula**: `MontoPeriodo` = `MontoTotal` + `MontoNoFacturable`

---

### A.5 Security Code

| # | Element | Description | Max | Type | Validation | Oblig |
|---|---------|-------------|-----|------|------------|-------|
| 31 | `<CodigoSeguridadeCF>` | Security code | 6 | ALFANUM | First 6 chars of SignatureValue hash | 1 |

---

## Section B: Digital Signature

| # | Element | Description | Oblig |
|---|---------|-------------|-------|
| 1 | `<Signature>` | XMLDSig enveloped signature | 1 |

See [Digital Signing Guide](../guides/digital-signing-guide.md) for implementation.

---

## Key Differences from Full e-CF

| Feature | Full e-CF | RFCE |
|---------|-----------|------|
| Root Element | `<ECF>` | `<RFCE>` |
| Item Detail | Yes (`<DetallesItems>`) | **No** |
| Subtotals | Yes (`<Subtotales>`) | No |
| Discounts/Surcharges | Yes | No |
| Reference Info | Yes | No |
| Scope | All invoice types | Type 32 < RD$250k only |
| TrackID | Yes | **No** (immediate response) |
| Domain | `ecf.dgii.gov.do` | `fc.dgii.gov.do` |

---

## Business Rules

1. **Scope**: Only for `TipoeCF = 32` with `MontoTotal < RD$250,000`
2. **RNC Validation**: `RNCEmisor` must be valid, registered, active
3. **Tax Calculation**: `TotalITBIS = TotalITBIS1 + TotalITBIS2 + TotalITBIS3`
4. **Security Code**: Derived from first 6 characters of digital signature hash
5. **Buyer Info**: Optional for consumer invoices under threshold
6. **Foreign Buyers**: If `IdentificadorExtranjero` used, `RNCComprador` must be empty

---

## Income Type Codes (TipoIngresos)

| Code | Description |
|------|-------------|
| 01 | Ingresos por operaciones |
| 02 | Ingresos financieros |
| 03 | Ingresos extraordinarios |
| 04 | Ingresos por arrendamientos |
| 05 | Ingresos por venta de activo depreciable |
| 06 | Otros ingresos |

---

## Payment Type Codes (TipoPago)

| Code | Description |
|------|-------------|
| 1 | Contado (Cash/Immediate) |
| 2 | Crédito (Credit) |
| 3 | Gratuito (Free/No charge) |

> [!WARNING]
> Invoices with `TipoPago = 3` (Gratuito) cannot be used for tax credit purposes.

---

## PDF Specification Footnotes

> [!NOTE]
> **Important footnotes from the official DGII PDF specification:**
>
> **Footnote 1**: By XML definition, for each element there must be a container tag that groups the fields contained in a table. Example: in the case of `<TablaFormasPago>`, they are grouped within the `<FormaDePago>` tag for each `<FormaPago>` and `<MontoPago>` pair specified.
>
> **Footnote 2**: If `IdentificadorExtranjero` is populated, `RNCComprador` must be blank (see Section A.3 Comprador).
>
> **Footnote 3**: If the 'Foreign Identifier' field is completed, the 'Buyer RNC' field must be blank.
>
> **Footnote 4**: In fields where numeric values of 16 integers and 2 decimals exist, the rounding rule must be applied according to the e-CF Technical Report.
>
> **Footnote 5**: See Footnote 2 above.
>
> **Footnote 6**: According to the 'Additional Tax Types Codification' Table, included in the e-CF Format document.

