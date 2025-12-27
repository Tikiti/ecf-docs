# Electronic Tax Receipt Format (e-CF)

**Version 1.0 | October 2025**

---

## Changelog

### Version 1.0

#### Updates as of 10-09-2025
Modifications do not imply a version change.

1. Table II is updated. Currency Coding, to add the currency type "Colombian Peso"

#### Updates as of 09-17-2024
Modifications do not imply a version change.

1. Table II is updated. Currency Coding, to add the currency types "Haitian Gourde" and "Mexican Peso"
2. Table IV is updated. Unit of Measure Coding, to add the measurement types "Hectare", "Milliliter", "Milligram", "Ounces" and "Troy Ounces"

#### Updates as of 08-30-2022
Modifications do not imply a version change.

1. Table IV is updated. Unit of Measure Coding, to add the measurement type "Tray".

#### Updates as of 05-06-2022
Modifications do not imply a version change.

1. Table IV is updated. Unit of Measure Coding, to add the measurement types "Gross Register Tonnage", "Square Foot", "Passenger", "Inches" and "Boat Dock Parking".

#### Updates as of 11-19-2021
Modifications do not imply a version change.

1. The Buyer Area `<Comprador>` obligatoriness codes are updated from 1 to 2, corresponding to the e-CF types Electronic Credit Note and Electronic Debit Note in the Header section.

#### Updates as of 11-04-2021
Modifications do not imply a version change.

1. Table IV is updated. Unit of Measure Coding, to add the measurement type "Quintal".

#### Updates as of 06-29-2021
Modifications do not imply a version change.

1. The 'Table III. Provinces and Municipalities Coding' is updated to separate Province and Municipality codes into columns.

#### Updates as of 11-10-2020
Modifications do not imply a version change.

1. The tags `<Liquidacion>` and `<Mineria>` of the Goods or Services Detail section are updated to remove accents.
2. The description of the 'Surcharge Distribution Table' and 'Surcharge Type' fields from the Goods or Services Detail section is updated.
3. The tag `<DescripcionDescuentooRecargo>` of the Discounts or Surcharges section is updated.

#### Updates as of 07-28-2020
Modifications do not imply a version change.

The fields `<TotalITBISRetenido>` and `<TotalISRRetencion>` of the Header section are modified to accept numeric values equal to zero (0).

---

## 1. Introduction

This document describes the content of Electronic Tax Receipts (e-CF), including both tax and commercial definitions.

From this perspective, this document aims to be an adequate instrument to support transactions between parties and to cover the information required for the use of the Electronic Invoice regime in the Dominican Republic.

This information considers the specifications necessary for the transaction between the issuer and buyer.

The electronic format of the e-CF types is described below:

### e-CF TYPE

| TYPE | e-CF |
|------|------|
| 31 | Electronic Tax Credit Invoice |
| 32 | Electronic Consumer Invoice |
| 33 | Electronic Debit Note |
| 34 | Electronic Credit Note |
| 41 | Electronic Purchases |
| 43 | Electronic Minor Expenses |
| 44 | Electronic Special Regimes |
| 45 | Electronic Government |
| 46 | Electronic Export Receipt |
| 47 | Electronic Foreign Payments Receipt |

---

## 2. e-CF Content

In accordance with the provisions of Decree No. 254-06, which establishes the Regulation for the Regulation of Printing, Issuance and Delivery of Tax Receipts, the General Directorate of Internal Taxes may authorize tax receipts that meet the requirements demanded by Law and the Regulation. Based on this provision, the format of electronic documents and the obligatoriness of the data contained therein are defined. Electronic documents have a unique format, where the main difference lies in whether certain data are mandatory or not.

Every e-CF issued must contain a digital signature, which allows authenticating its origin and certifying its integrity.

### 2.1. e-CF Composition

The following parts are distinguished in the e-CF:

**A. Header:** Corresponds to the e-CF identification, containing issuer data, buyer data and tax data.

**B. Goods or Services Detail:** In this section, one line must be detailed for each item.

**C. Informative Subtotals:** These subtotals do not increase or decrease the tax base, nor do they modify the totalizer fields; they are only informative fields.

**D. Discounts or Surcharges:** This section is used to specify global discounts or surcharges that affect the total of the e-CF. It is not necessary to specify item by item.

