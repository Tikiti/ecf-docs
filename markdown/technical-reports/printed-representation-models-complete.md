# Illustrative Models of Printed Representation (RI)
## Electronic Invoicing (Facturación Electrónica)

---

## Contents (Contenidos)

**1. Illustrative models of Electronic Tax Credit Invoice (Factura de Crédito Fiscal Electrónica)**
- 1.1 Illustrative model with totals at the end of the invoice
- 1.2 Illustrative model including ITBIS in the 'Value' field of goods or services detail
- 1.3 Illustrative model including ITBIS in the 'Value' field and totals in the goods or services detail section
- 1.4 Illustrative model of e-FCF for Selective Consumption Tax
- 1.5 Illustrative model of Electronic Debit Note
- 1.6 Illustrative model of Electronic Credit Note
- 1.7 Illustrative model including Pagination (e-CF with two pages)

**2. Illustrative models of Invoices without fiscal value**
- 2.1 Illustrative model of Electronic Consumer Invoice with total amount equal to or greater than DOP 250 thousand
- 2.2 Illustrative model of Electronic Consumer Invoice with total amount less than DOP$ 250 thousand
- 2.3 Illustrative model of Electronic Consumer Invoice with amount less than DOP$250 thousand, made through Continuous Paper

**3. Printed Representation generated in Deferred Sending mode**
- 3.1 e-CF in Deferred Sending
- 3.2 Document in Deferred Sending mode when the e-CF cannot be generated

**4. Illustrative model of invoice issued in Contingency Mode**
- 4.1 General connectivity failure (Offline/Intermittent mode)
- 4.2 When e-CF issuance is not possible (Technical Incapacity)

---

## 1. Illustrative models of Electronic Tax Credit Invoice (Factura de Crédito Fiscal Electrónica)

### 1.1 Illustrative model with totals at the end of the invoice¹

*[Reference to illustrative image of the model]*

**Footnote:**
¹ The amount in the 'Valor' field of goods or services detail does not include taxes (price x quantity).

---

### 1.2 Illustrative model including ITBIS in the 'Value' field of goods or services detail

*[Reference to illustrative image of the model]*

**Characteristics**:
- The 'Valor' field in goods or services detail includes ITBIS
- Totals are shown at the end of the document

---

### 1.3 Illustrative model including ITBIS in the 'Value' field and totals in the goods or services detail section

*[Reference to illustrative image of the model]*

**Characteristics**:
- The 'Valor' field includes ITBIS
- Totals are shown within the goods or services detail section

---

### 1.4 Illustrative model of e-FCF for Selective Consumption Tax (Impuesto Selectivo al Consumo)

*[Reference to illustrative image of the model]*

**Characteristics**:
- Includes additional columns for ISC (Selective Consumption Tax - Impuesto Selectivo al Consumo)
- Applies to products like alcohol and tobacco
- Shows alcohol grades, ISC per unit, and ad-valorem ISC

---

### 1.5 Illustrative model of Electronic Debit Note (Nota de Débito Electrónica)

*[Reference to illustrative image of the model]*

**Characteristics**:
- Includes "NCF que modifica" field to reference the original document
- Uses receipt type 33

---

### 1.6 Illustrative model of Electronic Credit Note (Nota de Crédito Electrónica)

*[Reference to illustrative image of the model]*

**Characteristics**:
- Includes "NCF que modifica" field to reference the original document
- Uses receipt type 34

---

### 1.7 Illustrative model including Pagination (e-CF with two pages)

**Page 1 (Página 1):**
*[Reference to illustrative image of first page]*

**Page 2 (Página 2):**
*[Reference to illustrative image of second page]*

**Characteristics**:
- Multi-page documents must include "Página X de Y" (Page X of Y)
- Header information may appear on each page
- QR code and digital signature appear on the last page

---

## 2. Illustrative models of Invoices without fiscal value

### 2.1 Illustrative model of Electronic Consumer Invoice (Factura de Consumo Electrónica) with total amount equal to or greater than DOP 250 thousand

