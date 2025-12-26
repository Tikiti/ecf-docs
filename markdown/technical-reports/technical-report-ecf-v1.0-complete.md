# Technical Report Electronic Fiscal Receipt

**Version 1.0**  
**Billing Department (Gerencia de Facturación)**  
**General Directorate of Internal Taxes (Dirección General de Impuestos Internos - DGII)**

---

## Changelog (Bitácora)

### Updates as of 16-03-2021

• Added to section 4. Communications and Web Service: RFCE Reception, Issuer-Receiver Communication, Service Status Query, and e-CF TrackId Query services.

• Limited the content of the different services indicated in section 4. Communications and Web Service to a general functional description and included reference to the technical description for more detail on the structure and operation of each service.

• Updated the example URL composing the electronic stamp (timbre) of an Electronic Consumer Invoice (**Factura de Consumo Electrónica**) less than DOP$250,000.

### Updates as of 17-08-2022

• Updated the additional tax calculation example for codes between 023-035 where the unit of measure is different from bulk (granel).

• Updated the additional tax calculation example for codes between 036-039.

• Updated the maximum limit of line items in e-CFs to a maximum of one thousand (1,000) lines.

• Excluded the term "Timbre Electrónico" in the reference document.

---

## Definitions

**Commercial Approval or Rejection (Aprobación o Rechazo Comercial):** the response issued by the Electronic Receiver regarding a received e-CF, informing both the electronic issuer of the e-CF and the DGII of their conformity or non-conformity, respectively, with the received document, which is sent via the Commercial Approval Web Service in the defined standard XML format.

**Acknowledgment of Receipt (Acuse de Recibo):** an automatic response indicating that the e-CF was received by the electronic receiver; this does not imply a positive or negative response regarding the commercial transaction.

**Digital Certificate (Certificado Digital):** a digital document issued and digitally signed by a certification authority that unequivocally identifies a subscriber during the certificate's validity period and constitutes proof that said subscriber is the source or originator of the content of a digital document or data message incorporating their associated certificate.

**Contingency (Contingencia):** the state defining exceptional situations that could prevent the normal course of the electronic invoicing cycle, for which specific actions are defined that model actors must follow in each situation.

**Digital Signature (Firma Digital):** understood as a numerical value adhered to a data message that, using a known mathematical procedure linked to the initiator's key and the message text, allows determining that this value has been obtained exclusively with the initiator's key and the message text, and that the initial message has not been modified after transmission.

**INDOTEL (Instituto Dominicano de las Telecomunicaciones):** regulatory body for telecommunications and electronic commerce, documents, and digital signatures, in accordance with Laws No. 153-98 on General Telecommunications and No. 126-02 on Electronic Commerce, Documents, and Digital Signatures of the Dominican Republic, respectively.

**Extensible Markup Language (XML - Lenguaje de Marcas Expansible):** a standard language structuring information exchange between different platforms, allowing document organization and tagging. Application fields include databases, text documents, spreadsheets, and web pages.

**Data Messages (Mensajes de Datos):** information generated, sent, received, stored, or communicated by electronic, optical, or similar means, such as Electronic Data Interchange (EDI), email, telegram, telex, or fax.

**Electronic Fiscal Receipt Number (e-NCF - Número de Comprobante Fiscal Electrónico):** alphanumeric sequence identifying an electronic fiscal receipt granted by the General Directorate of Internal Taxes (DGII).

**Virtual Office (OFV - Oficina Virtual):** a telematic space where taxpayers can execute tax procedures to facilitate and reduce compliance costs. It is located within the DGII portal, and access requires compliance with authentication mechanisms defined by the DGII.

**Trust Service Provider (Prestadora de servicios de confianza):** certification entity established in accordance with Law No. 126-02 and regulations issued by INDOTEL.

**Printed Representation of e-CF (RI - Representación Impresa de e-CF):** the printed paper version of the XML format of an e-CF, which will be delivered to non-electronic receivers so they can report their purchase transactions to the DGII, support fiscal credit, and preserve said documents as established by current legislation, as well as to those requiring it for selling goods involving transportation. For these purposes, it must contain all fields established as mandatory by Decree No. 254-06, according to the specifications of General Norm No. 06-2018.

**Signatory or Signer (Signatario o Firmante):** taxpayer acting on their own behalf or a person acting on their behalf, who, having previously obtained a digital certificate for tax use, has the capacity to sign a digital document and authenticate before the DGII to perform operations related to e-CFs.

**Web Service:** technology using a set of protocols and standards serving to exchange data between applications. Different software applications developed in different programming languages and executed on any platform can use web services to exchange data over networks like the Internet.

---

## 1. Introduction

The main purpose of this document is to inform taxpayers about the specific details they must know as they incorporate into the Electronic Fiscal Receipt (e-CF) issuance regime.

