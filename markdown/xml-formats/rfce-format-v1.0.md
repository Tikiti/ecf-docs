# Consumer Invoice Summary (RFCE) XML Format v1.0

> **Original**: Formato Resumen Factura de Consumo Electrónica (RFCE) V1.0  
> **Source**: [Formato Resumen Factura de Consumo Electrónica (RFCE) V1.0.pdf](file:///home/romulo/visual/ecf/ecf-docs/Formatos%20XML/Formato%20Resumen%20Factura%20de%20Consumo%20Electr%C3%B3nica%20(RFCE)%20V1.0.pdf)  
> **Scope**: Consumer invoices under RD$ 250,000

---

## Overview

The RFCE (Resumen de Factura de Consumo Electrónica) is a **simplified summary format** for electronic consumption invoices (type 32) with amounts **under RD$ 250,000**. Unlike the full e-CF, it does **not** include item-by-item details.

> [!IMPORTANT]
> **Routing Rule:**
> - Consumer invoices **≥ RD$250,000** → Use full e-CF format → Send to `ecf.dgii.gov.do`
> - Consumer invoices **< RD$250,000** → Use RFCE format → Send to `fc.dgii.gov.do`

**API Endpoint for RFCE Submission:**
- **Method**: `POST`
- **Base URL**: `https://fc.dgii.gov.do/{ambiente}/recepcionfc`
- **Endpoint**: `/api/RecepcionFC`
- **Body**: Signed RFCE XML
- **Response**: Immediate validation response (no TrackID required)

---

## Document Structure

```
<RFCE>
  <Encabezado>
    <IdDoc>...</IdDoc>
    <Emisor>...</Emisor>
    <Comprador>...</Comprador>  <!-- Optional -->
    <Totales>...</Totales>
  </Encabezado>
  <CodigoSeguridadeCF>...</CodigoSeguridadeCF>
  <FechaHoraFirma>...</FechaHoraFirma>
  <Signature>...</Signature>
</RFCE>
```

---

## XML Element Definitions

### IdDoc (Document Identification)

| Element | Type | Max Len | Req | Description |
|---------|------|---------|-----|-------------|
| `Version` | ALFANUM | 3 | 1 | Fixed: `1.0` |
| `TipoeCF` | NUM | 2 | 1 | Fixed: `32` (Consumer Invoice) |
| `eNCF` | ALFANUM | 13 | 1 | Sequence authorized by DGII |
| `TipoIngresos` | NUM | 2 | 1 | Income type (01-06) |
| `TipoPago` | NUM | 1 | 1 | Payment method type |

### Emisor (Issuer)

| Element | Type | Max Len | Req | Description |
|---------|------|---------|-----|-------------|
| `RNCEmisor` | NUM | 9/11 | 1 | Issuer's RNC |
| `RazonSocialEmisor` | ALFANUM | 150 | 1 | Issuer's legal name |
| `FechaEmision` | DATE | 10 | 1 | Format: DD-MM-YYYY |

### Comprador (Buyer) — Optional

| Element | Type | Max Len | Req | Description |
|---------|------|---------|-----|-------------|
| `RNCComprador` | NUM | 9/11 | 3 | Buyer's RNC |
| `IdentificadorExtranjero` | ALFANUM | 20 | 2 | Foreign ID (if applicable) |
| `RazonSocialComprador` | ALFANUM | 150 | 3 | Buyer's name |

### Totales

| Element | Type | Max Len | Req | Description |
|---------|------|---------|-----|-------------|
| `MontoGravadoTotal` | NUM | 18 | 2 | Total taxable amount |
| `MontoGravadoI1` | NUM | 18 | 2 | Taxable base at 18% |
| `MontoGravadoI2` | NUM | 18 | 2 | Taxable base at 16% |
| `MontoGravadoI3` | NUM | 18 | 2 | Taxable base at 0% |
| `MontoExento` | NUM | 18 | 2 | Exempt amount |
| `TotalITBIS` | NUM | 18 | 2 | Total ITBIS |
| `TotalITBIS1` | NUM | 18 | 2 | ITBIS at 18% |
| `TotalITBIS2` | NUM | 18 | 2 | ITBIS at 16% |
| `MontoTotal` | NUM | 18 | 1 | Grand total |

> [!NOTE]
> **Formula**: `MontoTotal` = `MontoGravadoTotal` + `MontoExento` + `TotalITBIS` + `MontoImpuestoAdicional`

### Security Elements

| Element | Type | Max Len | Req | Description |
|---------|------|---------|-----|-------------|
| `CodigoSeguridadeCF` | ALFANUM | 6 | 1 | First 6 chars of signature hash |
| `FechaHoraFirma` | ALFANUM | 19 | 1 | Format: DD-MM-YYYY HH:MM:SS |

### Impuestos Adicionales (Additional Taxes)

Applies when the consumer invoice includes ISC or other special taxes.

| Element | Type | Max Len | Req | Description |
|---------|------|---------|-----|-------------|
| `TipoImpuesto` | NUM | 3 | 2 | Tax code from Table I (see e-CF format) |
| `MontoImpuestoSelectivoConsumoEspecifico` | NUM | 18 | 2 | ISC Specific amount |
| `MontoImpuestoSelectivoConsumoAdvalorem` | NUM | 18 | 2 | ISC Ad-Valorem amount |
| `OtrosImpuestosAdicionales` | NUM | 18 | 2 | Other additional taxes |

### Non-Billable Amounts

| Element | Type | Max Len | Req | Description |
|---------|------|---------|-----|-------------|
| `MontoNoFacturable` | NUM | 18 | 2 | Non-billable amounts (can be negative) |
| `MontoPeriodo` | NUM | 18 | 3 | Period amount |

> [!NOTE]
> **Formula**: `MontoPeriodo` = `MontoTotal` + `MontoNoFacturable`

---

## Key Differences from Full e-CF

| Feature | Full e-CF | RFCE |
|---------|-----------|------|
| Root Element | `<ECF>` | `<RFCE>` |
| Item Detail | Yes (`<DetallesItems>`) | **No** |
| Subtotals | Yes (`<Subtotales>`) | No |
| Discounts/Surcharges | Yes | No |
| Reference Info | Yes | No |
| Scope | All invoice types | Only type 32 < RD$250k |

---

## Business Rules

1. **Scope**: Only for `TipoeCF = 32` with total under **RD$ 250,000**
2. **RNC Validation**: `RNCEmisor` must be valid registered RNC
3. **Tax Calculation**: `TotalITBIS` must equal sum of individual ITBIS rates
4. **Security Code**: Must derive from actual digital signature
5. **Buyer Info**: Optional unless foreign ID conditions apply

---

## Requirement Codes

| Code | Meaning |
|------|---------|
| `1` | Mandatory |
| `2` | Conditional |
| `3` | Optional |
