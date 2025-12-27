# e-NCF Annulment Format

**Version 1.0**

---

## Changelog

**Version 1.0**

Updates as of 05-24-2022  
Modifications do not imply version change

• The following is removed from validation e) of the "Annulment Detail" section: The e-NCF is greater than the one placed in the "e-NCF Sequence From" field of any annulment format previously submitted.

---

## 1. Introduction

The taxpayer may annul authorized sequences of electronic tax receipts, if the issued invoice has not been sent to DGII or to the receiver or if the sequence has not been used, for which they must issue an XML format for e-NCF annulment described in this document.

If the invoice was sent to DGII and/or to the receiver, the taxpayer will annul the sequence by issuing an Electronic Credit Note, with the specifications established in the e-CF XML format.

---

## 2. Content of the e-NCF annulment file

**a) Header:** this section contains the data of who annuls, the quantity of annulled sequences and the date on which the file is generated.

**b) Annulment Detail:** this section reports the e-NCF sequences that will be annulled.

**c) Digital Signature:** which guarantees the integrity of the file and authenticity of the issuer.

---

## 3. Obligat oriedad codes

**0** - Does not apply: means that the data should not be in the file.

**1** - Obligatory data: the data must always be in the file.

### Report Sections

| Report Sections | Section Obligatoriedad |
|-----------------|------------------------|
| Header | 1 |
| Annulment Detail | 1 |
| Digital Signature | 1 |

Below, the content of each section is described, the format specifications for each field and the obligatoriedad codes for each one, which the sequence annulment file must have.

---

## 4. e-NCF Sequence Annulment Format

### a) Header

| No. | Field Name | Description | Type | Max Length | Validation | Obligatoriedad |
|-----|------------|-------------|------|------------|------------|----------------|
| | AREA `<Encabezado>` | HEADER | | | | 1 |
| 1 | Version | Version of the e-NCF Annulment Format. | NUM | 3 | Value: 1.0 | 1 |
| 2 | Issuer RNC<br>`<RncEmisor>` | Corresponds to the National Registry Number of the taxpayer issuing the electronic invoice. | NUM | 9 or 11 | a) RNC complies with format structure.<br>b) RNC is authorized as Electronic Invoicer.<br>c) RNC has authorized sequences of the e-NCF type being annulled. | 1 |
| 3 | Quantity of Annulled e-NCFs<br>`<CantidadeNCFAnulados>` | Sum of the quantity of e-NCFs being reported in the Detail section of this format. | NUM | 10 | a) Quantity of Annulled e-NCFs=∑ quantity of annulled e-NCFs by e-CF type, from the Detail section. | 1 |
| 4 | e-NCF Annulment Generation Date and Time<br>`<FechaHoraAnulacioneNCF>` | Date and time when the e-NCF sequence annulment file was generated, in format dd-MM-YYYY HH:mm:ss | ALFANUM | 19 | a) Date and time format complies with dd-MM-YYYY HH:mm:ss format | 1 |
| | END AREA | HEADER | | | | |

---

### b) Annulment Detail

Depending on the type of tax receipt to be annulled, the section can have up to 8 repetitions.

