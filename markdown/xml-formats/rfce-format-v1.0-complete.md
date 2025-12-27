# Consumer Invoice Summary Format <DOP250,000 (RFCE)

**Version 1.0 | January 2020**

---

## 1. Introduction

Taxpayers who issue electronic consumer invoices less than DOP$250 thousand using the e-CF Format, must send to Internal Taxes the sales made through this type of e-CF, in the XML format established in this document.

Regarding the electronic consumer invoice issued to the receiver, it must comply with the specifications of the Electronic Tax Receipt Format; likewise, the issuer must have an electronic mechanism for consultation purposes by their clients.

---

## 2. Content of the Consumer Invoice Format <DOP250,000 (submission to DGII)

| Section | Consumer Invoice < 250 thousand (32) |
|---------|--------------------------------------|
| Header | 1 |
| Digital Signature | 1 |

### Obligatoriedad codes:

**1** - Obligatory data: the data must always be in the document, regardless of the transaction characteristics.

**2** - Conditional data: the data is not obligatory but becomes so in certain operations, if a certain condition is met.

**3** - Optional. The data is optional.

---

## 1.1. Detail by section

The content of each section will contain the format and the obligatoriedad code. The following are specified:

- **Maximum Length:** Maximum size of the field. The indicated length will be the maximum length.
- **Document Type:** Can be alpha (ALFA), numeric (NUM) or alphanumeric (ALFANUM). In numeric type information, decimals are separated with a period. Thousands should not be separated with any other type of character.

---

## A. Header