This Technical Report will allow such taxpayers to obtain the necessary guidelines for the correct implementation and use of e-CFs in the Dominican Republic.

## 2. System Actors

In the electronic invoicing system of the Dominican Republic, the following actors are identified:

- **General Directorate of Internal Taxes (DGII - Dirección General de Impuestos Internos):** as the entity empowered for the administration and application of taxes as established by articles 32, 34, and 35 of the Tax Code of the Dominican Republic (Law 11-92).

- **Electronic Issuer (Emisor electrónico):** any taxpayer authorized by the DGII to emit electronic fiscal receipts.

- **Electronic Receiver (Receptor electrónico):** any taxpayer who receives electronic fiscal receipts and is authorized by the DGII to emit them; that is, every electronic receiver is also an electronic issuer.

## 3. Issuer Authenticity and e-CF Integrity

The authenticity of the electronic issuer and the integrity of the remitted e-CFs are provided by:

- Use of digital certificates for digital signing and authentication in web services.
- Authentication in the OFV via linked username and access password.

The electronic issuer is absolutely responsible for their digital signature, which guarantees that the transaction is performed within an environment of security and trust between the interacting parties.

### Digital Certificate Standard

For e-CF issuance in the Dominican Republic, all electronic issuers must possess a digital certificate for tax processes¹, accredited by a trust service provider, issued digitally. This certificate will be used to validate the identity of the signatory operating on behalf of the taxpayer, delegate signing, authenticate web services, and digitally sign the XML file. It must comply with requirements established by INDOTEL and related regulations.

> ¹ Until INDOTEL regulations corresponding to these certificates are applied, physical person certificates accredited by a trust service provider may be used.

## 4. Communications and Web Service

The format of each electronic document used in the communications of the different web services is based on XML language, which follows a defined "XML schema" standard with a ".xsd" extension. These files consist of a specific format with tag names forming said electronic documents.

XML file communication will be performed via REST Web Service, for which the DGII will provide the following:

### 4.1. Web Service – Authentication (Autenticación)

Service responsible for validating the taxpayer's identity using a digital certificate on a seed file. Once validated, it provides a token used for consuming the remaining Electronic Invoicing services.

### 4.2. Web Service - e-CF Reception (Recepción e-CF)

Through this service, the electronic issuer sends the e-CF XML to the DGII, which receives it and returns a `TrackId`, with which the issuer can subsequently query the status of the sent document.

### 4.3. Web Service – RFCE Reception (Recepción RFCE)

Service responsible for receiving a summary containing the main information of an e-CF corresponding to an Electronic Consumer Invoice (**Factura de Consumo Electrónica**) with an amount less than RD$250,000.00. This invoice is not sent to DGII but must be fully preserved by the taxpayer for future processes.

### 4.4. Web Service - Commercial Approval Reception (Recepción de Aprobación Comercial)

This service is used by the electronic receiver to send the signed Commercial Approval or Rejection XML to the DGII, notifying their conformity with the received e-CF.

### 4.5. Web Service - e-CF Result Query (Consulta de Resultado de e-CF) - Issuers

Through this service, the electronic issuer can query the status of an e-CF using the `TrackId` delivered by the DGII via the e-CF reception service.

### 4.6. Web Service - e-CF Status Query (Consulta de Estado de e-CF) - Receivers

Service responding regarding the validity of an e-CF. To perform the query, the authenticated user must be delegated for the issuer or the receiver.

Through this service, e-CFs remitted via the consumer invoice summary reception service (amounts < RD$250,000.00) can also be queried.

### 4.7. Web Service - e-CF TrackId Query (Consulta de Trackid e-CF)

Service responsible for returning the collection of response numbers (`TrackId`) of an `e-NCF` that has been received by DGII and their statuses. To perform the query successfully, the authenticated user is required to be delegated for the issuer; otherwise, data cannot be obtained.

### 4.8. Web Service - Biller Directory Query (Consulta Directorio Facturadores)

This service is responsible for returning, exclusively in the production environment, a list of authorized electronic taxpayers and the URLs of their e-CF reception, commercial approval, and authentication (Optional) services. In the case of pre-certification, this service aims to provide test URLs enabled by DGII to simulate being another taxpayer, allowing authentication, receipt of vouchers, and/or commercial approvals.

### 4.9. Web Service - Service Status Query (Consulta Estatus Servicios)

Service responsible for providing the status and availability of electronic invoicing services, as well as their maintenance windows.

### 4.10. Web Service - e-NCF Annulment (Anulación de e-NCF)

Using this service and the e-NCF Annulment XML (ANECF), the electronic issuer can annul ranges of unused sequences or e-CFs that have been signed but not sent to the electronic receiver or the DGII.

### 4.11. Web Service - Issuer-Receiver Communication (Comunicación Emisor-Receptor)

