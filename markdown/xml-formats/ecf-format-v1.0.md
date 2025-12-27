# Electronic Fiscal Voucher (e-CF) XML Format v1.0

> **Original**: Formato Comprobante Fiscal Electrónico (e-CF) V1.0  
> **Source**: Formato Comprobante Fiscal Electrónico (e-CF) V1.0.pdf  
> **Pages**: 87  
> **Version**: 1.0 | October 2025

---

## Version History (Bitácora)

| Date | Changes |
|------|---------|
| **09-10-2025** | Added "Peso Colombiano" to Currency Table (Table II) |
| **17-09-2024** | Added "Gurda Haitiana" and "Peso Mexicano" currencies to Table II. Added units to Table IV: Hectárea, Mililitro, Miligramo, Onzas, Onzas Troy |
| **30-08-2022** | Added "Bandeja" unit of measure to Table IV |
| **06-05-2022** | Added units: Gross Register Tonnage, Pie cuadrado, Pasajero, Pulgadas, Parqueo Barcos en Muelle |
| **19-11-2021** | Updated Comprador obligatoriedad codes (1→2) for Nota de Crédito/Débito Electrónica |
| **04-11-2021** | Added "Quintal" unit of measure |
| **29-06-2021** | Separated Province and Municipality codes into columns in Table III |
| **10-11-2020** | Removed accents from `<Liquidacion>` and `<Mineria>` tags. Updated SubDescuento/SubRecargo descriptions |
| **28-07-2020** | Modified `<TotalITBISRetenido>` and `<TotalISRRetencion>` to accept zero values |

---

## 1. Introduction

This document describes the complete XML structure for Electronic Fiscal Vouchers (e-CF) in the Dominican Republic's DGII system, including field definitions, data types, validation rules, and obligatoriedad codes for each e-CF type.

Every e-CF must contain a **digital signature** that authenticates its origin and certifies its integrity.

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
  <InformacionReferencia>...</InformacionReferencia>  <!-- F. Reference Info -->
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
| `0` | **No Aplica** (Not Applicable) - Do not include |

---

## 5. Print Representation Codes (Columna I)

The PDF specification includes a "Representación Impresa" (Print Representation) column indicating how fields should appear in the printed version of the e-CF.

| Code | Meaning |
|------|---------|
| `N` | **No obligatoria** - Printing of this field is not mandatory |
| `I` | **Impresión obligatoria** - Printing of this data is mandatory |
| `P` | **Impreso en palabras** - Data must be printed in words (e.g., type codes must be spelled out, not just numbers) |

> [!NOTE]
> **Additional print representation rules from the PDF:**
> - Printing can be part of the field title in some cases
> - Foreign currency fields (`OtraMoneda`) printing is conditional on whether foreign currency transactions exist
> - For service invoicing, printing is not always mandatory

---

## 6. Data Type Reference

### 6.1 Contenido del e-CF (Section-Level Obligatoriedad Matrix)

The following table shows which sections are required for each e-CF type:

| Sección | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---------|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| Encabezado | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| Detalle de Bienes o Servicios | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| Subtotales Informativos | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| Descuentos o Recargos¹ | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| Paginación | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| Información de Referencia | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 2 |
| Fecha y Hora de la firma digital | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| Firma Digital | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |

> [!NOTE]
> ¹ *Descuentos o Recargos is conditional on whether a global discount/surcharge exists that affects the e-CF total.*

### 6.2 Field Type Reference

| Type in this Doc | PDF Original Type | Description |
|------------------|-------------------|-------------|
| `NUM` | NUM | Numeric integer |
| `ALFA` | ALFA | Alphabetic characters only |
| `ALFANUM` | ALFA NUM | Alphanumeric characters (letters and numbers) |
| `DATE` | ALFA NUM | Date field - PDF uses ALFA NUM with format validation `dd-MM-AAAA` |
| `DEC` | NUM | Decimal number - PDF uses NUM with decimal precision rules in validation column |

> [!IMPORTANT]
> **Type Mapping Note**: This document uses `DATE` and `DEC` as semantic types for developer convenience. The official PDF specification uses `ALFA NUM` for dates (with format `dd-MM-AAAA`) and `NUM` for decimals (with precision specified in validation). When implementing, ensure your data matches the PDF's underlying type expectations.

---

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
| 8 | `<TipoIngresos>` | Income type code | 2 | NUM | Values 01-06 (See Table VI) | N | 1 | 1 | 1 | 1 | 0 | 0 | 1 | 1 | 1 | 0 |
| 9 | `<TipoPago>` | Payment type | 1 | NUM | 1=Cash, 2=Credit, 3=Free | N | 1 | 1 | 1 | 1 | 1 | 3 | 1 | 1 | 1 | 3 |
| 10 | `<FechaLimitePago>` | Payment deadline | 10 | DATE | DD-MM-YYYY, ≥FechaEmision | N | 2 | 2 | 2 | 2 | 2 | 0 | 2 | 2 | 2 | 3 |
| 11 | `<TerminoPago>` | Payment terms | 15 | ALFANUM | Free text | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| — | `<TablaFormasPago>` | Payment methods table | — | — | Container (see note) | — | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 12 | `<FormaPago>` | Payment method code | 2 | NUM | Values 1-8 (Table V) | N | 3 | 3 | 3 | 0 | 3 | 0 | 3 | 3 | 3 | 3 |
| 13 | `<MontoPago>` | Payment amount | 18 | NUM | 16 int + 2 dec, ≥0 | N | 2 | 2 | 2 | 0 | 2 | 0 | 2 | 2 | 2 | 3 |
| 14 | `<TipoCuentaPago>` | Account type | 2 | ALFA | CT=Checking, AH=Savings, OT=Other | N | 3 | 3 | 3 | 0 | 3 | 0 | 3 | 3 | 3 | 3 |
| 15 | `<NumeroCuentaPago>` | Account number | 28 | ALFANUM | — | N | 3 | 3 | 3 | 0 | 3 | 0 | 3 | 3 | 3 | 3 |
| 16 | `<BancoPago>` | Bank name | 75 | ALFANUM | — | N | 3 | 3 | 3 | 0 | 3 | 0 | 3 | 3 | 3 | 3 |
| 17 | `<FechaDesde>` | Billing period start | 10 | ALFANUM | DD-MM-YYYY, ≤FechaHasta | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 3 |
| 18 | `<FechaHasta>` | Billing period end | 10 | ALFANUM | DD-MM-YYYY, ≥FechaDesde | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 3 |
| 19 | `<TotalPaginas>` | Total pages | 3 | NUM | >1, conditional if Paginación exists | I | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |

> [!NOTE]
> **`<TablaFormasPago>` Structure**: Each payment is wrapped in `<FormaDePago>` containing `<FormaPago>` + `<MontoPago>`.
> For multiple payments via cheque/transfer (code 2), only ONE `<TipoCuentaPago>` entry should be used.

> [!NOTE]
> **Footnote 1**: The e-NCF structure consists of: Series letter (E-Z, except P) + 2-digit type code + 10-digit sequence.
> 
> **Footnote 2**: `IndicadorNotaCredito = 1` means the credit note loses ITBIS credit benefit (issued >30 days after original).
>
> **Footnote 3**: `TipoPago = 3` (Gratuito/Free) invoices cannot be used for tax credit claims.

---

### A.2 Emisor (Issuer)

| # | Element | Description | Max | Type | Validation | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|---------|-------------|-----|------|------------|:-:|----|----|----|----|----|----|----|----|----|----| 
| 20 | `<RNCEmisor>` | Issuer RNC | 9/11 | NUM | Valid 9 or 11 digits | I | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 21 | `<RazonSocialEmisor>` | Legal name | 150 | ALFANUM | — | I | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 22 | `<NombreComercial>` | Trade name | 150 | ALFANUM | — | I | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 23 | `<Sucursal>` | Branch code | 20 | ALFANUM | — | I | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 24 | `<DireccionEmisor>` | Address | 100 | ALFANUM | — | I | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 25 | `<Municipio>` | Municipality code | 6 | NUM | Table III | P | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 26 | `<Provincia>` | Province code | 6 | NUM | Table III | P | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| — | `<TablaTelefonoEmisor>` | Phone container (up to 3) | — | — | — | — | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 27 | `<TelefonoEmisor>` | Phone number (up to 3) | 12 | ALFANUM | Format: xxx-xxx-xxxx | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 28 | `<CorreoEmisor>` | Email | 80 | ALFANUM | Valid email format | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 29 | `<WebSite>` | Website | 50 | ALFANUM | — | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 30 | `<ActividadEconomica>` | Economic activity | 100 | ALFANUM | — | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 31 | `<CodigoVendedor>` | Seller code | 60 | ALFANUM | Internal reference | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 32 | `<NumeroFacturaInterna>` | Internal invoice # | 20 | ALFANUM | — | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 33 | `<NumeroPedidoInterno>` | Internal order # | 20 | NUM | — | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 34 | `<ZonaVenta>` | Sales zone | 20 | ALFANUM | — | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 35 | `<RutaVenta>` | Sales route | 20 | ALFANUM | — | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 36 | `<InformacionAdicionalEmisor>` | Additional info | 250 | ALFANUM | — | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
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
| 44 | `<MunicipioComprador>` | Municipality | 6 | NUM | Table III | N | 3 | 3 | 3 | 3 | 3 | 0 | 3 | 3 | 3 | 3 |
| 45 | `<ProvinciaComprador>` | Province | 6 | NUM | Table III | N | 3 | 3 | 3 | 3 | 3 | 0 | 3 | 3 | 3 | 3 |
| 46 | `<PaisComprador>` | Country name | 60 | ALFA | Full country name | P | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 47 | `<FechaEntrega>` | Delivery date | 10 | DATE | DD-MM-YYYY | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 48 | `<ContactoEntrega>` | Delivery contact | 100 | ALFANUM | — | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 49 | `<DireccionEntrega>` | Delivery address | 100 | ALFANUM | — | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 50 | `<TelefonoAdicional>` | Delivery phone | 12 | ALFANUM | — | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 51 | `<FechaOrdenCompra>` | PO date | 10 | DATE | DD-MM-YYYY | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 52 | `<NumeroOrdenCompra>` | PO number | 20 | ALFANUM | — | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 53 | `<CodigoInternoComprador>` | Buyer internal code | 20 | ALFANUM | Internal reference | N | 3 | 3 | 3 | 3 | 3 | 0 | 3 | 3 | 3 | 0 |
| 54 | `<ResponsablePago>` | Payment responsible | 20 | ALFA | — | N | 3 | 3 | 3 | 3 | 3 | 0 | 3 | 3 | 3 | 0 |
| 55 | `<Informacionadicionalcomprador>` | Notes | 150 | ALFANUM | — | N | 3 | 3 | 3 | 3 | 3 | 0 | 3 | 3 | 3 | 0 |

> [!IMPORTANT]
> **Buyer Identification Rules (Reglas de Identificación del Comprador)**:
> - Type 31 (Crédito Fiscal): `RNCComprador` always mandatory
> - Type 32 (Consumo) ≥ RD$250,000: `RNCComprador` or `IdentificadorExtranjero` mandatory
> - Type 32 (Consumo) < RD$250,000: `RNCComprador` optional
> - Type 46 (Exports): Use `RNCComprador` for residents, `IdentificadorExtranjero` for non-residents

