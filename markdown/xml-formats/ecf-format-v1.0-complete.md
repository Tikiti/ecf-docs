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

| # | FIELDS | DESCRIPTION | Max Length | Type | Validation | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|--------|-------------|-----------|------|------------|---|----|----|----|----|----|----|----|----|----|----| 
| | TOTALS AREA `<Totales>` | | | | | | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 92 | Total Taxed Amount¹¹ `<MontoGravadoTotal>` | Total sum of taxed amounts with ITBIS at different rates.<br>Conditional on Taxed Amount 1, and/or Taxed Amount 2 and/or Taxed Amount 3 existing. | 18 | NUM | a) Numeric value of 16 integers, 2 decimals; ≥ 0 (Cannot be negative).<br>b) Numeric value of the sum total Taxed Amount ITBIS Rate1 + Taxed Amount ITBIS Rate 2 + Taxed Amount ITBIS Rate3. | I | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 0 |
| 93 | Taxed Amount ITBIS Rate 1 `<MontoGravadoI1>` | Total sum of values of taxed Items assigned to ITBIS rate 1 (18% rate), minus discounts plus surcharges.¹²<br>Conditional on any item taxed at ITBIS1 rate existing in the detail line. | 18 | NUM | a) Numeric value of 16 integers, 2 decimals; ≥ 0 (Cannot be negative).<br>b) Sum of values of item amount with billing indicator=1¹³, minus discounts plus surcharges.<br>c) If the taxed amount indicator is =1, the sum of values of item amount with billing indicator=1 must be divided by (1+ITBIS rate 1 rate), minus discounts plus surcharges.<br>d) If the 'Standard 10-07 Indicator' field is completed, the sum of values of item amount with billing indicator=1 must be divided by (1+ITBIS rate 1 rate+additional tax codes 002 and 004 rates, assigned to the item). If a discount exists, the corresponding discount amount should not be subtracted from the taxed amount ITBIS rate 1. | N | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 0 | 0 |
| 94 | Taxed Amount ITBIS Rate 2 `<MontoGravadoI2>` | Total sum of values of taxed Items assigned to ITBIS rate 2 (16% rate), minus discounts plus surcharges.<br>Conditional on any item taxed at ITBIS2 rate existing in the detail line. | 18 | NUM | a) Numeric value of 16 integers, 2 decimals; ≥ 0 (Cannot be negative).<br>b) Sum of values of item amount with billing indicator=2, minus discounts plus surcharges.<br>c) If the taxed amount indicator=1, the result must be divided by (1+ ITBIS rate 2). | N | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 0 | 0 |
| 95 | Taxed Amount ITBIS Rate 3 `<MontoGravadoI3>` | Total sum of values of taxed Items assigned to ITBIS rate 3 (0% rate), minus discounts plus surcharges.<br>Conditional on any item taxed at ITBIS3 rate existing in the detail line. | 18 | NUM | a) Numeric value of 16 integers, 2 decimals≥ 0 (Cannot be negative).<br>b) Sum of values of item amount with billing indicator=3, minus discounts plus surcharges. | N | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 0 |
| 96 | Exempt Amount `<MontoExento>` | Total sum of values of exempt items, minus discounts plus surcharges.<br>Conditional on any exempt item existing in the detail line. | 18 | NUM | a) Numeric value of 16 integers, 2 decimals. ≥ 0 (Cannot be negative).<br>b) Sum of values of item amount with billing indicator=4, minus discounts plus surcharges. | I | 2 | 2 | 2 | 2 | 2 | 2¹⁴ | 2 | 2 | 0 | 2 |
| 97 | ITBIS Rate 1 `<ITBIS1>` | ITBIS Rate 1 (18%).<br>Conditional on an item taxed at rate 1 existing in the detail line. | 2 | NUM | a) 2 integers in percentage e.g.: 18%<br>b) Item with billing indicator=1 exists | N¹⁵ | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 0 | 0 |
| 98 | ITBIS Rate 2 `<ITBIS2>` | ITBIS Rate 2 (16%). Conditional on an item taxed at rate 2 existing in the detail line. | 2 | NUM | a) 2 integers in percentage e.g.: 16%.<br>b) Item with billing indicator=2 exists. | N | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 0 | 0 |
| 99 | ITBIS Rate 3 `<ITBIS3>` | ITBIS Rate 3 (0%).<br>Conditional on an item taxed at rate 3 existing in the detail line. | 2 | NUM | a) 1 integer in percentage e.g.: 0%.<br>b) Item with billing indicator=3 exists. | N | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 0 |
| 100 | Total ITBIS `<TotalITBIS>` | Total sum of ITBIS values at different rates. Conditional on Total ITBIS Rate 1, and/or Total ITBIS Rate 2 and/or Total ITBIS Rate 3 existing. | 18 | NUM | a) Numeric value of 16 integers, 2 decimals; ≥ 0 (Cannot be negative).<br>b) Sum of Total ITBIS Rate 1 + Total ITBIS Rate 2 + Total ITBIS Rate 3. | I | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 0 |
| 101 | Total ITBIS Rate 1 `<TotalITBIS1>` | Numeric value equal to Taxed Amount ITBIS Rate1 times ITBIS Rate 1.<br>Conditional on Taxed Amount rate 1 and ITBIS rate 1 existing.<br>If there are selective consumption taxes that are part of the ITBIS tax base, these will be added to the taxed amount before multiplying by the ITBIS rate. | 18 | NUM | a) Numeric value of 16 integers, two decimals; ≥ 0 (Cannot be negative).<br>b) Total ITBIS Rate1= Taxed Amount ITBIS rate1 *ITBIS rate.<br>Only selective consumption taxes with codes from 006 to 039 corresponding to the Additional Tax Types Coding Table are part of the ITBIS tax base. | N | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 0 | 0 |
| 102 | Total ITBIS Rate 2 `<TotalITBIS2>` | Numeric value equal to Taxed Amount ITBIS Rate2*ITBIS rate 2.<br>Conditional on Taxed Amount rate 2 and ITBIS rate 2 existing. | 18 | NUM | a) Numeric value of 16 integers, two decimals; ≥ 0 (Cannot be negative).<br>b) Total ITBIS Rate2= Taxed Amount ITBIS rate2*ITBIS rate 2. | N | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 0 | 0 |
| 103 | Total ITBIS Rate3 `<TotalITBIS3>` | Numeric value equal to Taxed Amount ITBIS Rate3*ITBIS rate 3.<br>Conditional on Taxed Amount rate 3 and ITBIS rate 3 existing. | 18 | NUM | a)Numeric value of 16 integers, two decimals; ≥ 0 (Cannot be negative). | N | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 0 |
| 104 | Additional Tax Amount `<MontoImpuestoAdicional>` | Sum of the Specific Selective Consumption Tax Amount, Ad Valorem Selective Consumption Tax Amount and Other Additional Taxes Amount fields. | 18 | NUM | a) Numeric value of 16 integers, two decimals; >0 (must be positive).<br>b) Additional Tax Amount= Specific Selective Consumption Tax Amount+ Ad Valorem Selective Consumption Tax Amount+ Other Additional Taxes Amount. | I | 2 | 2 | 2 | 2 | 0 | 0 | 2¹⁶ | 2 | 0 | 0 |
| | **Additional Taxes Table `<ImpuestosAdicionales>`¹⁷** | Up to 20 repetitions of code-value pairs can be included.<br>Includes the following five fields: | | | a) Conditional on other tax(es) existing in the detail line different from ITBIS. | | 2 | 2 | 2 | 2 | 0 | 0 | **2¹⁸** | 2 | 0 | 0 |
| 105 | Additional Tax Code `<TipoImpuesto>` | Data corresponding to the Additional Tax Code according to Table I (Additional Tax Types Coding). | 3 | NUM | a) Validate with Table I (Additional Tax Types Coding). | N | 2 | 2 | 2 | 2 | 0 | 0 | 2¹⁹ | 2 | 0 | 0 |
| 106 | Additional Tax Rate `<TasaImpuestoAdicional>` | Data corresponding to the Additional Tax Rate.<br>The Tax rate must be indicated.²⁰ | 5 | NUM | a) Validate with Table I (Additional Tax Types Coding).<br>b) If the rate corresponds to codes between 006 to 022 of Table I (Additional Tax Types Coding), it must be validated that it matches the rate in effect for the period corresponding to the e-CF issuance date (issuance date field). | N²¹ | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 0 | 0 |
| 107 | Specific Selective Consumption Tax Amount²² `<MontoImpuestoSelectivoConsumoEspecifico>` | Value of the specific selective consumption tax (ISC) associated with the additional tax code. Conditional on code 006 to 022 existing²³.<br>The calculation of the specific ISC amount will depend on the rate corresponding to the tax code in Table I (Additional Tax Types Coding). | 18 | NUM | a) Numeric value of 16 integers, two decimals; >0 (must be positive).<br>b) If the tax code is between 006 to 018, the item's unit of measure must be verified; if it is bulk (code 18), the Specific Selective Consumption Tax should not be calculated.<br>c) For items with codes 006 to 018 from 'Table I (Additional Tax Types Coding)' and unit of measure other than bulk, the reference quantity must be multiplied by the alcohol degrees, by the tax rate indicated in the table for that code, by the subquantity and quantity.<br>d) For codes 019 to 022, it must be calculated by multiplying the quantity by the reference quantity, by the indicated additional tax rate. | N | 2 | 2 | 2 | 2 | 0 | 0 | 0 | 2 | 0 | 0 |
| 108 | Ad Valorem Selective Consumption Tax Amount `<MontoImpuestoSelectivoConsumoAdvalorem>` | Value of the ad valorem selective consumption tax (ISC) associated with the additional tax code. Conditional on code 023 to 039 existing²⁴.<br>The calculation of the ad valorem ISC amount will depend on the rate corresponding to the tax code in Table I (Additional Tax Types Coding). | 18 | NUM | a) Numeric value of 16 integers, two decimals; >0 (must be positive).<br>b) If the tax code is between 023 to 035, the item's unit of measure must be verified; if it is bulk (code 18), the Ad Valorem Selective Tax should be calculated by increasing the item's unit price (equivalent to the list price) by thirty percent (30%) times the item quantity times the corresponding tax rate.<br>c) For items with code between 023-035 (Ad valorem ISC)²⁵, and unit of measure other than bulk, the reference unit price must be divided by (1+ITBIS rate 1 rate). This result must be subtracted from the Unit Specific ISC²⁶ and this last result must be divided by (1+specified additional tax rate), this will result in the tax base. This base (unit Ad Valorem ISC) must be multiplied by the quantity, by the reference quantity and by the corresponding tax rate.<br>d) When the additional tax code is between 036-039 according to the 'Additional Tax Types Coding Table', the tax must be calculated by dividing the reference unit price by (1+ITBIS rate 1 rate). From this result, the Specific ISC rate must be subtracted and the result must be divided by (1+specified additional tax rate); this will result in the tax base for the Ad Valorem ISC. This base must be multiplied by the quantity, by the reference quantity and by the corresponding tax rate. | N | 2 | 2 | 2 | 2 | 0 | 0 | 0 | 2 | 0 | 0 |
| 109 | Other Additional Taxes Amount `<OtrosImpuestosAdicionales>` | Value of the additional tax associated with the additional tax code. Conditional on code 001 to 005 existing.<br>The calculation of the additional tax amount will depend on the rate corresponding to the tax code in Table I (Additional Tax Types Coding). | 18 | NUM | a) Numeric value of 16 integers, two decimals; >0 (must be positive).<br>b) If the tax code is between 001 to 005, the item amounts must be multiplied by the rate corresponding to the additional tax code.<br>c) For codes 001, 002, 003 and 004, if the taxed amount indicator=1, the item amount must be divided by (1+ ITBIS rate 1), and the result multiplied by the rate corresponding to the additional tax code.<br>d) For codes 002 and 004, if the field²⁷ 'Standard 10-07 Indicator' from the Discounts or Surcharges section is completed, the sum of the values of the item amount with billing indicator=1 must be divided by (1+ITBIS rate 1 rate+ additional tax code 002 rate + additional tax code 004 rate), then multiply this result by the rate corresponding to the additional tax code.<br>e) If a global discount exists, the percentage of the item amount per line²⁸ must be multiplied by the Discount Amount (global), this will result in the applicable discount amount for each detail line. | N²⁹ | 2 | 2 | 2 | 2 | 0 | 0 | 2²⁹ | 2 | 0 | 0 |
| | **END TABLE** | **ADDITIONAL TAXES** | | | | | | | | | | | | | | |