Service exclusively available in the pre-certification environment, responsible for simulating being an issuer and/or receiver and allowing testing of operations that would occur in the production environment: authentication (Optional), receipt and issuance of vouchers, acknowledgments of receipt, and commercial approvals.

> For more detail on the structure and operation of these services in different environments, access the e-CF documentation, Technical Description of Electronic Invoicing, section Web Service Description.

## 5. e-CF Queries (Consultas de e-CF)

The validity and status of an e-CF can be queried through various channels available by Internal Taxes (DGII), detailed below:

### 5.1. Query on the DGII Web Page

In this query, the electronic receiver can verify the status of an e-CF by entering the issuer's RNC, the receiver's RNC, the document's e-NCF, and Security Code² (if applicable). This query will present the following response messages:

- **Fiscal Receipt Number entered is incorrect or does not correspond to this RNC:** when there is an error in the e-NCF sequence or it is not authorized for said RNC.

- **e-CF not found:** when the e-NCF sequence is authorized but no valid e-CF associated with the provided data is found.

- **Valid NCF:** when the e-NCF sequence is authorized for the entered RNC and an associated e-CF exists, one of the following statuses will be shown, as appropriate³:

  - **Accepted (Aceptado):** indicates that the e-CF received at DGII is valid for tax purposes.
  - **Rejected (Rechazado):** indicates that the e-CF received at DGII from the issuer is not valid for tax purposes.

> ² Corresponds to the first six (6) digits of the signature hash, found below the QR code in the printed representation of the e-CF.
> 
> ³ The statuses of e-CFs will be the same for both query services, whether e-CF sending or e-CF status.

### 5.2. Queries in the Virtual Office (OFV)

In the Virtual Office (**Oficina Virtual - OFV**), a menu corresponding to Electronic Invoicing is enabled where queries related to Electronic Fiscal Receipts (e-CF) can be made, among other actions:

- **Annulment Query (Consulta de Anulaciones).** This option allows searching for Annulled Electronic Fiscal Receipt Numbers by date ranges.

- **Issued e-NCF Query (Consulta e-NCF Emitidos).** This option allows searching for Electronic Fiscal Receipt Numbers emitted by e-NCF or date range; it contains the following search filters:
  - e-NCF
  - Receiver RNC (`RNC Receptor`)
  - e-NCF Type (`Tipo e-NCF`)
  - Status (`Estado`)
  - Commercial Approval (`Aprobación Comercial`)
  - Emission Date (`Fecha Emisión`)

- **Received e-NCF Query (Consulta e-NCF Recibidos).** This option allows the taxpayer (as electronic receiver) to search for Received Electronic Fiscal Receipt Numbers, entering the RNC of the third party who generated the e-NCF and a date range; it contains the following search filters:
  - Issuer RNC (`RNC Emisor`)
  - e-NCF Type (`Tipo e-NCF`)
  - Commercial Approval (`Aprobación Comercial`)
  - Emission Date: Range From-To (`Fecha Emisión: Rango de fecha Desde-Hasta`)

- **Electronic Directory Query (Consulta Directorio Electrónico).** This option allows the taxpayer to visualize all electronic billers with their respective URLs for communication purposes.

  This query, in addition to showing the general list of authorized electronic issuers, allows the taxpayer to filter by RNC or Company Name (`Razón Social`) of the electronic issuer they wish to query.

- **FE Directory Maintenance (Mantenimiento Directorio FE).** This option allows the taxpayer to add or modify URLs where they can receive Reception, Approval, and Authentication responses (optional). The latter is optional, as it would only be used if the issuer requires the receiver to authenticate to access their URLs.

  Fields to complete in this option:
  - e-CF Reception URL (`URL Recepción e-CF`)
  - Commercial Approval URL (`URL Aprobación Comercial`)
  - Authentication URL (Optional) (`URL Autenticación`)

### 5.3. Mobile App Queries

In this application, e-CF validity can be verified in two ways:

- **NCF Query (Consulta de NCF):** this option allows verifying or querying an e-CF by entering issuer RNC, e-NCF series, and e-NCF sequential part.⁴

- **Document Validation (Validación de Documentos):** this option allows reading QR codes. For an e-CF QR code, the query is performed using data from said e-CF's QR code.

Resulting statuses in both queries are:

- **Accepted (Aceptado):** indicates the e-CF received at DGII is valid for tax purposes.
- **Rejected (Rechazado):** indicates the e-CF was not received at DGII, so it is not valid for tax purposes.
- **Not found (No encontrado):** indicates the e-CF is not found as received at DGII.

> ⁴ Also allows querying non-electronic fiscal receipts.

## 6. Electronic Fiscal Receipts (e-CF)

### 6.1. Types of Electronic Fiscal Receipts (e-CF)