**E. Pagination:** This section indicates the number of pages of the e-CF in the Print Representation and which items will be on each one. This must be repeated for the total number of pages specified.

**F. Reference Information:** This section must detail the e-CFs modified by Electronic Credit or Debit Note and the e-CFs issued due to replacement of a receipt issued in contingency.

**G. Date and Time of digital signature.**

**H. Digital signature over all previous information to guarantee the integrity of the e-CF.**

The obligatoriness of each of the e-CF parts is specified in the following table:

#### e-CF Content

| Section | Tax Credit Invoice Electronic (31) | Consumer Invoice Electronic (32) | Debit Note Electronic (33) | Credit Note Electronic (34) | Electronic Purchases (41) | Minor Expenses Electronic (43) | Special Regimes Electronic (44) | Government Electronic (45) | Exports Electronic (46) | Foreign Payments Electronic (47) |
|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|
| Header | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| Goods or Services Detail | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| Informative Subtotals | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| Discounts or Surcharges¹ | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| Pagination | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| Reference Information | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 2 |
| Date and Time of digital signature | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| Digital Signature | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |

**Obligatoriness Codes:**

**0:** Does not apply. Means that the data must not be included in a specific document.

**1:** Mandatory data. The data must always be in the document, regardless of transaction characteristics.

**2:** Conditional data. The data is not mandatory in all documents, but becomes mandatory in certain operations if a specific condition is met. Example: If there are discounts or surcharges that affect the e-CF total, the Discounts or Surcharges section must be included, otherwise the total amount will not balance.

**3:** Optional. The data is optional.

---

**¹** Subject to the existence of a global discount or surcharge.

---
## 2.2. Detail by section

The content of each section will contain the format and its obligatoriness codes according to the e-CF type. The following are specified:

➢ **Maximum Length:** Maximum size of the field. The indicated length will be the maximum length.

➢ **Document Type:** Can be alpha (ALFA), numeric (NUM) or alphanumeric (ALFANUM). In numeric type information, decimals are separated with a period. Thousands must not be separated with any other type of character.

➢ **Column I:** Indicates whether the data must be in the printed representation (PR) of the document. Below each field, the name of the associated XML tag is included. Example: `<TipoeCF>`.

In column 'I' the following values can be found:

- **N:** Printing of this field is not mandatory.
- **I:** Printing of the data is mandatory.
- **P:** The data must be printed in words. For example: if the e-CF type is coded, in the printed representation it must be in words (Electronic Tax Credit Invoice, Electronic Credit Note, etc.).

---

## A. HEADER

### AREA: HEADER `<Encabezado>`

| # | FIELDS | DESCRIPTION | Max Length | Type | Validation | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|--------|-------------|-----------|------|------------|---|----|----|----|----|----|----|----|----|----|----| 
| | HEADER AREA `<Encabezado>` | | | | | | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 1 | VERSION | Version of the format used. | 3 | ALPHA NUM | Value: 1.0 | N | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |

### AREA: DOCUMENT IDENTIFICATION `<IdDoc>`