*[Reference to illustrative image of the model]*

**Characteristics**:
- Receipt type 32 (Electronic Consumer Invoice - Factura de Consumo Electrónica)
- When total amount is ≥ DOP$250,000.00
- **Requires client data** (RNC or Cédula)
- QR code with all standard parameters

---

### 2.2 Illustrative model of Electronic Consumer Invoice with total amount less than DOP$ 250 thousand

*[Reference to illustrative image of the model]*

**Characteristics**:
- Receipt type 32 (Electronic Consumer Invoice - Factura de Consumo Electrónica)
- When total amount is < DOP$250,000.00
- **Client data optional**
- QR code with reduced parameters (without RncComprador, FechaEmision, FechaFirma)

---

### 2.3 Illustrative model of Electronic Consumer Invoice with amount less than DOP$250 thousand, made through Continuous Paper

*[Reference to illustrative image of the model]*

**Characteristics**:
- Narrow format for POS/thermal printers
- Ideal for high-volume retail sales
- Amount < DOP$250,000.00
- Vertical design optimized for continuous paper (tickets)

---

## 3. Printed Representation generated in Deferred Sending mode (Envío Diferido)

### 3.1 e-CF in Deferred Sending (e-CF en Envío Diferido)

*[Reference to illustrative image of the model]*

**Characteristics**:
- e-CF generated and signed but not immediately sent to DGII
- Deferred transmission within 24 hours
- **Mandatory legend**: "Consulte su validez después de 24 horas" (Consult its validity after 24 hours)
- Includes normal QR code

---

### 3.2 Document in Deferred Sending mode when the e-CF cannot be generated²

*[Reference to illustrative image of the model]*

**Characteristics**:
- Used when the e-CF cannot be generated at the time of sale
- **Mandatory consultation link** so the receiver can consult the e-CF once transmitted
- Legend: "Consulte su validez después de 24 horas" (Consult its validity after 24 hours)

**Footnote:**
² (Electronic provider consultation link - Enlace consulta proveedor electrónico) this route must be generated by the electronic issuer, where the receiver can later consult their e-CF.

---

## 4. Illustrative model of invoice issued in Contingency Mode (Modalidad de Contingencia)

### 4.1 General connectivity failure (Offline/Intermittent mode - Falta de conectividad general)

*[Reference to illustrative image of the model]*

**Characteristics**:
- e-CF generated locally when there is no connection with DGII
- Transmitted to DGII when connection is restored
- **Mandatory legend**: "Consulte su validez después de 72 horas" (Consult its validity after 72 hours)
- Includes QR code
- The e-CF must be sent to DGII immediately upon connection restoration

---

### 4.2 When e-CF issuance is not possible (Technical Incapacity - Incapacidad Técnica)³

*[Reference to illustrative image of the model]*

**Characteristics**:
- **NON-electronic fiscal receipt format** (B-series)
- Used when there is total technical incapacity (system down, expired certificates, etc.)
- **Does NOT include QR code**
- Legend: "Comprobante Fiscal" (not "Comprobante Fiscal Electrónico")
- The issuer must have authorized B-series sequences for contingency

**Footnote:**
³ The issuer must have Non-Electronic Fiscal Receipt sequences available and deliver them to the non-electronic receiver.

**Subsequent process**:
Once the technical problem is resolved:
1. Generate the corresponding e-CF (E-series) with reference to the issued B-series NCF
2. **DO NOT send** this e-CF to the receiver (they already have the B-series)
3. Send the e-CF only to DGII
4. Include in `InformacionReferencia` the B-series NCF with `CodigoModificacion = 4` (Contingency NCF)

---

**End of document**

**Note**: This document presents visual illustrative models. For complete technical specifications of each field and validation, consult:
- Technical Report e-CF v1.0 (Informe Técnico e-CF v1.0)
- Electronic Fiscal Receipt Format (e-CF) v1.0 (Formato Comprobante Fiscal Electrónico)
