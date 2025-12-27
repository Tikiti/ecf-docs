# Acknowledgment of Receipt Format (ARECF)

**Version 1.0**

---

## Update Changelog

**Version 1.0**

1. The label for the 'ACKNOWLEDGMENT OF RECEIPT DETAIL' area is updated.

---

## 1. Introduction

The acknowledgment of receipt is the response that the receiver must send to the issuer as proof of receipt of the Electronic Tax Receipt; it does not imply acceptance or rejection of the e-CF, it only indicates whether it was received or not.

Upon receiving the invoice, the receiver is obligated to confirm to the issuer the reception of the document with a receipt response¹, prior to commercial approval.

This document describes the content that the acknowledgment of receipt XML format must have, including the messages that will be used by electronic receivers.

---

## 2. Content of the Acknowledgment of Receipt XML Format

**a) Acknowledgment of Receipt Detail:** specifies the content of the response that the receiver must send to the issuer.

**b) Digital Signature:** which guarantees the integrity of the response and authenticity of the sender.

---

## 3. Obligatoriedad Codes

**1** - Obligatory data: the data must always be in the file.

**2** - Conditional data: the data is not obligatory but becomes so in certain cases, if a certain condition is met.

---

**¹** The Acknowledgment of Receipt confirms that the document corresponds to an electronic invoice and has been received.

---

### Content of the Acknowledgment of Receipt Format

| File Sections | Section Obligatoriedad |
|---------------|------------------------|
| Acknowledgment of Receipt Detail | 1 |
| Digital Signature | 1 |

Below, the content of each section is described, the format specifications for each field and the obligatoriedad code for each one. The names and characteristics are similar to the e-CF format.

---

## A. Acknowledgment of Receipt Detail

| No. | Field | Description | Type | Max Length | Validation | Obligatoriedad |
|-----|-------|-------------|------|------------|------------|----------------|
| | AREA `<DetalleAcusedeRecibo>` | ACKNOWLEDGMENT OF RECEIPT DETAIL | | | | 1 |
| 1 | Version | Version of the Acknowledgment of Receipt format. | NUM | 3 | Value: 1.0 | 1 |
| 2 | Issuer's RNC<br>`<RNCEmisor>` | National Registry Number of the taxpayer issuing the e-CF. | NUM | 9 or 11 | RNC/ID complies with format structure. | 1 |
| 3 | Buyer's RNC<br>`<RNCComprador>` | National Registry Number of the taxpayer issuing the Acknowledgment of Receipt of the e-CF. | NUM | 9 or 11 | RNC/ID complies with format structure. | 1 |
| 4 | e-NCF<br>`<eNCF>` | Electronic Tax Receipt Number (e-NCF) | ALFANUM | 13 | e-NCF complies with format structure. | 1 |
| 5 | Status<br>`<Estado>` | Acknowledgment of Receipt response code. | NUM | 1 | 0: e-CF Received<br>1: e-CF Not Received | 1 |
| 6 | Not Received Reason Code<br>`<CodigoMotivoNoRecibido>` | Numeric code indicating the reason for e-CF rejection.<br>Conditional on Status having value 1. | NUM | 1 | Not Received reason code<br>1: Specification error.<br>2: Digital Signature error.<br>3: Duplicate submission<br>4: Buyer RNC does not correspond | 2 |
| 7 | Acknowledgment of Receipt Generation Date and Time<br>`<FechaHoraAcuseRecibo>` | Date and time in format dd-MM-YYYY HH:mm:ss | ALFANUM | 19 | Date and time comply with the indicated format. | 1 |
| | END AREA | ACKNOWLEDGMENT OF RECEIPT DETAIL | | | | |

---

## B. Digital Signature

| No. | Fields | Description | Type | Max Length | Validation | Obligatoriedad |
|-----|--------|-------------|------|------------|------------|----------------|
| | AREA `<Signature>` | SIGNATURE | | | | 1 |
| 1 | Digital Signature | Digital signature over the Acknowledgment of Receipt file | | | | 1 |
| | END AREA | SIGNATURE | | | | |