The Electronic Fiscal Receipt (e-CF) has equal validity and legal effects as the non-electronic fiscal receipt; however, they differ in that they are emitted electronically, maintain a standard format (XML), and are electronically signed, offering greater security and integrity to the document.

Likewise, electronic fiscal receipt types maintain the general characteristics established in Decree 254-06, Norm 06-18, and Norm 05-2019. Thus, they are equivalent to each type of non-electronic fiscal receipt; they are distinguished by being named with the term "electronic" and coded differently. The e-CF types are:

| Type | e-CF |
|------|------|
| 31 | Electronic Fiscal Credit Invoice (**Factura de Crédito Fiscal Electrónica**) |
| 32 | Electronic Consumer Invoice (**Factura de Consumo Electrónica**) |
| 33 | Electronic Debit Note (**Nota de Débito Electrónica**) |
| 34 | Electronic Credit Note (**Nota de Crédito Electrónica**) |
| 41 | Electronic Purchase Receipt (**Comprobante Electrónico de Compras**) |
| 43 | Electronic Minor Expenses Receipt (**Comprobante Electrónico para Gastos Menores**) |
| 44 | Electronic Special Regimes Receipt (**Comprobante Electrónico para Regímenes Especiales**) |
| 45 | Electronic Governmental Receipt (**Comprobante Electrónico Gubernamental**) |
| 46 | Electronic Export Receipt (**Comprobante Electrónico para Exportaciones**) |
| 47 | Electronic Foreign Payments Receipt (**Comprobante Electrónico para Pagos al Exterior**) |

- **Factura de Crédito Fiscal Electrónica (Electronic Fiscal Credit Invoice):** Electronic fiscal receipts registering commercial transactions of buying and selling goods and/or services, allowing the receiver or user requesting it to support expenses and costs or fiscal credit for tax effects.

- **Factura de Consumo Electrónica (Electronic Consumer Invoice)⁵:** Electronic fiscal receipts crediting the transfer of goods, delivery in use, or provision of services to final consumers.

- **Nota de Débito Electrónica (Electronic Debit Note):** Electronic receipts emitted by sellers of goods and/or service providers to recover costs and expenses, such as late interest, freight, or others incurred by the seller after fiscal receipt issuance.

- **Nota de Crédito Electrónica (Electronic Credit Note):** Electronic receipts emitted by sellers of goods and/or service providers for subsequent modifications in originally agreed sales conditions, i.e., to annul operations, effect returns, grant discounts and bonuses, fix errors, or similar cases.

- **Comprobante Electrónico de Compras (Electronic Purchase Receipt):** Electronic fiscal receipts emitted by physical and juridical persons when acquiring goods or services from persons not registered as taxpayers.

- **Comprobante Electrónico para Gastos Menores (Electronic Minor Expenses Receipt):** Electronic receipts emitted by physical or juridical persons to support payments made by their personnel, whether in Dominican territory or abroad, related to work activities, such as: consumables, fares, public transport, parking fees, and tolls.

- **Comprobante Electrónico para Regímenes Especiales (Electronic Special Regimes Receipt):** Electronic fiscal receipts used to bill transfers of goods or service provisions exempt from ITBIS and/or ISC to physical or juridical persons under special taxation regimes via special laws, contracts, or agreements ratified by the National Congress.

- **Comprobante Electrónico Gubernamental (Electronic Governmental Receipt):** Electronic fiscal receipts used to bill the sale of goods or service provisions to the Central Government, Decentralized and Autonomous Institutions, Social Security Institutions, and any government entity not performing commercial activity.

- **Comprobante Electrónico para Exportaciones (Electronic Export Receipt):** Electronic fiscal receipts used to report sales of goods outside national territory used by national exporters, free zone companies, and Commercial Free Zones.

- **Comprobante Electrónico para Pagos al Exterior (Electronic Foreign Payments Receipt):** Electronic fiscal receipts emitted for payment of Dominican-source taxed income to non-resident physical or juridical persons obligated to perform total Income Tax retention, pursuant to articles 297 and 305 of the Tax Code.

> ⁵ During the pilot, this receipt type will only be used in massive or batch billing operations (not retail) after other receipt types are tested.

## 7. Structure, Format, and Expiration of Electronic Fiscal Receipt Numbers (e-NCF)

The electronic fiscal receipt sequence has a structure of thirteen (13) alphanumeric positions.

**E 31 0000000001**

- **E**: Series
- **31**: Receipt Type
- **0000000001**: Sequence

The letter E corresponds to the e-CF series, the next two digits identify the e-CF type, and the last ten correspond to the sequential number. Said sequence will be valid from the authorization date until December 31 of the following year and cannot be used after expiration.

## 8. Operation Model

The e-CFs are emitted unitarily, in a standard XML format specified by the DGII and transmitted via a web service platform, requiring digital certificate use.

