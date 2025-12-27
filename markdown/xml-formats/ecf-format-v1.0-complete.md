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
