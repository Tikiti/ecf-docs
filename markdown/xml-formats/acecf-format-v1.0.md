# Commercial Approval (ACECF) XML Format v1.0

> **Original**: Formato Aprobación Comercial v1.0  
> **Source**: [Formato Aprobación Comercial v1.0.pdf](file:///home/romulo/visual/ecf/ecf-docs/Formatos%20XML/Formato%20Aprobaci%C3%B3n%20Comercial%20v1.0.pdf)

---

## Overview

The ACECF (Aprobación Comercial) is sent by the **buyer** to the **issuer** to communicate **commercial acceptance or rejection** of a received e-CF. Unlike ARECF (receipt acknowledgment), this indicates the buyer's business decision on the invoice content.

> [!NOTE]
> **Prerequisites**: Before sending an ACECF:
> 1. The e-CF must have been **accepted by DGII** (status `Aceptado` or `Aceptado Condicional`)
> 2. The receiver must have already sent an **ARECF** (acknowledgment of receipt) to the issuer
>
> You **cannot** send a commercial approval for an e-CF that DGII rejected.

---

## Document Structure

```
<ACECF>
  <DetalleAprobacionComercial>
    <Version>1.0</Version>
    <RNCEmisor>...</RNCEmisor>
    <eNCF>...</eNCF>
    <FechaEmision>...</FechaEmision>
    <MontoTotal>...</MontoTotal>
    <RNCComprador>...</RNCComprador>
    <Estado>...</Estado>
    <DetalleMotivoRechazo>...</DetalleMotivoRechazo>
    <FechaHoraAprobacionComercial>...</FechaHoraAprobacionComercial>
  </DetalleAprobacionComercial>
  <Signature>...</Signature>
</ACECF>
```

---

## XML Element Definitions

| Element | Type | Max Len | Req | Description |
|---------|------|---------|-----|-------------|
| `Version` | NUM | 3 | 1 | Value: `1.0` |
| `RNCEmisor` | NUM | 9/11 | 1 | RNC of e-CF issuer |
| `eNCF` | ALFANUM | 13 | 1 | Electronic fiscal number |
| `FechaEmision` | ALFANUM | 10 | 1 | Format: DD-MM-YYYY |
| `MontoTotal` | NUM | 18 | 1 | Total amount from e-CF |
| `RNCComprador` | NUM | 9/11 | 1 | Buyer's RNC |
| `Estado` | NUM | 1 | 1 | Status code (see below) |
| `DetalleMotivoRechazo` | ALFANUM | 250 | 2 | Rejection reason (if Estado=2) |
| `FechaHoraAprobacionComercial` | ALFANUM | 19 | 1 | Format: DD-MM-YYYY HH:MM:SS |

---

## Status Codes (`Estado`)

| Code | Meaning |
|------|---------|
| `1` | e-CF Aceptado (Accepted) |
| `2` | e-CF Rechazado (Rejected) |

---

## Business Rules

1. **Purpose**: Communicates commercial acceptance/rejection of e-CF content
2. **Prerequisite**: e-CF must be already accepted by DGII before commercial approval
3. **One Per e-CF**: A unique ACECF must be sent for each e-CF received
4. **DGII Notification**: A **copy must be sent to DGII** to register the commercial decision
5. **Data Matching**: These fields **must exactly match** the original e-CF:
   - `RNCEmisor`
   - `eNCF`
   - `FechaEmision`
   - `MontoTotal`
   - `RNCComprador`
6. **Conditional Field**: `DetalleMotivoRechazo` is mandatory only when `Estado = 2`
7. **Digital Signature**: Every document must be digitally signed by the buyer
8. **Irreversibility**: Commercial approvals/rejections cannot be reversed once submitted

---

## Requirement Codes

| Code | Meaning |
|------|---------|
| `1` | Mandatory |
| `2` | Conditional |