### Figure I. Electronic Issuer-Receiver Model

**Mandatory steps:** 1-4  
**Optional steps:** 5-6

The model works as follows:

1. The electronic issuer sends the e-CF to the DGII at the moment of document issuance.
2. The DGII responds delivering a `trackId`, which the e-CF issuer can use to query document status via the enabled web service.⁶
3. Then, the electronic issuer sends the e-CF to the electronic receiver.
4. The electronic receiver must acknowledge receipt (`Acuse de Recibo`) of the e-CF to the electronic issuer.
5. The electronic receiver can respond with their conformity to the electronic issuer via Commercial Approval or Rejection (`Aprobación o Rechazo Comercial`).⁷
6. If the receiver sends Commercial Approval or Rejection to the issuer, they will notify DGII of their response.

The e-CF will be validated by the DGII, delivering to the issuer via the e-CF sending web service one of the following statuses: "e-CF accepted" (`e-CF aceptado`), "e-CF conditionally accepted" (`e-CF aceptado condicional`), "e-CF rejected" (`e-CF rechazado`), or "e-CF in process" (`e-CF en proceso`).⁸

> ⁶ Web Service for e-CF Result Query.
> 
> ⁷ Only commercial approvals of e-CFs previously accepted by DGII will be received.
> 
> ⁸ See status description in section 4 for e-CF Sending Query Web Service.

### Figure II. Electronic Issuer - Non-Electronic Receiver Model

**Mandatory steps:** 1-3

When the issuer is electronic but the receiver is not - see figure II -, the model works as follows:

1. The issuer sends the e-CF to the DGII at the moment of document issuance.
2. The DGII responds delivering a `trackId`, which the e-CF issuer can use to query document status via the enabled web service.
3. Then, the electronic issuer delivers a printed representation (**RI**) of the e-CF to the non-electronic receiver.

The receiver must query document validity in the query available on the DGII web page and proceed to report the purchase in the Costs and Expenses Sending Format (Format 606), pursuant to General Norm No. 07-18 on Information Remission and its modifications.

## 9. Consumer Electronic Invoice less than DOP$250k

### 9.1. Operation Model

For emission of consumer electronic invoices less than DOP$250,000, specifications of the Electronic Fiscal Receipt (e-CF) Format must be met.⁹

### Figure III. Emission Model Consumer Electronic Invoice < DOP$250k

The model works as follows:

1. Once the consumer electronic invoice < DOP$250k is emitted, the issuer must save said invoice in their database and remit to Internal Taxes a summary of the electronic consumer invoice,¹⁰ which must comply with the established summary format.

2. Internal Taxes returns the validation response of the remitted electronic consumer summary format, with one of the following statuses:

   - **Accepted (Aceptado):** indicates the electronic consumer invoice summary format meets established specifications and is received by DGII.

   - **Rejected (Rechazado):** means the electronic consumer invoice summary format does not meet established specifications, implying the file is not received by DGII. Upon this status, the issuer must correct and remit the electronic consumer invoice summary again to Internal Taxes.

   - **Conditionally Accepted (Aceptado Condicional):** with this response, DGII indicates the electronic consumer invoice summary format is accepted; however, an irregularity exists that does not merit rejection but must be observed and corrected for future remissions.

3. Subsequently, delivers to the non-electronic receiver a Printed Representation of the consumer electronic invoice < DOP$250k.

The issuer must store and preserve the consumer invoice emitted to the non-electronic receiver electronically for a period of ten (10) years,¹¹ and additionally must make it available to the receiver for query purposes.

> ⁹ See Electronic Fiscal Receipt Format.
> 
> ¹⁰ The specifications the electronic consumer invoice summary must contain are established in the document 'Summary Format of Electronic Invoices less than DOP$250k'.
> 
> ¹¹ As established in Article 50, literal h of the Tax Code (Law 11-92).

## 10. Corrections and Annulment of an e-CF

Corrections of an e-CF will be performed solely using electronic credit or debit notes, as appropriate. If the electronic credit note is emitted after thirty (30) days from the tax obligation birth, returns of goods taxed with ITBIS may only entail restitution of the price paid, without including ITBIS return, as established by Arts. 8 and 28 of Regulation 293-11.

In cases where the invoice has been emitted (digitally signed) and not yet sent to DGII or the receiver, the e-CF can be annulled via the e-NCF Annulment Web Service using the e-NCF Annulment XML format (**ANECF**).¹² Electronic documents not yet signed can also be annulled through this service to annul unused sequences.

If the e-CF is rejected by the receiver in Commercial Approval, the electronic issuer must annul the invoice sending a credit note to both Internal Taxes and the receiver, indicating the annulment reason. However, if the e-CF is approved by the receiver in Commercial Approval but rejected by DGII, the e-CF will not be considered valid (nor will the Commercial Approval, which will also be rejected) and the issuer must create a new e-CF and replace the one delivered to the receiver.

