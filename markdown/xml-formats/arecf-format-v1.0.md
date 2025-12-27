# Acknowledgment of Receipt (ARECF) XML Format v1.0

> **Original**: Formato Acuse de Recibo (ARECF) V1.0  
> **Source**: [Formato Acuse de Recibo v 1.0.pdf](file:///home/romulo/visual/ecf/ecf-docs/Formatos%20XML/Formato%20Acuse%20de%20Recibo%20v%201.0.pdf)  
> **Pages**: 6

---

## Version History (Bitácora)

**Version 1.0**
- Updated label for area 'DETALLE ACUSE DE RECIBO'

---

## Overview

The Acknowledgment of Receipt (ARECF - Acuse de Recibo) is the response that a **receiver** must send to an **issuer** as proof of e-CF reception. 

> [!IMPORTANT]
> **Key Points:**
> - This is **NOT** an acceptance/rejection of the invoice
> - It only confirms whether the e-CF was or was not received
> - Must be sent **before** the Commercial Approval (ACECF)
> - Receivers are **obligated** to confirm receipt
>
> **PDF Footnote 1:** The Acknowledgment of Receipt confirms that the document corresponds to an electronic invoice and has been received.

**Communication Flow:**
```
Issuer → e-CF → Receiver
Receiver → ARECF → Issuer (confirms receipt)
Receiver → ACECF → Issuer + DGII (commercial approval)
```

---

## Document Structure

```xml
<ARECF>
  <DetalleAcusedeRecibo>
    <Version>1.0</Version>
    <RNCEmisor>...</RNCEmisor>
    <RNCComprador>...</RNCComprador>
    <eNCF>...</eNCF>
    <Estado>...</Estado>
    <CodigoMotivoNoRecibido>...</CodigoMotivoNoRecibido>  <!-- Conditional -->
    <FechaHoraAcuseRecibo>...</FechaHoraAcuseRecibo>
  </DetalleAcusedeRecibo>
  <Signature>...</Signature>
</ARECF>
```

---

## Obligatoriedad Codes

| Code | Meaning |
|------|---------|
| `1` | **Obligatorio** (Mandatory) - Always required |
| `2` | **Condicional** (Conditional) - Required under specific conditions |

---

## Section A: DetalleAcusedeRecibo

| # | Element | Description | Type | Max | Validation | Oblig |
|---|---------|-------------|------|-----|------------|-------|
| 1 | `<Version>` | Format version | NUM | 3 | Fixed: `1.0` | 1 |
| 2 | `<RNCEmisor>` | Issuer's RNC | NUM | 9/11 | Valid RNC format | 1 |
| 3 | `<RNCComprador>` | Buyer's RNC (who sends ARECF) | NUM | 9/11 | Valid RNC format | 1 |
| 4 | `<eNCF>` | Electronic fiscal number | ALFANUM | 13 | Valid e-NCF format | 1 |
| 5 | `<Estado>` | Receipt status code | NUM | 1 | 0 or 1 | 1 |
| 6 | `<CodigoMotivoNoRecibido>` | Rejection reason code | NUM | 1 | 1-4 (conditional) | 2 |
| 7 | `<FechaHoraAcuseRecibo>` | Timestamp | ALFANUM | 19 | DD-MM-YYYY HH:mm:ss | 1 |

---

## Status Codes (Estado)

| Code | Meaning | Description |
|------|---------|-------------|
| `0` | **e-CF Recibido** | e-CF was successfully received |
| `1` | **e-CF No Recibido** | e-CF was NOT received (requires reason code) |

---

## Rejection Reason Codes (CodigoMotivoNoRecibido)

> [!NOTE]
> This field is **conditional** - only required when `Estado = 1` (Not Received)

| Code | Reason | Description |
|------|--------|-------------|
| `1` | Error de especificación | Specification/format error in the e-CF |
| `2` | Error de Firma Digital | Digital signature is invalid |
| `3` | Envío duplicado | Duplicate submission detected |
| `4` | RNC Comprador no corresponde | Buyer's RNC doesn't match |

---

## Section B: Digital Signature

| # | Element | Description | Oblig |
|---|---------|-------------|-------|
| 1 | `<Signature>` | XMLDSig enveloped signature | 1 |

The digital signature covers the entire ARECF document and must comply with:
- Signature Method: RSA-SHA256
- Reference URI: `""` (empty - covers entire document)

See [Digital Signing Guide](../guides/digital-signing-guide.md) for implementation.

---

## Sending the ARECF

**Direction**: Receiver → Issuer (direct P2P communication)

The ARECF is sent directly to the **issuer's** reception service URL, which can be obtained:
1. From the original e-CF header (`InformacionReferencia` section)
2. From DGII's directory service (`consultadirectorio` endpoint)

**Example Flow:**
```
1. Issuer sends e-CF to Receiver's /fe/recepcion/api/ecf
2. Receiver validates and creates ARECF
3. Receiver sends ARECF to Issuer's reception URL
4. Issuer confirms receipt
```

---

## Business Rules

1. **Timing**: ARECF must be sent **before** the Commercial Approval (ACECF)
2. **Scope**: Required for e-CF types that go between electronic issuers
3. **Signature**: Must be signed by an authorized delegate of the receiver's RNC
4. **Success Response**: If `Estado = 0`, no rejection reason is needed
5. **Failure Response**: If `Estado = 1`, must include `CodigoMotivoNoRecibido`

---

## Complete Example

```xml
<?xml version="1.0" encoding="UTF-8"?>
<ARECF>
  <DetalleAcusedeRecibo>
    <Version>1.0</Version>
    <RNCEmisor>123456789</RNCEmisor>
    <RNCComprador>987654321</RNCComprador>
    <eNCF>E310000000001</eNCF>
    <Estado>0</Estado>
    <FechaHoraAcuseRecibo>25-12-2024 10:30:45</FechaHoraAcuseRecibo>
  </DetalleAcusedeRecibo>
  <Signature xmlns="http://www.w3.org/2000/09/xmldsig#">
    <!-- Digital signature here -->
  </Signature>
</ARECF>
```

**Example with rejection:**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<ARECF>
  <DetalleAcusedeRecibo>
    <Version>1.0</Version>
    <RNCEmisor>123456789</RNCEmisor>
    <RNCComprador>987654321</RNCComprador>
    <eNCF>E310000000001</eNCF>
    <Estado>1</Estado>
    <CodigoMotivoNoRecibido>2</CodigoMotivoNoRecibido>
    <FechaHoraAcuseRecibo>25-12-2024 10:30:45</FechaHoraAcuseRecibo>
  </DetalleAcusedeRecibo>
  <Signature xmlns="http://www.w3.org/2000/09/xmldsig#">
    <!-- Digital signature here -->
  </Signature>
</ARECF>
```