*(Continuation of TOTALS AREA Table)*

| # | FIELDS | DESCRIPTION | Max Length | Type | Validation | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|--------|-------------|-----------|------|------------|---|----|----|----|----|----|----|----|----|----|----| 
| 110 | Total Amount `<MontoTotal>` | Total Taxed Amount + Exempt Amount + Total ITBIS + Additional Tax Amount. | 18 | NUM | a) Numeric value of 16 integers, two decimals; ≥ 0 (Cannot be negative)<br>b) Numeric value according to the sum total of the Description field.<br>c) If the Pagination section is completed, the total amount must equal the sum of the 'Page Subtotal Amount' field corresponding to the section.<br>d) If an e-CF type 34 is issued, the total amount must be less than or equal to the total amount of the modified e-CF.³⁰ | I | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 111 | Non-Billable Amount `<MontoNoFacturable>` | Total sum of amounts for goods or services with Billing Indicator=0.<br>Conditional on any item with billing indicator equal to zero (0) existing in the detail line. | 18 | NUM | a) Numeric value of 16 integers, two decimals. (Can be negative)<br>b) Numeric value according to the total sum of item amount with billing indicator=0. | N | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 2 | 0 |
| 112 | Period Amount `<MontoPeriodo>` | Total sum of Total Amount and Non-Billable Amount. | 18 | NUM | a) Numeric value of 16 integers, two decimals. (Can be negative)<br>b) Period amount= Total Amount+Non-Billable Amount. | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 113 | Previous Balance `<SaldoAnterior>` | Previous Balance. Included only for the purpose of clearly illustrating the charge. | 18 | NUM | Numeric value of 16 integers, two decimals. (Can be negative). | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 114 | Payment Advance Amount `<MontoAvancePago>` | Partial payment in advance of the invoice being issued. | 18 | NUM | a) Numeric value of 16 integers, two decimals. >0 (Cannot be negative) | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 115 | Amount Payable `<ValorPagar>` | Amount charged. | 18 | NUM | a) Numeric value of 16 integers, two decimals. (Can be negative or zero)<br>b) Amount payable= Total amount-Payment Advance amount ± Previous Balance (± depending on whether the value is positive or negative).<br>c) If the 'Standard 10-07 Indicator' field from the Discount or Surcharge section is completed, then: Amount payable= Total amount-Discount amount³¹- Payment Advance amount ± Previous Balance (± depending on whether the value is positive or negative). | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 116 | Total Withheld ITBIS Amount `<TotalITBISRetenido>` | Amount of ITBIS corresponding to the withholding that will be made by the buyer. Conditional on withholding existing in the detail line. | 18 | NUM | a) Numeric value of 16 integers, two decimals, ≥0 (Cannot be negative)<br>b) Withheld ITBIS Amount field from the Goods or Services Detail section. | N | 2 | 0 | 2 | 2 | 2 | 0 | 0 | 0 | 0 | 0 |
| 117 | Total Income Tax Withholding Amount `<TotalISRRetencion>` | Amount of Income Tax corresponding to the withholding made from the provision or rental of services. Conditional on withholding existing in the detail line. | 18 | NUM | a) Numeric value of 16 integers, two decimals, ≥0 (Cannot be negative)<br>b) Income Tax Withholding Amount from the Goods or Services Detail section. | N | 2 | 0 | 2 | 2 | 2 | 0 | 0 | 0 | 0 | 2 |
| 118 | Total ITBIS Perception Amount³² `<TotalITBISPercepcion>` | Amount of ITBIS that the taxpayer charges third parties as an advance of the tax that they will perceive in their operations. Conditional on perception existing in the detail line. | 18 | NUM | a) Numeric value of 16 integers, two decimals, >0 (Cannot be negative) | N | 2 | 0 | 2 | 2 | 2 | 0 | 0 | 0 | 0 | 0 |
| 119 | Total Income Perception Amount `<TotalISRPercepcion>` | Amount of Income Tax that the taxpayer charges third parties as an advance of the tax that they will perceive in their operations. Conditional on perception existing in the detail line. | 18 | NUM | a) Numeric value of 16 integers, two decimals; >0 (Cannot be negative) | N | 2 | 0 | 2 | 2 | 2 | 0 | 0 | 0 | 0 | 0 |
| | END AREA | **HEADER TOTALS** | | | | | | | | | | | | | | |