> ¹² Details of the e-NCF Sequence Annulment Format are included in Annex IV.

## 11. e-CF XML Format

### 11.1. e-CF Content

The e-CF must contain specifications established in the following box:¹³

| Section | Description | Requirement | e-CF |
|---------|-------------|-------------|------|
| **A. Encabezado** (Header) | Corresponds to e-CF identification, containing issuer, receiver, and tax data. Contains areas: Document Identification, Issuer, Receiver, Additional Info, Transport, Totals, and Other Currency. | Mandatory | All |
| **B. Detalle de bienes o Servicios** (Item Details) | Corresponds to detail of goods or services. | Mandatory | All |
| **C. Subtotales Informativos** (Informative Subtotals) | Corresponds to informative subtotal. Fields in this section do not modify totalizer fields, nor increase or decrease tax base. | Optional | All |
| **D. Descuentos o Recargos** (Discounts or Surcharges) | Section used to specify global discounts or surcharges affecting e-CF total. | Conditional | All |
| **E. Paginación** (Pagination) | Indicates e-CF page quantity in Printed Representation and which items are on each. | Optional | All |
| **F. Información de Referencia** (Reference Information) | e-CFs modified or replaced with e-CF must be detailed here. | Mandatory/Conditional | Mandatory only for Electronic Credit/Debit Notes modifying a paper or electronic document. Conditional for rest when substituting NCF with e-CF (contingency cases). |
| **H. Fecha y Hora de la firma digital** (Digital Signature Date and Time) | Indicates date and time of digital signature. | Mandatory | All |
| **I. Firma Digital** (Digital Signature) | Corresponds to digital signature over all information in previous sections, guaranteeing e-CF integrity. | Mandatory | All |

> ¹³ Detail is found in the 'e-CF Format' document.

#### 11.1.1. Detail by Section

Each section content will contain format and obligatoriness codes according to e-CF type,¹⁴ being these:

- **0: Does not correspond.** Data must not be in a specific document.
- **1: Mandatory data.** Data must always be in the document, independent of transaction characteristics.
- **2: Conditional data.** Data not mandatory in all documents but may be in certain operations if a condition is met. Example: If discounts/surcharges exist affecting e-CF total, **Descuentos o Recargos** section must be included; otherwise, total amount will not balance.
- **3: Optional.** Data is optional.

> ¹⁴ Included in the 'e-CF Format'.

#### 11.1.2. Format Instructions for Sections¹⁵

- Amount values must be completed in Dominican Pesos (DOP), except fields corresponding to another currency.
- In numeric data, decimals are separated with a point (`.`).
- In numeric data, thousands are **not** separated.
- In `ALFANUM` information, the following characters must not be employed within XML as they have meaning by themselves and must be replaced by standard definitions:

| Name | Character | Decimal Reference | Hexadecimal Reference |
|------|-----------|-------------------|----------------------|
| quot | " | &#34; | &#x22; |
| amp | & | &#38; | &#x26; |
| apos | ' | &#39; | &#x27; |
| lt | < | &#60; | &#x3C; |
| gt | > | &#62; | &#x3E; |

> ¹⁵ Instructions apply to the rest of XML formats.

## 12. Tolerance Rule. Balancing (Cuadratura).

Since in every commercial transaction it is necessary that billed and paid values match, for e-CF XML format purposes, balancing is defined as the action ensuring values in total balances coincide.

In this sense, to facilitate balancing these balances in XML, a tolerance rule is admitted for each line of the **Detalle de Bienes o Servicios** (Item Details) section: a difference of ± 1 unit of `price * item quantity` in each line. Also, a global tolerance on e-CF total amount is defined, equivalent to total lines of the Detalle section.

This implies both line amounts in Detalle section and those in Header must coincide or approximate results subject to the indicated tolerance rule. If difference exceeds tolerance, e-CF will be conditionally accepted.

## 13. Rounding Rule

The rounding rule establishes that numeric value fields allow up to two (2) decimal digits,¹⁶ which may be rounded as follows:

The third decimal must round the second decimal, leaving figures with two fixed decimals. When third decimal value is < 5, maintain second decimal value. If >= 5, increment second decimal by one unit.

**Example 1: Third decimal < 5.**  
750.5212 ≈ 750.52

**Example 2: Third decimal >= 5.**  
750.5276 ≈ 750.53

> ¹⁶ Exceptions: `<PrecioUnitarioItem>` and `<PrecioUnitarioItemOtraMoneda>` in Detalle section allow up to four (4) decimal digits, including `<TipoCambio>` in Header (as established by Central Bank) and `<Subcantidad>` in Detalle (up to 3 decimals).

## 14. Selective Consumption Tax (ISC) on Alcohol and Cigarettes

