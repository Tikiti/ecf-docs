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