| # | FIELDS | DESCRIPTION | Max Length | Type | Validation | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|--------|-------------|-----------|------|------------|---|----|----|----|----|----|----|----|----|----|----| 
| | DOCUMENT IDENTIFICATION AREA `<IdDoc>` | | | | | | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 2 | Electronic Tax Receipt Type `<TipoeCF>` | Indicates if the document is:<br>Type Code:<br><br>31: Electronic Tax Credit Invoice<br>32: Electronic Consumer Invoice<br>33: Electronic Debit Note<br>34: Electronic Credit Note<br>41: Electronic Purchases<br>43: Electronic Minor Expenses<br>44: Electronic Special Regimes<br>45: Electronic Government<br>46: Electronic Export Receipt<br>47: Electronic Foreign Payments Receipt | 2 | NUM | a) According to the Description field coding. | P | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 3 | e-NCF `<eNCF>` | Sequence authorized by DGII. | 13 | ALPHA NUM | a) Validate with Sequence No. authorized by DGII. | I | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 4 | Expiration Date `<FechaVencimientoSecuencia>` | Expiration date of the e-NCF sequence. | 10 | ALPHA NUM | Valid date:<br>a) Format (dd-MM-YYYY)<br>b) Validate with sequence authorization expiration date. | I | 1 | 0 | 1 | 0 | 1 | 1 | 1 | 1 | 1 | 1 |
| 5 | Credit Note Indicator greater than 30 days `<IndicadorNotaCredito>` | Only for Credit Notes that are not entitled to reduce ITBIS. The indicator will take value 1 if the date is greater than 30 calendar days from the issuance of the affected e-CF. | 1 | NUM | a) Value 0 if the affected e-CF issuance date is ≤ 30 calendar days.<br>b) Value 1 if the affected e-CF issuance date is > 30 calendar days. | N | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| 6 | Deferred Sending Indicator `<IndicadorEnvioDiferido>` | Identifies taxpayers who have been previously authorized to have sales through offline mobile devices, such as Handheld sales, among others.<br><br>Conditional on being authorized to make deferred shipments. | 1 | NUM | a) Code 1: Authorized deferred shipment.<br><br>b) Validates that the taxpayer (RNC/ID) is authorized to make deferred shipments. | N | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 2 | 0 |
| 7 | Taxed Amount Indicator `<IndicadorMontoGravado>` | Indicates if in the detail line, the amount includes ITBIS (additional taxes are not included in the item price).<br>Conditional on the good or service being taxed with ITBIS. | 1 | NUM | a) Value 0 if amounts in section B "Goods or Services Detail" lines do not have ITBIS included.<br>b) Value 1 if amounts in section B "Goods or Services Detail" lines have ITBIS included. | N | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 0 | 0 |
| 8 | Income Type `<TipoIngresos>` | Indicates the type of income received, according to the classification of the Goods or Services sales submission format. | 2 | NUM | a) Type Code:<br>01: Operating income (Non-financial).<br>02: Financial Income<br>03: Extraordinary Income<br>04: Rental Income<br>05: Depreciable Asset Sale Income<br>06: Other Income | N | 1 | 1 | 1 | 1 | 0 | 0 | 1 | 1 | 1 | 0 |
| 9 | Payment Type `<TipoPago>` | Indicates the customer's payment type.<br>Free delivery invoices (code 3) are not valid for tax credit. | 1 | NUM | a) Type Code:<br>1: Cash<br>2: Credit<br>3: Free | N | 1 | 1 | 1 | 1 | 1 | 3 | 1 | 1 | 1 | 3 |
| 10 | Payment Due Date `<FechaLimitePago>` | Only for credit invoices.<br>Conditional on the payment type being credit. | 10 | ALPHA NUM | Valid date:<br>a) Format dd-MM-YYYY<br>b) Payment due date must be ≥ Issuance date. | N | 2 | 2 | 2 | 2 | 2 | 0 | 2 | 2 | 2 | 3 |
| 11 | Payment Term `<TerminoPago>` | Indicates the time established for invoice payment and must specify whether it is in hours, days, weeks, months or other.<br>Example:<br>1) 72 hours<br>2) 120 days<br>3) 1 week<br>4) 3 months | 15 | ALPHA NUM | a) No Validation. | N | 3 | 3 | 3 | 0 | 3 | 0 | 3 | 3 | 3 | 3 |
| | **PAYMENT METHODS TABLE `<TablaFormasPago>`²** | Up to 07 repetitions.<br>Contains the following two fields. | | | | | 3 | 3 | 3 | 0 | 3 | 0 | 3 | 3 | 3 | 3 |
| 12 | Payment Method `<FormaPago>` | Indicates the method by which the invoice will be paid. | 2 | NUM | a) Method Code:<br>1: Cash<br>2: Check/Transfer/Deposit<br>3: Debit/Credit Card<br>4: Credit Sale<br>5: Gift Bonds or Certificates<br>6: Barter<br>7: Credit note<br>8: Other Payment Methods<br><br>If the payment method corresponds to type 5, the e-CF must be type 32. | N | 3 | 3 | 3 | 0 | 3 | 0 | 3 | 3 | 3 | 3 |

---

**²** By XML definition, for each element there must be a container tag that groups the fields contained in a table. E.g.: in the case of `<TablaFormasPago>`, they are grouped within the `<FormaDePago>` tag for each `<FormaPago>` and `<MontoPago>` pair specified.

---

*(Continuation of DOCUMENT IDENTIFICATION Table)*