For ISC calculation on Alcohol and Cigarette items, place in **Detalle de Bienes y Servicio** (Goods and Services Detail) the code attending to additional tax type specified in the Additional Tax Types Coding table (included in e-CF Format), then proceed to calculate per specifications in Header Totals area.

### ISC Alcohol (Specific Rate)

For specific ISC calculation for alcohol, the following fields must be taken into account:

`<MontoImpuestoSelectivoEspecifico> = <TasaImpuestoAdicional> x <GradosAlcohol> x <CantidadReferencia> x <Subcantidad> x <CantidadItem>`

### ISC Alcohol (Ad-Valorem Rate)

For Ad-Valorem ISC calculation for alcohol:

If tax code is between 023-035, verify item unit of measure. If bulk (granel - code 18), Ad-Valorem calculation increments unit price (list price equivalent) by 30% times item quantity times tax rate.

If tax code is between 023-035 and unit is NOT bulk, apply the corresponding formula according to document specifications.

### ISC Cigarettes (Specific Rate)

For specific ISC calculation for cigarettes, multiply item quantity by reference quantity by additional tax rate.

### ISC Cigarettes (Ad-Valorem Rate)

If tax code is between 036-039, apply the corresponding Ad-Valorem formula according to document specifications.

## 15. Other Additional Taxes

For additional taxes such as Legal Tip (**Propina Legal**), Telecommunications Development Contribution (**CDT**), General Insurance Services, Telecommunications Services, First Plate Issuance:

- If `<IndicadorMontoGravado>` = 0: `<MontoItem> x <TasaImpuestoAdicional>`
- If `<IndicadorMontoGravado>` = 1: `<OtrosImpuestosAdicionales> = <MontoItem> / (1+ ITBIS rate 1) x TasaImpuestoAdicional`

For **CDT** and **Telecommunications Services**, if `<IndicadorNorma1007>` in Descuentos/Recargos = 1, apply the corresponding formula considering Norm 10-07.

## 16. Treatment for e-CF with General Norm 07-07

Specifications for operations under General Norm 07-07 indicate that the operation must be divided into two items: one corresponding to the exempt part (90% of value) and another for the taxed part (10% of value).

## 17. e-CF Printed Representation (RI)

Mandatory minimum specifications must be presented in a Printed Representation (**RI**) of e-CF, as well as specific order and placement of information. If RI corresponds to an e-CF not received by DGII or rejected, it cannot be used to support fiscal credit.

e-CF information must be contained within RI to print with maximum 1,000 lines in **Detalle de Bienes o Servicios** section, except Consumer Electronic Invoices < DOP$250k (max 10,000 lines).

Printed Representation (RI) may be printed on multiple pages if required, provided it complies with pagination specifications indicated in both e-CF Format and this document.

### 17.1. Print Quality

Printed Representation print quality must ensure document legibility for at least ten (10) years, as established in literal f) of Article 44 of Law 11-92 Tax Code.

### 17.2. Order and Distribution of Information in e-CF Printed Representation

#### 17.2.1. Header (Encabezado)

Corresponds to e-CF identification, containing issuer, buyer,¹⁷ and tax data.

**A. Top right of header must contain:**

- **Electronic Fiscal Receipt Type (Tipo de Comprobante Fiscal Electrónico)**
- **e-NCF**
- **Expiration Date (Fecha Vencimiento)**
- **Modified e-NCF (e-NCF Modificado)** (applies to Debit and Credit Notes)
- **Modification Code (Código de Modificación)** (applies to Debit and Credit Notes)

| Modification Code (Código de Modificación) | Code Description (Descripción del Código) |
|---------------------------------------------|-------------------------------------------|
| 1 | Annuls modified NCF |
| 2 | Corrects Text of modified Fiscal Receipt |
| 3 | Corrects amounts of modified NCF |
| 4 | Replaces NCF emitted in contingency |

**B. Top left of header must contain issuer information:**

- Trade Name (if any)
- Name or Company Name (`Razón Social`)
- Branch (if applicable)
- National Taxpayer Registry Number (`RNC`)
- Address
- Municipality
- Province
- Emission Date

**C. Bottom left of header must contain client/recipient data:**

- Client Name or Company Name
- National Taxpayer Registry Number (if applicable)

> ¹⁷ For electronic consumer invoices when total amount is less than DOP$250k, Buyer RNC completion is optional.

#### 17.2.2. Central Part

Central part must contain data indicated below, per article 8 of Decree No. 254-06, General Norm 06-18, and according to good or service transacted.

**Transferred good/service data, transaction value, and tax data:**

