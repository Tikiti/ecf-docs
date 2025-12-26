# Commercial Approval (ACECF) XML Format v1.0

> **Original**: Formato Aprobación Comercial (ACECF) V1.0  
> **Source**: [Formato Aprobación Comercial v1.0.pdf](file:///home/romulo/visual/ecf/ecf-docs/Formatos%20XML/Formato%20Aprobaci%C3%B3n%20Comercial%20v1.0.pdf)  
> **Pages**: 6

---

## Overview

The Commercial Approval (ACECF - Aprobación Comercial) is the acceptance or rejection response that a **buyer** sends regarding an e-CF they received. Unlike the ARECF (which only confirms receipt), this document indicates whether the invoice is **commercially accepted or rejected**.

> [!IMPORTANT]
> **Key Differences from ARECF:**
> - **ARECF** = Confirms receipt only (did you get it?)
> - **ACECF** = Confirms acceptance/rejection (do you agree with it?)
>
> **Order of Operations:**
> 1. Issuer → e-CF → Receiver
> 2. Receiver → ARECF → Issuer (receipt confirmation)
> 3. Receiver → ACECF → Issuer **AND** DGII (commercial decision)

> [!WARNING]
> **Dual Submission Required:** The ACECF must be sent to **both**:
> - The original **issuer** (direct P2P)
> - **DGII** (for accepted e-CFs previously validated by DGII)

---

## Applicable e-CF Types

The Commercial Approval applies only to these e-CF types:

| Code | Type |
|------|------|
| 31 | Factura de Crédito Fiscal Electrónica |
| 33 | Nota de Débito Electrónica |
| 34 | Nota de Crédito Electrónica |
| 44 | Regímenes Especiales Electrónico |
| 45 | Gubernamental Electrónico |

> [!NOTE]
> Types 32 (Consumer), 41 (Purchases), 43 (Minor Expenses), 46 (Exports), and 47 (Foreign Payments) do **not** receive commercial approval.

---

## Document Structure

```xml
<ACECF>
  <DetalleAprobacionComercial>
    <Version>1.0</Version>
    <RNCEmisor>...</RNCEmisor>
    <eNCF>...</eNCF>
    <FechaEmision>...</FechaEmision>
    <MontoTotal>...</MontoTotal>
    <RNCComprador>...</RNCComprador>
    <Estado>...</Estado>
    <DetalleMotivoRechazo>...</DetalleMotivoRechazo>  <!-- Conditional -->
    <FechaHoraAprobacionComercial>...</FechaHoraAprobacionComercial>
  </DetalleAprobacionComercial>
  <Signature>...</Signature>
</ACECF>
```

---

## Obligatoriedad Codes

| Code | Meaning |
|------|---------|
| `1` | **Obligatorio** (Mandatory) |
| `2` | **Condicional** (Conditional) |
| `3` | **Opcional** (Optional) |

---

## Section A: DetalleAprobacionComercial

| # | Element | Description | Type | Max | Validation | Oblig |
|---|---------|-------------|------|-----|------------|-------|
| 1 | `<Version>` | Format version | NUM | 3 | Fixed: `1.0` | 1 |
| 2 | `<RNCEmisor>` | Issuer's RNC | NUM | 9/11 | a) Valid format b) Must match original e-CF | 1 |
| 3 | `<eNCF>` | e-NCF from original invoice | ALFANUM | 13 | a) Valid format b) Must match original e-CF | 1 |
| 4 | `<FechaEmision>` | Original e-CF issue date | ALFANUM | 10 | DD-MM-YYYY, must match original | 1 |
| 5 | `<MontoTotal>` | Total amount from e-CF | NUM | 18 | Must match original e-CF | 1 |
| 6 | `<RNCComprador>` | Buyer's RNC (sender of ACECF) | NUM | 9/11 | a) Valid format b) Must match original e-CF buyer | 1 |
| 7 | `<Estado>` | Approval status | NUM | 1 | 1 = Accepted, 2 = Rejected | 1 |
| 8 | `<DetalleMotivoRechazo>` | Rejection reason (text) | ALFANUM | 250 | Required when Estado = 2 | 2 |
| 9 | `<FechaHoraAprobacionComercial>` | Timestamp | ALFANUM | 19 | DD-MM-YYYY HH:mm:ss | 1 |