| # | FIELDS | DESCRIPTION | Max Length | Type | Validation | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|--------|-------------|-----------|------|------------|---|----|----|----|----|----|----|----|----|----|----| 
| 13 | Payment Amount `<MontoPago>` | Indicates the amount associated with each payment method. Conditional on a payment method existing. | 18 | NUM | a) Numeric value of 16 integers, 2 decimals; ≥ 0 (Must be positive) | N | 2 | 2 | 2 | 0 | 2 | 0 | 2 | 2 | 2 | 3 |
| | **END TABLE** | | | | | | | | | | | | | | | |
| 14 | Payment Account Type³ `<TipoCuentaPago>` | Source account for the transfer or check. | 2 | ALPHA | Type Code:<br>CT: Checking Account<br>AH: Savings<br>OT: Other | N | 3 | 3 | 3 | 0 | 3 | 0 | 3 | 3 | 3 | 3 |
| 15 | Payment Account `<NumeroCuentaPago>` | Account number if the payment method is by check or bank transfer. | 28 | ALPHA NUM | a) No validation | N | 3 | 3 | 3 | 0 | 3 | 0 | 3 | 3 | 3 | 3 |
| 16 | Payment Bank `<BancoPago>` | Account Bank. | 75 | ALPHA NUM | a) No validation | N | 3 | 3 | 3 | 0 | 3 | 0 | 3 | 3 | 3 | 3 |
| 17 | Date From `<FechaDesde>` | Billing period for Periodic Services e.g. Electricity, telephone, others.<br>Date from<br>(Start date of the billed service). | 10 | ALPHA NUM | Valid date:<br>a) Format dd-MM-YYYY<br>b) Less than or equal to "Date To".<br>According to the Description field Format. | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 3 |
| 18 | Date To `<FechaHasta>` | Billing period for Periodic Services. Date to<br>(End date of the billed service). | 10 | ALPHA NUM | Valid date:<br>a) Format dd-MM-YYYY<br>b) Greater than or equal to "Date From".<br>According to the Description field Format. | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 3 |
| 19 | Total Pages `<TotalPaginas>` | Indicates the total number of pages on which the e-CF will be printed.<br>Counts the number of times the Page No. field of the Pagination section is repeated.<br>Conditional on pagination existing. | 3 | NUM | a) Numeric value up to 3 integers, > 1 (Must be positive).<br>b) Total number of times the 'Page No.' field of the Pagination section is repeated. | I | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| | END AREA | **DOCUMENT IDENTIFICATION** | | | | | | | | | | | | | | |

---

**³** In cases where there is more than one check/transfer/deposit payment method, only enter one payment account type.

---

### AREA: ISSUER `<Emisor>`