---

---

### A.7 AREA: OTHER CURRENCY `<OtraMoneda>`

Conditional on billing being in Other Currency.**

| # | FIELDS | DESCRIPTION | Max Length | Type | Validation | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|--------|-------------|-----------|------|------------|---|----|----|----|----|----|----|----|----|----|----| 
| | HEADER OTHER CURRENCY AREA `<OtraMoneda>` | Conditional on billing being in Other Currency. | | | | | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| 120 | Other Currency Code `<TipoMoneda>` | Alternative currency in which the Amounts are expressed. Conditional on billing being done in foreign currency.³³<br>This field must have one of the values indicated in the 'Currency Coding Table'. For example: "USD" or "EUR", etc. | 3 | ALPHA | a) Validate with Table II (Currency Coding). | N | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| 121 | Exchange Rate `<TipoCambio>` | Conversion factor used.<br>Conditional on data existing in other currency code. | 7 | NUM | a) Numeric value of 3 integers and 4 decimals; > 0. (Must be positive) | N | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| 122 | Total Taxed Amount Other Currency `<MontoGravadoTotalOtraMoneda>` | Total sum of values of Taxed Amount ITBIS Other Currency at different rates.<br>Conditional on data existing in other currency code and Taxed Amount ITBIS in other currency at different rates (18%, 16% and 0%). | 18 | NUM | a) Numeric value of 16 integers, 2 decimals; ≥ 0 (Cannot be negative)<br>b) Numeric value of the sum total Taxed Amount ITBIS Rate1 Other Currency + Taxed Amount ITBIS Rate 2 Other Currency +Taxed Amount ITBIS Rate3 Other Currency. | N³⁴ | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 0 |
| 123 | Taxed Amount ITBIS Rate 1 Other Currency `<MontoGravado1OtraMoneda>` | Total sum of values of taxed Items assigned to ITBIS rate 1 (18% rate), minus discounts in Other Currency plus surcharges in Other Currency³⁵. (Assigned to taxed items in Other Currency).<br>Conditional on data existing in other currency code and the item containing billing indicator equal to 1. | 18 | NUM | a) Numeric value of 16 integers, 2 decimals; ≥ 0 (Cannot be negative).<br>b) Sum of values of item amount with billing indicator=1, minus discounts in Other Currency plus surcharges in Other Currency.<br>c) If the taxed amount indicator=1, the result must be divided by (1+ITBIS rate 1 rate) | N | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 0 | 0 |
| 124 | Taxed Amount ITBIS Rate 2 Other Currency `<MontoGravado2OtraMoneda>` | Total sum of values of taxed Items assigned to ITBIS rate 2 in Other Currency (16% rate), minus discounts in Other Currency plus surcharges in Other Currency. (Assigned to taxed items in Other Currency).<br>Conditional on data existing in other currency code and the item containing billing indicator equal to 2. | 18 | NUM | a) Numeric value of 16 integers, 2 decimals; ≥ 0 (Cannot be negative).<br>b) Sum of values of item amount with billing indicator=2, minus discounts in Other Currency plus surcharges in Other Currency. | N | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 0 | 0 |
| 125 | Taxed Amount ITBIS Rate 3 Other Currency `<MontoGravado3OtraMoneda>` | Total sum of values of taxed Items assigned to ITBIS rate 3 in Other Currency (0% rate), minus discounts in Other Currency plus surcharges in Other Currency. (Assigned to taxed items in Other Currency).<br>Conditional on data existing in other currency code and the item containing billing indicator equal to 3. | 18 | NUM | a) Numeric value of 16 integers, 2 decimals; ≥ 0 (Cannot be negative).<br>b) Sum of values of item amount with billing indicator=3, minus discounts in Other Currency plus surcharges in Other Currency. | N | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 0 |
| 126 | Exempt Amount in Other Currency `<MontoExentoOtraMoneda>` | Total sum of values of exempt items, minus discounts in Other Currency plus surcharges in Other Currency (assigned to exempt items).<br>Conditional on data existing in other currency code and the item containing billing indicator equal to 4. | 18 | NUM | a) Numeric value of 16 integers, 2 decimals; ≥ 0 (Cannot be negative).<br>Sum of values of item amount with billing indicator=4, minus discounts in Other Currency plus surcharges in Other Currency. | N | 2 | 2 | 2 | 2 | 2 | 2³⁶ | 2 | 2 | 0 | 2 |
| 127 | Total ITBIS in Other Currency `<TotalITBIS OtraMoneda>` | Total sum of ITBIS values in Other Currency at different rates. Conditional on Total ITBIS Rate 1 in Other Currency, and/or Total ITBIS Rate 2 in Other Currency and/or Total ITBIS Rate 3 in Other Currency existing. | 18 | NUM | a) Numeric value of 16 integers, 2 decimals; ≥ 0 (Cannot be negative).<br>b) Sum of Total ITBIS Rate 1 in Other Currency + Total ITBIS Rate 2 in Other Currency + Total ITBIS Rate 3 in Other Currency. | N | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 0 |
| 128 | Total ITBIS Rate 1 in Other Currency `<TotalITBIS1OtraMoneda>` | Numeric value equal to Taxed Amount ITBIS in Other Currency Rate1*ITBIS rate 1. Conditional on Taxed Amount ITBIS Rate 1 Other Currency existing.<br>Conditional on Taxed Amount rate 1 in Other Currency existing. | 18 | NUM | a) Numeric value of 16 integers, two decimals≥ 0 (Cannot be negative).<br>Total ITBIS Rate1 in Other Currency= Taxed Amount ITBIS rate1 Other Currency*ITBIS rate 1.³⁷ | N | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 0 | 0 |
| 129 | Total ITBIS Rate 2 in Other Currency `<TotalITBIS2OtraMoneda>` | Numeric value equal to Taxed Amount ITBIS in Other Currency Rate2*ITBIS rate 2.<br>Conditional on Taxed Amount ITBIS Rate 2 Other Currency existing. | 18 | NUM | a) Numeric value of 16 integers, two decimals; ≥0 (Cannot be negative).<br>Total ITBIS Rate 2 in Other Currency= Taxed Amount ITBIS rate2 Other Currency*ITBIS rate 2. | N | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 0 | 0 |
| 130 | Total ITBIS Rate 3 in Other Currency `<TotalITBIS3OtraMoneda>` | Numeric value equal to Taxed Amount ITBIS in Other Currency Rate3*ITBIS rate 3. Conditional on Taxed Amount ITBIS Rate 3 Other Currency existing. | 18 | NUM | a) Numeric value of 16 integers, two decimals; ≥ 0 (Cannot be negative). | N | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 0 |
| 131 | Additional Tax Amount in Other Currency³⁸ `<MontoImpuestoAdicionalOtraMoneda>` | Sum of the Specific Selective Consumption Tax Amount in Other Currency, Ad Valorem Selective Consumption Tax Amount in Other Currency and Other Additional Taxes Amount in Other Currency fields.<br>Conditional on data existing in other currency code and at least one of the Specific Selective Consumption Tax Amount in Other Currency, Ad Valorem Selective Consumption Tax Amount in Other Currency and/or Other Additional Taxes Amount in Other Currency fields existing. | 18 | NUM | a) Numeric value of 16 integers, two decimals; >0 (must be positive).<br>b) Additional Tax Amount in Other Currency= Specific Selective Consumption Tax Amount in Other Currency + Ad Valorem Selective Consumption Tax Amount in Other Currency + Other Additional Taxes Amount in Other Currency. | N | 2 | 2 | 2 | 2 | 0 | 0 | 2³⁹ | 2 | 0 | 0 |
| | **Additional Taxes Table in Other Currency: `<ImpuestosAdicionalesOtraMoneda>`⁴⁰** | Up to 20 repetitions of code-value pairs can be included. Includes the following five fields: | | | Conditional on other tax(es) existing in the detail line different from ITBIS and this field being completed | | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 0 | 0 |
| 132 | Additional Tax Code in Other Currency `<TipoImpuestoOtraMoneda>` | Data corresponding to the Additional Tax Code according to the 'Additional Tax Types Coding Table'.⁴¹ | 3 | NUM | a) Validate with Table I (Additional Tax Types Coding) | N | 2 | 2 | 2 | 2 | 0 | 0 | 2⁴² | 2 | 0 | 0 |
| 133 | Additional Tax Rate in Other Currency `<TasaImpuestoAdicionalOtraMoneda>` | Data corresponding to the Additional Tax Rate. The Tax rate must be indicated. | 5 | NUM | a) Validate with Table I (Additional Tax Types Coding) | N⁴³ | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 0 | 0 |
| 134 | Specific Selective Consumption Tax Amount in Other Currency `<MontoImpuestoSelectivoConsumoEspecificoOtraMoneda>` | Value of the Specific Selective Consumption Tax Amount field referenced to the exchange rate of the specified Other Currency code. Conditional on additional tax code 006 to 022 existing, the other currency code field being completed and the Specific Selective Tax Amount field.⁴⁴ | 18 | NUM | a) Numeric value of 16 integers, two decimals; >0 (must be positive).<br>b) Value of the Specific Selective Consumption Tax Amount field divided by the rate specified in the Exchange Rate field. | N | 2 | 2 | 2 | 2 | 0 | 0 | 0 | 2 | 0 | 0 |
| 135 | Ad Valorem Selective Consumption Tax Amount in Other Currency `<MontoImpuestoSelectivoConsumoAdvaloremOtraMoneda>` | Value of the Ad Valorem Selective Consumption Tax Amount field referenced to the exchange rate of the specified Other Currency code. Conditional on additional tax code 023 to 039 existing, the other currency code field being completed and the Ad Valorem Selective Tax Amount field.⁴⁵ | 18 | NUM | a) Numeric value of 16 integers, two decimals; >0 (must be positive).<br>a) Value of the Ad Valorem Selective Tax Amount field divided by the rate specified in the Exchange Rate field. | N | 2 | 2 | 2 | 2 | 0 | 0 | 0 | 2 | 0 | 0 |
| 136 | Other Additional Taxes Amount in Other Currency `<OtrosImpuestosAdicionalesOtraMoneda>` | Value of the Additional Taxes Amount referenced to the exchange rate of the specified Other Currency code.<br>Conditional on additional tax code 001 to 005 existing, the other currency code field being completed and the Other Additional Taxes Amount field.⁴⁶ | 18 | NUM | b) Numeric value of 16 integers, two decimals; >0 (must be positive).<br>c) Value of the Other Additional Tax Amount field divided by the rate specified in the Exchange Rate field. | N | 2 | 2 | 2 | 2 | 0 | 0 | 2⁴⁷ | 2 | 0 | 0 |
| | **END TABLE** | **ADDITIONAL TAXES** | | | | | | | | | | | | | | |
| 137 | Total Amount in Other Currency `<MontoTotalOtraMoneda>` | Total taxed amount in Other Currency + Exempt amount in Other Currency+ Total ITBIS in Other Currency+ Additional Tax Amount in Other Currency.<br>Conditional on at least one amount in other currency existing. | 18 | NUM | a) Numeric value of 16 integers, two decimals; ≥ 0 (cannot be negative).<br>b) Numeric value according to the total sum of the Description field. | N | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| | END AREA | **HEADER OTHER CURRENCY** | | | | | | | | | | | | | | |

