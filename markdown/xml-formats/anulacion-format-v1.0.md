# e-NCF Cancellation (Anulación) Format v1.0

> **Original**: Formato Anulación de e-NCF v1.0  
> **Source**: [Formato Anulación de e-NCF v1.0.pdf](file:///home/romulo/visual/ecf/ecf-docs/Formatos%20XML/Formato%20Anulaci%C3%B3n%20de%20e-NCF%20v1.0.pdf)

---

## Changelog (Bitácora)

**Version 1.0 - Updates as of 2022-05-24**

> [!NOTE]
> **Modification (does not imply version change):**  
> Validation e) was removed from the "Detalle de Anulación" section. Previously, it required that "the e-NCF must be greater than the one placed in the 'e-NCF Sequence From' field of any previously submitted annulment format." This validation has been eliminated.

---

## Overview

This format is used to **cancel (annul) unused e-NCF sequences** that were authorized by DGII but not yet used or sent. This applies only to sequences that have **not** been transmitted to the DGII or receptor.

**Common Use Cases:**
- Expiring sequences that won't be used before their expiration date
- Cleaning up test sequences before going to production
- Cancelling ranges due to configuration errors

**API Endpoint:**
- **Method**: `POST`
- **Service Path**: `{ambiente}/anulacionrangos/api/operaciones/anularrango`
- **Endpoint**: `/api/operaciones/anularrango`
- **Full URL Example**: `https://ecf.dgii.gov.do/testecf/anulacionrangos/api/operaciones/anularrango`
- **Body**: Signed ANECF XML (Content-Type: `multipart/form-data`, field: `xml`)

> [!CAUTION]
> If an invoice has already been sent to DGII or the receptor, it **cannot** be cancelled with this format. Use a **Nota de Crédito Electrónica (type 34)** instead.

---

## Document Structure

```
<AnulacionNCF>
  <Encabezado>
    <Version>1.0</Version>
    <RncEmisor>...</RncEmisor>
    <CantidadNCFAnulados>...</CantidadNCFAnulados>
    <FechaHoraAnulacioneNCF>...</FechaHoraAnulacioneNCF>
  </Encabezado>
  <DetalleAnulacion>
    <Anulacion>  <!-- 1 to 10 repetitions -->
      <NoLinea>...</NoLinea>
      <TipoeCF>...</TipoeCF>
      <TablaRangoSecuenciasAnuladaseNCF>
        <SecuenciaeNCFDesde>...</SecuenciaeNCFDesde>
        <SecuenciaeNCFHasta>...</SecuenciaeNCFHasta>
      </TablaRangoSecuenciasAnuladaseNCF>
      <CantidadeNCFAnulados>...</CantidadeNCFAnulados>
    </Anulacion>
  </DetalleAnulacion>
  <Signature>...</Signature>
</AnulacionNCF>
```

---

## XML Element Definitions

### Encabezado (Header)

| Element | Type | Max Len | Req | Description |
|---------|------|---------|-----|-------------|
| `Version` | NUM | 3 | 1 | Value: `1.0` |
| `RncEmisor` | NUM | 9/11 | 1 | Taxpayer RNC |
| `CantidadeNCFAnulados` | NUM | 10 | 1 | Total count of annulled sequences |
| `FechaHoraAnulacioneNCF` | ALFANUM | 19 | 1 | Format: DD-MM-YYYY HH:mm:ss |

> [!NOTE]
> The header field `CantidadeNCFAnulados` must equal the sum of all line-level `CantidadeNCFAnulados` values in the detail section.

### DetalleAnulacion (Detail)

| Element | Type | Max Len | Req | Description |
|---------|------|---------|-----|-------------|
| `NoLinea` | NUM | 2 | 1 | Line number (1-10) |
| `TipoeCF` | NUM | 2 | 1 | e-CF type code (31-47) |
| `SecuenciaeNCFDesde` | ALFANUM | 13 | 1 | Starting e-NCF of range |
| `SecuenciaeNCFHasta` | ALFANUM | 13 | 1 | Ending e-NCF of range |
| `CantidadeNCFAnulados` | NUM | 10 | 1 | Count for this line |

---

## e-CF Type Codes (TipoeCF)

| Code | Description |
|------|-------------|
| `31` | Factura de Crédito Fiscal Electrónica |
| `32` | Factura de Consumo Electrónica |
| `33` | Nota de Débito Electrónica |
| `34` | Nota de Crédito Electrónica |
| `41` | Comprobante de Compras Electrónico |
| `43` | Comprobante para Gastos Menores Electrónico |
| `44` | Comprobante de Regímenes Especiales Electrónico |
| `45` | Comprobante Gubernamental Electrónico |
| `46` | Comprobante para Exportaciones Electrónico |
| `47` | Comprobante para Pagos al Exterior Electrónico |