| No. | Fields | Description | Max Length | Type | Validation | Electronic Consumer Invoice (<250 thousand) 32 |
|-----|--------|-------------|------------|------|------------|------------------------------------------------|
| | AREA `<Encabezado>` | HEADER | | | | 1 |
| 1 | VERSION | Version of the format used. | 3 | ALFANUM | a) Value: 1.0 | 1 |
| | AREA `<IdDoc>` | DOCUMENT IDENTIFICATION | | | | 1 |
| 2 | Electronic Tax Receipt Type<br>`<TipoeCF>` | Indicates if the document is:<br>Type Code:<br>32: Electronic Consumer Invoice | 2 | NUM | a) Type Code:<br>32: Electronic Consumer Invoice | 1 |
| 3 | e-NCF<br>`<eNCF>` | Sequence authorized by DGII. | 13 | ALFANUM | a) Sequence number authorized by DGII. | 1 |
| 4 | Income Type<br>`<TipoIngresos>` | Indicates the type of income received, according to the classification of the goods or services sales submission format. | 2 | NUM | Type Code:<br>01: Income from operations (Non-financial).<br>02: Financial Income<br>03: Extraordinary Income<br>04: Income from Leases<br>05: Income from Sale of Depreciable Assets<br>06: Other Income | 1 |
| 5 | Payment Type<br>`<TipoPago>` | Indicates the customer's payment type. | 1 | NUM | Type Code:<br>1: Cash<br>2: Credit<br>3: Free | 1 |
| | PAYMENT METHODS TABLE¹<br>Up to 07 repetitions.<br>Contains the following two fields. | | | | | 3 |
| 6 | Payment Method<br>`<FormaPago>` | Indicates the method in which the invoice will be paid. | 2 | NUM | Method Code:<br>1: Cash<br>2: Check/Transfer/Deposit<br>3: Debit/Credit Card<br>4: Credit Sale<br>5: Gift Bonds or Certificates<br>6: Barter<br>7: Credit note<br>8: Other Payment Methods | 3 |
| 7 | Payment Amount<br>`<MontoPago>` | Indicates the amount associated with each payment method.<br>Conditional on the existence of a payment method. | 18 | NUM | a) Numeric value of 16 integers, 2 decimals; ≥ 0 (Must be positive) | 2 |
| | END AREA | DOCUMENT IDENTIFICATION | | | | |
| | AREA `<Emisor>` | ISSUER | | | | 1 |
| 8 | Issuer RNC<br>`<RNCEmisor>` | Corresponds to the issuer's RNC. | 9 or 11 | NUM | Validate in the National Registry of taxpayers.<br>Must validate:<br>a) RNC complies with format structure.<br>b) RNC is authorized as Electronic Invoicer.<br>c) RNC is in "Active" status.<br>d) RNC has no blocking marks. | 1 |
| 9 | Issuer Name or Legal Name<br>`<RazonSocialEmisor>` | Name or Legal Name of the issuer. | 150 | ALFANUM | a) No validation | 1 |
| 10 | Issue Date<br>`<FechaEmision>` | Issue date of the e-CF. | 10 | ALFANUM | Valid date:<br>a) Format dd-MM-YYYY<br>b) Validate start date as electronic invoicer. | 1 |
| | END AREA | ISSUER | | | | |
| | AREA `<Comprador>` | BUYER | | | | 3 |
| 11 | Buyer RNC<br>`<RNCComprador>` | Corresponds to the buyer's RNC. | 9 or 11 | NUM | a) No validation | 3 |
| 12 | Foreign Identifier<br>`<IdentificadorExtranjero>`³ | Corresponds to the identification number when the buyer is foreign and does not have RNC/ID. Conditional on the buyer being foreign. | 20 | ALFANUM | a) No validation | 2 |
| 13 | Name or Legal Name<br>`<RazonSocialComprador>` | Name or Legal Name of the buyer. | 150 | ALFANUM | a) No validation | 3 |
| | END AREA | BUYER | | | | |
| | AREA `<Totales>` | TOTALS | | | | 1 |
| 14 | Total Taxable Amount⁴<br>`<MontoGravadoTotal>` | Total of the sum of taxable amount values for ITBIS at different rates.<br>Conditional on the existence of Taxable amount1, and/or Taxable amount 2 and/or Taxable amount 3. | 18 | NUM | a) Numeric value of 16 integers, 2 decimals; ≥ 0 (Cannot be negative).<br>b) Value of the sum of Taxable Amount ITBIS Rate 1 + Taxable Amount ITBIS Rate 2 + Taxable Amount ITBIS Rate 3. | 2 |
| 15 | Taxable Amount ITBIS Rate 1<br>`<MontoGravadoI1>` | Corresponds to the total of ITBIS amounts at 18%, assigned in the electronic consumer invoice.<br>Conditional on a detail line having any item taxed at 18%. | 18 | NUM | a) Numeric value of 16 integers, 2 decimals; ≥ 0 (Cannot be negative). | 2 |
| 16 | Taxable Amount ITBIS Rate 2<br>`<MontoGravadoI2>` | Corresponds to the total of ITBIS amounts at 16%, assigned in the electronic consumer invoice.<br>Conditional on a detail line having any item taxed at 16%. | 18 | NUM | a) Numeric value of 16 integers, 2 decimals; ≥ 0 (Cannot be negative). | 2 |
| 17 | Taxable Amount ITBIS Rate 3<br>`<MontoGravadoI3>` | Corresponds to the total of ITBIS amounts at zero rate (0), assigned in the electronic consumer invoice.<br>Conditional on a detail line having any item taxed at rate 0. | 18 | NUM | a) Numeric value of 16 integers, 2 decimals≥ 0 (Cannot be negative). | 2 |
| 18 | Exempt Amount<br>`<MontoExento>` | Corresponds to the total of exempt amounts, assigned in the electronic consumer invoice.<br>Conditional on a detail line having any exempt item. | 18 | NUM | a) Numeric value of 16 integers, 2 decimals≥ 0 (Cannot be negative). | 2 |
| 19 | Total ITBIS<br>`<TotalITBIS>` | Corresponds to the total sum of ITBIS amounts (at their different rates), assigned in the issued electronic consumer invoice.<br>Conditional on the taxpayer indicating that ITBIS amounts exist for at least one of the rates (1, 2 and/or 3). | 18 | NUM | a) Numeric value of 16 integers, 2 decimals; ≥ 0 (Cannot be negative).<br>b) Value of the sum of Total ITBIS Rate1 + Total ITBIS Rate 2 + Total ITBIS Rate3. | 2 |
| 20 | Total ITBIS Rate 1<br>`<TotalITBIS1>` | Corresponds to the total of ITBIS amounts at 18%, assigned in the electronic consumer invoice.<br>Conditional on a detail line having any item taxed at 18%. | 18 | NUM | a) Numeric value of 16 integers, two decimals; ≥ 0 (Cannot be negative). | 2 |
| 21 | Total ITBIS Rate 2<br>`<TotalITBIS2>` | Corresponds to the total of ITBIS amounts at 16%, assigned in the electronic consumer invoice.<br>Conditional on a detail line having any item taxed at 16% | 18 | NUM | a) Numeric value of 16 integers, two decimals; ≥ 0 (Cannot be negative). | 2 |
| 22 | Total ITBIS Rate3<br>`<TotalITBIS3>` | Corresponds to the total of ITBIS amounts at zero rate (0%), assigned in the electronic consumer invoice.<br>Conditional on a detail line having any item taxed at rate 0. | 18 | NUM | a) Numeric value of 16 integers, two decimals; ≥ 0 (Cannot be negative). | 2 |
| 23 | Additional Tax Amount<br>`<MontoImpuestoAdicional>` | Corresponds to the sum of the fields Specific Selective Consumption Tax Amount and Ad Valorem and Other Additional Taxes Amount, assigned in the electronic consumer invoice.<br>Conditional on the existence of Selective Consumption Tax Amount. | 18 | NUM | a) Numeric value of 16 integers, two decimals; >0 (must be positive).<br>b) Value of the sum of Specific Selective Consumption Tax Amount+ Ad Valorem Selective Tax Amount+ Other Additional Taxes Amount. | 2 |
| | Additional Taxes Table<br>`<ImpuestosAdicionales>`⁵<br>Up to 20 repetitions of code-value pairs can be included. Includes the following five fields:<br>Conditional on the existence of additional taxes in the electronic consumer invoice. | | | | | 2 |
| 24 | Additional Tax Code<br>`<TipoImpuesto>` | Data corresponding to the additional tax Code according to Table I (Additional Tax Types Codification) of the electronic tax receipt (e-CF) format, assigned to the electronic consumer invoice. | 3 | NUM | a) Validate with Table I (Additional Tax Types Codification)⁶ | 2 |
| 25 | Specific Selective Consumption Tax Amount<br>`<MontoImpuestoSelectivoConsumoEspecifico>` | Value of the specific selective consumption tax (ISC) associated with the additional tax code.<br>Conditional on the taxpayer indicating that specific selective consumption tax exists in the issued electronic consumer invoice. | 18 | NUM | a) Numeric value of 16 integers, two decimals; >0 (must be positive). | 2 |
| 26 | Ad Valorem Selective Consumption Tax Amount<br>`<MontoImpuestoSelectivoConsumoAdvalorem>` | Value of the Ad-Valorem selective consumption tax (ISC) associated with the additional tax code.<br>Conditional on the taxpayer indicating that Ad-valorem selective tax exists in the issued electronic consumer invoice. | 18 | NUM | a) Numeric value of 16 integers, two decimals; >0 (must be positive). | 2 |
| 27 | Other Additional Taxes Amount<br>`<OtrosImpuestosAdicionales>` | Value of Other Additional Taxes associated with the additional tax code.<br>Conditional on the taxpayer indicating that other additional taxes exist in the issued electronic consumer invoice. | 18 | NUM | a) Numeric value of 16 integers, two decimals; >0 (must be positive). | 2 |
| | END TABLE | ADDITIONAL TAXES | | | | |
| 28 | Total Amount<br>`<MontoTotal>` | Value of the sum of the fields Total Taxable Amount + Exempt amount + Total ITBIS + Additional tax amount, assigned to the electronic consumer invoice. | 18 | NUM | a) Numeric value of 16 integers, two decimals; ≥ 0 (Cannot be negative)<br>b) Value of the sum of Total Taxable Amount + Exempt Amount + Total ITBIS + Additional Tax Amount. | 1 |
| 29 | Non-Billable Amount<br>`<MontoNoFacturable>` | Corresponds to the total of the non-billable amount, assigned in the electronic consumer invoice.<br>Conditional on the taxpayer indicating that non-billable amount exists in the issued electronic consumer invoice. | 18 | NUM | a) Numeric value of 16 integers, two decimals. (Can be negative) | 2 |
| 30 | Period Amount<br>`<MontoPeriodo>` | Corresponds to the total of the period amount, assigned in the electronic consumer invoice. | 18 | NUM | a) Numeric value of 16 integers, two decimals. (Can be negative)<br>b) Period amount= Total Amount+Non-Billable Amount. | 3 |
| | END AREA | TOTALS | | | | |
| 31 | Consumer Invoice Security Code DOP$<250 M<br>`<CodigoSeguridadeCF>` | Corresponds to the first 6 characters of the Hash of the digital signature corresponding to the issued electronic consumer invoice, less than DOP$250 M. | 6 | ALFANUM | a) No validation | 1 |
| | END AREA | HEADER | | | | |

---

**¹** By XML definition, for each element there must be a container tag that groups the fields contained in a table. Example: in the case of `<TablaFormasPago>`, they are grouped within the `<FormaDePago>` tag for each `<FormaPago>` and `<MontoPago>` pair specified.

**³** If the 'Foreign Identifier' field is completed, the 'Buyer RNC' field must be blank.

**⁴** In fields where numeric values of 16 integers and 2 decimals exist, the rounding rule must be applied according to the e-CF Technical Report.

**⁵** See note 2.

**⁶** According to the 'Additional Tax Types Codification' Table, included in the e-CF Format document.

---

## B. DIGITAL SIGNATURE

| No. | Fields | Description | Max Length | Type | Validation | Obligatoriedad |
|-----|--------|-------------|------------|------|------------|----------------|
| | AREA `<Signature>` | SIGNATURE | | | | 1 |
| 1 | Digital Signature | Digital signature over the entire document. | | | | 1 |
| | END AREA | SIGNATURE | | | | |