---

---

## B. GOODS OR SERVICES DETAIL

### AREA: ITEM DETAILS `<DetallesItem>`

This AREA is mandatory for all e-CF types.

### AREA: ITEM `<Item>`

Up to 100 repetitions can be included.**

| # | FIELDS | DESCRIPTION | Max Length | Type | Validation | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|--------|-------------|-----------|------|------------|---|----|----|----|----|----|----|----|----|----|----| 
| | ITEM DETAILS AREA `<DetallesItem>` | | | | | | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| | ITEM AREA `<Item>` | Up to 100 repetitions can be included. | | | | | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 1 | Line No. or Sequential No. `<NumeroLinea>` | Line that numbers the item. From 1 to 100 repetitions.⁴⁸ | 5 | NUM | a) Sequential line number. | N | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| | **Item Codes Table `<TablaCodigosItem>`** | Up to 5 repetitions of code-value pairs can be included. Includes the following two fields: | | | | | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 2 | Code Type `<TipoCodigo>` | Type of coding used for the item<br>Standard: EAN, PLU, DUN or Internal<br>(Up to 5 code types) | 14 | ALPHANUM | a) No validation. | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 3 | Item Code `<CodigoItem>` | Item code according to the coding type indicated in the previous field.<br>(Up to 5 codes) | 35 | ALPHANUM | a) No validation. | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| | **END TABLE** | **ITEM CODES** | | | | | | | | | | | | | | |
| 4 | Billing Indicator `<IndicadorFacturacion>` | Indicates if the item is exempt, taxed, or Non-billable. Will indicate different rates:<br>0: Non-Billable<br>ITBIS 1: item taxed at ITBIS rate1 (18%).<br>ITBIS 2: item taxed at ITBIS rate2 (16%).<br>ITBIS 3: item taxed at ITBIS rate3 (0%).<br>E: Exempt | 1 | NUM | a) Indicate if value is<br>0: Non-Billable<br>1: ITBIS 1 (18%)<br>2: ITBIS 2 (16%)<br>3: ITBIS 3 (0%)<br>4: Exempt (E) | P⁴⁹ | 1 | 1 | 1 | 1 | 1 | 1⁵⁰ | 1 | 1 | 1⁵¹ | 1 |
| | AREA `<Retencion>` | **WITHHOLDING** | | | Conditional on withholding existing. | | 2 | 0 | 2 | 2 | 1 | 0 | 0 | 0 | 0 | 1 |
| 5 | Withholding or Perception Agent Indicator⁵² `<IndicadorAgenteRetencionoPercepcion>` | For Withholding or Perception Agents. Indicates for each transaction if they are a withholding agent for the product being sold or the service. Conditional on withholding existing. | 1 | NUM | a) Coding:<br>1: "R"<br>2: "P" | N | 2 | 0 | 2 | 2 | 1 | 0 | 0 | 0 | 0 | 1 |
| 6 | Withheld ITBIS Amount `<MontoITBISRetenido>` | Amount of ITBIS corresponding to the withholding that will be made by the buyer. Conditional on withholding existing.⁵³ | 18 | NUM | a) Numeric value of 16 integers, two decimals, ≥0. | N | 2 | 0 | 2 | 2 | 2 | 0 | 0 | 0 | 0 | 0 |
| 7 | Income Tax Withholding Amount `<MontoISRRetenido>` | Amount of Income Tax corresponding to the withholding made from the provision or rental of services.<br>The e-CF type 41 is conditional on withholding existing and the 'Goods or Services Indicator' being equal to 2. | 18 | NUM | a) Numeric value of 16 integers, two decimals, ≥0.<br>b) The e-CF type 41 is conditional on withholding existing and the 'Goods or Services Indicator' being equal to 2. | N | 2 | 0 | 2 | 2 | 2 | 0 | 0 | 0 | 0 | 1 |
| | END AREA | **WITHHOLDING** | | | | | | | | | | | | | | |
| 8 | Item Name `<NombreItem>` | Product or service name. | 80 | ALPHANUM | a) No validation. | I | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 9 | Goods or Services Indicator `<IndicadorBienoServicio>` | Identifies if the item corresponds to Goods or Service. | 1 | NUM | a) Indicate if Value is:<br>1: Goods<br>2: Service | N | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1⁵⁴ |
| 10 | Additional Description `<DescripcionItem>` | Additional description of the item. | 1000 | ALPHANUM | a) No validation | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 11 | Quantity `<CantidadItem>` | Item quantity⁵⁵ | 18 | NUM | a) Numeric value of 16 integers, 2 decimals; >0 (Cannot be negative). | I | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 12 | Item Unit of Measure `<UnidadMedida>` | Indicates the unit of measure in which the quantity is expressed. | 2 | NUM | a) Validate with the Unit of Measure Coding Table. | P | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 13 | Reference Quantity `<CantidadReferencia>` | Quantity for the reference unit of measure (not used for Item Amount calculation).<br>Conditional on the item being taxed with additional tax codes between 006-022 in the Additional Tax Type Coding Table.⁵⁶ | 18 | NUM | a) Numeric value of 16 integers, 2 decimals; ≥0 (Cannot be negative). | N | 2 | 2 | 2 | 2 | 0 | 0 | 0 | 2 | 0 | 0 |
| 14 | Reference Unit `<UnidadReferencia>` | Indicates the reference unit of measure.<br>Conditional on the Reference quantity field being completed. | 2 | NUM | a) Validate with Table IV (Unit of Measure Coding). | N | 2 | 2 | 2 | 2 | 0 | 0 | 0 | 2 | 0 | 0 |
| | **Subquantity Distribution Table `<TablaSubcantidad>`⁵⁷** | This table must be included for the purpose of calculating selective consumption taxes on products derived from alcohol and beer and tobacco and cigarette products.<br>Conditional on code from 006 to 039 existing according to the 'Additional Tax Types Coding Table'.<br>Up to 5 repetitions of quantity-code pairs can be included. Includes the following two fields: | | | | N | 2 | 2 | 2 | 2 | 0 | 0 | 0 | 2 | 0 | 0 |
| 15 | Subquantity `<Subcantidad>` | Number of reference units that the item unit has.<br>Conditional on the item being taxed with additional tax codes from 006 to 022 in the Additional Tax Type Coding Table.⁵⁸ | 19 | NUM | a) Numeric value of 16 integers, 3 decimals; ≥0 (Cannot be negative). | N | 2 | 2 | 2 | 2 | 0 | 0 | 0 | 2 | 0 | 0 |
| 16 | Subquantity Code `<CodigoSubcantidad>` | Indicates the unit of measure for the subquantity. | 2 | NUM | a) Validate with Table IV (Unit of Measure Coding). | N | 2 | 2 | 2 | 2 | 0 | 0 | 0 | 2 | 0 | 0 |
| | **END TABLE** | **SUBQUANTITY** | | | | | | | | | | | | | | |
| 17 | Alcohol Degrees in %⁵⁹ `<GradosAlcohol>` | Corresponds to the percentage of alcohol in the total alcoholic concentration volume per product unit. Conditional on the item being taxed with additional tax codes 006 to 018 in the Additional Tax Type Coding Table (alcoholic beverages). | 5 | NUM | a) Numeric value of 3 integers and 2 decimals; >0. (Must be positive) | I | 2 | 2 | 2 | 2 | 0 | 0 | 0 | 2 | 0 | 0 |
| 18 | Reference Unit Price⁶⁰ `<PrecioUnitarioReferencia>` | Unit price for the reference unit of measure (not used for Total amount calculation).<br>Conditional on the item being taxed with additional tax codes from 023 to 039 in the Additional Tax Type Coding Table. | 18 | NUM | a) Numeric value of 16 integers, 2 decimals. >0 (Cannot be negative) | I | 2 | 2 | 2 | 2 | 0 | 0 | 0 | 2 | 0 | 0 |
| 19 | Manufacturing Date `<FechaElaboracion>` | Data corresponding to the item manufacturing date. | 10 | ALPHANUM | a) Valid date<br>Format: (dd-MM-YYYY) | N | 3 | 3 | 3 | 3 | 3 | 0 | 3 | 3 | 3 | 0 |
| 20 | Expiration Date `<FechaVencimientoItem>` | Data corresponding to the item expiration date. | 10 | ALPHANUM | a) Valid date<br>Format: (dd-MM-YYYY) | N | 3 | 3 | 3 | 3 | 3 | 0 | 3 | 3 | 3 | 0 |
| | AREA `<Mineria>` | **MINING.**<br>Conditional on billing related to the mining sector existing. | | | | | 0 | 2 | 2 | 2 | 0 | 0 | 0 | 0 | 2 | 0 |
| 21 | Net Weight Kilogram `<PesoNetoKilogramo>` | Indicates the net weight in kilogram of the mineral.⁶¹ | 19 | NUM | a) Numeric value of 16 integers, 3 decimals; ≥0 (Cannot be negative). | N | 0 | 2 | 2 | 2 | 0 | 0 | 0 | 0 | 2 | 0 |
| 22 | Net Weight `<PesoNetoMineria>` | Indicates the net weight of the mineral.⁶² | 19 | NUM | a) Numeric value of 16 integers, 3 decimals; ≥0 (Cannot be negative). | N | 0 | 2 | 2 | 2 | 0 | 0 | 0 | 0 | 2 | 0 |
| 23 | Affiliation Type `<TipoAfiliacion>` | Indicates if the recipient is affiliated or not.⁶³ | 1 | NUM | a) Indicate if value is:<br>1: Affiliated<br>2: Not affiliated | N | 0 | 2 | 2 | 2 | 0 | 0 | 0 | 0 | 2 | 0 |
| 24 | Settlement `<Liquidacion>` | Indicates if the mineral settlement is provisional or final.⁶⁴ | 1 | NUM | a) Indicate if value is:<br>1: Provisional<br>2: Final | N | 0 | 2 | 2 | 2 | 0 | 0 | 0 | 0 | 2 | 0 |
| | END AREA | **MINING** | | | | | | | | | | | | | | |
| 25 | Item Unit Price⁶⁵ `<PrecioUnitarioItem>` | Data corresponding to the item unit price. | 20 | NUM | a) Numeric value of 16 integers, 4 decimals; ≥0 (Cannot be negative). | I | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 26 | Discount Amount `<DescuentoMonto>` | Totalizes all sub-discounts granted to the item in amounts. Conditional on Subdiscount Amount existing. | 18 | NUM | a) Numeric value of 16 integers, 2 decimals; ≥0 (Cannot be negative).<br>b) Subdiscount Amount | I | 2 | 2 | 2 | 2 | 2 | 0 | 2 | 2 | 2 | 0 |
| | **Subdiscount Distribution Table `<TablaSubDescuento>`⁶⁶** | Conditional on discount existing on the item. Up to 12 repetitions can be included. Includes the following three fields: | | | | N | 2 | 2 | 2 | 2 | 2 | 0 | 2 | 2 | 2 | 0 |
| 27 | Subdiscount Type `<TipoSubDescuento>` | Indicates if the Subdiscount is in amount ($) or percentage (%). Conditional on discount existing on the item. | 1 | ALPHA | a) "$" or "%" | N | 2 | 2 | 2 | 2 | 2 | 0 | 2 | 2 | 2 | 0 |
| 28 | Subdiscount in % `<SubDescuentoPorcentaje>` | Value of the Subdiscount in percentage %. Conditional on Subdiscount type in percentage (%) existing. | 5 | NUM | a) Numeric value. 3 integers and 2 decimals; >0 (Cannot be negative) | N | 2 | 2 | 2 | 2 | 2 | 0 | 2 | 2 | 2 | 0 |
| 29 | Subdiscount Amount `<MontoSubDescuento>` | Corresponding to the discount value expressed in amount.<br>If the subdiscount is in %, the subdiscount amount must go. | 18 | NUM | a) Numeric value of 16 integers, 2 decimals. ≥0 (Cannot be negative).<br>b) If the subdiscount is in %, the subdiscount amount value must equal the item unit price times the subdiscount percentage, times the number of items. | N | 2 | 2 | 2 | 2 | 2 | 0 | 2 | 2 | 2 | 0 |
| | **END TABLE** | **SUBDISCOUNT** | | | | | | | | | | | | | | |
| 30 | Surcharge Amount `<RecargoMonto>` | Totalizes all Subsurcharges granted to the item in amounts. Conditional on Subsurcharge Amount existing. | 18 | NUM | a) Numeric value of 16 integers, 2 decimals; ≥0 (Cannot be negative).<br>b) Subsurcharge Amount. | I | 2 | 2 | 2 | 2 | 2 | 0 | 2 | 2 | 2 | 0 |
| | **Subsurcharge Distribution Table `<TablaSubRecargo>`⁶⁷** | Conditional on surcharge existing on the item. Up to 12 repetitions of Type-Value pairs can be included. Includes the following three fields: | | | | N | 2 | 2 | 2 | 2 | 2 | 0 | 2 | 2 | 2 | 0 |
| 31 | Subsurcharge Type `<TipoSubRecargo>` | Indicates if the Subsurcharge is in $ or %. Conditional on surcharge existing on the item. | 1 | ALPHA | "$" or "%" | N | 2 | 2 | 2 | 2 | 2 | 0 | 2 | 2 | 2 | 0 |
| 32 | Subsurcharge in % `<SubRecargoPorcentaje>` | Value of the Subsurcharge in percentage %. Conditional on Subsurcharge type in percentage (%) existing. | 5 | NUM | a) Numeric value, 3 integers and 2 decimals; >0 (Cannot be negative) | N | 2 | 2 | 2 | 2 | 2 | 0 | 2 | 2 | 2 | 0 |
| 33 | Subsurcharge Amount `<MontoSubRecargo>` | Corresponding to the Subsurcharge value expressed in amount. Conditional on subsurcharge existing.<br>If the subsurcharge is in %, the subsurcharge amount must go. | 18 | NUM | a) Numeric value of 16 integers, 2 decimals; ≥0 (Cannot be negative).<br>b) If the subsurcharge is in %, the subsurcharge amount value must equal the item unit price times the subsurcharge percentage value, times the number of items. | N | 2 | 2 | 2 | 2 | 2 | 0 | 2 | 2 | 2 | 0 |
| | **END TABLE** | **SUBSURCHARGE** | | | | | | | | | | | | | | |
| | **Additional Tax Codes Table `<TablaImpuestoAdicional>`⁶⁸** | Up to 2 repetitions of tax codes can be included. | | | | | 2 | 2 | 2 | 2 | 0 | 0 | **2⁶⁹** | 2 | 0 | 0 |
| 34 | Additional Tax Code `<TipoImpuesto>` | Data corresponding to the Additional Tax Code according to the Additional Tax Types Coding Table (Table I). Conditional on the item being taxed with Additional Tax.⁷⁰ | 3 | NUM | Valid code with respect to Table I (Additional Tax Types Coding). | N | 2 | 2 | 2 | 2 | 0 | 0 | 2⁷¹ | 2 | 0 | 0 |
| | **END TABLE** | **ADDITIONAL TAXES** | | | | | | | | | | | | | | |
| | AREA `<OtraMonedaDetalle>` | **DETAIL OTHER CURRENCY.**<br>Indicate prices in alternative currencies.⁷² | | | | | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| 35 | Unit price in other currency `<PrecioOtraMoneda>` | Data corresponding to the Item Unit Price in other currency. Conditional on the item being in Other Currency. | 20 | NUM | a) Numeric value of 16 integers, 4 decimals. ≥0 (Cannot be negative). | N⁷³ | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| 36 | Discount in Other Currency `<DescuentoOtraMoneda>` | Corresponds to the discount value granted in Other Currency. | 18 | NUM | a) Numeric value of 16 integers, 2 decimals. ≥0 (Cannot be negative). | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 37 | Surcharge in Other Currency `<RecargoOtraMoneda>` | Corresponds to the surcharge value granted in Other Currency. | 18 | NUM | a) Numeric value of 16 integers, 2 decimals. ≥0 (Cannot be negative). | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 38 | Item Amount Other Currency `<MontoItemOtraMoneda>` | (Unit Price in other currency * Quantity) – Discount in other currency + Surcharge in other currency.<br>Conditional on the item Price and Discounts or Surcharge (if they exist) being in Other Currency. | 18 | NUM | a) Numeric value of 16 integers, 2 decimals. ≥0 (Cannot be negative).<br>b) Numeric value according to the Description field. | N | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| | END AREA | **DETAIL OTHER CURRENCY** | | | | | | | | | | | | | | |
| 39 | Item Amount (Value per detail line) `<MontoItem>` | (Item Unit Price * Quantity) – Discount Amount + Surcharge Amount | 18 | NUM | a) Numeric value of 16 integers, 2 decimals; ≥ 0 (Cannot be negative).<br>b) Numeric value, according to description.<br>c) Must be zero when: it is a Credit Note for text correction purposes.⁷⁴<br>When it is zero, it may not be printed or an explanatory text may be printed (no value, no cost, etc.) | I | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| | END AREA | **ITEM** | | | | | | | | | | | | | | |
| | END AREA | **ITEM DETAILS** | | | | | | | | | | | | | | |