| # | FIELDS | DESCRIPTION | Max Length | Type | Validation | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|--------|-------------|-----------|------|------------|---|----|----|----|----|----|----|----|----|----|----| 
| | ISSUER AREA `<Emisor>` | | | | | | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 20 | Issuer RNC `<RNCEmisor>` | Corresponds to the issuer's RNC. | 9 or 11 | NUM | Validate in the National Taxpayer Registry.<br>Must validate:<br>a) RNC complies with format structure.<br>b) RNC is authorized as Electronic Invoicer.<br>c) RNC is in "Active" status.<br>d) RNC has no blocking flags. | I | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 21 | Issuer Name or Business Name `<RazonSocialEmisor>` | Issuer's Name or Business Name. | 150 | ALPHA NUM | a) No validation | I | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 22 | Trade Name `<NombreComercial>` | Trade Name. | 150 | ALPHA NUM | a) No validation | I | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 23 | Branch `<Sucursal>` | Indicates the name of the branch that issues the e-CF. Corresponds to data managed by the issuer. | 20 | ALPHA NUM | a) No validation | I | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 24 | Issuer Address `<DireccionEmisor>` | Data corresponding to the Issuer's Business Address. | 100 | ALPHA NUM | a) No validation | I | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 25 | Municipality `<Municipio>` | Data corresponding to the Issuer's business address. | 6 | NUM | a) Validate with Table III code (Provinces and Municipalities Coding) | P | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 26 | Province `<Provincia>` | Data corresponding to the Issuer's business address. | 6 | NUM | a) Validate with Table III code (Provinces and Municipalities Coding) | P | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| | **Issuer Phone Table `<TablaTelefonoEmisor>`** | Up to 3 repetitions can be included. | | | | | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 27 | Issuer Phone `<TelefonoEmisor>` | Data corresponding to the issuer's contact phone. | 12 | ALPHA NUM | Valid format:<br>Phone structure<br>(xxx-xxx-xxxx) | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| | **END TABLE** | **ISSUER PHONE** | | | | | | | | | | | | | | |
| 28 | Issuer Email `<CorreoEmisor>` | Data corresponding to the issuer's email. | 80 | ALPHA NUM | Valid format: Email structure<br>(xxxxx@xxx.xx) | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 29 | WebSite `<WebSite>` | Data corresponding to the issuer's website. | 50 | ALPHA NUM | a) No validation | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 30 | Issuer Economic Activity `<ActividadEconomica>` | Data corresponding to the Issuer's economic activity (only the economic activity corresponding to the transaction can be included). | 100 | ALPHA NUM | a) No validation | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 31 | Seller Code `<CodigoVendedor>` | Seller identifier. | 60 | ALPHA NUM | a) No validation | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 32 | Internal Invoice Number `<NumeroFacturaInterna>` | Corresponds to the internal invoice number. | 20 | ALPHA NUM | a) No validation | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 33 | Internal Order Number `<NumeroPedidoInterno>` | Corresponds to the internal order number assigned to the invoice. | 20 | NUM | a) No validation | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 34 | Sales Zone `<ZonaVenta>` | Corresponds to the seller's sales zone. | 20 | ALPHA NUM | a) No validation. | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 35 | Sales Route `<RutaVenta>` | Corresponds to the seller's sales route. | 20 | ALPHA NUM | a) No validation | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 36 | Additional Issuer Information `<InformacionAdicionalEmisor>` | Other information related to the Issuer. | 250 | ALPHA NUM | a) No validation | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 37 | Issuance Date `<FechaEmision>` | e-CF issuance date. | 10 | ALPHA NUM | Valid date:<br>a) Format dd-MM-YYYY<br>b) Validate start date as electronic invoicer. | I | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| | END AREA | **ISSUER** | | | | | | | | | | | | | | |

---
### AREA: BUYER `<Comprador>`

