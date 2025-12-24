# Printed Representation (Illustrative Models)

> **Original**: Representación Impresa (Modelos ilustrativos)  
> **Source**: [Representación Impresa (Modelos ilustrativos).pdf](file:///home/romulo/visual/ecf/ecf-docs/Informe%20y%20Descripci%C3%B3n%20T%C3%A9cnica/Representaci%C3%B3n%20Impresa%20(Modelos%20ilustrativos).pdf)  
> **Pages**: 17

---

## Overview

This document provides visual and technical guidelines for the printed version (Representación Impresa - RI) of electronic fiscal documents (e-CF) for the DGII in the Dominican Republic.

---

## Mandatory Layout Elements

Every printed representation must include:

### Header (Issuer Information)

| Element | Description |
|---------|-------------|
| Commercial Name | `NombreComercial` |
| Legal Name | `RazonSocial` |
| RNC | Taxpayer ID of the issuer |
| Branch Address | Address of the establishment |
| Document Title | e.g., "Factura de Crédito Fiscal Electrónica" |
| **e-NCF** | Electronic fiscal sequence number (starts with 'E') |
| Issue Date | `FechaEmision` |
| Expiration Date | `FechaVencimiento` |

### Client Information

| Element | When Required |
|---------|---------------|
| Client Name | Always |
| Client RNC/Cédula | Mandatory for E31; for E32 when total ≥ DOP 250,000 |

### Item Detail Table

| Column | Description |
|--------|-------------|
| Cantidad | Quantity |
| Descripción | Item description |
| UM | Unit of measure |
| Precio | Unit price |
| ITBIS | Tax amount |
| Valor | Line total |

> [!NOTE]
> The "Valor" column may include or exclude ITBIS, but must be consistent with the totals section.

### Totals Section

| Element | Description |
|---------|-------------|
| Subtotal Gravado | Taxable base amount |
| Total ITBIS | Total value added tax |
| ISC | Selective consumption tax (if applicable) |
| Propina Legal | Legal tip (if applicable) |
| **Total Facturado** | Grand total including all taxes |

### Footer and Security (Mandatory)

| Element | Description |
|---------|-------------|
| **QR Code** | For DGII verification |
| **Código de Seguridad** | 6-character security hash |
| **Fecha Firma** | Digital signature timestamp |
| **Legal Legend** | "Este documento es una representación impresa de un comprobante fiscal electrónico" |

---

## Model Variations

| Model | Type | Key Features |
|-------|------|--------------|
| **1.1** | Standard e-Credit Fiscal (E31) | Totals at end; "Valor" excludes tax |
| **1.2** | ITBIS in Detail | Shows ITBIS per line; "Valor" = subtotal before tax |
| **1.3** | Inclusive "Valor" | "Valor" includes tax; totals nested at bottom |
| **1.4** | Selective Tax (ISC) | Columns for alcohol/tobacco (grades, ISC/u, ISC%) |
| **1.5** | e-Debit Note (E33) | Includes "NCF que modifica" field |
| **1.6** | e-Credit Note (E34) | Includes "NCF que modifica" field |
| **1.7** | Pagination | Multi-page layout with "Página X de Y" |
| **2.1/2.2** | e-Consumption (E32) | Client data required when total ≥ 250k DOP |
| **2.3** | Continuous Paper (Ticket) | Narrow format for POS/thermal printers. Ideal for high-volume retail (< RD$250k). |
| **3.1** | Deferred Sending | Note: "Consult validity after 24 hours" |
| **4.1** | Contingency (Offline) | Note: "Consult validity after 72 hours" |
| **4.2** | Technical Incapacity | Fallback B-series NCF; no QR code |

---

## QR Code Requirements

| Property | Specification |
|----------|---------------|
| **Placement** | Bottom left or center |
| **Minimum Size** | ~2.5cm square (recommended) |
| **Purpose** | DGII verification scan |
| **Error Correction** | Level M or higher recommended |

**QR Code URL Format:**  
The QR code must contain a URL with the following parameters (in exact order):

```
https://ecf.dgii.gov.do/{ambiente}/consultatimbre?
  RncEmisor={RNCEmisor}&
  RncComprador={RNCComprador}&
  ENCF={eNCF}&
  FechaEmision={DD-MM-YYYY}&
  MontoTotal={amount}&
  FechaFirma={DD-MM-YYYY%20HH:MM:SS}&
  CodigoSeguridad={6-char-code}
```

> [!IMPORTANT]
> - URL-encode special characters in the Security Code
> - If no buyer RNC exists, leave the parameter empty (`RncComprador=`)
> - Use `%20` for spaces in the signature timestamp

---

## Special Scenarios

### Deferred Sending (Envío Diferido)

- Used when e-CF transmission is batched or delayed (but within 24 hours)
- Includes warning: **"Consulte su validez después de 24 horas"**
- The e-CF is generated and signed but not immediately transmitted to DGII
- **Mandatory Link**: Issuers **must** provide a URL where the receiver can consult the e-CF once it is transmitted to DGII.
  - *PDF Footnote*: "(Enlace consulta proveedor electrónico) esta ruta deberá ser generada por el emisor electrónico"

### Contingency Mode (Offline)

- Used during general connectivity failure to DGII services
- Includes warning: **"Consulte su validez después de 72 horas"**
- The e-CF is stored locally and transmitted when connection is restored
- QR code still included but consultation may be delayed

### Technical Incapacity (Incapacidad Técnica)

- **Fallback**: Issue standard B-series NCF (non-electronic)
- **No QR code** on these documents
- Must maintain authorized B-series sequences for this scenario
- Legend: "Comprobante Fiscal" (not "Comprobante Fiscal Electrónico")
- Once resolved, emit the corresponding e-CF with reference to the B-series NCF
