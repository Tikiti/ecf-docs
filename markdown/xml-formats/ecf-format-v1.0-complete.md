# Electronic Fiscal Voucher Format (e-CF) V1.0

**Version**: 1.0 | October 2025  
**Pages**: 87

---

## Version History (Bitácora)

| Date | Changes |
|------|---------|
| **09-10-2025** | Added "Colombian Peso" to Currency Table (Tabla II) |
| **17-09-2024** | Added "Haitian Gourde" and "Mexican Peso" currencies to Tabla II. Added units to Tabla IV: Hectare, Milliliter, Milligram, Ounces, Troy Ounces |
| **30-08-2022** | Added "Tray" unit of measure to Tabla IV |
| **06-05-2022** | Added units: Gross Register Tonnage, Square Foot, Passenger, Inches, Ship Dock Parking |
| **19-11-2021** | Updated Buyer obligatoriedad codes (1→2) for Electronic Credit/Debit Note |
| **04-11-2021** | Added "Quintal" unit of measure |
| **29-06-2021** | Separated Province and Municipality codes into columns in Tabla III |
| **10-11-2020** | Removed accents from `<Liquidacion>` and `<Mineria>` tags. Updated SubDescuento/SubRecargo descriptions |
| **28-07-2020** | Modified `<TotalITBISRetenido>` and `<TotalISRRetencion>` to accept zero values |

---

## 1. Introduction

This document describes the complete XML structure for Electronic Fiscal Vouchers (e-CF) in the Dominican Republic's DGII system, including field definitions, data types, validation rules, and obligatoriedad codes for each e-CF type.

Each e-CF must contain a **digital signature** that authenticates its origin and certifies its integrity.

---

## 2. e-CF Types

| Code | Type | Description |
|------|------|-------------|
| `31` | Factura de Crédito Fiscal Electrónica | B2B invoice with tax credit |
| `32` | Factura de Consumo Electrónica | Consumer/retail invoice |
| `33` | Nota de Débito Electrónica | Electronic debit note |
| `34` | Nota de Crédito Electrónica | Electronic credit note |
| `41` | Compras Electrónico | Purchase voucher |
| `43` | Gastos Menores Electrónico | Minor expenses voucher |
| `44` | Regímenes Especiales Electrónico | Special regimes voucher |
| `45` | Gubernamental Electrónico | Government voucher |
| `46` | Comprobante de Exportaciones Electrónico | Export voucher |
| `47` | Comprobante para Pagos al Exterior Electrónico | Foreign payments voucher |

---

## 3. Document Structure

The e-CF consists of the following sections:

```
<ECF>
  <Encabezado>                      <!-- A. Header -->
    <IdDoc>...</IdDoc>              <!-- Document identification -->
    <Emisor>...</Emisor>            <!-- Issuer data -->
    <Comprador>...</Comprador>      <!-- Buyer data -->
    <InformacionesAdicionales>...</InformacionesAdicionales>  <!-- Export/shipping -->
    <Transporte>...</Transporte>    <!-- Transport data -->
    <Totales>...</Totales>          <!-- Totals -->
    <OtraMoneda>...</OtraMoneda>    <!-- Foreign currency totals -->
  </Encabezado>
  <DetallesItem>                   <!-- B. Item Details -->
    <Item>...</Item>
  </DetallesItem>
  <Subtotales>...</Subtotales>      <!-- C. Informational Subtotals -->
  <DescuentosORecargos>...</DescuentosORecargos>  <!-- D. Global Discounts/Surcharges -->
  <Paginacion>...</Paginacion>      <!-- E. Pagination -->
  <InformacionReferencia>...</InformacionReferencia>  <!-- F. Reference Information -->
  <FechaHoraFirma>...</FechaHoraFirma>  <!-- G. Signature Timestamp -->
  <Signature>...</Signature>        <!-- H. Digital Signature -->
</ECF>
```

---

## 4. Obligatoriedad Codes

| Code | Meaning |
|------|---------|
| `1` | **Obligatorio** (Mandatory) - Must always be present |
| `2` | **Condicional** (Conditional) - Required under specific conditions |
| `3` | **Opcional** (Optional) - May be included |
| `0` | **No Aplica** (Not Applicable) - Should not be included |

---

## 5. Print Representation Codes (Column I)

The PDF specification includes a "Representación Impresa" (Print Representation) column indicating how fields should appear in the printed version of the e-CF.

| Code | Meaning |
|------|---------|
| `N` | **No obligatoria** - Printing of this field is not mandatory |
| `I` | **Impresión obligatoria** - Printing of this data is mandatory |
| `P` | **Impreso en palabras** - Data must be printed in words (e.g., type codes must be written out, not just numbers) |

---

## 6. Data Type Reference

| Type | Meaning | Validation |
|------|---------|------------|
| **NUM** | Numeric | Only digits 0-9 |
| **ALFANUM** | Alphanumeric | Letters, numbers, spaces, and allowed special characters |
| **FECHA** | Date | Format: YYYY-MM-DD |
| **DATETIME** | Date and Time | Format: YYYY-MM-DDTHH:MM:SS (ISO 8601) |
| **DECIMAL** | Decimal | Format: up to 2 decimals (e.g., 1234.56) |
| **EMAIL** | Email Address | Must contain @ and valid domain |
| **TELEFONO** | Phone Number | 10 digits (format: 809-555-1234) |

**General Rules**:
- All decimal numeric fields use **period (.)** as decimal separator
- No thousands separators (commas) allowed
- Monetary amounts have maximum **2 decimals**
- Tax rates have maximum **2 decimals**

---
## Section A: Encabezado (Header)

### A.1 IdDoc (Document Identification)

| # | Elemento | Descripción | Máx | Tipo | Validación | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|----------|-------------|-----|------|------------|:-:|----|----|----|----|----|----|----|----|----|----| 
| 1 | `<Version>` | Format version | 3 | ALFANUM | Value: "1.0" | N | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 2 | `<TipoeCF>` | e-CF type code | 2 | NUM | Valid type (31-47) | P | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 3 | `<eNCF>` | Electronic fiscal number | 13 | ALFANUM | Valid sequence format | I | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 4 | `<FechaVencimientoSecuencia>` | e-NCF expiry date | 10 | DATE | DD-MM-YYYY | I | 1 | 0 | 1 | 0 | 1 | 1 | 1 | 1 | 1 | 1 |
| 5 | `<IndicadorNotaCredito>` | Credit note >30 días | 1 | NUM | 0=≤30 días, 1=>30 días | N | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| 6 | `<IndicadorEnvioDiferido>` | Deferred sending | 1 | NUM | 0=normal, 1=diferido | N | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 2 | 0 |
| 7 | `<IndicadorMontoGravado>` | ITBIS included in prices | 1 | NUM | 0=excluido, 1=incluido | N | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 0 | 0 |
| 8 | `<TipoIngresos>` | Income type code | 2 | NUM | Values 01-06 (Ver Tabla VI) | N | 1 | 1 | 1 | 1 | 0 | 0 | 1 | 1 | 1 | 0 |
| 9 | `<TipoPago>` | Payment type | 1 | NUM | 1=Contado, 2=Crédito, 3=Gratuito | N | 1 | 1 | 1 | 1 | 1 | 3 | 1 | 1 | 1 | 3 |
| 10 | `<FechaLimitePago>` | Payment deadline | 10 | DATE | DD-MM-YYYY, ≥FechaEmision | N | 2 | 2 | 2 | 2 | 2 | 0 | 2 | 2 | 2 | 3 |
| 11 | `<TerminoPago>` | Payment terms | 15 | ALFANUM | Free text | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| — | `<TablaFormasPago>` | Payment methods table | — | — | Container (see note) | — | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 12 | `<FormaPago>` | Payment method code | 2 | NUM | Values 1-8 (Tabla V) | N | 3 | 3 | 3 | 0 | 3 | 0 | 3 | 3 | 3 | 3 |
| 13 | `<MontoPago>` | Payment amount | 18 | NUM | 16 ent + 2 dec, ≥0 | N | 2 | 2 | 2 | 0 | 2 | 0 | 2 | 2 | 2 | 3 |
| 14 | `<TipoCuentaPago>` | Account type | 2 | ALFA | CT=Corriente, AH=Ahorro, OT=Otra | N | 3 | 3 | 3 | 0 | 3 | 0 | 3 | 3 | 3 | 3 |
| 15 | `<NumeroCuentaPago>` | Account number | 28 | ALFANUM | — | N | 3 | 3 | 3 | 0 | 3 | 0 | 3 | 3 | 3 | 3 |
| 16 | `<BancoPago>` | Bank name | 75 | ALFANUM | — | N | 3 | 3 | 3 | 0 | 3 | 0 | 3 | 3 | 3 | 3 |
| 17 | `<FechaDesde>` | Billing period start | 10 | ALFANUM | DD-MM-YYYY, ≤FechaHasta | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 3 |
| 18 | `<FechaHasta>` | Billing period end | 10 | ALFANUM | DD-MM-YYYY, ≥FechaDesde | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 3 |
| 19 | `<TotalPaginas>` | Total pages | 3 | NUM | >1, condicional si existe Paginación | I | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |

> [!NOTE]
> **Estructura de `<TablaFormasPago>`**: Cada pago está envuelto en `<FormaDePago>` conteniendo `<FormaPago>` + `<MontoPago>`.
> Para múltiples pagos vía cheque/transferencia (código 2), solo se debe usar UNA entrada `<TipoCuentaPago>`.

