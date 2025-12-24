# e-NCF Cancellation (Anulación) Format v1.0

> **Original**: Formato Anulación de e-NCF v1.0  
> **Source**: [Formato Anulación de e-NCF v1.0.pdf](file:///home/romulo/visual/ecf/ecf-docs/Formatos%20XML/Formato%20Anulaci%C3%B3n%20de%20e-NCF%20v1.0.pdf)

---

## Overview

This format is used to **cancel (annul) unused e-NCF sequences** that were authorized by DGII but not yet used or sent. This applies only to sequences that have **not** been transmitted to the DGII or receptor.

**Common Use Cases:**
- Expiring sequences that won't be used before their expiration date
- Cleaning up test sequences before going to production
- Cancelling ranges due to configuration errors

**API Endpoint:**
- **Method**: `POST`
- **Endpoint**: `/api/AnulacionSecuencias`
- **Body**: Signed ANECF XML

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
| `CantidadeNCFAnulados` | NUM | — | 1 | Total count of annulled sequences |
| `FechaHoraAnulacioneNCF` | ALFA | 19 | 1 | Format: DD-MM-YYYY HH:MM:SS |

### DetalleAnulacion (Detail)

| Element | Type | Max Len | Req | Description |
|---------|------|---------|-----|-------------|
| `NoLinea` | NUM | — | 1 | Line number (1-10) |
| `TipoeCF` | NUM | 2 | 1 | e-CF type code (31-47) |
| `SecuenciaeNCFDesde` | ALFA | 13 | 1 | Starting e-NCF of range |
| `SecuenciaeNCFHasta` | ALFA | 13 | 1 | Ending e-NCF of range |
| `CantidadeNCFAnulados` | NUM | — | 1 | Count for this line |

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
