# Technical Specification: DGII Electronic Invoicing (e-CF)

> **Original**: Descripción Técnica de Facturación Electrónica v1.6  
> **Source**: [Descripcion-tecnica-de-facturacion-electronica.pdf](file:///home/romulo/visual/ecf/ecf-docs/Informe%20y%20Descripci%C3%B3n%20T%C3%A9cnica/Descripcion-tecnica-de-facturacion-electronica.pdf)  
> **Audience**: Developers / Solution Architects  
> **Scope**: Implementation Details, API Endpoints, and Business Logic  
> **Last Updated**: June 2023

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

## 2. Authentication (The Handshake)

All API requests require a **Bearer Token**. The token is valid for **1 hour**.

### Step A: Request Seed
* **Method**: `GET`
* **Endpoint**: `/api/Autenticacion/Semilla`
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
* **Endpoint**: `/api/Autenticacion/ValidarSemilla`
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
* **Endpoint**: `/api/Recepcion/EnviarFacturaElectronica`
* **Body**: Signed e-CF XML.
* **Return**: `trackId` (UUID).
* **Next Step**: You **must** poll the status using this `trackId`.

### Scenario B: Consumer Summary (Reducible)
**Scope**: Consumer Invoices (32) **< RD$250,000**.

* **Method**: `POST`
* **Endpoint**: `/api/Recepcion/EnviarResumenFacturaConsumo` (Note: Uses `fc` domain!)
* **Body**: Signed RFCE XML.
* **Return**: **Immediate response** (no TrackID required).

```json
{
  "rnc": "string",
  "encf": "string",
  "secuenciaUtilizada": true,
  "codigo": "string",
  "estado": "string",
  "mensajes": [{ "valor": "string", "codigo": 0 }]
}
```
*   `estado`: `1`=Accepted, `2`=Rejected.
*   `secuenciaUtilizada`: If `false` on rejection, you **can reuse** that e-NCF.

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
| `4` | **Aceptado Condicional** | Valid but with warnings | Review and fix for future invoices |

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

---

## 5. Construction of the QR Code (Timbre)

The "Respresentación Impresa" (Printed Invoice) must include a QR code pointing to the consultation URL.

**Base URL**: `https://ecf.dgii.gov.do/ecf/consultatimbre` (Varies by environment)

**Parameter Order (MANDATORY concatenation):**
1. `RncEmisor`
2. `RncComprador` (If present, else empty)
3. `eNCF`
4. `FechaEmision` (DD-MM-YYYY)
5. `MontoTotal`
6. `FechaFirma` (DD-MM-YYYY HH:MM:SS)
7. `CodigoSeguridad` (Take the first **6 characters** of the signature hash)

**URL Encoding Rules:**
You **must** URL-encode special characters in the Security Code if they appear:
`Space` `!` `#` `$` `&` `'` `(` `)` `*` `+` `,` `/` `:` `;` `=` `?` `@` `[` `]`

**Example Constructed URL**:
`https://ecf.dgii.gov.do/ecf/consultatimbre?RncEmisor=101672919&RncComprador=&eNCF=E310000000001&FechaEmision=20-01-2023&MontoTotal=100.00&FechaFirma=20-01-2023%2010:00:00&CodigoSeguridad=AbC123`

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

To be an Electronic Issuer, you **must also be a Receiver**. You must build an API to accept XMLs from other companies.

### Required Endpoints to Build/Expose

1.  **Reception Service**
    *   **Path**: `/fe/recepcion/api/ecf` (Standard convention)
    *   **Method**: `POST`
    *   **Payload**: Standard e-CF XML
    *   **Action**: Validate signature, store XML, return 200/202.

2.  **Commercial Approval Service**
    *   **Path**: `/fe/aprobacioncomercial/api/ecf`
    *   **Method**: `POST`
    *   **Payload**: ACECF XML (Commercial Approval/Rejection)
    *   **Action**: Process buyer's acceptance/rejection of your invoice.

3.  **Authentication (Optional)**
    *   You may implement the Seed/Token flow (`/fe/autenticacion/api/semilla`) if you wish to require authentication.

### Discovery (Where to send?)
Use the **Directory Query** to find another company's endpoints.
* **Endpoint**: `/api/Consulta/Directorio?rnc={destination_rnc}`
* **Response**: Returns `urlRecepcion` and `urlAceptacion` for that taxpayer.

---

## 8. Technical Constraints

*   **Character Set**: **UTF-8** is mandatory.
*   **File Naming**: `[RNC_EMISOR][E-NCF].xml` (e.g., `101672919E3100000001.xml`).
*   **Empty Tags**: **Forbidden**. Do not include `<Field></Field>` or `<Field />`. Omit the tag entirely if the value is null/empty.
*   **Floating Point**: Max 2 decimal places for amounts (standard), unless specified otherwise.
*   **Signature**:
    *   **KeyInfo** must contain the X.509 Certificate.
    *   **Reference URI** must be empty (`""`).

---

## 9. e-NCF Cancellation Service

To cancel **unused** e-NCF sequences (authorized but never sent):

* **Method**: `POST`
* **Endpoint**: `/api/AnulacionSecuencias`
* **Body**: Signed ANECF XML with ranges to cancel.

> [!CAUTION]
> You **cannot** cancel sequences that have already been sent to DGII or a receptor. Use a **Nota de Crédito** (type 34) instead.

See [Anulación Format](../xml-formats/anulacion-format-v1.0.md) for XML structure.

---

## Change Log Summary (Context)

*   **v1.6 (June 2023)**: Added RFCE query by security code.
*   **v1.5 (May 2023)**: Added RNC filter to directory. Clarified `secuenciaUtilizada` in consumer response. Universal date format for tokens.
*   **v1.4 (Apr 2022)**: UTF-8 standardized. File naming convention strictly enforcing RNC+eNCF.