| # | FIELDS | DESCRIPTION | Max Length | Type | Validation | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|--------|-------------|-----------|------|------------|---|----|----|----|----|----|----|----|----|----|----| 
| | BUYER AREA `<Comprador>` | | | | | | 1 | 1 | 2 | 2 | 1 | 0 | 1 | 1 | 1 | 3 |
| 38 | Buyer RNC `<RNCComprador>` | Corresponds to the buyer's RNC.<br><br>Conditional on the total amount of the type 32 e-CF being equal to or greater than DOP$ 250K.⁴<br><br>In case the e-CF is type 46, the field is conditional on the Commercial Free Zone (Airports and Ports) making a transfer of goods to Residents and the 'Foreign Identifier' field being empty. | 9 or 11 | NUM | a) Validate structure.<br><br>b) If the e-CF is type 32 and the total amount is ≥ DOP$250,000.00, the Buyer RNC must be identified.<br><br>c) If the e-CF type 33 and type 34 modifies an e-CF type 32 with total amount ≥ DOP$250,000.00, the Buyer RNC must be identified.<br><br>d) If the e-CF is type 32 and the buyer is foreign, this field can be left blank and the Foreign Identifier field completed. | I | 1 | 2 | 2 | 2 | 1 | 0 | 2⁵ | 1 | 2⁶ | 0 |
| 39 | Foreign Identifier `<IdentificadorExtranjero>`⁷ | Corresponds to the identification number when the buyer is foreign and does not have RNC/ID.<br><br>Conditional on the e-CF being type 32>DOP$250,000.00 (also applies to credit/debit notes that reference that type of e-CF), and the Buyer RNC field being empty.<br><br>In case the e-CF is type 46, the field is conditional on the Commercial Free Zone (Airports and Ports) making a transfer of goods to Non-Residents and the 'Buyer RNC' field being empty. | 20 | ALPHA NUM | a) The electronic consumer e-CF is > DOP$250,000.00 (also applies to credit/debit notes that reference that type of e-CF).<br><br>b) The Buyer RNC field is blank. | I | 0 | 2 | 2 | 2 | 0 | 0 | 2⁸ | 0 | 2⁹ | 3 |
| 40 | Buyer Name or Business Name `<RazonSocialComprador>` | Buyer's Name or Business Name.<br><br>In case the e-CF is type 46, the field is conditional on the 'Buyer RNC' or 'Foreign Identifier' field existing. | 150 | ALPHA NUM | a) If the e-CF is type 32 and the total amount is ≥ DOP$250,000.00, the buyer's name or business name must be indicated.<br><br>b) If the e-CF type 33 and type 34 modifies an e-CF type 32 with total amount ≥ DOP$250,000.00, the buyer's name or business name must be indicated. | I | 1 | 2 | 2 | 2 | 1 | 0 | 1 | 1 | 1 | 3 |
| 41 | Buyer Contact `<ContactoComprador>` | Buyer's contact name and phone. | 80 | ALPHA NUM | a) No validation | N | 3 | 3 | 3 | 3 | 3 | 0 | 3 | 3 | 3 | 0 |
| 42 | Buyer Email `<CorreoComprador>` | Data corresponding to the buyer's email. | 80 | ALPHA NUM | Valid format: Email structure.<br>(xxxxx@xxx.xx) | N | 3 | 3 | 3 | 3 | 3 | 0 | 3 | 3 | 3 | 0 |
| 43 | Buyer Address `<DireccionComprador>` | Buyer's address. | 100 | ALPHA NUM | a) No validation | N | 3 | 3 | 3 | 3 | 3 | 0 | 3 | 3 | 3 | 0 |
| 44 | Buyer Municipality `<MunicipioComprador>` | Data corresponding to buyer's address. | 6 | NUM | a) Validate with Table III code (Provinces and Municipalities Coding) | N | 3 | 3 | 3 | 3 | 3 | 0 | 3 | 3 | 3 | 0 |
| 45 | Buyer Province `<ProvinciaComprador>` | Data corresponding to buyer's address. | 6 | NUM | a) Validate with Table III code (Provinces and Municipalities Coding) | N | 3 | 3 | 3 | 3 | 3 | 0 | 3 | 3 | 3 | 0 |
| 46 | Buyer Country `<PaisComprador>` | Data corresponding to the country to which the billing is made. | 60 | ALPHA | a) No validation. | P | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 47 | Delivery Date `<FechaEntrega>` | Corresponds to the item delivery date. | 10 | ALPHA NUM | a) Valid date:<br>Format (dd-MM-YYYY) | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 48 | Delivery Contact `<ContactoEntrega>` | Contact information where the item will be delivered or sent (different from the buyer). | 100 | ALPHA NUM | a) No validation | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 49 | Delivery Address `<DireccionEntrega>` | Corresponds to the address or destination of the delivery contact. | 100 | ALPHA NUM | a) No validation | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 50 | Phone `<TelefonoAdicional>` | Phone data corresponding to the delivery contact. | 12 | ALPHA NUM | a)Valid format:<br>Phone structure<br>(xxx-xxx-xxxx) | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 51 | Purchase Order Date `<FechaOrdenCompra>` | Corresponds to the purchase order date. | 10 | ALPHA NUM | a)Valid date:<br>Format (dd-MM-YYYY) | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 52 | Purchase Order Number `<NumeroOrdenCompra>` | Corresponds to the purchase order number. | 20 | ALPHA NUM | a) No Validation | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 53 | Buyer Internal Code `<CodigoInternoComprador>` | For internal buyer identification, for example, customer code, meter number, etc. | 20 | ALPHA NUM | a) No validation | N | 3 | 3 | 3 | 3 | 3 | 0 | 3 | 3 | 3 | 0 |
| 54 | Payment Responsible `<ResponsablePago>` | Corresponds to the identification of who makes the document payment. | 20 | ALPHA | a) No validation | N | 3 | 3 | 3 | 3 | 3 | 0 | 3 | 3 | 3 | 0 |
| 55 | Additional Buyer Information `<Informacionadicionalcomprador>` | Other information related to the buyer. | 150 | ALPHA NUM | a) No validation | N | 3 | 3 | 3 | 3 | 3 | 0 | 3 | 3 | 3 | 0 |
| | END AREA | **BUYER** | | | | | | | | | | | | | | |

---