---

## Business Rules

1. **Authorized Issuer**: `RncEmisor` must be registered as electronic biller
2. **Eligibility**: A sequence can only be annulled if:
   - Authorized by DGII but not yet used
   - Invoice generated but **not sent** to DGII or receptor
3. **Post-Submission**: Cannot annul sequences already sent—use Nota de Crédito instead
4. **Range Validation**: `SecuenciaNCFHasta` ≥ `SecuenciaNCFDesde`
5. **Consistency**: Header `CantidadNCFAnulados` = sum of all line quantities
6. **Limits**:
   - Up to 10 different e-CF types per file
   - Up to 10,000 sequence ranges per type
7. **Digital Signature**: Document must be signed

---

## Requirement Codes

| Code | Meaning |
|------|---------|
| `1` | Mandatory |

---

## Example (Anexo I)

The following example demonstrates the ANECF format structure for cancelling e-NCF sequences.

### A. Encabezado (Header)

| Field | Value |
|-------|-------|
| Versión | 1.00 |
| RNC Emisor | 123456789 |
| Cantidad de e-NCF Anulados | 84 |
| Fecha y Hora de Firma | 01-01-2019 08:50:15 |

### B. DetalleAnulacion

**Line 1: Type 31**

| Field | Value |
|-------|-------|
| Número de Línea | 1 |
| Tipo de e-CF | 31 |
| Secuencia de e-NCF Desde | E310000000001 |
| Secuencia de e-NCF Hasta | E310000000001 |
| Secuencia de e-NCF Desde | E310000000005 |
| Secuencia de e-NCF Hasta | E310000000050 |
| Cantidad de e-NCF Anulados | 47 |

**Line 2: Type 44**

| Field | Value |
|-------|-------|
| Número de Línea | 2 |
| Tipo de e-CF | 44 |
| Secuencia de e-NCF Desde | E440000000010 |
| Secuencia de e-NCF Hasta | E440000000046 |
| Cantidad de e-NCF Anulados | 37 |

> [!NOTE]
> **Footnote 1**: The e-NCF structure consists of: series letter (E-Z, except P) + 2-digit type code + 10-digit sequence.
>
> **Footnote 2**: Series letters A-D and P are reserved and cannot be used.

---

## XML Structure Example

```xml
<?xml version="1.0" encoding="UTF-8"?>
<AnulacionNCF>
  <Encabezado>
    <Version>1.0</Version>
    <RncEmisor>123456789</RncEmisor>
    <CantidadeNCFAnulados>84</CantidadeNCFAnulados>
    <FechaHoraAnulacioneNCF>01-01-2019 08:50:15</FechaHoraAnulacioneNCF>
  </Encabezado>
  <DetalleAnulacion>
    <Anulacion>
      <NoLinea>1</NoLinea>
      <TipoeCF>31</TipoeCF>
      <TablaRangoSecuenciasAnuladaseNCF>
        <SecuenciaeNCFDesde>E310000000001</SecuenciaeNCFDesde>
        <SecuenciaeNCFHasta>E310000000001</SecuenciaeNCFHasta>
      </TablaRangoSecuenciasAnuladaseNCF>
      <TablaRangoSecuenciasAnuladaseNCF>
        <SecuenciaeNCFDesde>E310000000005</SecuenciaeNCFDesde>
        <SecuenciaeNCFHasta>E310000000050</SecuenciaeNCFHasta>
      </TablaRangoSecuenciasAnuladaseNCF>
      <CantidadeNCFAnulados>47</CantidadeNCFAnulados>
    </Anulacion>
    <Anulacion>
      <NoLinea>2</NoLinea>
      <TipoeCF>44</TipoeCF>
      <TablaRangoSecuenciasAnuladaseNCF>
        <SecuenciaeNCFDesde>E440000000010</SecuenciaeNCFDesde>
        <SecuenciaeNCFHasta>E440000000046</SecuenciaeNCFHasta>
      </TablaRangoSecuenciasAnuladaseNCF>
      <CantidadeNCFAnulados>37</CantidadeNCFAnulados>
    </Anulacion>
  </DetalleAnulacion>
  <Signature xmlns="http://www.w3.org/2000/09/xmldsig#">
    <!-- Digital signature goes here -->
  </Signature>
</AnulacionNCF>
```