---


---

| 36 | `<DescuentoOtraMoneda>` | Discount (OC) | 18 | NUM | ≥0, 2 decimals | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 37 | `<RecargoOtraMoneda>` | Surcharge (OC) | 18 | NUM | ≥0, 2 decimals | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 38 | `<MontoItemOtraMoneda>` | Line total (OC) | 18 | NUM | ≥0, 2 decimals | N | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |

---

### B.12 Line Total (Field 39)

| # | Element | Description | Max | Type | Validation | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|----------|-------------|-----|------|------------|:-:|----|----|----|----|----|----|----|----|----|----| 
| 39 | `<MontoItem>` | Line total | 18 | NUM | =(Price×Qty)−Discount+Surcharge | I | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |

> [!NOTE]
> `MontoItem` can be **0** for text correction credit notes (when `CodigoModificacion=2` in Reference Information).

---

## C. INFORMATIVE SUBTOTALS

Optional informative subtotals (do not affect main totals). Up to 20 `<Subtotal>` entries can be included.

**XML Structure:**
```xml
<Subtotales>
  <Subtotal>...</Subtotal>
  <Subtotal>...</Subtotal>
</Subtotales>
```

| # | Element | Description | Max | Type | Validation | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|----------|-------------|-----|------|------------|:-:|----|----|----|----|----|----|----|----|----|----| 
| 1 | `<NumeroSubTotal>` | Subtotal number | 2 | NUM | Sequential 1 to n | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 2 | `<DescripcionSubtotal>` | Title | 40 | ALPHA | — | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 3 | `<Orden>` | Display order | 2 | NUM | — | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 4 | `<SubTotalMontoGravadoTotal>` | Total taxed subtotal | 18 | NUM | ≥0, 2 decimals | N | 3 | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 0 |
| 5 | `<SubTotalMontoGravadoI1>` | Subtotal at 18% | 18 | NUM | ≥0, 2 decimals | N | 3 | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 0 | 0 |
| 6 | `<SubTotalMontoGravadoI2>` | Subtotal at 16% | 18 | NUM | ≥0, 2 decimals | N | 3 | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 0 | 0 |
| 7 | `<SubTotalMontoGravadoI3>` | Subtotal at 0% | 18 | NUM | ≥0, 2 decimals | N | 3 | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 0 |
| 8 | `<SubTotaITBIS>` | ITBIS subtotal | 18 | NUM | ≥0, 2 decimals | N | 3 | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 0 |
| 9 | `<SubTotaITBIS1>` | ITBIS subtotal 18% | 18 | NUM | ≥0, 2 decimals | N | 3 | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 0 | 0 |
| 10 | `<SubTotaITBIS2>` | ITBIS subtotal 16% | 18 | NUM | ≥0, 2 decimals | N | 3 | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 0 | 0 |
| 11 | `<SubTotaITBIS3>` | ITBIS subtotal 0% | 18 | NUM | ≥0, 2 decimals | N | 3 | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 0 |
| 12 | `<SubTotalImpuestoAdicional>` | Additional taxes subtotal | 18 | NUM | >0, 2 decimals | N | 3 | 3 | 3 | 3 | 3 | 0 | 3 | 3 | 0 | 0 |
| 13 | `<SubTotalExento>` | Exempt subtotal | 18 | NUM | ≥0, 2 decimals | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 0 | 3 |
| 14 | `<MontoSubTotal>` | Subtotal amount | 18 | NUM | ≥0, 2 decimals | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 15 | `<Lineas>` | Line count in subtotal | 2 | NUM | >0 | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |


---

## D. DISCOUNTS OR SURCHARGES

Global discounts/surcharges that apply to the entire invoice (not per item). Up to 20 `<DescuentoORecargo>` entries can be included.

**XML Structure:**
```xml
<DescuentosORecargos>
  <DescuentoORecargo>...</DescuentoORecargo>
  <DescuentoORecargo>...</DescuentoORecargo>
</DescuentosORecargos>
```

| # | Element | Description | Max | Type | Validation | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|----------|-------------|-----|------|------------|:-:|----|----|----|----|----|----|----|----|----|----| 
| 1 | `<NumeroLinea>` | Line number | 2 | NUM | 1-20 | N | 2 | 2 | 2 | 2 | 2 | 0 | 2 | 2 | 2 | 0 |
| 2 | `<TipoAjuste>` | D (Discount) or R (Surcharge) | 1 | ALPHA | — | N | 2 | 2 | 2 | 2 | 2 | 0 | 2 | 2 | 2 | 0 |
| 3 | `<IndicadorNorma1007>` | Standard 10-07 Indicator | 1 | NUM | 1=Yes | N | 3 | 3 | 3 | 3 | 0 | 0 | 0 | 3 | 0 | 0 |
| 4 | `<DescripcionDescuentooRecargo>` | Description | 45 | ALPHA | — | I | 3 | 3 | 3 | 3 | 3 | 0 | 3 | 3 | 3 | 0 |
| 5 | `<TipoValor>` | Value type (% or $) | 1 | ALPHA | "%" or "$" | I | 2 | 2 | 2 | 2 | 2 | 0 | 2 | 2 | 2 | 0 |
| 6 | `<ValorDescuentooRecargo>` | Discount/surcharge percentage | 5 | NUM | >0, 3 int + 2 dec | I | 2 | 2 | 2 | 2 | 2 | 0 | 2 | 2 | 2 | 0 |
| 7 | `<MontoDescuentooRecargo>` | Discount/surcharge amount | 18 | NUM | ≥0, 2 decimals | I | 2 | 2 | 2 | 2 | 2 | 0 | 2 | 2 | 2 | 0 |
| 8 | `<MontoDescuentooRecargoOtraMoneda>` | Amount (foreign currency) | 18 | NUM | ≥0, 2 decimals | N | 3 | 3 | 3 | 3 | 3 | 0 | 3 | 3 | 3 | 0 |
| 9 | `<IndicadorFacturacionDescuentooRecargo>` | Tax indicator | 1 | NUM | 1=ITBIS1, 2=ITBIS2, 3=ITBIS3, 4=Exempt | N | 2 | 2 | 2 | 2 | 2 | 0 | 2 | 2 | 2 | 0 |