> [!NOTE]
> **Detailed Buyer Identification Footnotes:**
>
> **Footnote 4** (Field 38 `RNCComprador`): If the total amount of the electronic consumer invoice (Type 32) is **less than DOP$250,000**, the 'Buyer RNC' field is **optional**. Above this threshold, buyer identification becomes **mandatory**.
>
> **Footnote 5** (Field 38-39): Conditional on the buyer having RNC/ID. If the buyer is **foreign (diplomatic)**, the `RNCComprador` field must be **left blank** and the `IdentificadorExtranjero` field must be **completed** instead.
>
> **Footnote 6** (Field 38 - Type 46): According to **Article 10 of General Standard 05-19**, when **Commercial Free Zones (Airports and Ports)** make transfers of goods to **Residents**, the `RNCComprador` field **must be completed**.
>
> **Footnote 7** (Field 39 `IdentificadorExtranjero`): This field is completed ONLY if:
> - The e-CF is an electronic consumer invoice (Type 32) **> DOP$250,000** AND
> - The buyer **does not have RNC/ID** (is foreign)
> - The same applies to electronic credit/debit notes (Types 33/34) that affect Type 32 e-CF with value > DOP$250,000
> - When `IdentificadorExtranjero` exists, the `RNCComprador` field must be **omitted**.
>
> **Footnote 8** (Field 39 - Type 44): Conditional on the buyer being **foreign (diplomatic)**. If the `IdentificadorExtranjero` field is completed, the `RNCComprador` field should **not be completed** (mutually exclusive).
>
> **Footnote 9** (Field 39 - Type 46): According to **Article 10 of General Standard 05-19**, when **Commercial Free Zones (Airports and Ports)** make transfers of goods to **Non-Residents**, the `IdentificadorExtranjero` field **must be completed**.

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
| 72 | `<UnidadPesoBruto>` | Gross weight unit | 2 | NUM | Table IV | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 73 | `<UnidadPesoNeto>` | Net weight unit | 2 | NUM | Table IV | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 74 | `<CantidadBulto>` | Number of packages | 18 | DEC | >0, 2 decimals | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 75 | `<UnidadBulto>` | Package unit | 2 | NUM | Table IV | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 76 | `<VolumenBulto>` | Volume | 18 | DEC | >0, 2 decimals | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 77 | `<UnidadVolumen>` | Volume unit | 2 | NUM | Table IV | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |

> [!NOTE]
> **Port Tag Distinction**: Per DGII spec, these are 3 different ports:
> - `NombrePuertoEmbarque` (#60) = Port where goods are loaded
> - `NombrePuertoSalida` (#68) = Port of departure (may differ from loading port)
> - `NombrePuertoDesembarque` (#69) = Destination port (unloading)

---

### A.5 Transporte (Transport)

| # | Element | Description | Max | Type | Validation | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|---------|-------------|-----|------|------------|:-:|----|----|----|----|----|----|----|----|----|----| 
| 78 | `<ViaTransporte>` | Transport mode | 2 | NUM | 01=Terrestre, 02=Marítimo, 03=Aérea | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 79 | `<PaisOrigen>` | Country of origin of merchandise | 60 | ALFA | — | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
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
| 92 | `<MontoGravadoTotal>` | Total taxable amount | 18 | DEC | Sum of gravado amounts | I | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 0 |
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
| 105 | `<TipoImpuesto>` | Tax type code | 3 | NUM | Table I (001-039) | N | 2 | 2 | 2 | 2 | 0 | 0 | 0 | 2 | 0 | 0 |
| 106 | `<TasaImpuestoAdicional>` | Tax rate | 5 | NUM | Per Table I | N | 2 | 2 | 2 | 2 | 0 | 0 | 0 | 2 | 0 | 0 |
| 107 | `<MontoImpuestoSelectivoConsumoEspecifico>` | ISC Specific | 18 | DEC | ≥0 | N | 2 | 2 | 2 | 2 | 0 | 0 | 0 | 2 | 0 | 0 |
| 108 | `<MontoImpuestoSelectivoConsumoAdvalorem>` | ISC Ad-Valorem | 18 | DEC | ≥0, **see Granel rule** | N | 2 | 2 | 2 | 2 | 0 | 0 | 0 | 2 | 0 | 0 |
| 109 | `<OtrosImpuestosAdicionales>` | Other taxes | 18 | DEC | ≥0 | N | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 0 | 0 |

---

#### **ISC Calculation Formulas (Fórmulas de Cálculo ISC)**

The following calculation logic applies to **Field 107-109** based on tax code ranges defined in **Table I**.

> [!CAUTION]
> **Critical**: ISC (Impuesto Selectivo al Consumo / Selective Consumption Tax) calculations are STRICTLY regulated by DGII. Incorrect calculations will cause invoice rejection.

##### **Field 107: ISC Específico (Specific ISC) — Codes 006-022**

ISC Específico applies a **fixed amount per unit** (RD$ por unidad) for alcoholic beverages and tobacco products.

**Calculation Steps:**

1. **Verify Unit of Measure**:
   - If `UnidadMedida` = 18 (GRAN / Granel / Bulk): **DO NOT calculate ISC Específico** (set to 0)
   - Otherwise: Proceed to step 2

2. **For Alcohol Products (Codes 006-018)**:
   ```
   ISC_Específico = CantidadReferencia × GradosAlcohol × TasaISC × Subcantidad × CantidadItem
   ```
   - `CantidadReferencia` (Field 13): Reference quantity
   - `GradosAlcohol` (Field 17): Alcohol percentage (e.g., 40% = 40)
   - `TasaISC`: Rate from Table I for the specific code (e.g., 632.58)
   - `Subcantidad` (Field 15): Sub-quantity (liters of absolute alcohol per unit)
   - `CantidadItem` (Field 11): Item quantity

3. **For Tobacco Products (Codes 019-022)**:
   ```
   ISC_Específico = CantidadItem × CantidadReferencia × TasaISC
   ```
   - `CantidadItem` (Field 11): Item quantity
   - `CantidadReferencia` (Field 13): Reference quantity (cigarettes per pack)
   - `TasaISC`: Rate from Table I (e.g., RD$53.51 for 20-unit pack)

**Example (Beer @ Code 006):**
```
Item: 100 crates × 24 bottles × 0.355L @ 5% alcohol
ISC = 24 (ref qty) × 5 (alcohol %) × 632.58 (rate) × 0.355 (liters) × 100 (qty)
ISC = RD$2,689,266.00
```

---

##### **Field 108: ISC Ad-Valorem (Ad-Valorem ISC) — Codes 023-039**

ISC Ad-Valorem applies a **percentage of the sale price** for various products.

> [!WARNING]
> **Granel (Bulk) Products**: Code 023-035 items sold by bulk (UnidadMedida=18) require a **30% markup** on the base price before calculating tax.

**Calculation Steps:**

1. **Check if Granel (Bulk)**:
   - If `TipoImpuesto` is 023-035 AND `UnidadMedida` = 18 (Granel):
     ```
     ISC_AdValorem = (PrecioUnitarioItem × 1.30) × CantidadItem × TasaISC
     ```
   - Otherwise: Proceed to step 2

2. **For Non-Granel Products (Codes 023-035)**:
   ```
   Step 1: Remove ITBIS from reference price
   PrecioSinITBIS = PrecioUnitarioReferencia / (1 + ITBIS_Tasa1)
   
   Step 2: Subtract ISC Específico per unit (if any)
   BaseISC = PrecioSinITBIS - ISC_Específico_Unitario
   
   Step 3: Remove additional tax from base
   BaseISC = BaseISC / (1 + TasaImpuestoAdicional)
   
   Step 4: Calculate total ISC Ad-Valorem
   ISC_AdValorem = BaseISC × CantidadItem × CantidadReferencia × TasaISC
   ```

3. **For Other Ad-Valorem Products (Codes 036-039)**:
   ```
   Step 1: Remove ITBIS
   PrecioSinITBIS = PrecioUnitarioReferencia / (1 + ITBIS_Tasa1)
   
   Step 2: Subtract ISC Específico RATE (not amount)
   BaseISC = PrecioSinITBIS - Tasa_ISC_Específico
   
   Step 3: Remove additional tax
   BaseISC = BaseISC / (1 + TasaImpuestoAdicional)
   
   Step 4: Calculate total
   ISC_AdValorem = BaseISC × CantidadItem × CantidadReferencia × TasaISC
   ```

**Example (Granel Product @ Code 023):**
```
Item: 500L alcohol @ RD$100/L
ISC = (100 × 1.30) × 500 × 0.10 (10% rate)
ISC = RD$6,500.00
```

---

##### **Field 109: OtrosImpuestosAdicionales (Other Additional Taxes) — Codes 001-005**

Other additional taxes (Propina Legal, CDT, ISC Seguros, ISC Telecomunicaciones, Primera Placa).

**Calculation Steps:**

1. **Standard Calculation (Codes 001-005)**:
   ```
   OtrosImpuestos = MontoItem × TasaImpuesto
   ```

2. **If `IndicadorMontoGravado` = 1** (prices include ITBIS) for Codes 001-004:
   ```
   MontoSinITBIS = MontoItem / (1 + ITBIS_Tasa1)
   OtrosImpuestos = MontoSinITBIS × TasaImpuesto
   ```

3. **If `IndicadorNorma1007` = 1** (Standard 10-07) for Codes 002 & 004:
   ```
   Step 1: Sum all items with billing indicator = 1
   MontoGravadoTotal = Σ(MontoItem donde IndicadorFacturacion = 1)
   
   Step 2: Remove all taxes from base
   Base = MontoGravadoTotal / (1 + ITBIS_Tasa1 + Tasa_Codigo_002 + Tasa_Codigo_004)
   
   Step 3: Calculate tax
   OtrosImpuestos = Base × TasaImpuesto_Correspondiente
   ```

4. **If Global Discount Exists** (Section D - DescuentosORecargos):
   ```
   Step 1: Calculate line percentage
   PorcentajeLinea = MontoItem / Σ(TodosMontoItem)
   
   Step 2: Apply proportional discount
   DescuentoLinea = PorcentajeLinea × MontoDescuentoGlobal
   
   Step 3: Adjust item amount
   MontoItemAjustado = MontoItem - DescuentoLinea
   
   Step 4: Calculate tax on adjusted amount
   OtrosImpuestos = MontoItemAjustado × TasaImpuesto
   ```

**Example (Propina Legal 10% @ Code 001):**
```
Item amount: RD$1,000.00
Propina Legal = 1,000 × 0.10 = RD$100.00
```

> [!NOTE]
> **Footnote 27**: The `IndicadorNorma1007` field is located in Section D (Descuentos o Recargos / Discounts or Surcharges).
>
> **Footnote 28**: Line percentage = (Item amount / Total of all item amounts). This is used for proportional discount allocation.

---

| # | Element | Description | Max | Type | Validation | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|---------|-------------|-----|------|------------|:-:|----|----|----|----|----|----|----|----|----|----|
| 110 | `<MontoTotal>` | Grand total | 18 | DEC | ≥0, sum of components | I | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 111 | `<MontoNoFacturable>` | Non-billable amounts | 18 | DEC | Can be negative | N | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 2 | 0 |
| 112 | `<MontoPeriodo>` | Period amount | 18 | DEC | MontoTotal+MontoNoFacturable | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 113 | `<SaldoAnterior>` | Previous balance | 18 | DEC | Can be ± (positive or negative) | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 114 | `<MontoAvancePago>` | Advance payment amount | 18 | DEC | >0 (must be positive) | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 115 | `<ValorPagar>` | Amount to pay | 18 | DEC | Can be ± or 0 | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 116 | `<TotalITBISRetenido>` | ITBIS withheld total | 18 | DEC | ≥0 | N | 2 | 0 | 2 | 2 | 2 | 0 | 0 | 0 | 0 | 0 |
| 117 | `<TotalISRRetencion>` | ISR withheld total | 18 | DEC | ≥0 | N | 2 | 0 | 2 | 2 | 2 | 0 | 0 | 0 | 0 | 2 |
| 118 | `<TotalITBISPercepcion>` | ITBIS perceived total | 18 | DEC | >0 (must be positive) | N | 2 | 0 | 2 | 2 | 2 | 0 | 0 | 0 | 0 | 0 |
| 119 | `<TotalISRPercepcion>` | ISR perceived total | 18 | DEC | >0 (must be positive) | N | 2 | 0 | 2 | 2 | 2 | 0 | 0 | 0 | 0 | 0 |

---

#### **MontoTotal & ValorPagar Validation Formulas**

##### **Field 110: MontoTotal (Grand Total / Total General)**

**Formula:**
```
MontoTotal = MontoGravadoTotal + MontoExento + TotalITBIS + MontoImpuestoAdicional
```

> [!IMPORTANT]
> **Critical Validations for MontoTotal**:
>
> 1. **Pagination Consistency** (If Section E Paginación exists):
>    ```
>    MontoTotal MUST EQUAL Σ(MontoSubtotalPagina) from ALL pages
>    ```
>    If pagination is used, the sum of all page subtotals must exactly match the grand total. Mismatch will cause rejection.
>
> 2. **Credit Note Limit** (Type 34 - Nota de Crédito Electrónica):
>    ```
>    MontoTotal ≤ MontoTotal_of_NCFModificado
>    ```
>    Credit note amount cannot exceed the original invoice's total. Validate against the referenced e-NCF in Section F.
>
> 3. **Components Must Be Non-Negative**:
>    - `MontoGravadoTotal` ≥ 0
>    - `MontoExento` ≥ 0  
>    - `TotalITBIS` ≥ 0
>    - `MontoImpuestoAdicional` ≥ 0 (or omit if none)

> [!NOTE]
> **Footnote 30**: For e-CF type 34 (Electronic Credit Note), the total amount cannot exceed the total amount of the e-CF being modified.
>
> **Footnote ¹¹**: Conditional on taxed amount existing with at least one of the ITBIS rates (18%, 16%, or 0%).
>
> **Footnote ¹²**: Discounts and surcharges must be proportional to each ITBIS rate.

---

##### **Field 115: ValorPagar (Amount to Pay / Valor a Pagar)**

> [!IMPORTANT]
> **Two calculation methods** exist depending on whether **Norma 10-07** discount is applied:

**1. Standard Calculation (Sin Norma 10-07 / Without Standard 10-07):**
```
ValorPagar = MontoTotal - MontoAvancePago ± SaldoAnterior
```
- If `SaldoAnterior` is POSITIVE: Add it (customer owes from previous period)
- If `SaldoAnterior` is NEGATIVE: Subtract it (credit balance in favor of customer)

**2. With Norma 10-07 Discount (Con Norma 10-07):**
```
ValorPagar = MontoTotal - MontoDescuento - MontoAvancePago ± SaldoAnterior
```
- `MontoDescuento`: From Section D (Global discount with `IndicadorNorma1007 = 1`)
- This discount is subtracted AFTER the total, not before calculating ITBIS

> [!WARNING]
> **Norma 10-07 Special Rule** (General Standard 10-07):
> When `IndicadorNorma1007 = 1` in Section D (DescuentosORecargos), the discount applies to the **net base BEFORE ITBIS calculation**, but is reflected in `ValorPagar` as a direct subtraction from the total.
>
> For tax purposes, the discount must be distributed proportionally across ITBIS rates when calculating the tax base.

> [!NOTE]
> **Footnote 31**: The 'Discount amount' (`MontoDescuento`) field is located in Section D (Descuentos o Recargos / Discounts or Surcharges).
>
> **Footnote ³¹** (duplicate numbering in PDF): If the 'Standard 10-07 Indicator' field from the Discount or Surcharge section is completed, then: Amount payable = Total amount - Discount amount - Payment Advance amount ± Previous Balance.

---

> [!NOTE]
> **Perception Regime**: The PDF notes "Régimen de percepción no está vigente" (perception regime is not currently in force). Fields 118-119 are included for future use.



---

### A.7 OtraMoneda (Foreign Currency Totals in Header)

When transactions are in foreign currency, this section mirrors the Totales structure in the alternative currency.

| # | Element | Description | Max | Type | Validation | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|---------|-------------|-----|------|------------|:-:|----|----|----|----|----|----|----|----|----|----| 
| 120 | `<TipoMoneda>` | Currency code | 3 | ALFA | Table II | N | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
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
| 132 | `<TipoImpuestoOtraMoneda>` | Tax type code (FC) | 3 | NUM | Table I (001-039) | N | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 0 | 0 |
| 133 | `<TasaImpuestoAdicionalOtraMoneda>` | Tax rate (FC) | 5 | NUM | Per Table I | N | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 0 | 0 |
| 134 | `<MontoImpuestoSelectivoConsumoEspecificoOtraMoneda>` | ISC Specific (FC) | 18 | DEC | >0, 2 decimals | N | 2 | 2 | 2 | 2 | 0 | 0 | 0 | 2 | 0 | 0 |
| 135 | `<MontoImpuestoSelectivoConsumoAdvaloremOtraMoneda>` | ISC Ad-Valorem (FC) | 18 | DEC | >0, 2 decimals | N | 2 | 2 | 2 | 2 | 0 | 0 | 0 | 2 | 0 | 0 |
| 136 | `<OtrosImpuestosAdicionalesOtraMoneda>` | Other addtl taxes (FC) | 18 | DEC | >0, 2 decimals | N | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 0 | 0 |
| 137 | `<MontoTotalOtraMoneda>` | Grand total (FC) | 18 | DEC | ≥0, 2 decimals | N | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |

> [!NOTE]
> **OtraMoneda ImpuestosAdicionales**: When invoicing in foreign currency with additional taxes (ISC, etc.), this structure mirrors the DOP `ImpuestosAdicionales` structure but in the foreign currency amounts. **Up to 20 repetitions** of `<ImpuestosAdicionalesOtraMoneda>` entries are allowed.


---

## Section B: DetallesItem (Line Items)

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
| `0` | No Facturable (Non-billable) |
| `1` | Gravado ITBIS Tasa 1 (18%) |
| `2` | Gravado ITBIS Tasa 2 (16%) |
| `3` | Gravado ITBIS Tasa 3 (0%) |
| `4` | Exento (Exempt) |

> [!NOTE]
> **Type 43, 44, 47**: IndicadorFacturacion must = 4 (Exento). **Type 46**: must = 3 (ITBIS 0%).

> [!WARNING]
> If `IndicadorFacturacion=4` (Exento) AND `IndicadorAgenteRetencionoPercepcion=1` (R), then `MontoITBISRetenido` **must be 0**.

> [!NOTE]
> **Key Item Detail Footnotes (Notas Claves de Detalle de Ítem):**
>
> **Footnote 48** (Field 1 `NumeroLinea`): Line number must be **sequential starting at 1** and can go up to:
> - **100 items**: General limit for all e-CF types
> - **1,000 items**: Type 32 (Consumer) ≥ DOP$250,000
> - **10,000 items**: Type 32 (Consumer) < DOP$250,000
>
> **Footnote 49** (Field 4 `IndicadorFacturacion`): The billing indicator must be **printed in words** in the printed representation:
> - `0` → "No Facturable"
> - `1` → "Gravado ITBIS 18%"
> - `2` → "Gravado ITBIS 16%"
> - `3` → "Gravado ITBIS 0%"
> - `4` → "Exento"
>
> **Footnote 50** (Field 4 - Type 43): For e-CF type 43 (Minor Expenses / Gastos Menores), only values **1 or 4** are allowed (ITBIS 18% or Exempt).
>
> **Footnote 51** (Field 4 - Type 46): For e-CF type 46 (Exports / Exportaciones), only values **1, 3 or 4** are allowed (ITBIS 18%, 0%, or Exempt).
>
> **Footnote 52** (Field 5 `IndicadorAgenteRetencionoPercepcion`): Agent indicator meanings:
> - `1` = **Retención (R)** - Withholding agent
> - `2` = **Percepción (P)** - Perception agent
>
> **Footnote 53** (Field 6 `MontoITBISRetenido`): The ITBIS withheld at **item level** is summed to populate the header's `TotalITBISRetenido` field (Field 116 in Section A.6).
>
> **Footnote 54** (Field 9 `IndicadorBienoServicio` - Type 47): For e-CF type 47 (Foreign Payments / Pagos al Exterior), it is **mandatory** to indicate if the item is goods (1) or service (2). For services, this field **must = 2**.

---

### B.3 Item Details (Fields 8-14)

| # | Element | Description | Max | Type | Validation | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|---------|-------------|-----|------|------------|:-:|----|----|----|----|----|----|----|----|----|----| 
| 8 | `<NombreItem>` | Item name | 80 | ALFANUM | — | I | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 9 | `<IndicadorBienoServicio>` | Good/Service | 1 | NUM | 1=Bien, 2=Servicio | N | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 10 | `<DescripcionItem>` | Description | 1000 | ALFANUM | — | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 11 | `<CantidadItem>` | Quantity | 18 | NUM | >0, 2 decimals | I | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 12 | `<UnidadMedida>` | Unit of measure | 2 | NUM | Table IV codes | P | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 13 | `<CantidadReferencia>` | Reference qty | 18 | NUM | ≥0, for ISC 006-022 | N | 2 | 2 | 2 | 2 | 0 | 0 | 0 | 2 | 0 | 0 |
| 14 | `<UnidadReferencia>` | Reference unit | 2 | NUM | Table IV codes | N | 2 | 2 | 2 | 2 | 0 | 0 | 0 | 2 | 0 | 0 |

> [!NOTE]
> **Type 47 (Pagos al Exterior)**: Field 9 `IndicadorBienoServicio` must = 2 (Servicio).

---

### B.4 Subcantidad for ISC Products (Fields 15-18)

For alcohol, tobacco products with ISC codes 006-022 (specific) and 023-039 (ad-valorem).

| # | Element | Description | Max | Type | Validation | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|---------|-------------|-----|------|------------|:-:|----|----|----|----|----|----|----|----|----|----| 
| — | `<TablaSubcantidad>` | — | — | — | Container (up to 5 reps) | N | 2 | 2 | 2 | 2 | 0 | 0 | 0 | 2 | 0 | 0 |
| 15 | `<Subcantidad>` | Sub-quantity | 19 | NUM | ≥0, 3 decimals | N | 2 | 2 | 2 | 2 | 0 | 0 | 0 | 2 | 0 | 0 |
| 16 | `<CodigoSubcantidad>` | Sub-qty unit code | 2 | NUM | Table IV codes | N | 2 | 2 | 2 | 2 | 0 | 0 | 0 | 2 | 0 | 0 |
| 17 | `<GradosAlcohol>` | Alcohol % | 5 | NUM | >0, 3 int + 2 dec | I | 2 | 2 | 2 | 2 | 0 | 0 | 0 | 2 | 0 | 0 |
| 18 | `<PrecioUnitarioReferencia>` | Reference unit price | 18 | NUM | >0 (PVP for ISC calc) | I | 2 | 2 | 2 | 2 | 0 | 0 | 0 | 2 | 0 | 0 |

> [!NOTE]
> **Field 15 (Subcantidad)**: For alcohol = absolute alcohol content in liters. For tobacco = cigarette units per pack.
> **Field 18 (PrecioUnitarioReferencia)**: For ISC Ad-Valorem (codes 023-039), this is the retail price (PVP) used as tax base.

> [!NOTE]
> **ISC-Specific Footnotes (Notas Específicas ISC):**
>
> **Footnote 55** (Field 11 `CantidadItem`): The item quantity is **multiplied by the unit price** to obtain the item amount before discounts/surcharges.
>
> **Footnote 56** (Field 13 `CantidadReferencia`): Reference quantity is used to calculate **selective consumption taxes (ISC)** for certain products. Required for tax codes **006-022** (ISC  Específico).
>
> **Footnote 57** (Field 15 `Subcantidad` - Table): The subquantity table is **necessary** to calculate ISC on products derived from:
> - **Alcoholand beer** (codes 006-012)
> - **Tobacco and cigarettes** (codes 019-022)
> - This field is **only required** when invoicing goods at the **producer or manufacturer level**.
>
> **Footnote 58** (Field 15 `Subcantidad`): The subquantity represents the **reference units of measure** contained in the item unit. Examples:
> - **Alcohol**: Liters of absolute alcohol per bottle/container
> - **Tobacco**: Number of cigarettes per pack (cajetilla)
>
> **Footnote 59** (Field 17 `GradosAlcohol`): Alcohol degrees (%) are used to calculate ISC on **alcoholic beverages** with tax codes **006-018**. This is the percentage of absolute alcohol in the total volume per unit. Example: 40% alcohol = value "40".
>
> **Footnote 60** (Field 18 `PrecioUnitarioReferencia`): Reference unit price is used to calculate **ISC Ad-Valorem** on products with codes **023-039**. This is the retail price (PVP / Precio de Venta al Público) that serves as the tax base.

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
| 34 | `<TipoImpuesto>` | Tax code | 3 | NUM | Table I (001-039) | N | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 0 | 0 |

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

## Section C: Subtotales Informativos

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
| 3 | `<IndicadorNorma1007>` | Norma 10-07 indicator | 1 | NUM | 1=Yes | N | 3 | 3 | 3 | 3 | 0 | 0 | 0 | 3 | 0 | 0 |
| 4 | `<DescripcionDescuentooRecargo>` | Description | 45 | ALFA | — | I | 3 | 3 | 3 | 3 | 3 | 0 | 3 | 3 | 3 | 0 |
| 5 | `<TipoValor>` | Value type (% or $) | 1 | ALFA | "%" or "$" | I | 2 | 2 | 2 | 2 | 2 | 0 | 2 | 2 | 2 | 0 |
| 6 | `<ValorDescuentooRecargo>` | Discount/surcharge % | 5 | NUM | >0, 3 int + 2 dec | I | 2 | 2 | 2 | 2 | 2 | 0 | 2 | 2 | 2 | 0 |
| 7 | `<MontoDescuentooRecargo>` | Discount/surcharge amount | 18 | NUM | ≥0, 2 decimals | I | 2 | 2 | 2 | 2 | 2 | 0 | 2 | 2 | 2 | 0 |
| 8 | `<MontoDescuentooRecargoOtraMoneda>` | Amount (foreign currency) | 18 | NUM | ≥0, 2 decimals | N | 3 | 3 | 3 | 3 | 3 | 0 | 3 | 3 | 3 | 0 |
| 9 | `<IndicadorFacturacionDescuentooRecargo>` | Tax indicator | 1 | NUM | 1=ITBIS1, 2=ITBIS2, 3=ITBIS3, 4=Exento | N | 2 | 2 | 2 | 2 | 2 | 0 | 2 | 2 | 2 | 0 |


**TipoDescuentoRecargo Values:**

| Code | Description |
|------|-------------|
| `1` | Descuento (Discount) |
| `2` | Recargo (Surcharge) |

**TipoValor Values (ALFA field):**

| Code | Description |
|------|-------------|
| `%` | Porcentaje (Percentage) |
| `$` | Monto (Fixed Amount) |

> [!WARNING]
> **Use literal characters**: `TipoValor` is an ALFA field. Send the actual characters `%` or `$`, not numeric values. The PDF explicitly defines these as "%" o "$".

**IndicadorFacturacionDescuentooRecargo Values:**

| Code | Description |
|------|-------------|
| `1` | ITBIS Tasa 1 (18%) |
| `2` | ITBIS Tasa 2 (16%) |
| `3` | ITBIS Tasa 3 (0%) |
| `4` | Exento (displayed as "E" in DGII documentation, but send value `4`) |

> [!CAUTION]
> **Do not send "E"**: Although DGII documentation labels Exento as "E", the field is NUM type. You must send the numeric value `4`, not the letter "E".

---

## Section E: Paginacion (Pagination)

For printed representation, indicates which items appear on each page.

> [!NOTE]
> Each `<Pagina>` element is wrapped inside the `<Paginacion>` container.
> Structure: `<Paginacion><Pagina>...</Pagina></Paginacion>`

| # | Element | Description | Max | Type | Validation | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|---------|-------------|-----|------|------------|:-:|----|----|----|----|----|----|----|----|----|----|
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
|---|---------|-------------|-----|------|------------|:-:|----|----|----|----|----|----|----|----|----|----|
| 1 | `<NCFModificado>` | Modified e-NCF | 11/13/19 | ALFA | Valid NCF/e-NCF format | I | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2 | `<RNCOtroContribuyente>` | Other taxpayer RNC | 9/11 | NUM | Valid RNC (9 or 11 digits) | N | 0 | 0 | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| 3 | `<FechaNCFModificado>` | Modified e-CF date | 10 | DATE | DD-MM-YYYY | N | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| 4 | `<CodigoModificacion>` | Modification code | 1 | NUM | Values 1-5 | P | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| 5 | `<RazonModificacion>` | Modification reason | 90 | ALFA | Free text (e.g. "error en precio") | N | 0 | 0 | 3 | 3 | 0 | 0 | 0 | 0 | 0 | 0 |

**Modification Codes (CodigoModificacion):**

| Code | Description | Applies To |
|------|-------------|------------|
| `1` | Anula documento completo (Full cancellation) | Nota Crédito/Débito |
| `2` | Corrige texto (Text correction) | Nota Crédito/Débito |
| `3` | Corrige montos (Amount correction) | Nota Crédito/Débito |
| `4` | Reemplazo NCF emitido en contingencia (Contingency replacement) | Nota Crédito/Débito |
| `5` | Referencia Factura de Consumo Electrónica | Factura Crédito Fiscal only |

> [!NOTE]
> **Footnote 80**: Codes 1, 2, 3 apply only when issuing a credit or debit note.
> 
> **Footnote 81**: Code 5 applies only for Factura de Crédito Fiscal referencing a consumer invoice.

---

## Section G: Fecha y Hora de Firma Digital

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

## Code Tables (TABLAS)

### Table I: Impuestos Adicionales (Additional Tax Codes)

| Code | Tax Type | Abbreviation | Description | Rate |
|------|----------|--------------|-------------|------|
| 001 | Propina Legal | Propina Legal | Legal tip | 10% |
| 002 | CDT | CDT | Contribución Desarrollo Telecomunicaciones (Ley 153-98 Art. 45) | 2% |
| 003 | ISC | ISC | Servicios Seguros en general | 16% |
| 004 | ISC | ISC | Servicios de Telecomunicaciones | 10% |
| 005 | Primera Placa | Primera Placa | Expedición de la primera placa (First vehicle registration) | 17% |
| 006 | ISC Específico | ISC Específico | Cerveza | 632.58 |
| 007 | ISC Específico | ISC Específico | Vinos de uva | 632.58 |
| 008 | ISC Específico | ISC Específico | Vermut y demás vinos de uvas frescas | 632.58 |
| 009 | ISC Específico | ISC Específico | Demás bebidas fermentadas | 632.58 |
| 010 | ISC Específico | ISC Específico | Alcohol Etílico sin desnaturalizar (≥80%) | 632.58 |
| 011 | ISC Específico | ISC Específico | Alcohol Etílico sin desnaturalizar (<80%) | 632.58 |
| 012 | ISC Específico | ISC Específico | Aguardientes de uva | 632.58 |
| 013 | ISC Específico | ISC Específico | Whisky | 632.58 |
| 014 | ISC Específico | ISC Específico | Ron y demás aguardientes de caña | 632.58 |
| 015 | ISC Específico | ISC Específico | Gin y Ginebra | 632.58 |
| 016 | ISC Específico | ISC Específico | Vodka | 632.58 |
| 017 | ISC Específico | ISC Específico | Licores | 632.58 |
| 018 | ISC Específico | ISC Específico | Demás bebidas espirituosas | 632.58 |
| 019 | ISC Específico | ISC Específico | Alcohol etílico desnaturalizado | 632.58 |
| 020 | ISC Específico | ISC Específico | Cigarrillos de tabaco rubio | Per unit |
| 021 | ISC Específico | ISC Específico | Cigarrillos de tabaco negro | Per unit |
| 022 | ISC Específico | ISC Específico | Cigarros (puros) | Per unit |
| 023 | ISC Ad-Valorem | ISC Ad-Valorem | Productos de alcohol y bebidas alcohólicas | 10% |
| 024 | ISC Ad-Valorem | ISC Ad-Valorem | Vehículos de motor | Variable |
| 025 | ISC Ad-Valorem | ISC Ad-Valorem | Electrodomésticos | Variable |
| 026 | CESC | CESC | Contribución especial sector construcción | 5% |
| 027-039 | Various | Various | Other ISC codes per DGII classification | Variable |

> [!NOTE]
> ISC Específico rates are updated periodically by DGII. The 632.58 figure is the rate per liter of absolute alcohol as of the document date.

---

### Table II: Monedas (Currencies) — OFFICIAL DGII List

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

### Table III: Provincias y Municipios (Province/Municipality Codes)

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

### Table IV: Unidades de Medida (Units of Measure) - Complete List

| Code | Abbr | Measure |
|------|------|---------|
| 1 | BARR | Barril |
| 2 | BOL | Bolsa |
| 3 | BOT | Bote |
| 4 | BULTO | Bultos |
| 5 | BOTELLA | Botella |
| 6 | CAJ | Caja/Cajón |
| 7 | CAJETILLA | Cajetilla |
| 8 | CM | Centímetro |
| 9 | CIL | Cilindro |
| 10 | CONJ | Conjunto |
| 11 | CONT | Contenedor |
| 12 | DÍA | Día |
| 13 | DOC | Docena |
| 14 | FARD | Fardo |
| 15 | GL | Galones |
| 16 | GRAD | Grado |
| 17 | GR | Gramo |
| 18 | GRAN | Granel |
| 19 | HOR | Hora |
| 20 | HUAC | Huacal |
| 21 | KG | Kilogramo |
| 22 | kWh | Kilovatio Hora |
| 23 | LB | Libra |
| 24 | LITRO | Litro |
| 25 | LOT | Lote |
| 26 | M | Metro |
| 27 | M2 | Metro Cuadrado |
| 28 | M3 | Metro Cúbico |
| 29 | MMBTU | Millones de Unidades Térmicas |
| 30 | MIN | Minuto |
| 31 | PAQ | Paquete |
| 32 | PAR | Par |
| 33 | PIE | Pie |
| 34 | PZA | Pieza |
| 35 | ROL | Rollo |
| 36 | SOBR | Sobre |
| 37 | SEG | Segundo |
| 38 | TANQUE | Tanque |
| 39 | TONE | Tonelada |
| 40 | TUB | Tubo |
| 41 | YD | Yarda |
| 42 | YD2 | Yarda cuadrada |
| 43 | UND | Unidad |
| 44 | EA | Elemento |
| 45 | MILLAR | Millar |
| 46 | SAC | Saco |
| 47 | LAT | Lata |
| 48 | DIS | Display |
| 49 | BID | Bidón |
| 50 | RAC | Ración |
| 51 | Q | Quintal |
| 52 | GRT | Gross Register Tonnage (Toneladas de registro bruto) |
| 53 | P2 | Pie cuadrado |
| 54 | PAX | Pasajero |
| 55 | PULG | Pulgadas |
| 56 | STAY | Parqueo barcos en muelle |
| 57 | BDJ | Bandeja |
| 58 | HA | Hectárea |
| 59 | ML | Mililitro |
| 60 | MG | Miligramo |
| 61 | OZ | Onzas |
| 62 | OZT | Onzas Troy |

---

### Table V: Payment Methods (Formas de Pago)

| Code | Description |
|------|-------------|
| 1 | Efectivo (Cash) |
| 2 | Cheque/Transferencia/Depósito (Check/Transfer/Deposit) |
| 3 | Tarjeta de Crédito/Débito (Credit/Debit Card) |
| 4 | Venta a Crédito (Credit Sale) |
| 5 | Bonos o Certificados de regalo (Vouchers/Gift Certificates) |
| 6 | Permuta (Barter/Exchange) |
| 7 | Nota de crédito (Credit Note) |
| 8 | Otras Formas de pago (Other Payment Methods) |

> [!NOTE]
> If `FormaPago = 05` (gift certificates), the e-CF must be type 32 (Consumer Invoice).

---

### Table VI: Income Types (Tipos de Ingresos)

| Code | Description |
|------|-------------|
| 01 | Ingresos por operaciones (Operational income) |
| 02 | Ingresos financieros (Financial income) |
| 03 | Ingresos extraordinarios (Extraordinary income) |
| 04 | Ingresos por arrendamientos (Rental income) |
| 05 | Ingresos por venta de activo depreciable (Depreciable asset sale) |
| 06 | Otros ingresos (Other income) |

---

### Table VII: Payment Types (Tipos de Pago)

| Code | Description |
|------|-------------|
| 1 | Contado (Cash/Immediate payment) |
| 2 | Crédito (Credit) |
| 3 | Gratuito (Free/No charge) |

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
| `ALFA` | Alphanumeric string |
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