---

## Status Codes (Estado)

| Code | Meaning | Action |
|------|---------|--------|
| `1` | **e-CF Aceptado** | Invoice is commercially approved |
| `2` | **e-CF Rechazado** | Invoice is commercially rejected (requires reason) |

> [!NOTE]
> **When rejecting**, you **must** populate `DetalleMotivoRechazo` with a detailed explanation (free text up to 250 characters).

---

## Section B: Digital Signature

| # | Element | Description | Oblig |
|---|---------|-------------|-------|
| 1 | `<Signature>` | XMLDSig enveloped signature | 1 |

See [Digital Signing Guide](../guides/digital-signing-guide.md) for implementation.

---

## Sending the ACECF

### To Issuer (P2P)
- **Direction**: Receiver → Issuer  
- **Endpoint**: Issuer's `/fe/aprobacioncomercial/api/ecf`
- **Method**: `POST`

### To DGII
- **Direction**: Receiver → DGII
- **Service Path**: `{ambiente}/aprobacioncomercial/api/aprobacioncomercial`
- **Full URL Example**: `https://ecf.dgii.gov.do/ecf/aprobacioncomercial/api/aprobacioncomercial`
- **Method**: `POST`

> [!WARNING]
> DGII only accepts commercial approvals for e-CFs that were **previously accepted** by DGII's validation.

---

## Validation Rules

1. **RNCEmisor** must match the issuer from the original e-CF
2. **eNCF** must match the e-NCF from the original e-CF
3. **FechaEmision** must match the issue date from the original e-CF
4. **MontoTotal** must match the total from the original e-CF
5. **RNCComprador** must match the buyer from the original e-CF
6. **DetalleMotivoRechazo** is mandatory when `Estado = 2`

---

## Business Rules

1. **Signature**: Must be signed by an authorized delegate of the buyer's RNC
2. **Timing**: Should be sent after the ARECF (receipt acknowledgment)
3. **Scope**: Only for e-CF types 31, 33, 34, 44, 45
4. **DGII Copy**: Must also be sent to DGII for e-CFs that DGII accepted
5. **Rejection**: Free text explanation up to 250 characters

---

## Complete Example (Acceptance)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<ACECF>
  <DetalleAprobacionComercial>
    <Version>1.0</Version>
    <RNCEmisor>123456789</RNCEmisor>
    <eNCF>E310000000001</eNCF>
    <FechaEmision>25-12-2024</FechaEmision>
    <MontoTotal>15000.00</MontoTotal>
    <RNCComprador>987654321</RNCComprador>
    <Estado>1</Estado>
    <FechaHoraAprobacionComercial>25-12-2024 14:30:00</FechaHoraAprobacionComercial>
  </DetalleAprobacionComercial>
  <Signature xmlns="http://www.w3.org/2000/09/xmldsig#">
    <!-- Digital signature here -->
  </Signature>
</ACECF>
```

## Complete Example (Rejection)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<ACECF>
  <DetalleAprobacionComercial>
    <Version>1.0</Version>
    <RNCEmisor>123456789</RNCEmisor>
    <eNCF>E310000000001</eNCF>
    <FechaEmision>25-12-2024</FechaEmision>
    <MontoTotal>15000.00</MontoTotal>
    <RNCComprador>987654321</RNCComprador>
    <Estado>2</Estado>
    <DetalleMotivoRechazo>Precio incorrecto en artículos. Favor revisar factura y emitir nota de crédito.</DetalleMotivoRechazo>
    <FechaHoraAprobacionComercial>25-12-2024 14:30:00</FechaHoraAprobacionComercial>
  </DetalleAprobacionComercial>
  <Signature xmlns="http://www.w3.org/2000/09/xmldsig#">
    <!-- Digital signature here -->
  </Signature>
</ACECF>
```