**⁴** If the total amount of the electronic consumer invoice is less than DOP$250 thousand, the 'Buyer RNC' field will be completed optionally.

**⁵** Conditional on the buyer having RNC/ID. If the buyer is foreign (diplomatic), the 'Buyer RNC' field must be left blank and the 'Foreign Identifier' field completed.

**⁶** According to Article 10 of General Standard 05-19, in case Commercial Free Zones (Airports and Ports) make transfers of goods to Residents, the 'Buyer RNC' field must be completed.

**⁷** This field is completed if the e-CF is an electronic consumer invoice > DOP$250,000 and the buyer does not have RNC/ID for being foreign. The same applies to electronic credit/debit notes that affect type 32 e-CF with value > DOP$250,000. When Foreign Identifier exists, the Buyer RNC field will be omitted.

**⁸** Conditional on the buyer being foreign (diplomatic). If the 'Foreign Identifier' field is completed, the Buyer RNC field should not be completed.

**⁹** According to Article 10 of General Standard 05-19, in case Commercial Free Zones (Airports and Ports) make

 transfers of goods to Non-Residents, the 'Foreign Identifier' field must be completed.

---

### AREA: ADDITIONAL INFORMATION `<InformacionesAdicionales>`

| # | FIELDS | DESCRIPTION | Max Length | Type | Validation | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|--------|-------------|-----------|------|------------|---|----|----|----|----|----|----|----|----|----|----| 
| | ADDITIONAL INFORMATION AREA `<InformacionesAdicionales>` | | | | | | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 56 | Shipment Date `<FechaEmbarque>` | Corresponds to the shipment date. | 10 | ALPHA NUM | a)Valid date:<br>Format (dd-MM-YYYY) | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 57 | Shipment Number `<NumeroEmbarque>` | Data corresponding to the shipment number. | 25 | ALPHA NUM | a) No validation | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 58 | Container Number `<NumeroContenedor>` | Data corresponding to the container number. | 100 | ALPHA NUM | a) No validation | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 59 | Reference Number `<NumeroReferencia>` | Data corresponding to the reference number. | 20 | NUM | a) No validation | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 60 | Loading Port Name `<NombrePuertoEmbarque>` | Name of the loading port for the goods. | 40 | ALPHA NUM | a) No validation | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 61 | Delivery Terms `<CondicionesEntrega>` | Refers to the commercial terms set by the buyer and seller regarding the delivery conditions of the goods and/or products.<br><br>Indicates if it is CIF, FOB, etc. | 3 | ALPHA | a) No validation | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 62 | Total FOB `<TotalFob>` | Corresponds to the sum of the FOB value of all goods. | 18 | NUM | a) Numeric value of 16 integers, 2 decimals; > 0 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 63 | Insurance `<Seguro>` | Corresponds to the total amount of the premium stated in the shipping document or the document certifying the premium value assigned by the insurance company. | 18 | NUM | a) Numeric value of 16 integers, 2 decimals; > 0 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 64 | Freight `<Flete>` | Corresponds to the amount paid for the transportation of goods from Dominican ports abroad. | 18 | NUM | a) Numeric value of 16 integers, 2 decimals; > 0 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 65 | Other Expenses `<OtrosGastos>` | Amount for expenses for other services, up to the transportation of goods at the destination customs. | 18 | NUM | a) Numeric value of 16 integers, 2 decimals; > 0 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 66 | Total CIF `<TotalCif>` | Corresponds to the FOB value, Freight, Insurance and other expenses. | 18 | NUM | a) Numeric value of 16 integers, 2 decimals; > 0 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 67 | Customs Regime `<RegimenAduanero>` | Corresponds to the customs regime under which the exported goods fall, as defined in DGA10. | 35 | ALPHA | a) No validation | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 68 | Departure Port Name `<NombrePuertoSalida>` | Name of the port from which the goods depart, different from the loading port. | 40 | ALPHA NUM | a) No validation | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 69 | Unloading Port Name `<NombrePuertoDesembarque>` | Name of the destination port for the goods. | 40 | ALPHA NUM | a) No validation | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 70 | Gross Weight `<PesoBruto>` | Corresponds to the gross weight of the container. | 18 | NUM | a) Numeric value of 16 integers, 2 decimals; > 0 (Cannot be negative) | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 71 | Net Weight `<PesoNeto>` | Corresponds to the net weight of the container. | 18 | NUM | a) Numeric value of 16 integers, 2 decimals; > 0 (Cannot be negative) | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 72 | Gross Weight Unit `<UnidadPesoBruto>` | Corresponds to the unit of measure for the gross weight of the goods. | 2 | NUM | a) Validate with Table IV (Unit of Measure Coding) | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 73 | Net Weight Unit `<UnidadPesoNeto>` | Corresponds to the unit of measure for the net weight of the goods. | 2 | NUM | a) Validate with Table IV (Unit of Measure Coding) | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 74 | Number of Packages `<CantidadBulto>` | Corresponds to the number of packages covered by the document. | 18 | NUM | a) Numeric value of 16 integers, 2 decimals; > 0 | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 75 | Package Unit `<UnidadBulto>` | Corresponds to the unit of measure for the packages. | 2 | NUM | a) Validate with Table IV (Unit of Measure Coding) | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 76 | Volume `<VolumenBulto>` | Corresponds to the volume of the packages. | 18 | NUM | a) Numeric value of 16 integers, 2 decimals; > 0 | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 77 | Volume Unit `<UnidadVolumen>` | Corresponds to the unit of measure for the volume of the packages. | 2 | NUM | a) Validate with Table IV (Unit of Measure Coding) | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| | END AREA | **ADDITIONAL INFORMATION** | | | | | | | | | | | | | | |