> [!NOTE]
> **Nota al pie 1**: La estructura del e-NCF consiste de: Letra de serie (E-Z, excepto P) + código de tipo de 2 dígitos + secuencia de 10 dígitos.
> 
> **Nota al pie 2**: `IndicadorNotaCredito = 1` significa que la nota de crédito pierde el beneficio de crédito fiscal de ITBIS (emitida >30 días después de la original).
>
> **Nota al pie 3**: Facturas con `TipoPago = 3` (Gratuito/Libre) no pueden ser usadas para reclamaciones de crédito fiscal.

---

### A.2 Emisor (Issuer)

| # | Elemento | Descripción | Máx | Tipo | Validación | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|----------|-------------|-----|------|------------|:-:|----|----|----|----|----|----|----|----|----|----| 
| 20 | `<RNCEmisor>` | RNC del Emisor | 9/11 | NUM | 9 u 11 dígitos válidos | I | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 21 | `<RazonSocialEmisor>` | Razón social | 150 | ALFANUM | — | I | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 22 | `<NombreComercial>` | Nombre comercial | 150 | ALFANUM | — | I | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 23 | `<Sucursal>` | Código de sucursal | 20 | ALFANUM | — | I | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 24 | `<DireccionEmisor>` | Dirección | 100 | ALFANUM | — | I | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 25 | `<Municipio>` | Código de municipio | 6 | NUM | Tabla III | P | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 26 | `<Provincia>` | Código de provincia | 6 | NUM | Tabla III | P | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| — | `<TablaTelefonoEmisor>` | Container de teléfonos (hasta 3) | — | — | — | — | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 27 | `<TelefonoEmisor>` | Número de teléfono (hasta 3) | 12 | ALFANUM | Formato: xxx-xxx-xxxx | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 28 | `<CorreoEmisor>` | Correo electrónico | 80 | ALFANUM | Formato de email válido | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 29 | `<WebSite>` | Sitio web | 50 | ALFANUM | — | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 30 | `<ActividadEconomica>` | Actividad económica | 100 | ALFANUM | — | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 31 | `<CodigoVendedor>` | Código de vendedor | 60 | ALFANUM | Referencia interna | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 32 | `<NumeroFacturaInterna>` | Número de factura interna | 20 | ALFANUM | — | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 33 | `<NumeroPedidoInterno>` | Número de pedido interno | 20 | NUM | — | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 34 | `<ZonaVenta>` | Zona de venta | 20 | ALFANUM | — | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 35 | `<RutaVenta>` | Ruta de venta | 20 | ALFANUM | — | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 36 | `<InformacionAdicionalEmisor>` | Información adicional | 250 | ALFANUM | — | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 37 | `<FechaEmision>` | Fecha de emisión | 10 | ALFANUM | DD-MM-YYYY, validar fecha inicio emisor electrónico | I | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |

## Section A: Encabezado (Header)

### A.1 IdDoc (Document Identification)

| # | Element | Description | Max | Type | Validation | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|---------|-------------|-----|------|------------|:-:|----|----|----|----|----|----|----|----|----|----| 
| 1 | `<Version>` | Format version | 3 | ALFANUM | Value: "1.0" | N | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 2 | `<TipoeCF>` | e-CF type code | 2 | NUM | Valid type (31-47) | P | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 3 | `<eNCF>` | Electronic fiscal number | 13 | ALFANUM | Valid sequence format | I | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 4 | `<FechaVencimientoSecuencia>` | e-NCF expiry date | 10 | DATE | DD-MM-YYYY | I | 1 | 0 | 1 | 0 | 1 | 1 | 1 | 1 | 1 | 1 |
| 5 | `<IndicadorNotaCredito>` | Credit note >30 days | 1 | NUM | 0=≤30 days, 1=>30 days | N | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| 6 | `<IndicadorEnvioDiferido>` | Deferred sending | 1 | NUM | 0=normal, 1=deferred | N | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 2 | 0 |
| 7 | `<IndicadorMontoGravado>` | ITBIS included in prices | 1 | NUM | 0=excluded, 1=included | N | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 0 | 0 |
| 8 | `<TipoIngresos>` | Income type code | 2 | NUM | Values 01-06 (See Tabla VI) | N | 1 | 1 | 1 | 1 | 0 | 0 | 1 | 1 | 1 | 0 |
| 9 | `<TipoPago>` | Payment type | 1 | NUM | 1=Cash, 2=Credit, 3=Free | N | 1 | 1 | 1 | 1 | 1 | 3 | 1 | 1 | 1 | 3 |
| 10 | `<FechaLimitePago>` | Payment deadline | 10 | DATE | DD-MM-YYYY, ≥FechaEmision | N | 2 | 2 | 2 | 2 | 2 | 0 | 2 | 2 | 2 | 3 |
| 11 | `<TerminoPago>` | Payment terms | 15 | ALFANUM | Free text | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| — | `<TablaFormasPago>` | Payment methods table | — | — | Container (see note) | — | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 12 | `<FormaPago>` | Payment method code | 2 | NUM | Values 1-8 (Tabla V) | N | 3 | 3 | 3 | 0 | 3 | 0 | 3 | 3 | 3 | 3 |
| 13 | `<MontoPago>` | Payment amount | 18 | NUM | 16 int + 2 dec, ≥0 | N | 2 | 2 | 2 | 0 | 2 | 0 | 2 | 2 | 2 | 3 |
| 14 | `<TipoCuentaPago>` | Account type | 2 | ALFA | CT=Checking, AH=Savings, OT=Other | N | 3 | 3 | 3 | 0 | 3 | 0 | 3 | 3 | 3 | 3 |
| 15 | `<NumeroCuentaPago>` | Account number | 28 | ALFANUM | — | N | 3 | 3 | 3 | 0 | 3 | 0 | 3 | 3 | 3 | 3 |
| 16 | `<BancoPago>` | Bank name | 75 | ALFANUM | — | N | 3 | 3 | 3 | 0 | 3 | 0 | 3 | 3 | 3 | 3 |
| 17 | `<FechaDesde>` | Billing period start | 10 | ALFANUM | DD-MM-YYYY, ≤FechaHasta | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 3 |
| 18 | `<FechaHasta>` | Billing period end | 10 | ALFANUM | DD-MM-YYYY, ≥FechaDesde | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 3 |
| 19 | `<TotalPaginas>` | Total pages | 3 | NUM | >1, conditional if Paginación exists | I | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |

> [!NOTE]
> **`<TablaFormasPago>` Structure**: Each payment is wrapped in `<FormaDePago>` containing `<FormaPago>` + `<MontoPago>`.
> For multiple payments via check/transfer (code 2), only ONE `<TipoCuentaPago>` entry should be used.

> [!NOTE]
> **Footnote 1**: The e-NCF structure consists of: Series letter (E-Z, except P) + 2-digit type code + 10-digit sequence.
> 
> **Footnote 2**: `IndicadorNotaCredito = 1` means the credit note loses the ITBIS tax credit benefit (issued >30 days after original).
>
> **Footnote 3**: Invoices with `TipoPago = 3` (Free/No charge) cannot be used for tax credit claims.

---

### A.2 Emisor (Issuer)

| # | Element | Description | Max | Type | Validation | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|---------|-------------|-----|------|------------|:-:|----|----|----|----|----|----|----|----|----|----| 
| 20 | `<RNCEmisor>` | Issuer RNC | 9/11 | NUM | Valid 9 or 11 digits | I | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 21 | `<RazonSocialEmisor>` | Legal name | 150 | ALFANUM | — | I | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 22 | `<NombreComercial>` | Trade name | 150 | ALFANUM | — | I | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 23 | `<Sucursal>` | Branch code | 20 | ALFANUM | — | I | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 24 | `<DireccionEmisor>` | Address | 100 | ALFANUM | — | I | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 25 | `<Municipio>` | Municipality code | 6 | NUM | Tabla III | P | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 26 | `<Provincia>` | Province code | 6 | NUM | Tabla III | P | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| — | `<TablaTelefonoEmisor>` | Phone container (up to 3) | — | — | — | — | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 27 | `<TelefonoEmisor>` | Phone number (up to 3) | 12 | ALFANUM | Format: xxx-xxx-xxxx | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 28 | `<CorreoEmisor>` | Email | 80 | ALFANUM | Valid email format | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 29 | `<WebSite>` | Website | 50 | ALFANUM | — | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 30 | `<ActividadEconomica>` | Economic activity | 100 | ALFANUM | — | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 31 | `<CodigoVendedor>` | Seller code | 60 | ALFANUM | Internal reference | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 32 | `<NumeroFacturaInterna>` | Internal invoice number | 20 | ALFANUM | — | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 33 | `<NumeroPedidoInterno>` | Internal order number | 20 | NUM | — | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 34 | `<ZonaVenta>` | Sales zone | 20 | ALFANUM | — | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 35 | `<RutaVenta>` | Sales route | 20 | ALFANUM | — | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 36 | `<InformacionAdicionalEmisor>` | Additional information | 250 | ALFANUM | — | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 37 | `<FechaEmision>` | Issue date | 10 | ALFANUM | DD-MM-YYYY, validate e-invoicer start date | I | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |

---

### A.3 Comprador (Buyer)

