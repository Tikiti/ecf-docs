# Commercial Approval Format (ACECF)

**Version 1.0 | January 2020**

---

## 1. Introduction

The commercial approval or rejection is the response that the buyer must send to the issuer as proof of their conformity with the transaction carried out. Upon receiving the invoice, the buyer (receiver) is obligated to confirm to the issuer the receipt of the document with a receipt response¹ and may optionally submit the commercial approval or rejection, of which they must send a copy to DGII.²

This document describes the content that the XML format of the commercial approval must have, including the messages that will be used by electronic receivers.

---

## 2. Content of the Commercial Approval XML Format

**a) Commercial Approval Detail:** specifies the content of the response that the receiver must send to the issuer and submit a copy to DGII.

**b) Digital Signature:** which guarantees the integrity of the response and authenticity of the sender.

---

## 3. Obligatoriedad Codes

**1** - Obligatory data: the data must always be in the file.

**2** - Conditional data: the data is not obligatory but becomes so in certain cases, if a certain condition is met.

**3** - Optional data: the data is optional.

---

**¹** The Acknowledgment of Receipt notifies the reception of the electronic invoice, that is, whether it is received or not.

**²** DGII will receive commercial approval or rejection of e-CFs previously accepted by DGII.

---

### Content of the Commercial Approval Format

| File Sections | Section Obligatoriedad |
|---------------|------------------------|
| Commercial Approval Detail | 1 |
| Digital Signature | 1 |

Below, the content of each section is described, the format specifications for each field, and the obligatoriedad codes for each one. The names and characteristics are similar to the e-CF format.

---

## 4. Commercial Approval Detail

### AREA: COMMERCIAL APPROVAL DETAIL `<DetalleAprobacionComercial>`

| No. | Field | Description | Type | Max Length | Validation | Obligatoriedad |
|-----|-------|-------------|------|------------|------------|----------------|
| | AREA `<DetalleAprobacionComercial>` | COMMERCIAL APPROVAL DETAIL | | | | 1 |
| 1 | Version | Version of the Commercial Approval format. | NUM | 3 | Value: 1.0 | 1 |
| 2 | Issuer's RNC<br>`<RNCEmisor>` | National Registry Number of the taxpayer issuing the e-CF. | NUM | 9 or 11 | a) RNC complies with format structure.<br>b) RNC must match the issuer's RNC of the e-CF. | 1 |
| 3 | e-NCF<br>`<eNCF>` | Electronic Tax Receipt Number (e-NCF). | ALFANUM | 13 | a) e-NCF complies with format structure.<br>b) e-NCF must match the e-NCF of the e-CF submitted by the electronic issuer. | 1 |
| 4 | Issue Date<br>`<FechaEmision>` | Issue date of the e-CF. | ALFANUM | 10 | a) Date format complies with dd-MM-YYYY structure.<br>b) Issue date must match in the commercial approval and in the e-CF submitted by the electronic issuer. | 1 |
| 5 | Total Amount<br>`<MontoTotal>` | Value indicated in the Total Amount field of the e-CF. | NUM | 18 | a) Total Amount must match the value of the Total Amount field of the issued e-CF. | 1 |
| 6 | Buyer's RNC<br>`<RNCComprador>` | National Registry Number of the taxpayer issuing the Commercial Approval of the e-CF. | NUM | 9 or 11 | a) RNC complies with format structure.<br>b) RNC must match the buyer's RNC of the e-CF. | 1 |
| 7 | Status<br>`<Estado>` | Numeric code indicating the status of the Commercial Approval. | NUM | 1 | Numeric code of the Commercial Approval status<br>1: e-CF Accepted<br>2: e-CF Rejected | 1 |
| 8 | Rejection Reason Detail<br>`<DetalleMotivoRechazo>` | The rejection reason is indicated in detail.<br>Conditional on the Status field being code 2. | ALFANUM | 250 | No validation | 2 |
| 9 | Commercial Approval Generation Date and Time<br>`<FechaHoraAprobacionComercial>` | Date and time in format dd-MM-YYYY HH:mm:ss | ALFANUM | 19 | Date and time comply with the indicated format | 1 |
| | END AREA | COMMERCIAL APPROVAL DETAIL | | | | |

---

## 5. Digital Signature

### AREA: SIGNATURE `<Signature>`

| No. | Field | Description | Type | Max Length | Validation | Obligatoriedad |
|-----|-------|-------------|------|------------|------------|----------------|
| | AREA `<Signature>` | SIGNATURE | | | | 1 |
| 1 | Digital Signature | Digital signature over the Commercial Approval file | | | | 1 |
| | END AREA | SIGNATURE | | | | |