---

### AREA: TRANSPORT `<Transporte>`

| # | FIELDS | DESCRIPTION | Max Length | Type | Validation | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|--------|-------------|-----------|------|------------|---|----|----|----|----|----|----|----|----|----|----| 
| | TRANSPORT AREA `<Transporte>` | | | | | | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 78 | Transport Route `<ViaTransporte>` | Specifies whether transport is by sea, land or air. | 2 | NUM | Must validate:<br>01: Land<br>02: Maritime<br>03: Air | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 79 | Country of Origin `<PaisOrigen>` | Corresponds to the country of origin of the goods. | 60 | ALPHA | a) No validation | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 80 | Destination Address `<DireccionDestino>` | Corresponds to the destination address where the item will be sent (different from the buyer's address). | 100 | ALPHA NUM | a) No validation | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 81 | Destination Country `<PaisDestino>` | Corresponds to the destination country where the item will be sent (different from the buyer's country). | 60 | ALPHA | a) No validation | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 3 |
| 82 | RNC or Transport Company ID `<RNCIdentificacionCompaniaTransportista>` | Corresponds to the RNC or Identification data of the company performing the transport. | 20 | ALPHA NUM | a) No validation | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 83 | Transport Company Name `<NombreCompaniaTransportista>` | Corresponds to the name or business name of the company performing the transport. | 150 | ALPHA NUM | a) No validation | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 84 | Trip Number `<NumeroViaje>` | Corresponds to the trip number or flight number. | 20 | ALPHA NUM | a) No validation | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| | END AREA | **TRANSPORT** | | | | | | | | | | | | | | |

---

*(Continuation of TRANSPORT AREA)*

| # | FIELDS | DESCRIPTION | Max Length | Type | Validation | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|--------|-------------|-----------|------|------------|---|----|----|----|----|----|----|----|----|----|----| 
| 85 | Driver `<Conductor>` | Corresponds to the driver's code or name. | 20 | ALPHA NUM | a) No validation | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 86 | Document `<DocumentoTransporte>` | Corresponds to the driver's transport document. | 20 | NUM | a) No validation | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 87 | File `<Ficha>` | Corresponds to the transport file. | 10 | ALPHA NUM | a) No validation | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 88 | License Plate `<Placa>` | Corresponds to the transport vehicle's license plate number. | 7 | ALPHA NUM | a) No validation | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 89 | Transport Route `<RutaTransporte>` | Corresponds to the established transport route. | 20 | ALPHA NUM | a) No validation | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 90 | Transport Zone `<ZonaTransporte>` | Corresponds to the transport zone. | 20 | ALPHA NUM | a) No validation | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 91 | Delivery Note Number `<NumeroAlbaran>` | Corresponds to the delivery note number. | 20 | ALPHA NUM | a) No validation | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| | END AREA | **TRANSPORT** | | | | | | | | | | | | | | |

---

### A.2 AREA: TOTALS `<Totales>`
