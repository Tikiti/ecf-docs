# Acknowledgment of Receipt (ARECF) XML Format v1.0

> **Original**: Formato Acuse de Recibo v1.0  
> **Source**: [Formato Acuse de Recibo v 1.0.pdf](file:///home/romulo/visual/ecf/ecf-docs/Formatos%20XML/Formato%20Acuse%20de%20Recibo%20v%201.0.pdf)

---

## Overview

The ARECF (Acuse de Recibo) is a confirmation document sent from the **receiver** to the **issuer** to indicate whether an e-CF was received. This is a **receipt confirmation only** — it does not indicate commercial acceptance.

> [!IMPORTANT]
> **Order of Operations:**
> 1. Receiver receives e-CF from issuer
> 2. Receiver sends ARECF (this document) to issuer — confirms receipt
> 3. Receiver sends [ACECF](./acecf-format-v1.0.md) to issuer — commercial acceptance/rejection
>
> The ARECF **must** be sent before the commercial approval (ACECF).

---

## Document Structure

```
<ARECF>
  <DetalleAcuseDeRecibo>
    <Version>1.0</Version>
    <RNCEmisor>...</RNCEmisor>
    <RNCComprador>...</RNCComprador>
    <eNCF>...</eNCF>
    <Estado>...</Estado>
    <CodigoMotivoNoRecibido>...</CodigoMotivoNoRecibido>
    <FechaHoraAcuseRecibo>...</FechaHoraAcuseRecibo>
  </DetalleAcuseDeRecibo>
  <Signature>...</Signature>
</ARECF>
```

---

## XML Element Definitions

| Element | Type | Max Len | Req | Description |
|---------|------|---------|-----|-------------|
| `Version` | NUM | 3 | 1 | Value: `1.0` |
| `RNCEmisor` | NUM | 9/11 | 1 | RNC of e-CF issuer |
| `RNCComprador` | NUM | 9/11 | 1 | RNC of entity issuing receipt |
| `eNCF` | ALFANUM | 13 | 1 | Electronic fiscal number |
| `Estado` | NUM | 1 | 1 | Status code (see below) |
| `CodigoMotivoNoRecibido` | NUM | 1 | 2 | Rejection reason (if Estado=1) |
| `FechaHoraAcuseRecibo` | ALFANUM | 19 | 1 | Format: DD-MM-YYYY HH:MM:SS |

---

## Status Codes (`Estado`)

| Code | Meaning |
|------|---------|
| `0` | e-CF Recibido (Received) |
| `1` | e-CF No Recibido (Not Received) |

---

## Rejection Reason Codes (`CodigoMotivoNoRecibido`)

| Code | Meaning |
|------|---------|
| `1` | Error de especificación (Specification error) |
| `2` | Error de Firma Digital (Digital signature error) |
| `3` | Envío duplicado (Duplicate submission) |
| `4` | RNC Comprador no corresponde (Buyer RNC mismatch) |

---

## Business Rules

1. **Purpose**: Confirms receipt only, not commercial acceptance
2. **Timing**: Must be sent immediately upon receipt of e-CF, before any commercial decision
3. **Digital Signature**: Entire XML must be signed by the acknowledging party (receiver)
4. **Conditional Field**: `CodigoMotivoNoRecibido` required only when `Estado = 1`
5. **One-to-One**: Each ARECF corresponds to exactly one e-CF
6. **No DGII Submission**: Unlike ACECF, the ARECF is sent directly to the issuer (not to DGII)
7. **Format Requirements**:
   - Dates: `DD-MM-YYYY HH:MM:SS`
   - RNC: 9 or 11 digits
   - eNCF: Exactly 13 characters

---

## Requirement Codes

| Code | Meaning |
|------|---------|
| `1` | Mandatory |
| `2` | Conditional |