| No. | Field | Description | Type | Max Length | Validation | Obligatoriedad |
|-----|-------|-------------|------|------------|------------|----------------|
| | AREA `<DetalleAnulacion>` | ANNULMENT DETAIL | | | | 1 |
| | AREA `<Anulacion>` | ANNULMENT<br>Up to 10 repetitions can be included. | | | | 1 |
| 1 | Line Number<br>`<NoLinea>` | Number of the line or sequential. From 1 to 10 repetitions. | NUM | 2 | | 1 |
| 2 | e-CF Type<br>`<TipoeCF>` | Electronic Tax Receipt Type (e-CF) | NUM | 2 | a) The e-CF type is:<br>31: Electronic Credit Fiscal Invoice<br>32: Electronic Consumer Invoice<br>33: Electronic Debit Note<br>34: Electronic Credit Note<br>41: Electronic Purchases<br>43: Electronic Minor Expenses<br>44: Electronic Special Regimes<br>45: Electronic Governmental<br>46: Electronic Export Receipt<br>47: Electronic Foreign Payment Receipt | 1 |
| | Table of Annulled e-NCF Sequence Ranges<br>`<TablaRangoSecuenciasAnuladaseNCF>` | Table containing a range of consecutively annulled sequences, according to the e-CF type. Up to 10,000 repetitions can be included. | | | | 1 |
| 3 | e-NCF Sequence From<br>`<SecuenciaeNCFDesde>` | Refers to the Electronic Tax Receipt Number (e-NCF) with the sequential that starts the range of sequences to be annulled. | ALFANUM | 13 | a) The e-NCF complies with the tax receipt number format structure (13 positions)¹. Ex.: E310000000001.<br>b) The first character of the e-NCF (Series) is between E-Z²<br>c) The sequence's e-CF type must correspond to that indicated in the 'e-CF Type' field.<br>d) The initial sequence of the range to be annulled must be placed. Ex.: If the range of sequences to be annulled is from E310000000001 to E310000000005, the 'e-NCF Sequence From' field will be completed with e-NCF E310000000001.<br>e) The e-NCF is less than or equal to the "e-NCF Sequence To" and is greater than zero (>0). | 1 |
| 4 | e-NCF Sequence To<br>`<SecuenciaeNCFHasta>` | Refers to the Electronic Tax Receipt Number (e-NCF) with the sequential that ends the range of sequences to be annulled. | ALFANUM | 13 | a) The e-NCF complies with the tax receipt number format structure (13 positions)³. Ex.: E310000000001.<br>b) The e-NCF has the same series and tax receipt type as that placed in the "e-NCF Sequence From" field.<br>c) The e-NCF is greater than or equal to that placed in the "e-NCF Sequence From" field and is greater than zero (>0). | 1 |
| | END TABLE | SEQUENCE RANGES | | | | |
| 5 | Quantity of Annulled e-NCFs<br>`<CantidadeNCFAnulados>` | Quantity of e-NCF sequences being annulled.<br>This field must sum the sequences placed in the table of annulled e-NCF sequence ranges. | NUM | 10 | a) ∑ quantity of annulled e-NCFs by e-CF type. | 1 |
| | END AREA | ANNULMENT | | | | |
| | END AREA | ANNULMENT DETAIL | | | | |

---

**¹** The structure of the electronic tax receipt number (e-NCF) is composed of a series or letter between E-Z (excluding letter P), the tax receipt type specified with 2 digits, followed by a 10-digit sequential with numeric value, which indicate the quantity of receipts used.

**²** Letter P is excluded.

**³** The structure of the electronic tax receipt number (e-NCF) is composed of a series or letter between E-Z (excluding letter P, the tax receipt type specified with 2 digits, followed by a 10-digit sequential with numeric value, which indicate the quantity of receipts used.

---

### c) Digital Signature

| No. | Fields | Description | Type | Max Length | Validation | Obligatoriedad |
|-----|--------|-------------|------|------------|------------|----------------|
| | AREA `<Signature>` | SIGNATURE | | | | 1 |
| 1 | Digital Signature | Digital signature over the e-NCF Annulment file. | | | | 1 |
| | END AREA | SIGNATURE | | | | |

---

## Appendix I

Example of the e-NCF sequence annulment format in the Header sections and Annulment Detail section.

### A. Header

| No. | Field | Value |
|-----|-------|-------|
| 1 | Version | 1.00 |
| 2 | Issuer RNC | 123456789 |
| 3 | Quantity of Annulled e-NCFs | 84 |
| 4 | Date and Time of Digital Signature of Annulment File | 01-01-2019 08:50:15 |

### B. Annulment Detail

| No. | Field | Value |
|-----|-------|-------|
| 1 | Line Number | 1 |
| 2 | e-CF Type | 31 |
| | **Table of Annulled Sequence Ranges** | |
| 3 | e-NCF Sequence From | E310000000001 |
| 4 | e-NCF Sequence To | E310000000001 |
| 3 | e-NCF Sequence From | E310000000005 |
| 4 | e-NCF Sequence To | E310000000050 |
| 5 | Quantity of Annulled e-NCFs | 47 |
| 1 | Line Number | 2 |
| 2 | e-CF Type | 44 |
| | **Table of Annulled Sequence Ranges** | |
| 3 | e-NCF Sequence From | E440000000010 |
| 4 | e-NCF Sequence To | E440000000046 |
| 5 | Quantity of Annulled e-NCFs | 37 |
