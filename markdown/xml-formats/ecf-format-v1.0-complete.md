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

