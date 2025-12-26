# Technical Specification: DGII Electronic Invoicing (e-CF)

> **Original**: Descripción Técnica de Facturación Electrónica v1.6  
> **Source**: [Descripcion-tecnica-de-facturacion-electronica.pdf](file:///home/romulo/visual/ecf/ecf-docs/Informe%20y%20Descripci%C3%B3n%20T%C3%A9cnica/Descripcion-tecnica-de-facturacion-electronica.pdf)  
> **Audience**: Developers / Solution Architects  
> **Scope**: Implementation Details, API Endpoints, and Business Logic  
> **Last Updated**: June 2023

> [!WARNING]
> **Pre-Certification Sequences Expiring**: Test ranges expire `31-12-2025`. Monitor DGII avisos/announcements for extensions (common in past years). Request production authorization early if certifying.

---

## 0. Overview & Purpose

### What is Electronic Invoicing?

Electronic Invoicing (Facturación Electrónica) is a business modality that uses **Electronic Fiscal Vouchers (e-CF)** instead of traditional paper invoices. These digital documents:

- Are **legally equivalent** to traditional fiscal invoices (NCF)
- Enable **real-time validation** by the tax authority (DGII)
- Support **automated B2B/B2C** document exchange between taxpayers
- Ensure **transparent audit trails** for fiscal compliance
- Reduce paper usage and manual processing errors

### Core Requirement: Dual Role

> [!IMPORTANT]
> To be an **Electronic Issuer**, you **must also be an Electronic Receiver**. 
>
> This creates a network where businesses exchange validated fiscal documents directly with each other, while DGII maintains oversight through parallel validation of all transactions.

### Communication Standard

All data exchange uses **XML (Extensible Markup Language)** transmitted via **REST APIs over HTTPS**. Each operation has a predefined XML format with corresponding XSD schemas available on the DGII portal. The tax authority defines specific formats for each type of document and operation.

### Document Flow Overview

```
┌────────────┐                    ┌────────────┐                    ┌────────────┐
│   Issuer   │                    │    DGII    │                    │  Receiver  │
│  (Emisor)  │                    │            │                    │ (Receptor) │
└─────┬──────┘                    └─────┬──────┘                    └─────┬──────┘
      │                                 │                                 │
      │ 1. Authenticate & get token     │                                 │
      ├────────────────────────────────>│                                 │
      │                                 │                                 │
      │ 2. Submit signed e-CF           │                                 │
      ├────────────────────────────────>│                                 │
      │                                 │                                 │
      │ 3. Receive trackId              │                                 │
      │<────────────────────────────────┤                                 │
      │                                 │                                 │
      │ 4. Poll for validation result   │                                 │
      ├────────────────────────────────>│                                 │
      │                                 │                                 │
      │ 5. If accepted, send to receiver│                                 │
      ├─────────────────────────────────┼────────────────────────────────>│
      │                                 │                                 │
      │                                 │ 6. Receiver sends ARECF         │
      │<────────────────────────────────┼─────────────────────────────────┤
      │                                 │                                 │
      │                                 │ 7. Receiver sends ACECF         │
      │<────────────────────────────────┼─────────────────────────────────┤
      │                                 │<────────────────────────────────┤
      │                                 │    (copy to DGII)               │
```

---

## XML Document Types Quick Reference

| Root Tag | Document Type | Use Case |
|----------|--------------|----------|
| `<ECF>` | Electronic Fiscal Invoice | Standard invoices (types 31-47) |
| `<ACECF>` | Commercial Approval | Buyer acceptance/rejection |
| `<ARECF>` | Acknowledgment of Receipt | Receiver confirms delivery |
| `<ANECF>` | Sequence Cancellation | Cancel unused e-NCF ranges |
| `<RFCE>` | Consumer Invoice Summary | Fast-track for <RD$250k |

---

## 1. Environments & Base URLs

The system is divided into three isolated environments. You must configure your application to switch base URLs dynamically.

| Environment | Purpose | Standard Base URL | Consumer Invoice Base URL (`fc`) |
|-------------|---------|-------------------|----------------------------------|
| **Pre-Certification** | Sandbox / Integration Testing | `https://ecf.dgii.gov.do/testecf/` | `https://fc.dgii.gov.do/testecf/` |
| **Certification** | Final Validation (15-step process) | `https://ecf.dgii.gov.do/certecf/` | `https://fc.dgii.gov.do/certecf/` |
| **Production** | Live Fiscal Data | `https://ecf.dgii.gov.do/ecf/` | `https://fc.dgii.gov.do/ecf/` |

> [!IMPORTANT]
> **Consumer Invoices (Facturas de Consumo)** have distinct routing.
> - **Class A (> RD$250,000)**: Sent to `ecf` domain (Standard).
> - **Class B (< RD$250,000)**: Sent to `fc` domain (Fast Track).

**Pre-Certification Environment Details:**
- Data is retained for **60 days**.
- Sequence ranges per e-CF type: `1` to `10,000,000` (except type 32).
- Type 32 (Consumer): `1` to `50,000,000`.
- Sequence expiration: `31-12-2025` (except type 32 and 34 which have no expiry).

---

## 📘 Interactive API Documentation (Swagger/OpenAPI)

Every environment exposes **Swagger/OpenAPI** documentation with interactive testing capabilities:

| Environment | Swagger URL Pattern |
|-------------|--------------------|
| Pre-Certification | `https://ecf.dgii.gov.do/testecf/{service}/help/index.html` |
| Certification | `https://ecf.dgii.gov.do/certecf/{service}/help/index.html` |
| Production | `https://ecf.dgii.gov.do/ecf/{service}/help/index.html` |

**Example URLs:**
- Pre-Cert Authentication: `https://ecf.dgii.gov.do/testecf/autenticacion/help/index.html`
- Pre-Cert Reception: `https://ecf.dgii.gov.do/testecf/recepcion/help/index.html`
- Consumer FC (Pre-Cert): `https://fc.dgii.gov.do/testecf/recepcionfc/help/index.html`

> [!TIP]
> Use Swagger UI to test endpoints interactively before writing code. It shows all available methods, parameters, and response schemas.

---

## 2. Authentication (The Handshake)

All API requests require a **Bearer Token**. The token is valid for **1 hour**.

### Step A: Request Seed
* **Method**: `GET`
* **Base URL**: `https://ecf.dgii.gov.do/{ambiente}/autenticacion`
* **Endpoint**: `/api/autenticacion/semilla`
* **Full URL Example**: `https://ecf.dgii.gov.do/testecf/autenticacion/api/autenticacion/semilla`
* **Response**: XML containing a random `<Valor>` (Seed) and timestamp.

```xml
<?xml version="1.0" encoding="utf-8"?>
<SemillaModel xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
  <valor>0000000-0000-0000-0000-000000000000</valor>
  <fecha>2019-03-13T14:33:32.8617792-04:00</fecha>
</SemillaModel>
```

**Response Fields:**
- `valor`: Encrypted seed value (UUID format)
- `fecha`: Timestamp when seed was generated

### Step B: Sign the Seed
You must digitally sign the **entire** XML received in Step A using your **Digital Certificate (.p12/.pfx)**.
* **Format**: XML-DSig (Enveloped Signature)
* **Algorithm**: RSA-SHA256
* **Reference URI**: `""` (Empty string, signing the whole doc)
* **Required**: X.509 Certificate must be embedded in `<KeyInfo>`

### Step C: Exchange for Token
* **Method**: `POST`
* **Base URL**: `https://ecf.dgii.gov.do/{ambiente}/autenticacion`
* **Endpoint**: `/api/autenticacion/validarsemilla`
* **Full URL Example**: `https://ecf.dgii.gov.do/testecf/autenticacion/api/autenticacion/validarsemilla`
* **Content-Type**: `multipart/form-data`
* **Body**: The **Signed XML** from Step B (field name: `xml`).
* **Response**: JSON/XML with the JWT `token`.

```json
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "expira": "2023-01-01T11:00:00Z",
  "expedido": "2023-01-01T10:00:00Z"
}
```

**Token Fields:**
- `token`: Bearer token for API authorization
- `expira`: Token expiration timestamp
- `expedido`: Token issuance timestamp

**Usage in Headers**: 
`Authorization: Bearer {token}`

> [!NOTE]
> See [RFC 6750](https://tools.ietf.org/html/rfc6750) for Bearer token authentication details.

---

## 3. Sending Invoices (The Core Loop)

Use the correct endpoint based on the document type and amount.

### Scenario A: Standard e-CF
**Scope**: B2B (31), Credit Notes (34), Gov (45), Export (46), and Consumer (32) **>= RD$250,000**.

* **Method**: `POST`
* **Base URL**: `https://ecf.dgii.gov.do/{ambiente}/recepcion`
* **Endpoint**: `/api/facturaselectronicas`
* **Full URL Example**: `https://ecf.dgii.gov.do/testecf/recepcion/api/facturaselectronicas`
* **Body**: Signed e-CF XML (Content-Type: `multipart/form-data`, field: `xml`).
* **Next Step**: You **must** poll the status using the response `trackId`.

**Response (JSON):**
```json
{
  "trackId": "string",
  "error": "string",
  "mensaje": "string"
}
```

**Response (XML):**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<RespuestaRecepcion>
  <trackId>string</trackId>
  <error>string</error>
  <mensaje>string</mensaje>
</RespuestaRecepcion>
```

**Response Fields:**
- `trackId`: Unique identifier to query validation status
- `error`: Error code if submission failed (null on success)
- `mensaje`: Descriptive message if submission failed

### Scenario B: Consumer Summary (RFCE)
**Scope**: Consumer Invoices (32) **< RD$250,000**.

* **Method**: `POST`
* **Service Path**: `{ambiente}/recepcionfc/api/recepcion/ecf` (Uses `fc` domain!)
* **Endpoint**: `/api/recepcion/ecf`
* **Full URL Example**: `https://fc.dgii.gov.do/testecf/recepcionfc/api/recepcion/ecf`
* **Body**: Signed RFCE XML (Content-Type: `multipart/form-data`, field: `xml`).
* **Return**: **Immediate validation response** with optional `trackId` for reference.

```json
{
  "trackId": "string",
  "rnc": "string",
  "encf": "string",
  "secuenciaUtilizada": true,
  "codigo": "string",
  "estado": "string",
  "mensajes": [{ "valor": "string", "codigo": 0 }]
}
```

**Response (XML):**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<Respuesta>
  <codigo>1</codigo>
  <estado>string</estado>
  <mensajes>
    <codigo>string</codigo>
    <valor>string</valor>
  </mensajes>
  <encf>string</encf>
  <secuenciaUtilizada>true</secuenciaUtilizada>
</Respuesta>
```

*   `estado`: `1`=Accepted, `2`=Rejected, `4`=Accepted Conditional.
*   `secuenciaUtilizada`: If `false` on rejection, you **can reuse** that e-NCF.
*   `trackId`: Returned for reference; status is already included in response (no polling needed).

> [!NOTE]
> **RFCE QR Code has fewer parameters** (see PDF page 43):
> - `RNCEmisor`
> - `eNCF`
> - `MontoTotal`
> - `CodigoSeguridad`
> 
> Unlike standard e-CF QR codes, RFCE does NOT require `RncComprador`, `FechaEmision`, or `FechaFirma`.

> [!WARNING]
> Do NOT send small consumer invoices to the Standard endpoint. They will be rejected or misprocessed.

---

## 4. Querying Status

### By TrackID (Standard Invoices)
* **Base URL**: `https://ecf.dgii.gov.do/{ambiente}/consultaresultado`
* **Endpoint**: `/api/consultas/estado?trackid={trackId}`
* **Method**: `GET`

**JSON Response Structure:**
```json
{
  "trackId": "string",
  "codigo": 0,
  "estado": "string",
  "rnc": "string",
  "eNCF": "string",
  "secuenciaUtilizada": true,
  "fechaRecepcion": "string",
  "mensajes": [
    { "valor": "string", "codigo": 0 }
  ]
}
```

**Status Codes (`codigo`/`estado`):**

| Code | Status | Meaning | Action |
|------|--------|---------|--------|
| `0` | **No encontrado** | TrackID not in system | Wait and retry, or check ID |
| `1` | **Aceptado** | Valid e-CF, has fiscal validity | **Success**. Store proof. |
| `2` | **Rechazado** | Validation failed, null invoice | Check `mensajes` for errors. See `secuenciaUtilizada`. |
| `3` | **En Proceso** | Invoice is being validated | Wait ~200-500ms, then poll again |
| `4` | **Aceptado Condicional** | Valid but with warnings (RFCE only) | Review warnings, fix for future invoices |

> [!TIP]
> **When can you reuse a rejected e-NCF sequence?**
> 
> If `secuenciaUtilizada = false` on a rejection, the following errors allow reuse:
> - Certificate and/or signature invalid
> - XML structure invalid (XSD failure)
> - Signer is not an authorized delegate for the RNC Emisor
> - e-NCF is not authorized for the RNC Emisor
> - e-NCF has expired at the time of submission
> - RNC Emisor is not an electronic issuer
> - RNC Emisor does not exist
> - RNC Emisor is not active

### By e-NCF (Consumer Summaries < 250k)
Since there is no TrackID for fast-track consumer invoices, query by document data.

* **Base URL**: `https://fc.dgii.gov.do/{ambiente}/consultarfce`
* **Endpoint**: `/api/Consultas/Consulta`
* **Method**: `GET`
* **Params**: 
    - `RNC_Emisor`: Issuer's RNC
    - `ENCF`: Electronic fiscal number (e.g., `E320000000001`)
    - `Cod_Seguridad_eCF`: Security code (first **6 characters** of signature hash)

**Example URL:**
```
https://fc.dgii.gov.do/ecf/consultarfce/api/Consultas/Consulta?RNC_Emisor=111111111&ENCF=E320000000001&Cod_Seguridad_eCF=AbC123
```

### By RNC/e-NCF (Alternative to TrackID)

If you lost the `trackId`, you can query standard e-CF status using document identifiers instead:

* **Service Path**: `{ambiente}/consultaestado/api/consultas/estado`
* **Endpoint**: `/api/consultas/estado`
* **Method**: `GET`
* **Params**:
    - `rncemisor`: Issuer's RNC
    - `ncfelectronico`: The e-NCF
    - `rnccomprador`: Buyer's RNC (optional)
    - `codigoseguridad`: Security code (optional)

**Example URL:**
```
https://ecf.dgii.gov.do/testecf/consultaestado/api/consultas/estado?rncemisor=101672919&ncfelectronico=E3100000001
```

> [!NOTE]
> To use this service, the authenticated user must be an authorized delegate for the RNC Emisor.

### Consulta TrackIds (Multiple Submissions)

When the same e-NCF was submitted multiple times (e.g., due to network errors), use this service to retrieve all associated TrackIDs:

* **Service Path**: `{ambiente}/consultatrackids/api/trackids/consulta`
* **Endpoint**: `/api/trackids/consulta`
* **Method**: `GET`
* **Params**:
    - `rncemisor`: Issuer's RNC
    - `encf`: The e-NCF

**Example URL:**
```
https://ecf.dgii.gov.do/testecf/consultatrackids/api/trackids/consulta?rncemisor=101672919&encf=E3100000001
```

**JSON Response Structure:**
```json
{
  "trackings": [
    {
      "trackId": "string",
      "estado": "string",
      "fechaRecepcion": "string"
    }
  ]
}
```

---

## 5. Construction of the QR Code (Timbre)

The "Representación Impresa" (Printed Invoice) must include a QR code pointing to the consultation URL.

> [!IMPORTANT]
> **Use QR Code Version 8** as specified by DGII: https://www.qrcode.com/en/about/version.html

**Base URL**: `https://ecf.dgii.gov.do/ecf/consultatimbre` (Varies by environment)

**Parameter Order (concatenate in this order as per DGII spec):**
1. `RncEmisor`
2. `RncComprador` (If present, else empty)
3. `eNCF`
4. `FechaEmision` (DD-MM-YYYY)
5. `MontoTotal`
6. `FechaFirma` (DD-MM-YYYY HH:MM:SS)
7. `CodigoSeguridad` (Take the first **6 characters** of the signature hash)

**URL Encoding Rules:**
You **must** URL-encode special characters in the Security Code if they appear. Common characters and their hex codes:

| Char | Hex | Char | Hex | Char | Hex |
|------|-----|------|-----|------|-----|
| Space | `%20` | `*` | `%2A` | `>` | `%3E` |
| `!` | `%21` | `+` | `%2B` | `\` | `%5C` |
| `#` | `%23` | `,` | `%2C` | `^` | `%5E` |
| `$` | `%24` | `/` | `%2F` | `_` | `%5F` |
| `&` | `%26` | `:` | `%3A` | `` ` `` | `%60` |
| `'` | `%27` | `;` | `%3B` | `"` | `%22` |
| `(` | `%28` | `=` | `%3D` | `-` | `%2D` |
| `)` | `%29` | `?` | `%3F` | `.` | `%2E` |
| `[` | `%5B` | `]` | `%5D` | `@` | `%40` |
| `<` | `%3C` | | | | |

**Example Constructed URL**:
`https://ecf.dgii.gov.do/ecf/consultatimbre?RncEmisor=101672919&RncComprador=&eNCF=E310000000001&FechaEmision=20-01-2023&MontoTotal=100.00&FechaFirma=20-01-2023%2010:00:00&CodigoSeguridad=AbC123`

> [!IMPORTANT]
> **Two Different QR Validation Endpoints:**
> - **Standard e-CF**: Use `consultatimbre` (e.g., `https://ecf.dgii.gov.do/ecf/consultatimbre?...`)
> - **RFCE (Consumer < 250k)**: Use `consultatimbrefc` (e.g., `https://fc.dgii.gov.do/ecf/consultatimbrefc?...`)
>
> The PDF example shows lowercase parameter names (`rncemisor`, `encf`, `codigoseguridad`). While services are case-insensitive, matching the PDF convention is safest.

---

## 6. Security Code Derivation

The **Security Code** (`CodigoSeguridadeCF`) displayed on printed invoices is derived from the signature:

- Take the first **6 characters** of the `<SignatureValue>` element (the digital signature hash).
- This code allows for quick document verification without full XML signature validation.
- The security code is **alphanumeric** and may contain special characters.

> [!IMPORTANT]
> When constructing the QR code URL, you **must** URL-encode the security code if it contains special characters.

---

## 7. Issuer-Receiver (B2B) Requirements

To be an Electronic Issuer, you **must also be a Receiver**. You must build an API to accept XMLs from other companies. This section describes the standard endpoints you must implement.

> [!IMPORTANT]
> **Requerimientos Generales (from PDF):**
> 1. Develop or acquire specialized software for generating, issuing, and receiving e-CF and commercial approvals
> 2. Work over SSL (use HTTPS)
> 3. Use REST API for communication
> 4. Use traditional network ports (80/443)
> 5. Services are NOT case-sensitive
> 6. Services must be publicly accessible via internet and always available
> 7. Have a digital certificate for physical person for tax procedures issued by INDOTEL/DGII authorized CA

---

### Required Endpoints to Build/Expose

All endpoints follow the same URL structure pattern:
```
https://{your-domain}/fe/{service}/api/{resource}
```

#### 1. Authentication Service (Optional but Recommended)

If implemented, provides security and access control for your P2P services.

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/fe/autenticacion/api/semilla` | `GET` | Returns XML seed for signing |
| `/fe/autenticacion/api/validacioncertificado` | `POST` | Validates signed seed and returns token |

**Semilla Response:**
```xml
<?xml version="1.0" encoding="utf-8"?>
<SemillaModel xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
  <valor>0XgGeOL2rFxxmt22g4abxa91yCXBlmyeci6H1+519R...</valor>
  <fecha>2022-07-27T11:59:31.3551245-04:00</fecha>
</SemillaModel>
```

**ValidacionCertificado Response:**
```json
{
  "token": "string",
  "expira": "yyyy-MM-ddTHH:mm:ssZ",
  "expedido": "yyyy-MM-ddTHH:mm:ssZ"
}
```

---

#### 2. Reception Service (Mandatory)

Receives e-CF documents from other taxpayers and returns an Acknowledgment of Receipt (ARECF).

| Property | Value |
|----------|-------|
| **Endpoint** | `/fe/recepcion/api/ecf` |
| **Method** | `POST` |
| **Content-Type** | `multipart/form-data` |
| **Input** | XML file of e-CF document |
| **Output** | Signed ARECF XML (Acknowledgment of Receipt) |
| **Auth Header** | `Authorization: Bearer {token}` (if auth is enabled) |

**Validations to Perform:**
- Valid file format
- Valid XML structure (XSD)
- Valid digital signature
- Required input parameter completed
- RNC of token authorized

**e-CF Types NOT to Accept (send rejection):**
Types 32, 41, 43, 45, 46, and 47 should NOT be accepted from other taxpayers.

**Example ARECF Response:**
```xml
<?xml version="1.0" encoding="utf-8"?>
<ARECF xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
  <DetalleAcusedeRecibo>
    <Version>1.0</Version>
    <RNCEmisor>131880600</RNCEmisor>
    <RNCComprador>132880600</RNCComprador>
    <eNCF>E310000000001</eNCF>
    <Estado>0</Estado>
    <FechaHoraAcuseRecibo>17-12-2020 11:19:06</FechaHoraAcuseRecibo>
  </DetalleAcusedeRecibo>
</ARECF>
```

---

#### 3. Commercial Approval Service (Mandatory)

Receives Commercial Approval (ACECF) documents from buyers.

| Property | Value |
|----------|-------|
| **Endpoint** | `/fe/aprobacioncomercial/api/ecf` |
| **Method** | `POST` |
| **Content-Type** | `multipart/form-data` |
| **Input** | XML file of ACECF document |
| **Output** | HTTP 200 (Success) or HTTP 400 (Failure) |
| **Auth Header** | `Authorization: Bearer {token}` (if auth is enabled) |

**Validations:**
- Commercial approvals for types 32, 41, 43, 46, 47 are NOT applicable
- Valid file format
- Valid XML structure (XSD)
- Valid digital signature
- Required input parameter completed
- RNC of token authorized

### Discovery (Where to send?)
Use the **Directory Query** to find another company's endpoints.

**List All Issuers:**
* **Service Path**: `{ambiente}/consultadirectorio/api/consultas/listado`
* **Endpoint**: `/api/consultas/listado`

**Get Specific Issuer:**
* **Service Path**: `{ambiente}/consultadirectorio/api/consultas/obtenerdirectorioporrnc`
* **Endpoint**: `/api/consultas/obtenerdirectorioporrnc?rnc={destination_rnc}`
* **Response Fields**:
  - `nombre`: Legal name of the taxpayer
  - `rnc`: Taxpayer's RNC
  - `urlRecepcion`: Host URL for e-CF reception service
  - `urlAceptacion`: Host URL for commercial approval service
  - `urlOpcional`: Host URL for authentication service (if used)

### Query Acknowledgment of Receipt
As an issuer, you can query whether the receiver acknowledged your e-CF:

* **Base URL**: `https://ecf.dgii.gov.do/{ambiente}/emisorreceptor`
* **Endpoint**: `/api/emision/consultaacuserecibo`
* **Method**: `GET`
* **Params**: `Rnc={ReceiverRNC}`, `Encf={eNCF}`
* **Response**:

```json
{
  "rnc": "string",
  "encf": "string",
  "estado": "string",
  "mensajes": ["string"]
}
```

**Response (XML):**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<RespuestaConsultaAcuseRecibo>
  <rnc>string</rnc>
  <encf>string</encf>
  <estado>string</estado>
  <mensajes>string</mensajes>
</RespuestaConsultaAcuseRecibo>
```

### Send Invoice to Another Taxpayer (Simulation)

Use the DGII simulation service to test sending e-CFs to another taxpayer.

* **Base URL**: `https://ecf.dgii.gov.do/{ambiente}/emisorreceptor`
* **Endpoint**: `/api/emision/emisioncomprobantes`
* **Method**: `POST`
* **Body**: JSON with e-CF details and target URL

**Input:**
```json
{
  "urlRecepcion": "string",
  "urlAutenticacion": "string",
  "rnc": "string",
  "encf": "string"
}
```

> [!NOTE]
> e-CF types 32, 41, 43, 45, 46, and 47 are NOT applicable for P2P sending to other taxpayers.

### Send Commercial Approval

> [!IMPORTANT]
> Commercial approvals must be sent to **two destinations**:
> 1. **To the Vendor/Issuer**: Via their P2P URL (found via Directory Query)
> 2. **To DGII**: Via the official `aprobacioncomercial` service to register the decision

**Simulation (P2P Testing)**:
* **Base URL**: `https://ecf.dgii.gov.do/{ambiente}/emisorreceptor`
* **Endpoint**: `/api/emision/envioaprobacioncomercial`
* **Method**: `POST`
* **Body**: Signed ACECF XML

**Official DGII Registration**:
* **Base URL**: `https://ecf.dgii.gov.do/{ambiente}/aprobacioncomercial`
* **Endpoint**: `/api/aprobacioncomercial`
* **Method**: `POST`
* **Body**: Signed ACECF XML

---

## 8. Technical Constraints & Infrastructure Requirements

### 8.1 Infrastructure Requirements

To participate in electronic invoicing, taxpayers must meet these technical requirements:

| Requirement | Description |
|-------------|-------------|
| **SSL/TLS** | All communication must use HTTPS |
| **REST API** | Standard HTTP methods (GET, POST) |
| **Network Ports** | Traditional ports (80/443) |
| **Case Sensitivity** | Services are **NOT** case-sensitive (added v1.6) |
| **Public Accessibility** | Your endpoints must be reachable via public internet (no VPN/private IPs) |
| **High Availability** | 24/7 uptime expected for production |

### 8.2 Digital Certificate Requirements

| Requirement | Specification |
|-------------|---------------|
| **Issuer** | Must be from an INDOTEL or DGII-authorized Certification Authority |
| **Type** | Physical Person (Persona Física) for tax purposes |
| **Format** | `.p12` or `.pfx` with private key |
| **SN Field Validation** | The certificate's Serial Number (SN) field **must** contain the owner's RNC, Cédula, or Passport number |
| **Usage** | Sign all outgoing XML documents |

> [!IMPORTANT]
> The certificate's SN (Serial Number) field is validated by DGII. If the SN does not contain a valid RNC, Cédula, or Passport number corresponding to the certificate owner, signature validation will fail.

### 8.3 Character Encoding & XML Rules

*   **Character Set**: **UTF-8** is mandatory.
*   **XML Special Characters**: The following characters must be escaped in XML content:

| Character | Name | XML Entity |
|-----------|------|------------|
| `"` | Quote | `&#34;` or `&quot;` |
| `&` | Ampersand | `&#38;` or `&amp;` |
| `'` | Apostrophe | `&#39;` or `&apos;` |
| `<` | Less than | `&#60;` or `&lt;` |
| `>` | Greater than | `&#62;` or `&gt;` |

### 8.4 File Naming Conventions

| Document Type | Naming Format | Example |
|---------------|---------------|---------|
| **e-CF** | `RNCEmisor` + `e-NCF` | `101672919E3100000001.xml` |
| **ACECF** | `RNCComprador` + `e-NCF` | `101672919E3100000001.xml` |
| **ARECF** | `RNCComprador` + `e-NCF` | `101672919E3100000001.xml` |
| **RFCE** | `RNCEmisor` + `e-NCF` | `101672919E3200000001.xml` |

> [!NOTE]
> For RFCE, the e-NCF used is typically the sequence of the summary itself, e.g., `E32...`.

### 8.5 Additional Rules

*   **Empty Tags**: **Forbidden**. Do not include `<Field></Field>` or `<Field />`. Omit the tag entirely if the value is null/empty.
*   **Floating Point**: Max 2 decimal places for amounts (standard), unless specified otherwise.

### 8.6 Digital Signature Requirements

*   **KeyInfo** must contain the X.509 Certificate.
*   **Reference URI** must be empty (`""`).
*   **Certificate SN**: The "SN" (Serial Number) field in the certificate must correspond to the RNC, Cédula, or Pasaporte of the certificate owner.
*   **Whitespace Handling**: Sign with `preserveWhiteSpace = false`. This is critical—signature validation will fail otherwise.
*   **Immutability**: Once signed, the XML **cannot be modified** in any way.

---

## 9. e-NCF Cancellation Service

To cancel **unused** e-NCF sequences (authorized but never sent):

* **Method**: `POST`
* **Service Path**: `{ambiente}/anulacionrangos/api/operaciones/anularrango`
* **Endpoint**: `/api/operaciones/anularrango`
* **Full URL Example**: `https://ecf.dgii.gov.do/testecf/anulacionrangos/api/operaciones/anularrango`
* **Body**: Signed ANECF XML with ranges to cancel (Content-Type: `multipart/form-data`, field: `xml`).

> [!CAUTION]
> You **cannot** cancel sequences that have already been sent to DGII or a receptor. Use a **Nota de Crédito** (type 34) instead.

See [Anulación Format](../xml-formats/anulacion-format-v1.0.md) for XML structure.

---

## 10. Service Status (Estatus Servicios)

Check if DGII e-CF services are online or in maintenance. This is essential for building robust retry logic.

**Base URL**: `https://statusecf.dgii.gov.do`

> [!WARNING]
> This service requires an **APIKEY** header instead of (or in addition to) the standard Bearer token.

### Get Platform Status

* **Endpoint**: `/api/estatusservicios/obtenerestatus`
* **Method**: `GET`
* **Headers**: `Authorization: Apikey {YOUR_API_KEY}`

**Returns**: Array of service statuses by environment.

```json
[
  {
    "servicio": "Recepcion",
    "estatus": "Disponible",
    "ambiente": "Produccion"
  },
  {
    "servicio": "Consulta Estado",
    "estatus": "Disponible",
    "ambiente": "Produccion"
  }
]
```

### Get Maintenance Windows

* **Endpoint**: `/api/estatusservicios/obtenerventanasmantenimiento`
* **Method**: `GET`
* **Headers**: `Authorization: Apikey {YOUR_API_KEY}`

**Returns**: Scheduled maintenance windows.

```json
{
  "ventanasMantenimiento": [
    {
      "ambiente": "Produccion",
      "horaInicio": "1:00 PM",
      "horaFin": "4:00 PM",
      "dias": [
        "06-08-2020",
        "20-08-2020",
        "10-09-2020"
      ]
    },
    {
      "ambiente": "Certificacion",
      "horaInicio": "1:00 PM",
      "horaFin": "4:00 PM",
      "dias": [
        "06-08-2020",
        "20-08-2020"
      ]
    }
  ]
}
```

### Verify Environment Status

* **Endpoint**: `/api/estatusservicios/verificarestado?ambiente={code}`
* **Method**: `GET`
* **Params**:
    - `ambiente`: `1` = PreCertificación, `2` = Producción, `3` = Certificación

---

## 11. Best Practices (Recomendaciones)

### Pre-Submission Checklist

1. **URL Validation**: Always verify endpoint URLs are correct before sending—typos cause silent failures
2. **XSD Validation**: Validate XML against official schemas **before** submitting to DGII
3. **Certificate Testing**: Test signature validation in Pre-Cert before going to Production
4. **Amount Threshold**: Double-check consumer invoice routing (RD$250,000 boundary) to use correct service

### Runtime Operations

5. **Token Management**: Implement token refresh **5-10 minutes before expiration** (1-hour lifetime). Never wait until expiration.
6. **Retry Logic**: On `En Proceso` status (code 3), wait 200-500ms before re-querying. Average validation time is ~200ms.
7. **Error Logging**: Store complete error responses (`mensajes` array) for debugging
8. **Delegate Verification**: Confirm authorization before querying status endpoints to avoid authorization errors

### Architecture Recommendations

9. **P2P Authentication**: Even though optional, implement token-based auth for your receiver endpoints—it's a security best practice
10. **Two QR Endpoints**: Remember to use:
    - `consultatimbre` for standard e-CFs
    - `consultatimbrefc` for consumer invoices (RFCE < RD$250k)
11. **Preserve Full XMLs**: Keep complete signed e-CFs for RFCE (<250k)—summaries are sent, but originals are required for audits
12. **Service Status Checks**: Integrate `statusecf.dgii.gov.do` checks before bulk operations to avoid maintenance windows

### Compliance Requirements

13. **File Naming**: Strictly follow `RNCEmisor+eNCF.xml` format for all document types
14. **Empty Tag Rule**: Never include empty tags—omit them entirely if no value
15. **Two-Destination Approvals**: Send commercial approvals to **BOTH** the vendor (P2P) AND DGII's official endpoint

---

## Appendix A: Common Validation Errors

### Reception Service Errors

| Error Message | Cause | Resolution |
|---------------|-------|------------|
| `Archivo no válido` | File format invalid | Ensure XML is well-formed UTF-8 |
| `Tipo de archivo no válido, favor proveer un XML` | Wrong Content-Type | Use `multipart/form-data` with `xml` field |
| `La estructura del archivo XML no es válido` | XSD validation failed | Validate against official XSD schema |
| `La firma del XML no es válida` | Signature verification failed | Check certificate, signing algorithm (SHA-256), and preserveWhiteSpace=false |
| `El RNC del certificado no está delegado...` | Certificate RNC not authorized | Verify signer is an authorized delegate for the RNC Emisor |

### Commercial Approval Errors

| Error Message | Meaning |
|---------------|---------|
| `Factura no encontrada para esta Aprobación comercial` | Referenced e-NCF doesn't exist in DGII system |
| `Aprobación Comercial no es requerida para este tipo de e-CF` | Document type (32, 41, 43, 46, 47) doesn't require approval |
| `No se encuentra un e-CF válido para esta aprobación comercial` | Referenced invoice was rejected or not found |

### TrackID Query Errors

| Error Message | Resolution |
|---------------|------------|
| `El campo RNC Emisor es requerido` | Missing required RNC parameter |
| `La longitud del RNC Emisor es inválida` | RNC must be 9 or 11 digits |
| `El RNC del token no está autorizado a consultar el trackid de este e-NCF` | Authenticated user not delegated for this RNC |

### Sequence Cancellation Errors

| Error Message | Meaning |
|---------------|---------|
| `Las secuencias que está intentando anular han sido utilizadas` | Cannot cancel sequences already used in submitted invoices |
| `El valor del campo SecuenciaeNCFDesde es mayor al del campo SecuenciaeNCFHasta` | Invalid range (FROM > TO) |
| `El campo NoLinea no es válido, no cumple orden secuencial` | Line numbers not sequential |

---

## Change Log Summary (Context)

*   **v1.6 (June 2023)**: Added RFCE query by security code.
*   **v1.5 (May 2023)**: Added RNC filter to directory. Clarified `secuenciaUtilizada` in consumer response. Universal date format for tokens.
*   **v1.4 (Apr 2022)**: UTF-8 standardized. File naming convention strictly enforcing RNC+eNCF.