| # | Element | Description | Max | Type | Validation | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|---------|-------------|-----|------|------------|:-:|----|----|----|----|----|----|----|----|----|----| 
| 38 | `<RNCComprador>` | Buyer RNC | 11 | NUM | Valid 9 or 11 digits | I | 1 | 2 | 2 | 2 | 1 | 0 | 1 | 1 | 2 | 2 |
| 39 | `<IdentificadorExtranjero>` | Foreign ID | 20 | ALFANUM | For non-residents | I | 0 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 2 | 2 |
| 40 | `<RazonSocialComprador>` | Legal name | 150 | ALFANUM | — | I | 2 | 2 | 2 | 2 | 2 | 0 | 2 | 2 | 2 | 2 |
| 41 | `<ContactoComprador>` | Contact name/phone | 80 | ALFANUM | — | N | 3 | 3 | 3 | 3 | 3 | 0 | 3 | 3 | 3 | 0 |
| 42 | `<CorreoComprador>` | Email | 80 | ALFANUM | Valid email | N | 3 | 3 | 3 | 3 | 3 | 0 | 3 | 3 | 3 | 3 |
| 43 | `<DireccionComprador>` | Address | 100 | ALFANUM | — | N | 3 | 3 | 3 | 3 | 3 | 0 | 3 | 3 | 3 | 3 |
| 44 | `<MunicipioComprador>` | Municipality | 6 | NUM | Tabla III | N | 3 | 3 | 3 | 3 | 3 | 0 | 3 | 3 | 3 | 3 |
| 45 | `<ProvinciaComprador>` | Province | 6 | NUM | Tabla III | N | 3 | 3 | 3 | 3 | 3 | 0 | 3 | 3 | 3 | 3 |
| 46 | `<PaisComprador>` | Country name | 60 | ALFA | Full country name | P | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 47 | `<FechaEntrega>` | Delivery date | 10 | DATE | DD-MM-YYYY | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 48 | `<ContactoEntrega>` | Delivery contact | 100 | ALFANUM | — | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 49 | `<DireccionEntrega>` | Delivery address | 100 | ALFANUM | — | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 50 | `<TelefonoAdicional>` | Delivery phone | 12 | ALFANUM | — | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 51 | `<FechaOrdenCompra>` | Purchase order date | 10 | DATE | DD-MM-YYYY | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 52 | `<NumeroOrdenCompra>` | Purchase order number | 20 | ALFANUM | — | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 53 | `<CodigoInternoComprador>` | Buyer internal code | 20 | ALFANUM | Internal reference | N | 3 | 3 | 3 | 3 | 3 | 0 | 3 | 3 | 3 | 0 |
| 54 | `<ResponsablePago>` | Payment responsible | 20 | ALFA | — | N | 3 | 3 | 3 | 3 | 3 | 0 | 3 | 3 | 3 | 0 |
| 55 | `<Informacionadicionalcomprador>` | Notes | 150 | ALFANUM | — | N | 3 | 3 | 3 | 3 | 3 | 0 | 3 | 3 | 3 | 0 |

> [!IMPORTANT]
> **Buyer Identification Rules:**
> - Type 31 (Crédito Fiscal): `RNCComprador` always mandatory
> - Type 32 (Consumo) ≥ RD$250,000: `RNCComprador` or `IdentificadorExtranjero` mandatory
> - Type 32 (Consumo) < RD$250,000: `RNCComprador` optional
> - Type 46 (Exports): Use `RNCComprador` for residents, `IdentificadorExtranjero` for non-residents

---

### A.4 InformacionesAdicionales (Export/Shipping Information)

This section is primarily used for **Type 46 (Exports)** and shipping-related invoices.

| # | Element | Description | Max | Type | Validation | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|---------|-------------|-----|------|------------|:-:|----|----|----|----|----|----|----|----|----|----| 
| 56 | `<FechaEmbarque>` | Shipping date | 10 | DATE | DD-MM-YYYY | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 57 | `<NumeroEmbarque>` | Shipment number | 25 | ALFA | — | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 58 | `<NumeroContenedor>` | Container number | 100 | ALFA | — | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 59 | `<NumeroReferencia>` | Reference number | 20 | NUM | — | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 60 | `<NombrePuertoEmbarque>` | Port of loading | 40 | ALFA | — | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 61 | `<CondicionesEntrega>` | Delivery terms | 3 | ALFA | CIF/FOB/EXW etc. | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 62 | `<TotalFob>` | Total FOB value | 18 | DEC | ≥0, 2 decimals | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 63 | `<Seguro>` | Insurance amount | 18 | DEC | ≥0, 2 decimals | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 64 | `<Flete>` | Freight amount | 18 | DEC | ≥0, 2 decimals | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 65 | `<OtrosGastos>` | Other expenses | 18 | DEC | ≥0, 2 decimals | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 66 | `<TotalCif>` | Total CIF value | 18 | DEC | FOB+Insurance+Freight+Other | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 67 | `<RegimenAduanero>` | Customs regime | 35 | ALFA | Per DGA classification | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 68 | `<NombrePuertoSalida>` | Departure port | 40 | ALFANUM | — | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 69 | `<NombrePuertoDesembarque>` | Destination port | 40 | ALFANUM | — | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 70 | `<PesoBruto>` | Gross weight | 18 | DEC | ≥0, 2 decimals | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 71 | `<PesoNeto>` | Net weight | 18 | DEC | ≥0, 2 decimals | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 72 | `<UnidadPesoBruto>` | Gross weight unit | 2 | NUM | Tabla IV | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 73 | `<UnidadPesoNeto>` | Net weight unit | 2 | NUM | Tabla IV | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 74 | `<CantidadBulto>` | Number of packages | 18 | DEC | >0, 2 decimals | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 75 | `<UnidadBulto>` | Package unit | 2 | NUM | Tabla IV | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 76 | `<VolumenBulto>` | Volume | 18 | DEC | >0, 2 decimals | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 77 | `<UnidadVolumen>` | Volume unit | 2 | NUM | Tabla IV | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |

> [!NOTE]
> **Port Tag Distinction**: Per DGII specification, these are 3 different ports:
> - `NombrePuertoEmbarque` (#60) = Port where goods are loaded
> - `NombrePuertoSalida` (#68) = Port of departure (may differ from loading port)
> - `NombrePuertoDesembarque` (#69) = Destination port (unloading)

---

### A.5 Transporte (Transport)

| # | Element | Description | Max | Type | Validation | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|---------|-------------|-----|------|------------|:-:|----|----|----|----|----|----|----|----|----|----| 
| 78 | `<ViaTransporte>` | Transport mode | 2 | NUM | 01=Land, 02=Maritime, 03=Air | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 79 | `<PaisOrigen>` | Country of origin of merchandise | 60 | ALFA | — | N |  0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 80 | `<DireccionDestino>` | Destination address | 100 | ALFANUM | — | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 81 | `<PaisDestino>` | Destination country | 60 | ALFA | — | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 3 |
| 82 | `<RNCIdentificacionCompaniaTransportista>` | Carrier RNC/ID | 20 | ALFANUM | — | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 83 | `<NombreCompaniaTransportista>` | Carrier company name | 150 | ALFANUM | — | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 84 | `<NumeroViaje>` | Trip/voyage/flight number | 20 | ALFANUM | — | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 85 | `<Conductor>` | Driver code or name | 20 | ALFANUM | — | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 86 | `<DocumentoTransporte>` | Transport document | 20 | NUM | — | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 87 | `<Ficha>` | Transport file/record | 10 | ALFANUM | — | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 88 | `<Placa>` | Vehicle plate number | 7 | ALFANUM | — | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 89 | `<RutaTransporte>` | Established transport route | 20 | ALFANUM | — | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 90 | `<ZonaTransporte>` | Transport zone | 20 | ALFANUM | — | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 91 | `<NumeroAlbaran>` | Delivery note number | 20 | ALFANUM | — | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |

---

### A.6 Totales

| # | Element | Description | Max | Type | Validation | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|---------|-------------|-----|------|------------|:-:|----|----|----|----|----|----|----|----|----|----| 
| 92 | `<MontoGravadoTotal>` | Total taxable amount | 18 | DEC | Sum of taxable amounts | I | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 0 |
| 93 | `<MontoGravadoI1>` | Amount at ITBIS 18% | 18 | DEC | ≥0, 2 decimals | N | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 0 | 0 |
| 94 | `<MontoGravadoI2>` | Amount at ITBIS 16% | 18 | DEC | ≥0, 2 decimals | N | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 0 | 0 |
| 95 | `<MontoGravadoI3>` | Amount at ITBIS 0% | 18 | DEC | ≥0, 2 decimals | N | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 0 |
| 96 | `<MontoExento>` | Exempt amount | 18 | DEC | ≥0, 2 decimals | I | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 2 |
| 97 | `<ITBIS1>` | ITBIS rate 1 | 2 | NUM | 18% rate (value: 18) | N | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 0 | 0 |
| 98 | `<ITBIS2>` | ITBIS rate 2 | 2 | NUM | 16% rate (value: 16) | N | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 0 | 0 |
| 99 | `<ITBIS3>` | ITBIS rate 3 | 2 | NUM | 0% rate (value: 0) | N | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 0 |
| 100 | `<TotalITBIS>` | Total ITBIS | 18 | DEC | Sum of ITBIS amounts | I | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 0 |
| 101 | `<TotalITBIS1>` | ITBIS at 18% | 18 | DEC | MontoGravadoI1 × 0.18 | N | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 0 | 0 |
| 102 | `<TotalITBIS2>` | ITBIS at 16% | 18 | DEC | MontoGravadoI2 × 0.16 | N | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 0 | 0 |
| 103 | `<TotalITBIS3>` | ITBIS at 0% | 18 | DEC | MontoGravadoI3 × 0 = 0 | N | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 0 |
| 104 | `<MontoImpuestoAdicional>` | Total additional taxes | 18 | DEC | Sum of ISC + Others | I | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 0 | 0 |
| — | `<ImpuestosAdicionales>` | — | — | — | Container (up to 20 reps) | — | 2 | 2 | 2 | 2 | 0 | 0 | 0 | 2 | 0 | 0 |
| 105 | `<TipoImpuesto>` | Tax type code | 3 | NUM | Tabla I (001-039) | N | 2 | 2 | 2 | 2 | 0 | 0 | 0 | 2 | 0 | 0 |
| 106 | `<TasaImpuestoAdicional>` | Tax rate | 5 | NUM | Per Tabla I | N | 2 | 2 | 2 | 2 | 0 | 0 | 0 | 2 | 0 | 0 |
| 107 | `<MontoImpuestoSelectivoConsumoEspecifico>` | ISC Specific | 18 | DEC | ≥0 | N | 2 | 2 | 2 | 2 | 0 | 0 | 0 | 2 | 0 | 0 |
| 108 | `<MontoImpuestoSelectivoConsumoAdvalorem>` | ISC Ad-Valorem | 18 | DEC | ≥0, **see Granel rule** | N | 2 | 2 | 2 | 2 | 0 | 0 | 0 | 2 | 0 | 0 |
| 109 | `<OtrosImpuestosAdicionales>` | Other taxes | 18 | DEC | ≥0 | N | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 0 | 0 |

> [!CAUTION]
> **30% "Granel" Markup Rule for ISC Ad-Valorem** (Codes 023-035):
> When the unit of measure is **Granel** (Code 18), the base price must be **increased by 30%** before calculating the Ad-Valorem tax.
> Formula: `ISC = (BasePrice × 1.30) × AdValoremRate`

> [!WARNING]
> **ISC Tax Codes (006-039)**: These require strict calculation logic. If `TipoImpuesto` is in range 006-039, you must calculate either ISC Específico OR ISC Ad-Valorem based on the tax code type. See DGII formulas in Tabla I.

| # | Element | Description | Max | Type | Validation | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|---------|-------------|-----|------|------------|:-:|----|----|----|----|----|----|----|----|----|----:|
| 110 | `<MontoTotal>` | Grand total | 18 | DEC | ≥0, sum of components | I | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 111 | `<MontoNoFacturable>` | Non-billable amounts | 18 | DEC | Can be negative | N | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 2 | 0 |
| 112 | `<MontoPeriodo>` | Period amount | 18 | DEC | MontoTotal+MontoNoFacturable | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 113 | `<SaldoAnterior>` | Previous balance | 18 | DEC | Can be ± (positive or negative) | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 114 | `<MontoAvancePago>` | Advance payment amount | 18 | DEC | >0 (must be positive) | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 115 | `<ValorPagar>` | Amount to pay | 18 | DEC | Can be ±  or 0 | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 116 | `<TotalITBISRetenido>` | ITBIS withheld total | 18 | DEC | ≥0 | N | 2 | 0 | 2 | 2 | 2 | 0 | 0 | 0 | 0 | 0 |
| 117 | `<TotalISRRetencion>` | ISR withheld total | 18 | DEC | ≥0 | N | 2 | 0 | 2 | 2 | 2 | 0 | 0 | 0 | 0 | 2 |
| 118 | `<TotalITBISPercepcion>` | ITBIS perceived total | 18 | DEC | >0 (must be positive) | N | 2 | 0 | 2 | 2 | 2 | 0 | 0 | 0 | 0 | 0 |
| 119 | `<TotalISRPercepcion>` | ISR perceived total | 18 | DEC | >0 (must be positive) | N | 2 | 0 | 2 | 2 | 2 | 0 | 0 | 0 | 0 | 0 |

> [!NOTE]
> **Perception Regime**: The PDF notes "Régimen de percepción no está vigente" (perception regime is not currently in force). Fields 118-119 are included for future use.

> [!NOTE]
> **Formula**: `MontoTotal` = `MontoGravadoTotal` + `MontoExento` + `TotalITBIS` + `MontoImpuestoAdicional`
> Note: Discounts/surcharges are handled in the global DescuentosORecargos section, not in this formula.

---

### A.7 OtraMoneda (Foreign Currency Totals in Header)

When transactions are in foreign currency, this section mirrors the Totales structure in the alternative currency.

| # | Element | Description | Max | Type | Validation | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|---------|-------------|-----|------|------------|:-:|----|----|----|----|----|----|----|----|----|----| 
| 120 | `<TipoMoneda>` | Currency code | 3 | ALFA | Tabla II | N | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| 121 | `<TipoCambio>` | Exchange rate | 7 | NUM | 3 int + 4 dec, >0 | N | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| 122 | `<MontoGravadoTotalOtraMoneda>` | Total taxable (FC) | 18 | DEC | ≥0, 2 decimals | N | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 0 |
| 123 | `<MontoGravado1OtraMoneda>` | Amount at ITBIS 18% (FC) | 18 | DEC | ≥0, 2 decimals | N | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 0 | 0 |
| 124 | `<MontoGravado2OtraMoneda>` | Amount at ITBIS 16% (FC) | 18 | DEC | ≥0, 2 decimals | N | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 0 | 0 |
| 125 | `<MontoGravado3OtraMoneda>` | Amount at ITBIS 0% (FC) | 18 | DEC | ≥0, 2 decimals | N | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 0 |
| 126 | `<MontoExentoOtraMoneda>` | Exempt (FC) | 18 | DEC | ≥0, 2 decimals | N | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 2 |
| 127 | `<TotalITBISOtraMoneda>` | Total ITBIS (FC) | 18 | DEC | ≥0, 2 decimals | N | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 0 |
| 128 | `<TotalITBIS1OtraMoneda>` | ITBIS 18% (FC) | 18 | DEC | ≥0, 2 decimals | N | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 0 | 0 |
| 129 | `<TotalITBIS2OtraMoneda>` | ITBIS 16% (FC) | 18 | DEC | ≥0, 2 decimals | N | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 0 | 0 |
| 130 | `<TotalITBIS3OtraMoneda>` | ITBIS 0% (FC) | 18 | DEC | ≥0, 2 decimals | N | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 0 |
| 131 | `<MontoImpuestoAdicionalOtraMoneda>` | Addtl taxes (FC) | 18 | DEC | ≥0, 2 decimals | N | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 0 | 0 |
| — | `<ImpuestosAdicionalesOtraMoneda>` | — | — | — | Container (up to 20 reps) | — | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 0 | 0 |
| 132 | `<TipoImpuestoOtraMoneda>` | Tax type code (FC) | 3 | NUM | Tabla I (001-039) | N | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 0 | 0 |
| 133 | `<TasaImpuestoAdicionalOtraMoneda>` | Tax rate (FC) | 5 | NUM | Per Tabla I | N | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 0 | 0 |
| 134 | `<MontoImpuestoSelectivoConsumoEspecificoOtraMoneda>` | ISC Specific (FC) | 18 | DEC | >0, 2 decimals | N | 2 | 2 | 2 | 2 | 0 | 0 | 0 | 2 | 0 | 0 |
| 135 | `<MontoImpuestoSelectivoConsumoAdvaloremOtraMoneda>` | ISC Ad-Valorem (FC) | 18 | DEC | >0, 2 decimals | N | 2 | 2 | 2 | 2 | 0 | 0 | 0 | 2 | 0 | 0 |
| 136 | `<OtrosImpuestosAdicionalesOtraMoneda>` | Other addtl taxes (FC) | 18 | DEC | >0, 2 decimals | N | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 0 | 0 |
| 137 | `<MontoTotalOtraMoneda>` | Grand total (FC) | 18 | DEC | ≥0, 2 decimals | N | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |

> [!NOTE]
> **OtraMoneda ImpuestosAdicionales**: When invoicing in foreign currency with additional taxes (ISC, etc.), this structure mirrors the DOP `ImpuestosAdicionales` structure but in the foreign currency amounts. **Up to 20 repetitions** of `<ImpuestosAdicionalesOtraMoneda>` entries are allowed.


---

## Code Tables (TABLAS)

### Tabla I: Impuestos Adicionales (Additional Tax Codes)

| Code | Tax Type | Abbreviation | Description | Rate |
|------|----------|--------------|-------------|------|
| 001 | Propina Legal | Propina Legal | Legal tip | 10% |
| 002 | CDT | CDT | Contribución Desarrollo Telecomunicaciones (Law 153-98 Art. 45) | 2% |
| 003 | ISC | ISC | General insurance services | 16% |
| 004 | ISC | ISC | Telecommunications services | 10% |
| 005 | Primera Placa | Primera Placa | First vehicle registration plate issuance | 17% |
| 006 | ISC Específico | ISC Específico | Beer | 632.58 |
| 007 | ISC Específico | ISC Específico | Grape wines | 632.58 |
| 008 | ISC Específico | ISC Específico | Vermouth and other wines from fresh grapes | 632.58 |
| 009 | ISC Específico | ISC Específico | Other fermented beverages | 632.58 |
| 010 | ISC Específico | ISC Específico | Undenatured ethyl alcohol (≥80%) | 632.58 |
| 011 | ISC Específico | ISC Específico | Undenatured ethyl alcohol (<80%) | 632.58 |
| 012 | ISC Específico | ISC Específico | Grape spirits | 632.58 |
| 013 | ISC Específico | ISC Específico | Whisky | 632.58 |
| 014 | ISC Específico | ISC Específico | Rum and other sugarcane spirits | 632.58 |
| 015 | ISC Específico | ISC Específico | Gin | 632.58 |
| 016 | ISC Específico | ISC Específico | Vodka | 632.58 |
| 017 | ISC Específico | ISC Específico | Liqueurs | 632.58 |
| 018 | ISC Específico | ISC Específico | Other spirituous beverages | 632.58 |
| 019 | ISC Específico | ISC Específico | Denatured ethyl alcohol | 632.58 |
| 020 | ISC Específico | ISC Específico | Blond tobacco cigarettes | Per unit |
| 021 | ISC Específico | ISC Específico | Black tobacco cigarettes | Per unit |
| 022 | ISC Específico | ISC Específico | Cigars | Per unit |
| 023 | ISC Ad-Valorem | ISC Ad-Valorem | Alcohol and alcoholic beverage products | 10% |
| 024 | ISC Ad-Valorem | ISC Ad-Valorem | Motor vehicles | Variable |
| 025 | ISC Ad-Valorem | ISC Ad-Valorem | Household appliances | Variable |
| 026 | CESC | CESC | Special contribution construction sector | 5% |
| 027-039 | Various | Various | Other ISC codes per DGII classification | Variable |

> [!NOTE]
> ISC Específico rates are updated periodically by DGII. The 632.58 figure is the rate per liter of absolute alcohol as of the document date.

---

### Tabla II: Monedas (Currencies) — OFFICIAL DGII List

> [!WARNING]
> Only the following 17 currencies are officially recognized by DGII for foreign currency transactions. Using non-listed codes may cause validation errors. Note: DOP (Dominican Peso) is the native currency and is NOT listed here—this table is for `<OtraMoneda>` (foreign currency) fields only.

| Code | Currency (Spanish) | Currency (English) |
|------|-------------------|-------------------| 
| BRL | Real Brasileño | Brazilian Real |
| CAD | Dólar Canadiense | Canadian Dollar |
| CHF | Franco Suizo | Swiss Franc |
| CHY | Yuan Chino (Renminbi) | Chinese Yuan *(DGII uses CHY; ISO 4217 is CNY)* |
| COP | Peso Colombiano | Colombian Peso *(added 2025)* |
| DKK | Corona Danesa | Danish Krone |
| EUR | Euro | Euro |
| GBP | Libra Esterlina | British Pound |
| HTG | Gurda Haitiana *(PDF typo, correct: Gourde)* | Haitian Gourde *(added 2024)* |
| JPY | Yen Japonés | Japanese Yen |
| MXN | Peso Mexicano | Mexican Peso *(added 2024)* |
| NOK | Corona Noruega | Norwegian Krone |
| SCP | Libra Escocesa | Scottish Pound |
| SEK | Corona Sueca | Swedish Krona |
| USD | Dólar Estadounidense | US Dollar |
| VEF | Bolívar Fuerte Venezolano | Venezuelan Bolívar *(obsolete - Venezuela now uses VES)* |
| XDR | Derecho Especial de Giro (DEG) | IMF Special Drawing Rights |

> [!NOTE]
> **Footnote 83**: XDR (DEG) is not a currency but the IMF's unit of account.

---

### Tabla III: Provincias y Municipios (Province/Municipality Codes)

> [!WARNING]
> **Sample Only** - This table contains 22 pages (158+ municipalities) in the original PDF. Do not hardcode these values. 
> 
> **Full list available in: [provinces.md](provinces.md)**

This is a 22-page table in the original PDF (pages 63-85). A sample is provided below:

| Province Code | Municipality Code | Description |
|---------------|-------------------|-------------|
| 010000 | — | DISTRITO NACIONAL |
| — | 010100 | MUNICIPIO SANTO DOMINGO DE GUZMÁN |
| — | 010101 | Santo Domingo de Guzmán (D.M.) |
| 020000 | — | PROVINCIA AZUA |
| — | 020100 | MUNICIPIO AZUA |
| — | 020101 | Azua (D.M.) |
| 320000 | — | PROVINCIA SANTO DOMINGO |
| — | 320100 | MUNICIPIO SANTO DOMINGO ESTE |
| — | 320101 | Santo Domingo Este (D.M.) |
| — | 320200 | MUNICIPIO SANTO DOMINGO OESTE |
| — | 320300 | MUNICIPIO SANTO DOMINGO NORTE |
| — | 320400 | MUNICIPIO BOCA CHICA |
| — | 320500 | MUNICIPIO SAN ANTONIO DE GUERRA |
| — | 320600 | MUNICIPIO LOS ALCARRIZOS |
| — | 320700 | MUNICIPIO PEDRO BRAND |

> [!TIP]
> Source: Oficina Nacional de Estadística (ONE), Departamento de Cartografía, División de Límites y Linderos. Updated June 30, 2014.

---

### Tabla IV: Unidades de Medida (Units of Measure) - Complete List

| Code | Abbr | Measure |
|------|------|---------|
| 1 | BARR | Barrel (Barril) |
| 2 | BOL | Bag (Bolsa) |
| 3 | BOT | Can (Bote) |
| 4 | BULTO | Bundles (Bultos) |
| 5 | BOTELLA | Bottle (Botella) |
| 6 | CAJ | Box/Crate (Caja/Cajón) |
| 7 | CAJETILLA | Pack (Cajetilla) |
| 8 | CM | Centimeter (Centímetro) |
| 9 | CIL | Cylinder (Cilindro) |
| 10 | CONJ | Set (Conjunto) |
| 11 | CONT | Container (Contenedor) |
| 12 | DÍA | Day (Día) |
| 13 | DOC | Dozen (Docena) |
| 14 | FARD | Bale (Fardo) |
| 15 | GL | Gallons (Galones) |
| 16 | GRAD | Degree (Grado) |
| 17 | GR | Gram (Gramo) |
| 18 | GRAN | Bulk (Granel) |
| 19 | HOR | Hour (Hora) |
| 20 | HUAC | Crate (Huacal) |
| 21 | KG | Kilogram (Kilogramo) |
| 22 | kWh | Kilowatt Hour (Kilovatio Hora) |
| 23 | LB | Pound (Libra) |
| 24 | LITRO | Liter (Litro) |
| 25 | LOT | Lot (Lote) |
| 26 | M | Meter (Metro) |
| 27 | M2 | Square Meter (Metro Cuadrado) |
| 28 | M3 | Cubic Meter (Metro Cúbico) |
| 29 | MMBTU | Million Thermal Units (Millones de Unidades Térmicas) |
| 30 | MIN | Minute (Minuto) |
| 31 | PAQ | Package (Paquete) |
| 32 | PAR | Pair (Par) |
| 33 | PIE | Foot (Pie) |
| 34 | PZA | Piece (Pieza) |
| 35 | ROL | Roll (Rollo) |
| 36 | SOBR | Envelope (Sobre) |
| 37 | SEG | Second (Segundo) |
| 38 | TANQUE | Tank (Tanque) |
| 39 | TONE | Ton (Tonelada) |
| 40 | TUB | Tube (Tubo) |
| 41 | YD | Yard (Yarda) |
| 42 | YD2 | Square Yard (Yarda cuadrada) |
| 43 | UND | Unit (Unidad) |
| 44 | EA | Element (Elemento) |
| 45 | MILLAR | Thousand (Millar) |
| 46 | SAC | Sack (Saco) |
| 47 | LAT | Can (Lata) |
| 48 | DIS | Display (Display) |
| 49 | BID | Drum (Bidón) |
| 50 | RAC | Ration (Ración) |
| 51 | Q | Quintal (Quintal) |
| 52 | GRT | Gross Register Tonnage (Toneladas de registro bruto) |
| 53 | P2 | Square Foot (Pie cuadrado) |
| 54 | PAX | Passenger (Pasajero) |
| 55 | PULG | Inches (Pulgadas) |
| 56 | STAY | Ship Dock Parking (Parqueo barcos en muelle) |
| 57 | BDJ | Tray (Bandeja) |
| 58 | HA | Hectare (Hectárea) |
| 59 | ML | Milliliter (Mililitro) |
| 60 | MG | Milligram (Miligramo) |
| 61 | OZ | Ounces (Onzas) |
| 62 | OZT | Troy Ounces (Onzas Troy) |

---

### Tabla V: Payment Methods (Formas de Pago)

| Code | Description |
|------|-------------|
| 1 | Cash (Efectivo) |
| 2 | Check/Transfer/Deposit (Cheque/Transferencia/Depósito) |
| 3 | Credit/Debit Card (Tarjeta de Crédito/Débito) |
| 4 | Credit Sale (Venta a Crédito) |
| 5 | Gift Vouchers/Certificates (Bonos o Certificados de regalo) |
| 6 | Barter/Exchange (Permuta) |
| 7 | Credit Note (Nota de crédito) |
| 8 | Other Payment Methods (Otras Formas de pago) |

> [!NOTE]
> If `FormaPago = 05` (gift certificates), the e-CF must be type 32 (Consumer Invoice).

---

### Tabla VI: Income Types (Tipos de Ingresos)

| Code | Description |
|------|-------------|
| 01 | Operational income (Ingresos por operaciones) |
| 02 | Financial income (Ingresos financieros) |
| 03 | Extraordinary income (Ingresos extraordinarios) |
| 04 | Rental income (Ingresos por arrendamientos) |
| 05 | Depreciable asset sale (Ingresos por venta de activo depreciable) |
| 06 | Other income (Otros ingresos) |

---

### Tabla VII: Payment Types (Tipos de Pago)

| Code | Description |
|------|-------------|
| 1 | Cash/Immediate payment (Contado) |
| 2 | Credit (Crédito) |
| 3 | Free/No charge (Gratuito) |

> [!WARNING]
> Invoices with `TipoPago = 3` (Gratuito) cannot be used for tax credit purposes.

---

## Validation Rules Summary

| Rule ID | Description |
|---------|-------------|
| E01 | `eNCF` must match issuer RNC and be from an authorized, non-expired range |
| E05 | For type 31, `RNCComprador` is mandatory and must be valid/active |
| E32 | For type 32 ≥ RD$250,000, buyer identification is mandatory |
| E-DATE | `FechaEmision` cannot be >30 days in past from submission |
| E-TOTAL | `MontoTotal` must equal sum of components |
| E-SIG | `RNCEmisor` must match the signer's authorized RNC |
| E-EXP | e-NCF sequence must not be expired at submission time |
| E-EMPTY | Empty tags are forbidden; omit tags with null values |

> [!CAUTION]
> **Empty Tags Are Forbidden**: Do not include empty elements like `<Field></Field>` or `<Field />`. If a value is null/empty, **omit the tag entirely**.

---

## Data Type Reference

| Type | Description |
|------|-------------|
| `ALFA` | Alphabetic string |
| `NUM` | Numeric (integers) |
| `DEC` | Decimal number (16 integers, 2-6 decimals as specified) |
| `DATE` | Date in DD-MM-YYYY format |

---

## Line Item Limits

| e-CF Type | Condition | Max Lines |
|-----------|-----------|-----------|
| 32 (Consumer) | < RD$250,000 | 10,000 |
| 32 (Consumer) | ≥ RD$250,000 | 1,000 |
| All other types | — | 10,000 |

> [!NOTE]
> **Footnote 48**: Consumer invoices ≥ RD$250,000 have a maximum of 1,000 line items.

---

## Key Business Rules from Footnotes

1. **Footnote 4**: Consumer invoices < DOP$250,000 have optional buyer RNC.
2. **Footnote 30**: Credit note amounts must be ≤ original invoice total.
3. **Footnote 36**: Amounts on Gastos Menores (type 43) cannot be used as ITBIS advance.
4. **Footnote 48**: Consumer invoices ≥ DOP$250k limited to 1,000 line items.
5. **Footnote 54**: For Pagos al Exterior (type 47), `IndicadorBienoServicio` must be `2` (Service).
6. **Footnotes 57-58 (ISC special reporting)**:
   - For **alcohol and alcoholic beverages** (ISC codes **006-012**): Report the **absolute alcohol content (volume per unit) in liters**.
   - For **tobacco and cigarette products** (ISC codes **013-022**): Report the **number of units per pack** (cajetilla).
   - This field is **only required** when invoicing goods whose transfer, at the **producer or manufacturer level**, is taxed with ISC (codes 006-022).

---

## Section B: DetallesItem (Line Item Details)

Each `<Item>` element describes one line item (good or service). Up to 100 items per e-CF (up to 1,000 for type 32 ≥DOP$250k, or 10,000 for type 32 <DOP$250k).

### B.1 Item Identification (Fields 1-3)

| # | Element | Description | Max | Type | Validation | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|---------|-------------|-----|------|------------|:-:|----|----|----|----|----|----|----|----|----|----| 
| 1 | `<NumeroLinea>` | Line number | 5 | NUM | Sequential 1 to n | N | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| — | `<TablaCodigosItem>` | — | — | — | Container (up to 5 reps) | — | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 2 | `<TipoCodigo>` | Code type | 14 | ALFANUM | EAN, PLU, DUN, Interna | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 3 | `<CodigoItem>` | Item code | 35 | ALFANUM | Up to 5 codes | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |

### B.2 Tax Indicator & Retention (Fields 4-7)

| # | Element | Description | Max | Type | Validation | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|---------|-------------|-----|------|------------|:-:|----|----|----|----|----|----|----|----|----|----| 
| 4 | `<IndicadorFacturacion>` | Tax indicator | 1 | NUM | 0-4 (see codes below) | P | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| — | `<Retencion>` | — | — | — | Container (if retention exists) | — | 2 | 0 | 2 | 2 | 1 | 0 | 0 | 0 | 0 | 1 |
| 5 | `<IndicadorAgenteRetencionoPercepcion>` | Agent indicator | 1 | NUM | 1=R (Retention), 2=P (Perception) | N | 2 | 0 | 2 | 2 | 1 | 0 | 0 | 0 | 0 | 1 |
| 6 | `<MontoITBISRetenido>` | ITBIS withheld | 18 | NUM | ≥0, 2 decimals | N | 2 | 0 | 2 | 2 | 2 | 0 | 0 | 0 | 0 | 0 |
| 7 | `<MontoISRRetenido>` | ISR withheld | 18 | NUM | ≥0, 2 decimals | N | 2 | 0 | 2 | 2 | 2 | 0 | 0 | 0 | 0 | 1 |

**IndicadorFacturacion Values:**

| Code | Description |
|------|-------------|
| `0` | Non-billable (No Facturable) |
| `1` | Taxable ITBIS Rate 1 (18%) (Gravado ITBIS Tasa 1) |
| `2` | Taxable ITBIS Rate 2 (16%) (Gravado ITBIS Tasa 2) |
| `3` | Taxable ITBIS Rate 3 (0%) (Gravado ITBIS Tasa 3) |
| `4` | Exempt (Exento) |

> [!NOTE]
> **Type 43, 44, 47**: IndicadorFacturacion must = 4 (Exempt). **Type 46**: must = 3 (ITBIS 0%).

> [!WARNING]
> If `IndicadorFacturacion=4` (Exempt) AND `IndicadorAgenteRetencionoPercepcion=1` (R), then `MontoITBISRetenido` **must be 0**.

---

### B.3 Item Details (Fields 8-14)

| # | Element | Description | Max | Type | Validation | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|---------|-------------|-----|------|------------|:-:|----|----|----|----|----|----|----|----|----|----| 
| 8 | `<NombreItem>` | Item name | 80 | ALFANUM | — | I | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 9 | `<IndicadorBienoServicio>` | Good/Service | 1 | NUM | 1=Good, 2=Service | N | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 10 | `<DescripcionItem>` | Description | 1000 | ALFANUM | — | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 11 | `<CantidadItem>` | Quantity | 18 | NUM | >0, 2 decimals | I | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 12 | `<UnidadMedida>` | Unit of measure | 2 | NUM | Tabla IV codes | P | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 13 | `<CantidadReferencia>` | Reference qty | 18 | NUM | ≥0, for ISC 006-022 | N | 2 | 2 | 2 | 2 | 0 | 0 | 0 | 2 | 0 | 0 |
| 14 | `<UnidadReferencia>` | Reference unit | 2 | NUM | Tabla IV codes | N | 2 | 2 | 2 | 2 | 0 | 0 | 0 | 2 | 0 | 0 |

> [!NOTE]
> **Type 47 (Pagos al Exterior)**: Field 9 `IndicadorBienoServicio` must = 2 (Service).

---

### B.4 Subcantidad for ISC Products (Fields 15-18)

For alcohol, tobacco products with ISC codes 006-022 (specific) and 023-039 (ad-valorem).

| # | Element | Description | Max | Type | Validation | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|---------|-------------|-----|------|------------|:-:|----|----|----|----|----|----|----|----|----|----| 
| — | `<TablaSubcantidad>` | — | — | — | Container (up to 5 reps) | N | 2 | 2 | 2 | 2 | 0 | 0 | 0 | 2 | 0 | 0 |
| 15 | `<Subcantidad>` | Sub-quantity | 19 | NUM | ≥0, 3 decimals | N | 2 | 2 | 2 | 2 | 0 | 0 | 0 | 2 | 0 | 0 |
| 16 | `<CodigoSubcantidad>` | Sub-qty unit code | 2 | NUM | Tabla IV codes | N | 2 | 2 | 2 | 2 | 0 | 0 | 0 | 2 | 0 | 0 |
| 17 | `<GradosAlcohol>` | Alcohol % | 5 | NUM | >0, 3 int + 2 dec | I | 2 | 2 | 2 | 2 | 0 | 0 | 0 | 2 | 0 | 0 |
| 18 | `<PrecioUnitarioReferencia>` | Reference unit price | 18 | NUM | >0 (retail price for ISC calc) | I | 2 | 2 | 2 | 2 | 0 | 0 | 0 | 2 | 0 | 0 |

> [!NOTE]
> **Field 15 (Subcantidad)**: For alcohol = absolute alcohol content in liters. For tobacco = cigarette units per pack.
> **Field 18 (PrecioUnitarioReferencia)**: For ISC Ad-Valorem (codes 023-039), this is the retail price (PVP) used as tax base.

---

### B.5 Product Dates (Fields 19-20)

| # | Element | Description | Max | Type | Validation | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|---------|-------------|-----|------|------------|:-:|----|----|----|----|----|----|----|----|----|----| 
| 19 | `<FechaElaboracion>` | Manufacturing date | 10 | ALFANUM | dd-MM-AAAA | N | 3 | 3 | 3 | 3 | 3 | 0 | 3 | 3 | 3 | 0 |
| 20 | `<FechaVencimientoItem>` | Expiry date | 10 | ALFANUM | dd-MM-AAAA | N | 3 | 3 | 3 | 3 | 3 | 0 | 3 | 3 | 3 | 0 |

---

### B.6 Minería Section (Fields 21-24)

For mining sector invoices only (conditional on mining transactions).

| # | Element | Description | Max | Type | Validation | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|---------|-------------|-----|------|------------|:-:|----|----|----|----|----|----|----|----|----|----| 
| — | `<Mineria>` | — | — | — | Container (mining sector) | — | 0 | 2 | 2 | 2 | 0 | 0 | 0 | 0 | 2 | 0 |
| 21 | `<PesoNetoKilogramo>` | Net weight (kg) | 19 | NUM | ≥0, 3 decimals | N | 0 | 2 | 2 | 2 | 0 | 0 | 0 | 0 | 2 | 0 |
| 22 | `<PesoNetoMineria>` | Mineral net weight | 19 | NUM | ≥0, 3 decimals | N | 0 | 2 | 2 | 2 | 0 | 0 | 0 | 0 | 2 | 0 |
| 23 | `<TipoAfiliacion>` | Affiliation type | 1 | NUM | 1=Affiliated, 2=Non-affiliated | N | 0 | 2 | 2 | 2 | 0 | 0 | 0 | 0 | 2 | 0 |
| 24 | `<Liquidacion>` | Settlement type | 1 | NUM | 1=Provisional, 2=Final | N | 0 | 2 | 2 | 2 | 0 | 0 | 0 | 0 | 2 | 0 |

---

### B.7 Unit Price (Field 25)

| # | Element | Description | Max | Type | Validation | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|---------|-------------|-----|------|------------|:-:|----|----|----|----|----|----|----|----|----|----| 
| 25 | `<PrecioUnitarioItem>` | Unit price | 20 | NUM | ≥0, 4 decimals | I | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |

> [!NOTE]
> For alcohol/beer producers: this is the **list price**. For insurance services: this is the **insurance premium**.

---

### B.8 Discounts (Fields 26-29)

| # | Element | Description | Max | Type | Validation | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|---------|-------------|-----|------|------------|:-:|----|----|----|----|----|----|----|----|----|----| 
| 26 | `<DescuentoMonto>` | Total discount | 18 | NUM | ≥0, 2 decimals | I | 2 | 2 | 2 | 2 | 2 | 0 | 2 | 2 | 2 | 0 |
| — | `<TablaSubDescuento>` | — | — | — | Container (up to 12 reps) | N | 2 | 2 | 2 | 2 | 2 | 0 | 2 | 2 | 2 | 0 |
| 27 | `<TipoSubDescuento>` | Sub-discount type | 1 | ALFA | "$" or "%" | N | 2 | 2 | 2 | 2 | 2 | 0 | 2 | 2 | 2 | 0 |
| 28 | `<SubDescuentoPorcentaje>` | Discount % | 5 | NUM | >0, 3 int + 2 dec | N | 2 | 2 | 2 | 2 | 2 | 0 | 2 | 2 | 2 | 0 |
| 29 | `<MontoSubDescuento>` | Sub-discount amount | 18 | NUM | ≥0, 2 decimals | N | 2 | 2 | 2 | 2 | 2 | 0 | 2 | 2 | 2 | 0 |

---

### B.9 Surcharges (Fields 30-33)

| # | Element | Description | Max | Type | Validation | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|---------|-------------|-----|------|------------|:-:|----|----|----|----|----|----|----|----|----|----| 
| 30 | `<RecargoMonto>` | Total surcharge | 18 | NUM | ≥0, 2 decimals | I | 2 | 2 | 2 | 2 | 2 | 0 | 2 | 2 | 2 | 0 |
| — | `<TablaSubRecargo>` | — | — | — | Container (up to 12 reps) | N | 2 | 2 | 2 | 2 | 2 | 0 | 2 | 2 | 2 | 0 |
| 31 | `<TipoSubRecargo>` | Sub-surcharge type | 1 | ALFA | "$" or "%" | N | 2 | 2 | 2 | 2 | 2 | 0 | 2 | 2 | 2 | 0 |
| 32 | `<SubRecargoPorcentaje>` | Surcharge % | 5 | NUM | >0, 3 int + 2 dec | N | 2 | 2 | 2 | 2 | 2 | 0 | 2 | 2 | 2 | 0 |
| 33 | `<MontoSubRecargo>` | Sub-surcharge amount | 18 | NUM | ≥0, 2 decimals | N | 2 | 2 | 2 | 2 | 2 | 0 | 2 | 2 | 2 | 0 |

---

### B.10 Additional Taxes per Item (Field 34)

| # | Element | Description | Max | Type | Validation | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|---------|-------------|-----|------|------------|:-:|----|----|----|----|----|----|----|----|----|----| 
| — | `<TablaImpuestoAdicional>` | — | — | — | Container (up to 2 reps) | N | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 0 | 0 |
| 34 | `<TipoImpuesto>` | Tax code | 3 | NUM | Tabla I (001-039) | N | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 0 | 0 |

---

### B.11 OtraMoneda per Item (Fields 35-38)

Foreign currency detail at item level.

| # | Element | Description | Max | Type | Validation | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|---------|-------------|-----|------|------------|:-:|----|----|----|----|----|----|----|----|----|----| 
| — | `<OtraMonedaDetalle>` | — | — | — | Container (FC detail) | N | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| 35 | `<PrecioOtraMoneda>` | Unit price (FC) | 20 | NUM | ≥0, 4 decimals | N | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| 36 | `<DescuentoOtraMoneda>` | Discount (FC) | 18 | NUM | ≥0, 2 decimals | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 37 | `<RecargoOtraMoneda>` | Surcharge (FC) | 18 | NUM | ≥0, 2 decimals | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 38 | `<MontoItemOtraMoneda>` | Line total (FC) | 18 | NUM | ≥0, 2 decimals | N | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |

---

### B.12 Line Total (Field 39)

| # | Element | Description | Max | Type | Validation | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|---------|-------------|-----|------|------------|:-:|----|----|----|----|----|----|----|----|----|----| 
| 39 | `<MontoItem>` | Line total | 18 | NUM | =(Price×Qty)−Discount+Surcharge | I | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |

> [!NOTE]
> `MontoItem` can be **0** for text correction credit notes (when `CodigoModificacion=2` in Información de Referencia).

---

## Section C: Subtotales Informativos (Informational Subtotals)

Optional informational subtotals (do not affect main totals). Up to 20 `<Subtotal>` entries can be included.

**XML Structure:**
```xml
<Subtotales>
  <Subtotal>...</Subtotal>
  <Subtotal>...</Subtotal>
</Subtotales>
```

| # | Element | Description | Max | Type | Validation | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|---------|-------------|-----|------|------------|:-:|----|----|----|----|----|----|----|----|----|----| 
| 1 | `<NumeroSubTotal>` | Subtotal number | 2 | NUM | Sequential 1 to n | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 2 | `<DescripcionSubtotal>` | Title | 40 | ALFA | — | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 3 | `<Orden>` | Display order | 2 | NUM | — | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 4 | `<SubTotalMontoGravadoTotal>` | Total taxable subtotal | 18 | NUM | ≥0, 2 decimals | N | 3 | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 0 |
| 5 | `<SubTotalMontoGravadoI1>` | Subtotal at 18% | 18 | NUM | ≥0, 2 decimals | N | 3 | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 0 | 0 |
| 6 | `<SubTotalMontoGravadoI2>` | Subtotal at 16% | 18 | NUM | ≥0, 2 decimals | N | 3 | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 0 | 0 |
| 7 | `<SubTotalMontoGravadoI3>` | Subtotal at 0% | 18 | NUM | ≥0, 2 decimals | N | 3 | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 0 |
| 8 | `<SubTotaITBIS>` | Subtotal ITBIS | 18 | NUM | ≥0, 2 decimals | N | 3 | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 0 |
| 9 | `<SubTotaITBIS1>` | Subtotal ITBIS 18% | 18 | NUM | ≥0, 2 decimals | N | 3 | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 0 | 0 |
| 10 | `<SubTotaITBIS2>` | Subtotal ITBIS 16% | 18 | NUM | ≥0, 2 decimals | N | 3 | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 0 | 0 |
| 11 | `<SubTotaITBIS3>` | Subtotal ITBIS 0% | 18 | NUM | ≥0, 2 decimals | N | 3 | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 0 |
| 12 | `<SubTotalImpuestoAdicional>` | Subtotal addtl taxes | 18 | NUM | >0, 2 decimals | N | 3 | 3 | 3 | 3 | 3 | 0 | 3 | 3 | 0 | 0 |
| 13 | `<SubTotalExento>` | Subtotal exempt | 18 | NUM | ≥0, 2 decimals | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 0 | 3 |
| 14 | `<MontoSubTotal>` | Subtotal amount | 18 | NUM | ≥0, 2 decimals | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 15 | `<Lineas>` | Line count in subtotal | 2 | NUM | >0 | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |


---

## Section D: DescuentosORecargos (Global Discounts/Surcharges)

Global discounts/surcharges that apply to the entire invoice (not per item). Up to 20 `<DescuentoORecargo>` entries can be included.

**XML Structure:**
```xml
<DescuentosORecargos>
  <DescuentoORecargo>...</DescuentoORecargo>
  <DescuentoORecargo>...</DescuentoORecargo>
</DescuentosORecargos>
```

| # | Element | Description | Max | Type | Validation | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|---------|-------------|-----|------|------------|:-:|----|----|----|----|----|----|----|----|----|----| 
| 1 | `<NumeroLinea>` | Line number | 2 | NUM | 1-20 | N | 2 | 2 | 2 | 2 | 2 | 0 | 2 | 2 | 2 | 0 |
| 2 | `<TipoAjuste>` | D (Discount) or R (Surcharge) | 1 | ALFA | — | N | 2 | 2 | 2 | 2 | 2 | 0 | 2 | 2 | 2 | 0 |
| 3 | `<IndicadorNorma1007>` | Norm 10-07 indicator | 1 | NUM | 1=Yes | N | 3 | 3 | 3 | 3 | 0 | 0 | 0 | 3 | 0 | 0 |
| 4 | `<DescripcionDescuentooRecargo>` | Description | 45 | ALFA | — | I | 3 | 3 | 3 | 3 | 3 | 0 | 3 | 3 | 3 | 0 |
| 5 | `<TipoValor>` | Value type (% or $) | 1 | ALFA | "%" or "$" | I | 2 | 2 | 2 | 2 | 2 | 0 | 2 | 2 | 2 | 0 |
| 6 | `<ValorDescuentooRecargo>` | Discount/surcharge % | 5 | NUM | >0, 3 int + 2 dec | I | 2 | 2 | 2 | 2 | 2 | 0 | 2 | 2 | 2 | 0 |
| 7 | `<MontoDescuentooRecargo>` | Discount/surcharge amount | 18 | NUM | ≥0, 2 decimals | I | 2 | 2 | 2 | 2 | 2 | 0 | 2 | 2 | 2 | 0 |
| 8 | `<MontoDescuentooRecargoOtraMoneda>` | Amount (foreign currency) | 18 | NUM | ≥0, 2 decimals | N | 3 | 3 | 3 | 3 | 3 | 0 | 3 | 3 | 3 | 0 |
| 9 | `<IndicadorFacturacionDescuentooRecargo>` | Tax indicator | 1 | NUM | 1=ITBIS1, 2=ITBIS2, 3=ITBIS3, 4=Exento | N | 2 | 2 | 2 | 2 | 2 | 0 | 2 | 2 | 2 | 0 |


**TipoDescuentoRecargo Values:**

| Code | Description |
|------|-------------|
| `1` | Discount (Descuento) |
| `2` | Surcharge (Recargo) |

**TipoValor Values (ALFA field):**

| Code | Description |
|------|-------------|
| `%` | Percentage (Porcentaje) |
| `$` | Fixed Amount (Monto) |

> [!WARNING]
> **Use literal characters**: `TipoValor` is an ALFA field. Send the actual characters `%` or `$`, not numeric values. The PDF explicitly defines these as "%" or "$".

**IndicadorFacturacionDescuentooRecargo Values:**

| Code | Description |
|------|-------------|
| `1` | ITBIS Rate 1 (18%) (ITBIS Tasa 1) |
| `2` | ITBIS Rate 2 (16%) (ITBIS Tasa 2) |
| `3` | ITBIS Rate 3 (0%) (ITBIS Tasa 3) |
| `4` | Exempt (Exento) - displayed as "E" in DGII documentation, but send value `4` |

> [!CAUTION]
> **Do not send "E"**: Although DGII documentation labels Exempt as "E", the field is NUM type. You must send the numeric value `4`, not the letter "E".

---

## Section E: Paginacion (Pagination)

For printed representation, indicates which items appear on each page.

> [!NOTE]
> Each `<Pagina>` element is wrapped inside the `<Paginacion>` container.
> Structure: `<Paginacion><Pagina>...</Pagina></Paginacion>`

| # | Element | Description | Max | Type | Validation | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|---------|-------------|-----|------|------------|:-:|----|----|----|----|----|----|----|----|----|----:|
| 1 | `<PaginaNo>` | Page number | 3 | NUM | 1-100, sequential | I | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| 2 | `<NoLineaDesde>` | Starting line | 3 | NUM | >0, ≤NoLineaHasta | N | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| 3 | `<NoLineaHasta>` | Ending line | 3 | NUM | >0, ≥NoLineaDesde | N | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| 4 | `<SubtotalMontoGravadoPagina>` | Page taxable subtotal | 18 | NUM | ≥0, 2 decimals | I | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 0 |
| 5 | `<SubtotalMontoGravado1Pagina>` | Page subtotal 18% | 18 | NUM | ≥0, 2 decimals | N | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 0 | 0 |
| 6 | `<SubtotalMontoGravado2Pagina>` | Page subtotal 16% | 18 | NUM | ≥0, 2 decimals | N | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 0 | 0 |
| 7 | `<SubtotalMontoGravado3Pagina>` | Page subtotal 0% | 18 | NUM | ≥0, 2 decimals | N | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 0 |
| 8 | `<SubtotalExentoPagina>` | Page exempt subtotal | 18 | NUM | ≥0, 2 decimals | I | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 2 |
| 9 | `<SubtotalItbisPagina>` | Page ITBIS subtotal | 18 | NUM | ≥0, 2 decimals | I | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 0 |
| 10 | `<SubtotalItbis1Pagina>` | Page ITBIS 18% | 18 | NUM | ≥0, 2 decimals | N | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 0 | 0 |
| 11 | `<SubtotalItbis2Pagina>` | Page ITBIS 16% | 18 | NUM | ≥0, 2 decimals | N | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 0 | 0 |
| 12 | `<SubtotalItbis3Pagina>` | Page ITBIS 0% | 18 | NUM | ≥0, 2 decimals | N | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 0 |
| 13 | `<SubtotalImpuestoAdicionalPagina>` | Page addtl taxes | 18 | NUM | >0, 2 decimals | I | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 0 | 0 |
| — | `<SubtotalImpuestoAdicional>` | Addtl taxes container (AREA) | — | — | — | — | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 0 | 0 |
| 14 | `<SubtotalImpuestoSelectivoConsumoEspecificoPagina>` | Page ISC specific | 18 | NUM | >0, 2 decimals | N | 2 | 2 | 2 | 2 | 0 | 0 | 0 | 2 | 0 | 0 |
| 15 | `<SubtotalOtrosImpuesto>` | Page other taxes | 18 | NUM | >0, 2 decimals | N | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 0 | 0 |
| 16 | `<MontoSubtotalPagina>` | Page subtotal | 18 | NUM | ≥0, 2 decimals | I | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| 17 | `<SubtotalMontoNoFacturablePagina>` | Page non-billable | 18 | NUM | ≥0, 2 decimals | N | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |

> [!WARNING]
> **Foreign currency pagination tags**: The tags `SubtotalMontoGravadoPaginaOtraMoneda` and `MontoSubtotalPaginaOtraMoneda` from earlier versions may not be present in all PDF versions. Verify against your specific PDF version before implementing.

> [!TIP]
> **Type "NUM" for monetary fields**: The PDF uses NUM for all monetary fields. When the field contains decimals, the validation specifies "2 decimals". This is the DGII convention.

---

## Section F: InformacionReferencia (Reference Information)

Used for Debit/Credit Notes (types 33, 34) to reference the modified invoice.

| # | Element | Description | Max | Type | Validation | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|---------|-------------|-----|------|------------|:-:|----|----|----|----|----|----|----|----|----|----:|
| 1 | `<NCFModificado>` | Modified e-NCF | 11/13/19 | ALFA | Valid NCF/e-NCF format | I | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2 | `<RNCOtroContribuyente>` | Other taxpayer RNC | 9/11 | NUM | Valid RNC (9 or 11 digits) | N | 0 | 0 | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| 3 | `<FechaNCFModificado>` | Modified e-CF date | 10 | DATE | DD-MM-YYYY | N | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| 4 | `<CodigoModificacion>` | Modification code | 1 | NUM | Values 1-5 | P | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| 5 | `<RazonModificacion>` | Modification reason | 90 | ALFA | Free text (e.g., "price error") | N | 0 | 0 | 3 | 3 | 0 | 0 | 0 | 0 | 0 | 0 |

**Modification Codes (CodigoModificacion):**

| Code | Description | Applies To |
|------|-------------|------------|
| `1` | Full cancellation (Anula documento completo) | Credit/Debit Note |
| `2` | Text correction (Corrige texto) | Credit/Debit Note |
| `3` | Amount correction (Corrige montos) | Credit/Debit Note |
| `4` | Contingency replacement (Reemplazo NCF emitido en contingencia) | Credit/Debit Note |
| `5` | Consumer Invoice Reference (Referencia Factura de Consumo Electrónica) | Factura Crédito Fiscal only |

> [!NOTE]
> **Footnote 80**: Codes 1, 2, 3 apply only when issuing a credit or debit note.
> 
> **Footnote 81**: Code 5 applies only for Factura de Crédito Fiscal referencing a consumer invoice.

---

## Section G: Fecha y Hora de Firma Digital (Signature Timestamp)

| # | Element | Description | Max | Type | Validation |
|---|---------|-------------|-----|------|------------|
| 1 | `<FechaHoraFirma>` | Signature timestamp | 19 | ALFANUM | DD-MM-YYYY HH:mm:ss, GMT-4. Must be ≤ current time. |

---

## Section H: Firma Digital (Digital Signature)

| # | Element | Description | Obligatoriedad |
|---|---------|-------------|----------------|
| 1 | `<Signature>` | XML-DSig enveloped signature covering entire document | 1 (Mandatory) |

See [Digital Signing Guide](../guides/digital-signing-guide.md) for implementation details.

---