- Quantity
- Billing Indicator (`Indicador de Facturación`)
- Description
- Unit of Measure (if applicable)
- Alcohol Degrees in % (if applicable)
- PVP (if applicable)
- Price
- Specific ISC (if applicable)
- Ad-Valorem ISC (if applicable)
- ITBIS (if applicable)
- Discount (if applicable)
- Surcharge (if applicable)
- Value
- Taxed Subtotal (if applicable)
- Exempt Subtotal (if applicable)
- Total ISC (if applicable)
- Total ITBIS (if applicable)
- CDT (if applicable)
- Legal Tip (if applicable)
- Total
- Discount or Surcharge Description (if applicable)
- Discount or Surcharge in % (if applicable)
- Discount or Surcharge Amount (if applicable)

#### 17.2.3. Additional Data for RI

**e-CF query information:**

- **QR Code (Código QR):** must be placed at **bottom left**¹⁸ of e-CF, maintain minimum distance of **two (2) centimeters** from sheet edge to where QR code starts, and have minimum size of **22 x 22 mm**, with **3mm margin** on its sides.

  QR code composition must contain the following parameters:¹⁹
  - `RncEmisor`
  - `RncComprador`
  - `ENCF`
  - `FechaEmision` (dd-MM-yyyy)
  - `MontoTotal`
  - `FechaFirma` (dd-MM-yyyy HH:mm:ss)
  - `CodigoSeguridad`: corresponds to first six (6) digits of hash generated in `SignatureValue` of e-CF digital signature.

  **Example URL:**  
  `https://ecf.dgii.gov.do/ecf/ConsultaTimbre?RncEmisor=XXXXXXXXXXX&RncComprador=XXXXXXXXXXXX&ENCF=XXXXXXXXXXXXX&FechaEmision=dd-MMyyyy&MontoTotal=XXXX.XX&FechaFirma=dd-MMyyyy%20HH:mm:ss&CodigoSeguridad=XXXXXX`

- **Security Code (Código de Seguridad):** First six (6) digits of `SignatureValue` hash in words, **below QR code**.

- **Digital Signature Date (Fecha de Firma Digital):** Format dd-MM-yyyy HH:mm:ss.

**Query information for Consumer Electronic Invoice < DOP$250k:**

For consumer electronic invoice < DOP$250k QR code, composition must contain:
- `RncEmisor`
- `ENCF`
- `MontoTotal`
- `CodigoSeguridad`

**Example URL:**  
`https://fc.dgii.gov.do/eCF/ConsultaTimbreFC?RncEmisor=XXXXXXXXXXX&ENCF=XXXXXXXXXXXXX&MontoTotal=XXXX.XX&CodigoSeguridad=XXXXXX`

> ¹⁸ Except for Handheld devices, can also be bottom center of final e-CF part.
> 
> ¹⁹ Consumer invoices < DOP$250k are excepted from these parameters.

### 17.3. Illustrative Models

- 17.3.1. Illustrative model with totals at invoice end.
- 17.3.2. Illustrative model including ITBIS in 'Value' field of goods/services detail.
- 17.3.3. Illustrative model including ITBIS in 'Value' field and totals in goods/services detail part.
- 17.3.4. Illustrative model of e-FCF via Continuous Paper.
- 17.3.5. Illustrative model of e-FCF for Selective Consumption Tax.
- 17.3.6. Illustrative model of Electronic Credit Note.
- 17.3.7. Illustrative model including Pagination (2-page e-CF).
- 17.3.8. Illustrative model of Electronic Consumer Invoice with total amount >= DOP$250k.
- 17.3.9. Illustrative model of Electronic Consumer Invoice with total amount < DOP$250k.
- 17.3.10. Illustrative model of Electronic Consumer Invoice < DOP$250k via Continuous Paper.

## 18. Contingency Operation

Contingency state is considered when the following conditions exist:

- **No connection:** If e-CF sending to Internal Taxes via web service is not possible due to no connection, e-CFs emitted must be sent when connection is restored.

- **Cannot emit e-CF:** When e-CF emission is not possible, Series B sequences will be available for use only in contingency. Once situation is solved, vouchers emitted as Series B must be replaced with corresponding Series E (e-CF), without sending to receiver, only to DGII.

**Contingency state notification**

Contingency state must be reported immediately. DGII will notify via enabled channels for these purposes. The issuer must report to DGII via contingency module available in Virtual Office (OFV) or contacting the Taxpayer Service Center.

### 18.1. Contingency Types

- **Total Contingency (Contingencia total):** system failure affecting taxpayer's total operation (e-CF emission). The taxpayer must indicate contingency start date and state reason. This state will be automatically deactivated when DGII receives first e-CF after contingency start date or when taxpayer notifies failure was solved, whichever comes first.

- **Partial Contingency (Contingencia parcial):** system failure affecting only part of taxpayer's operations, i.e., one or several branches or business units cannot electronically invoice but the rest continues operating normally, emitting electronic vouchers.

---

**End of document**