**TipoDescuentoRecargo Values:**

| Code | Description |
|--------|-------------|
| `1` | Discount |
| `2` | Surcharge |

**TipoValor Values (ALPHA field):**

| Code | Description |
|--------|-------------|
| `%` | Percentage |
| `$` | Amount (Fixed quantity) |

> [!WARNING]
> **Use literal characters**: `TipoValor` is an ALPHA field. Send the actual characters `%` or `$`, not numeric values. The PDF explicitly defines these as "%" or "$".

**IndicadorFacturacionDescuentooRecargo Values:**

| Code | Description |
|--------|-------------|
| `1` | ITBIS Rate 1 (18%) |
| `2` | ITBIS Rate 2 (16%) |
| `3` | ITBIS Rate 3 (0%) |
| `4` | Exempt (shown as "E" in DGII documentation, but send value `4`) |

> [!CAUTION]
> **Do not send "E"**: Although DGII documentation labels Exempt as "E", the field is NUM type. You must send the numeric value `4`, not the letter "E".

---

## E. PAGINATION

For printed representation, indicates which items appear on each page.

> [!NOTE]
> Each `<Pagina>` element is wrapped within the `<Paginacion>` container.
> Structure: `<Paginacion><Pagina>...</Pagina></Paginacion>`

| # | Element | Description | Max | Type | Validation | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|----------|-------------|-----|------|------------|:-:|----|----|----|----|----|----|----|----|----|----:|
| 1 | `<PaginaNo>` | Page number | 3 | NUM | 1-100, sequential | I | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| 2 | `<NoLineaDesde>` | Starting line | 3 | NUM | >0, ≤NoLineaHasta | N | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| 3 | `<NoLineaHasta>` | Ending line | 3 | NUM | >0, ≥NoLineaDesde | N | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| 4 | `<SubtotalMontoGravadoPagina>` | Page taxed subtotal | 18 | NUM | ≥0, 2 decimals | I | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 0 |
| 5 | `<SubtotalMontoGravado1Pagina>` | Page subtotal 18% | 18 | NUM | ≥0, 2 decimals | N | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 0 | 0 |
| 6 | `<SubtotalMontoGravado2Pagina>` | Page subtotal 16% | 18 | NUM | ≥0, 2 decimals | N | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 0 | 0 |
| 7 | `<SubtotalMontoGravado3Pagina>` | Page subtotal 0% | 18 | NUM | ≥0, 2 decimals | N | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 0 |
| 8 | `<SubtotalExentoPagina>` | Page exempt subtotal | 18 | NUM | ≥0, 2 decimals | I | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 2 |
| 9 | `<SubtotalItbisPagina>` | Page ITBIS subtotal | 18 | NUM | ≥0, 2 decimals | I | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 0 |
| 10 | `<SubtotalItbis1Pagina>` | Page ITBIS 18% | 18 | NUM | ≥0, 2 decimals | N | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 0 | 0 |
| 11 | `<SubtotalItbis2Pagina>` | Page ITBIS 16% | 18 | NUM | ≥0, 2 decimals | N | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 0 | 0 |
| 12 | `<SubtotalItbis3Pagina>` | Page ITBIS 0% | 18 | NUM | ≥0, 2 decimals | N | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 0 |
| 13 | `<SubtotalImpuestoAdicionalPagina>` | Page additional taxes | 18 | NUM | >0, 2 decimals | I | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 0 | 0 |
| — | `<SubtotalImpuestoAdicional>` | Additional taxes container (AREA) | — | — | — | — | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 0 | 0 |
| 14 | `<SubtotalImpuestoSelectivoConsumoEspecificoPagina>` | Page specific ISC | 18 | NUM | >0, 2 decimals | N | 2 | 2 | 2 | 2 | 0 | 0 | 0 | 2 | 0 | 0 |
| 15 | `<SubtotalOtrosImpuesto>` | Page other taxes | 18 | NUM | >0, 2 decimals | N | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 0 | 0 |
| 16 | `<MontoSubtotalPagina>` | Page subtotal | 18 | NUM | ≥0, 2 decimals | I | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| 17 | `<SubtotalMontoNoFacturablePagina>` | Page non-billable | 18 | NUM | ≥0, 2 decimals | N | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |

> [!WARNING]
> **Foreign currency pagination tags**: The tags `SubtotalMontoGravadoPaginaOtraMoneda` and `MontoSubtotalPaginaOtraMoneda` from previous versions may not be present in all PDF versions. Verify against your specific PDF version before implementing.

> [!TIP]
> **"NUM" type for monetary fields**: The PDF uses NUM for all monetary fields. When the field contains decimals, the validation specifies "2 decimals". This is the DGII convention.

---

## F. REFERENCE INFORMATION

Used for Debit/Credit Notes (types 33, 34) to reference the modified invoice.

| # | Element | Description | Max | Type | Validation | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|----------|-------------|-----|------|------------|:-:|----|----|----|----|----|----|----|----|----|----:|
| 1 | `<NCFModificado>` | Modified e-NCF | 11/13/19 | ALPHA | Valid NCF/e-NCF format | I | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2 | `<RNCOtroContribuyente>` | Other taxpayer's RNC | 9/11 | NUM | Valid RNC (9 or 11 digits) | N | 0 | 0 | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| 3 | `<FechaNCFModificado>` | Modified e-CF date | 10 | DATE | DD-MM-YYYY | N | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| 4 | `<CodigoModificacion>` | Modification code | 1 | NUM | Values 1-5 | P | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| 5 | `<RazonModificacion>` | Modification reason | 90 | ALPHA | Free text (e.g. "price error") | N | 0 | 0 | 3 | 3 | 0 | 0 | 0 | 0 | 0 | 0 |

**Modification Codes (CodigoModificacion):**

| Code | Description | Applies To |
|--------|-------------|------------|
| `1` | Cancels complete document | Credit/Debit Note |
| `2` | Corrects text | Credit/Debit Note |
| `3` | Corrects amounts | Credit/Debit Note |
| `4` | Replacement of NCF issued in contingency | Credit/Debit Note |
| `5` | Reference to Electronic Consumer Invoice | Tax Credit Invoice Only |

> [!NOTE]
> **Footnote 80**: Codes 1, 2, 3 apply only when a credit or debit note is issued.
> 

---


## G. DATE AND DIGITAL SIGNATURE

**AREA: Signature `<Signature>`**

**Digital signature and timestamp information for the e-CF.**

| # | FIELDS | DESCRIPTION | Max Length | Type | Validation | Obligatoriness |
|---|--------|-------------|-----------|------|------------|----------------|
| | **Signature AREA `<Signature>`** | | | | | **1** |
| 1 | e-CF digital signature Date and Time `<FechaHoraFirma>` | Date and time in format dd-MM-YYYY HH:mm:ss; Time zone GMT -4 | 19 | ALPHANUM | a) Valid date and time in indicated format, dd-MM-YYYY HH:mm:ss, respectively.<br>b) Validates that e-CF signature date and time=< current date and time. | 1 |
| 2 | Digital Signature | Digital signature over the entire document. (Header, Detail, Discounts - Surcharges, Pagination, Reference Information, e-CF Signature Date and Time). | - | - | - | 1 |
| | **END AREA** | **SIGNATURE** | | | | |

---

## H. ADDITIONAL NOTES  

**AREA: Notes `<Notas>`**

**Free-format additional notes for supplementary information.**

| # | FIELDS | DESCRIPTION | Max Length | Type | Validation | Obligatoriness |
|---|--------|-------------|-----------|------|------------|----------------|
| | **Notes AREA `<Notas>`** | | | | | **3** |
| 1 | Note `<Nota>` | Free text field for additional unstructured information. | 4000 | ALPHANUM | a) No specific validation | 3 |
| | **END AREA** | **NOTES** | | | | |

---

## CODING TABLES (REFERENCE TABLES)

**IMPORTANT:** Complete reference tables are available in separate markdown files. This section shows the structure and representative examples.

---

### TABLE I: Additional Tax Types Coding

**Source:** PDF pages 61-72

**Selective consumption taxes and other additional taxes applicable in the Dominican Republic.**

**Summary of main codes:**
- **001:** Legal Tip (10%)
- **002:** Telecommunications Development Contribution - CDT (2%)
- **003-004:** ISC on Insurance and Telecommunications (16%, 10%)
- **005:** Tax on First Vehicle Registration (17%)
- **006-022:** Specific ISC (RD$ per unit) - Alcoholic beverages and tobacco products
  - Beer, wines, vermouth: RD$632.58/unit
  - Aguardientes, whiskey,rum, gin, vodka, liquors: RD$632.58/unit  
  - Cigarettes 20 units: RD$53.51/pack
  - Cigarettes 10 units: RD$26.75/pack
- **023-039:** Ad Valorem ISC (%)  - Various products, percentage of value

**Note:** For the complete catalog of ~40 additional tax codes with specific rates, consult the official PDF pages 61-72.

---

### TABLE II: Currency Coding (ISO 4217)

**Source:** PDF page 63

**Currency codes authorized for e-CF:**

| ISO Code | Currency |
|------------|--------|
| BRL | Brazilian Real |
| CAD | Canadian Dollar |
| CHF | Swiss Franc |
| CHY | Chinese Yuan |
| COP | Colombian Peso |
| DKK | Danish Krone |
| EUR | Euro |
| GBP | Pound Sterling |
| HTG | Haitian Gourde |
| JPY | Japanese Yen |
| MXN | Mexican Peso |
| NOK | Norwegian Krone |
| SCP | Scottish Pound |
| SEK | Swedish Krona |
| USD | US Dollar |
| VEF | Venezuelan Strong Bolívar⁸³ |
| XDR | Special Drawing Right⁸³ |

**Total:** 17 authorized currencies

---

### TABLE III: Provinces and Municipalities of the Dominican Republic

**Source:** PDF pages 73-85  
**Complete table:** See file [`tablas-provincias-completa.md`](tablas-provincias-completa.md) (572 entries)

**6-digit code structure:**
- Format: `PPMMDD` where:
  - `PP` = Province Code (01-32)
  - `MM` = Municipality Code within the province
  - `DD` = Municipal District Code (00 = head municipality)

**Structural examples:**

| Code | Type | Name |
|--------|------|--------|
| 010000 | **Province** | **NATIONAL DISTRICT** |
| 010100 | Municipality | Santo Domingo de Guzmán |
| 020000 | **Province** | **AZUA PROVINCE** |
| 020100 | Municipality | AZUA DE COMPOSTELA MUNICIPALITY |
| 020101 | Municipality | AZUA DE COMPOSTELA (M. D.). |
| 020102 | Municipality | BARRO ARRIBA (M. D.). |
| 020103 | Municipality | LAS BARIAS-LA ESTANCIA (M. D.). |
| 020104 | Municipality | LOS JOVILLOS (M. D.). |
| 020105 | Municipality | PUERTO VIEJO (M. D.). |
| 020106 | Municipality | BARRERAS (M. D.). |
| 020107 | Municipality | DOÑA EMMA BALAGUER VIUDA VALLEJO (M. D.). |
| 020108 | Municipality | CLAVELLINA (M. D.). |
| 020200 | Municipality | LAS CHARCAS MUNICIPALITY |
| 020201 | Municipality | LAS CHARCAS |
| ... | ... | *(see complete table for 333 more entries)* |
| 320700 | Municipality | PEDRO BRAND MUNICIPALITY |
| 320701 | Municipality | PEDRO BRAND (M. D.). |
| 320702 | Municipality | LA GUÁYIGA (M. D.). |
| 320703 | Municipality | LA CUABA (M. D.). |

**Total:** 32 provinces + ~540 municipalities and municipal districts = **572 entries**

**📄 Complete table:** [`tablas-provincias-completa.md`](tablas-provincias-completa.md)
