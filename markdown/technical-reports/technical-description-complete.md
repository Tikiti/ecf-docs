# Technical Description of Electronic Invoicing

**Version 1.6**  
**June 2023**

**INFORMATION TECHNOLOGY AND COMMUNICATIONS MANAGEMENT (GERENCIA DE TECNOLOGIA DE LA INFORMACION Y COMUNICACIONES)**  
**Dominican Republic (República Dominicana)**

---

## Table of Contents (Índice)

- Changelog (Bitácora)
- Purpose (Propósito)
- Electronic Invoicing Tax Authority (Facturación Electrónica Autoridad Tributaria)
  - Standard Communication Language (Lenguaje Estándar de Comunicación)
  - Environment Description (Descripción de Ambientes)
  - Web Services Description (Descripción de Servicios Web)
- Issuer-Receiver Communication Standard (Estándar de Comunicación Emisor-Receptor)
  - General Requirements (Requerimientos Generales)
  - Service Creation and Parameterization (Creación y Parametrización De Servicios)
  - Content and/or Character Restrictions in XML (Restricciones de Contenido y/o Caracteres en los XML)
  - XML File Naming Format (Formato de Nombre de los Archivos XML)
  - XML Signing (Firmado de XML)
  - Recommendations (Recomendaciones)

---

## Changelog (Bitácora)

### Updates as of 12-06-2023

1. A new invoice summary query service was added that allows querying a specific receipt given an RNC, ENCF, and security code to view its status.

### Updates as of 18-05-2023

1. A new endpoint was added to the directory query service that allows filtering by a specific RNC.

2. Descriptions of output parameters for Internal Taxes services were added.

3. New points were added to the general requirements of the issuer-receiver communication standard:
   - Services not sensitive to uppercase and lowercase.
   - Use of traditional network ports.

4. Two parameters "encf" and "secuenciaUtilizada" were included in the response of the electronic consumer invoice summary Reception service to provide feedback when the electronic fiscal receipt number (eNCF) can be reused.

5. The availability status of pre-certification environment services was included in the status service ObtenerEstatus endpoint.

6. A reference to the universal date format to be used in the issuance and expiration date parameters of the token returned by the authentication service was added.

### Updates as of 18-04-2022

1. Two parameters were included in the Result Query service response to provide feedback when the electronic fiscal receipt number (eNCF) can be reused.

2. The standard for character encoding format is specified.

3. The standard for file naming of all formats is specified.

4. The validity period of submissions made in the pre-certification environment is updated.

### Updates as of 28-12-2021

1. The expiration date of sequences enabled for taxpayers for testing purposes in the pre-certification environment was updated.

### Updates as of 01-03-2021

1. Two new endpoints were added to the Issuer/Receiver service in the test environment to receive commercial approvals and authenticate.

2. The description of the directory query service was modified to highlight its functionality according to the interaction environment.

### Updates as of 28-12-2020

1. The subsection name was modified from 'Character Restrictions' to 'Content and/or Character Restrictions' and the requirement not to include empty tags in XMLs was added.

2. The URLs for the range annulment, status query, trackids query, and directory query services were removed for the certification environment as they are not yet available to the public.

3. The URL of the Issuer Receiver service in the test environment was completed, adding the '/help/index.html' resources at the end.

### Updates as of 02-10-2020

1. A trailing slash was added as a reference at the end of the swagger URL for the Consumer Invoice (FC) Reception service.

2. The URL of the Consumer Invoice (FC) Reception service for the certification environment was removed as it is not yet available to the public.

3. The format to be used for file names (XML) was specified in both the reception service description and the electronic invoicing standard.

4. Points to consider regarding e-CF signing in general requirements were added, as well as recommendations for these purposes.

5. The authentication URL parameter was added to the receipt submission service in pre-certification.

6. A table with character restrictions regarding the security code of QR codes was added for proper URL composition use.

7. The new Issuer-Receiver service was added with the description and structure of the following endpoints for interaction:
   - EmisionComprobantes
   - Consulta de acuse de recibo
   - RecepcioneCF

8. The consumer electronic invoice summary domain structure was added to the base URLs.

### Updates as of 30-04-2020

1. The URLs for the consumer electronic invoice summary reception service and the query stamp service for said consumer electronic invoices were modified due to a domain change.

### Updates as of 22-04-2020

1. Reference to important information about the pre-certification environment was added in the environment description section.

2. The description and structure of the new trackids query service was added to the web services description section.

---

## Purpose (Propósito)

The purpose of this document is to describe in general terms the technical aspects that make up the tax electronic invoicing system of the General Directorate of Internal Taxes (**Dirección General de Impuestos Internos - DGII**), as well as specifically, the necessary requirements to be made available by taxpayers to enter this modality and communicate correctly with the tax authority and other electronic taxpayers.

---

## Electronic Invoicing Tax Authority (Facturación Electrónica Autoridad Tributaria)

When talking about Electronic Invoicing, it refers to the business modality that uses electronic fiscal receipts (**comprobantes fiscales electrónicos**). In this sense, this section details the technical aspects of the General Directorate of Internal Taxes (DGII) such as the communication language, environments, and existing web services.

### Standard Communication Language (Lenguaje Estándar de Comunicación)

For information exchange, the Extensible Markup Language (XML) has been established, a standard that through web services allows information exchange between heterogeneous platforms.

For each operation to be performed in Electronic Invoicing, the tax authority has a pre-established format on the portal to describe the data and validations that these operations contemplate, in addition to an XSD as a structural reference for said XMLs.

Each format has a tag (label) by which it is recognized, detailed below:

| XML Format (Formato XML) | Parent Tag (Mandatory) (Etiqueta Madre - Obligatoria) |
|--------------------------|-------------------------------------------------------|
| e-CF Format (Formato e-CF) | ECF |
| Commercial Approval Format (Formato Aprobación Comercial) | ACECF |
| Acknowledgment of Receipt Format (Formato Acuse de recibo) | ARECF |
| e-NCF Sequence Annulment Format (Formato Anulación de secuencias e-NCF) | ANECF |
| Consumer Invoice Summary Format (32 < 250,000.00) (Formato de Resumen Factura de Consumo) | RFCE |

### Environment Description (Descripción de Ambientes)

In Electronic Invoicing, an environment is a setting that allows taxpayers to interact with the Tax Authority's services in different contexts, currently having the following:

**Pre-Certification (Pre-Certificación):** publishes services so that taxpayers can perform system adaptation and integration tests, storing submissions for a period of 60 days.

Every taxpayer enabled in this environment has by receipt type a sequence range from 1 to 10,000,000, except for electronic consumer invoices (32) which have a range from 1 to 50,000,000.

The expiration date of these sequences corresponds to 31-12-2025, except for electronic consumer invoices (32) and electronic credit notes (34) which have no sequence expiration date.

**Certification (Certificación):** environment whose objective is to validate capabilities by the taxpayer's system prior to its productive incorporation into the tax electronic invoicing system, requiring the exhaustion of a set of tests that require the use of web services.

**Production (Producción):** productive environment where all submissions and operations have fiscal validity.

```
                    Pre-Certification (Pre-Certificación)


                       Environments (Ambientes)


                Production (Producción)            Certification (Certificación)


                   Environment Illustration (Ilustración de Ambientes)
```

In each base URL of the different environments, the Swagger (OpenAPI) document can be found which specifies the list of available resources in the REST API and the operations (Methods) that can be invoked on each of them, with their parameters and possible responses.

Below, you can identify the defined structure for communication or invocation of electronic invoicing services according to the environment:

**TesteCF:** Pre-certification environment, example:
- `https://ecf.dgii.gov.do/testecf/nombredelservicio/help/index.html`
- `https://fc.dgii.gov.do/testecf/nombredelservicio/help/index.html`

**CerteCF:** Certification environment, example:
- `https://ecf.dgii.gov.do/certecf/nombredelservicio/help/index.html`
- `https://fc.dgii.gov.do/certecf/nombredelservicio/help/index.html`

**eCF:** Production environment, example:
- `https://ecf.dgii.gov.do/ecf/nombredelservicio/help/index.html`
- `https://fc.dgii.gov.do/ecf/nombredelservicio/help/index.html`

*Structure of services and environments of electronic invoicing of the General Directorate of Internal Taxes (DGII), for more detail refer to the Web Services Description section.*

---

## Web Services Description (Descripción de Servicios Web)

Web services are a set of protocols and standards that in this case through the use of Extensible Markup Language (XML) and REST API, allow data exchange between heterogeneous invoicing software of taxpayers and the tax authority through an environment defined as {Ambiente}, finding the following services in electronic invoicing:

### Authentication (Autenticación)

Web service responsible for generating a session for the taxpayer, validating their identity through the use of a digital certificate on a file (Seed - Semilla) that will be obtained from a request and which must be sent signed to receive a token with a determined duration (1 hour at the moment).

With the delivery of said token, the taxpayer can use the remaining electronic invoicing services, specifying it as an authorization header in requests (Authorization: Bearer {token}).

#### Service URLs

- **TesteCF:** Pre-certification environment:  
  `https://ecf.dgii.gov.do/testecf/autenticacion`

- **CerteCF:** Certification environment:  
  `https://ecf.dgii.gov.do/certecf/autenticacion`

- **eCF:** Production environment:  
  `https://ecf.dgii.gov.do/ecf/autenticacion`

#### Methods and Parameters

Within the URL, the following two (2) resources (Endpoints) will be found:

##### GET SEED FILE (OBTENER ARCHIVO SEMILLA)

| Field | Description |
|-------|-------------|
| **DESCRIPTION** | Returns the seed file (in XML format) that will allow obtaining the token. |
| **METHOD** | GET |
| **RESOURCE (ENDPOINT)** | `/api/autenticacion/semilla` |
| **REQUEST URL** | `https://eCF.dgii.gov.do/{ambiente}/autenticacion/api/autenticacion/semilla` |
| **CURL EXAMPLE** | `curl -X 'GET' \`<br>`'https://ecf.dgii.gov.do/testecf/autenticacion/api/autenticacion/semilla' \`<br>`-H 'accept: */*' \` |
| **INPUT** | Input parameters<br>N/A |
| **OUTPUT** | Response in XML format<br>`<?xml version="1.0" encoding="utf-8"?>`<br>`<SemillaModel xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">`<br>`<valor>0000000-0000-0000-0000-000000000000</valor>`<br>`<fecha>2019-03-13T14:33:32.8617792-04:00</fecha>`<br>`</SemillaModel>` |
| **OUTPUT PARAMETER DESCRIPTION** | - **Valor:** seed value, sequence of encrypted characters.<br>- **Fecha:** date and time when the seed file was generated. |

##### FILE VALIDATION: VALIDATE SEED (VALIDACIÓN DE ARCHIVO: VALIDAR SEMILLA)

| Field | Description |
|-------|-------------|
| **DESCRIPTION** | Allows sending the signed file (Seed) and returns an object containing an authentication string (token) associated with an issuance date and an expiration date of the received token. |
| **METHOD** | POST |
| **RESOURCE (ENDPOINT)** | `/api/autenticacion/validarsemilla` |
| **REQUEST URL** | `https://ecf.dgii.gov.do/{ambiente}/autenticacion/api/autenticacion/validarsemilla` |
| **CURL EXAMPLE** | `curl -X 'POST' \`<br>`'https://ecf.dgii.gov.do/testecf/autenticacion/api/autenticacion/validarsemilla' \`<br>`-H 'accept: application/json' \`<br>`-H 'Content-Type: multipart/form-data' \`<br>`-F 'xml=@response_1659304894166.xml;type=text/xml'` |
| **INPUT** | Input parameters<br>`xml*` |
| **OUTPUT FORMATS** | **Response in JSON format**<br>`{`<br>`"token": "string",`<br>`"expira": "yyyy-MM-ddTHH:mm:ssZ",`<br>`"expedido": "yyyy-MM-ddTHH:mm:ssZ"`<br>`}`<br><br>**Response in XML format**<br>`<?xml version="1.0" encoding="UTF-8"?>`<br>`<RespuestaAutenticacion>`<br>`<token>string</token>`<br>`<expira>yyyy-MM-ddTHH:mm:ssZ</expira>`<br>`<expedido>yyyy-MM-ddTHH:mm:ssZ</expedido>`<br>`</RespuestaAutenticacion>` |
| **OUTPUT PARAMETER DESCRIPTION** | - **Token:** value issued by Internal Taxes as a security key to use Electronic Invoicing services.<br>- **Expira:** date and time when the received token expires.<br>- **Expedido:** date and time when the token was received. |

See RFC 6750 (https://tools.ietf.org/html/rfc6750) for more information about token authentication.

---

### e-CF Reception (Recepción de e-CF)

Web service responsible for receiving a tentative e-CF (digitally signed XML) and a token associated with a valid session and in response returning an object containing a string called TrackId as an acknowledgment of receipt, with which the taxpayer can query the status of its validation.

Receipt of the TrackId and having received a satisfactory validation status enables the issuer to send the e-CF to the receiver and if the receiver is not electronic, delivery of the corresponding printed representation.

Electronic Consumer Invoices (**Facturas de Consumo Electrónica**) with an amount less than RD$250,000.00 will not be received by this service; a summary of it must be sent to the e-CF consumer invoice summary reception service.

Additionally, XMLs representing e-CFs must comply with the File Name Format specified in the "Issuer-Receiver Communication Standard" section.

#### Service URLs

- **TesteCF:** Pre-certification environment:  
  `https://ecf.dgii.gov.do/testecf/recepcion`

- **CerteCF:** Certification environment:  
  `https://ecf.dgii.gov.do/certecf/recepcion`

- **eCF:** Production environment:  
  `https://ecf.dgii.gov.do/ecf/recepcion`

#### METHODS AND PARAMETERS

| Field | Description |
|-------|-------------|
| **METHOD** | POST |
| **RESOURCE (ENDPOINT)** | `/api/facturaselectronicas` |
| **REQUEST URL** | `https://ecf.dgii.gov.do/{ambiente}/recepcion/api/facturaselectronicas` |
| **CURL EXAMPLE** | `curl -X 'POST' \`<br>`'https://ecf.dgii.gov.do/testecf/recepcion/api/facturaselectronicas' \`<br>`-H 'accept: application/json' \`<br>`-H 'Authorization: bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...' \`<br>`-H 'Content-Type: multipart/form-data' \`<br>`-F 'xml=@response_1659304894166.xml;type=text/xml'` |
| **INPUT** | Input parameters<br>`xml*` |
| **OUTPUT FORMATS** | **Response in JSON format**<br>`{`<br>`"trackId": "string",`<br>`"error": "string",`<br>`"mensaje": "string"`<br>`}`<br><br>**Response in XML format**<br>`<?xml version="1.0" encoding="UTF-8"?>`<br>`<RespuestaRecepcion>`<br>`<trackId>string</trackId>`<br>`<error>string</error>`<br>`<mensaje>string</mensaje>`<br>`</RespuestaRecepcion>` |
| **OUTPUT PARAMETER DESCRIPTION** | - **Trackid:** unique number generated by Internal Taxes for a received e-CF.<br>- **Error:** reason for received error message (If applicable).<br>- **Mensaje:** message associated with an error received when attempting to send an e-CF (If applicable). |

---

### Consumer Invoice Summary Reception (Recepción de resumen factura de consumo e-CF)

Web service responsible for receiving a summary containing the main information of the e-CF corresponding to Electronic Consumer Invoices (**Facturas de Consumo Electrónica**) with an amount less than RD$250,000.00 (digitally signed XML) and a token associated with a valid session and in response returning Accepted in case of successful reception and processing, Conditionally Accepted if it did not comply at some point but did not merit rejection, or otherwise Rejected.

Although we will be receiving a summary, the taxpayer must preserve the extended e-CF corresponding to the Electronic Consumer Invoice for future processes where required.

e-CFs corresponding to Electronic Consumer Invoices with an amount greater than or equal to RD$250,000.00 must be submitted in their entirety (all information corresponding to this e-CF) through the e-CF Reception service.

Additionally, XMLs representing these summaries must comply with the File Name Format specified in the "Issuer-Receiver Communication Standard" section.

#### Service URLs

- **TesteCF:** Pre-certification environment:  
  `https://fc.dgii.gov.do/testecf/recepcionfc/`

- **eCF:** Production environment:  
  `https://fc.dgii.gov.do/ecf/recepcionfc/`

#### METHODS AND PARAMETERS

| Field | Description |
|-------|-------------|
| **METHOD** | POST |
| **RESOURCE (ENDPOINT)** | `/api/recepcion/ecf` |
| **REQUEST URL** | `https://fc.dgii.gov.do/{ambiente}/recepcionfc/api/recepcion/ecf` |
| **CURL EXAMPLE** | `curl -X POST`<br>`"https://fc.dgii.gov.do/testecf/recepcionfc/api/recepcion/ecf"`<br>`-H "accept: application/json"`<br>`-H "Authorization: bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."`<br>`-H "Content-Type: multipart/form-data"`<br>`-F "xml=@response_1659306932058_180702.xml;type=text/xml"` |
| **INPUT** | Input parameters<br>`xml*` |
| **OUTPUT FORMATS** | **Response in JSON format**<br>`{`<br>`"codigo": 1,`<br>`"estado": "string",`<br>`"mensajes": [`<br>`{`<br>`"codigo": "string",`<br>`"valor": "string"`<br>`}`<br>`],`<br>`"encf": "string",`<br>`"secuenciaUtilizada": true`<br>`}`<br><br>**Response in XML format**<br>`<?xml version="1.0" encoding="UTF-8"?>`<br>`<Respuesta>`<br>`<codigo>1</codigo>`<br>`<estado>string</estado>`<br>`<mensajes>`<br>`<codigo>string</codigo>`<br>`<valor>string</valor>`<br>`</mensajes>`<br>`<encf>string</encf>`<br>`<secuenciaUtilizada>true</secuenciaUtilizada>`<br>`</Respuesta>` |

**OUTPUT PARAMETER DESCRIPTION:**

- **Codigo:** code associated with the validation status of the received consumer invoice summary.
- **Estado:** validation status granted by Internal Taxes to the received consumer invoice summary.
- **Mensajes:** messages and codes associated with the validation status of the received consumer invoice summary.
- **Encf:** sequence number used by the taxpayer in the consumer invoice summary.
- **SecuenciaUtilizada:** allows indicating whether the sequence number received by Internal Taxes can be reused in another Consumer Invoice Summary in the scenario that the validation result was "Rejected" for the following reasons:

  - Invalid certificate and/or signature.
  - Receipt structure (XML) is not valid.
  - Electronic fiscal receipt signer does not correspond to an authorized delegate to make transactions for the Issuer RNC.
  - The e-NCF is not authorized for the Issuer RNC of the electronic fiscal receipt.
  - The authorized e-NCF is expired as of the electronic fiscal receipt submission date.
  - The Issuer RNC of the receipt does not correspond to an electronic issuer.
  - The Issuer RNC does not exist.
  - The Issuer RNC is not active.

  Possible parameter values:
  - **True** = Sequence cannot be reused.
  - **False** = Sequence can be reused.

---

### Invoice Summary Query - RFCE (Consulta de Resumen de Factura)

Web service responsible for responding to the validity or status of an ENCF to a receiver or even an issuer, through presentation of issuer RNC, e-NCF, and security code.

To perform queries of the previously described data, the authenticated user is required to be delegated for the issuer.

Through this service, e-CFs submitted via the consumer invoice summary reception service (amounts < RD$250,000.00) can also be queried.

#### Service URLs

- **eCF:** Production environment:  
  `https://fc.dgii.gov.do/ecf/consultarfce`

#### METHODS AND PARAMETERS

| Field | Description |
|-------|-------------|
| **METHOD** | GET |
| **RESOURCE (ENDPOINT)** | `/api/Consultas/Consulta` |
| **REQUEST URL** | `https://fc.dgii.gov.do/ecf/consultarfce/api/Consultas/Consulta?RNC_Emisor=111111111&ENCF=E320000000000&Cod_Seguridad_eCF=XXXXXX` |
| **CURL EXAMPLE** | `curl -X 'GET' \`<br>`'https://fc.dgii.gov.do/ecf/consultarfce/api/Consultas/Consulta?RNC_Emisor=111111111&ENCF=E320000000000&Cod_Seguridad_eCF=XXXXXX' \`<br>`-H 'accept: application/json' \`<br>`-H 'Authorization: bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...'` |
| **INPUT** | Input parameters<br>`RncEmisor*`<br>`ENCF*`<br>`CodigoSeguridad*` |
| **OUTPUT FORMATS** | **Response in JSON format**<br>`{`<br>`"rnc": "string",`<br>`"encf": "string",`<br>`"secuenciaUtilizada": true,`<br>`"codigo": "string",`<br>`"estado": "string",`<br>`"mensajes": [`<br>`{`<br>`"valor": "string",`<br>`"codigo": 0`<br>`}`<br>`]`<br>`}` |

**OUTPUT PARAMETER DESCRIPTION:**

- **Codigo:** code associated with the validation status of the received e-CF.
- **Estado:** validation status granted by Internal Taxes to the received e-CF.
- **RncEmisor:** national registry number of the taxpayer who sent the e-CF.
- **NcfElectronico:** sequence number used by the taxpayer in the ENCF.
- **CodigoSeguridad:** extracted from the first six (6) digits of the hash generated in the SignatureValue of the digital signature found in the CodigoSeguridadeCF tag of the invoice summary.

**OUTPUT STATUSES:**

- **Not found (0):** implies the receipt was not found in records, possibly because it has not yet been reported.
- **Accepted (1):** implies the e-CF generated by the issuer was accepted and has fiscal validity.
- **Rejected (2):** corresponds to nullity of the receipt generated by the issuer.

**Note:** in addition to the above statuses, the service allows viewing receipts whose status is 'Conditionally Accepted' exclusively for Electronic Consumer Invoices with an amount less than RD$250,000.00.

---

### e-CF Result Query (Consulta de resultado e-CF)

Web service responsible for returning the processing status or validity of the tentative e-CF sent exclusively through the e-CF reception web service, through presentation of a Trackid and a token associated with a valid session.

#### Service URLs

- **TesteCF:** Pre-certification environment:  
  `https://eCF.dgii.gov.do/testecf/consultaresultado`

- **CerteCF:** Certification environment:  
  `https://eCF.dgii.gov.do/certecf/consultaresultado`

- **eCF:** Production environment:  
  `https://eCF.dgii.gov.do/ecf/consultaresultado`

#### METHODS AND PARAMETERS

| Field | Description |
|-------|-------------|
| **METHOD** | GET |
| **RESOURCE (ENDPOINT)** | `/api/consultas/estado` |
| **REQUEST URL** | `https://ecf.dgii.gov.do/{ambiente}/consultaresultado/api/consultas/estado?trackId=XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX` |
| **CURL EXAMPLE** | `curl -X 'GET' \`<br>`'https://ecf.dgii.gov.do/testecf/consultaresultado/api/consultas/estado?trackId=XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX' \`<br>`-H 'accept: application/json' \`<br>`-H 'Authorization: bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...'` |
| **INPUT** | Input parameters<br>`trackId*` |
| **OUTPUT FORMATS** | **Response in JSON format**<br>`{`<br>`"codigo": "string",`<br>`"estado": "string",`<br>`"mensaje": "string",`<br>`"encf": "string",`<br>`"secuenciaUtilizada": true`<br>`}`<br><br>**Response in XML format**<br>`<?xml version="1.0" encoding="UTF-8"?>`<br>`<RespuestaConsulta>`<br>`<codigo>string</codigo>`<br>`<estado>string</estado>`<br>`<mensaje>string</mensaje>`<br>`<encf>string</encf>`<br>`<secuenciaUtilizada>true</secuenciaUtilizada>`<br>`</RespuestaConsulta>` |

**OUTPUT PARAMETER DESCRIPTION:**

- **Codigo:** code associated with the validation status of the received e-CF.
- **Estado:** validation status granted by Internal Taxes to the received e-CF.
- **Mensaje:** message associated with the validation status code of the received e-CF.
- **Encf:** sequence number used by the taxpayer in the e-CF.
- **SecuenciaUtilizada:** allows indicating whether the sequence number received by Internal Taxes can be reused in another e-CF (remember that the same e-CF can be sent more than once), in the scenario that the validation result was "Rejected" (for the same reasons established in the electronic consumer invoice summary Reception service).

**OUTPUT STATUSES:**

- **Not found (0):** implies the provided trackId was not found in records.
- **Accepted (1):** implies the e-CF generated by the issuer was accepted and has fiscal validity.
- **Rejected (2):** corresponds to nullity of the receipt generated by the issuer.
- **In process (3):** implies the receipt is under verification by Internal Taxes.
- **Conditionally Accepted (4):** implies the e-CF generated by the issuer meets established specifications however there are conditions that must be reviewed and corrected which during the validation process did not merit rejection.

---

### e-CF Status Query (Consulta estado e-CF)

Web service responsible for responding to the validity or status of an e-NCF to a receiver or even an issuer, through presentation of issuer RNC, buyer RNC (when applicable), e-NCF, and security code.

To perform queries of the previously described data, the authenticated user is required to be delegated for the issuer or receiver.

Through this service, e-CFs submitted via the consumer invoice summary reception service (amounts < RD$250,000.00) can also be queried.

#### Service URLs

- **TesteCF:** Pre-certification environment:  
  `https://eCF.dgii.gov.do/testecf/consultaestado`

- **CerteCF:** Certification environment:  
  `https://eCF.dgii.gov.do/certecf/consultaestado`

- **eCF:** Production environment:  
  `https://eCF.dgii.gov.do/ecf/consultaestado`

#### METHODS AND PARAMETERS

| Field | Description |
|-------|-------------|
| **METHOD** | GET |
| **RESOURCE (ENDPOINT)** | `/api/consultas/estado` |
| **REQUEST URL** | `https://ecf.dgii.gov.do/{ambiente}/consultaestado/api/consultas/estado?RncEmisor=111111111&NcfElectronico=E310000000001&RncComprador=222222222&CodigoSeguridad=XXXXXX` |
| **CURL EXAMPLE** | `curl -X 'GET' \`<br>`'https://ecf.dgii.gov.do/testecf/consultaestado/api/consultas/estado?RncEmisor=111111111&NcfElectronico=E310000000001&RncComprador=222222222&CodigoSeguridad=XXXXXX' \`<br>`-H 'accept: application/json' \`<br>`-H 'Authorization: bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...'` |
| **INPUT** | Input parameters<br>`RncEmisor*`<br>`NcfElectronico*`<br>`RncComprador`<br>`CodigoSeguridad*` |
| **OUTPUT FORMATS** | **Response in JSON format**<br>`{`<br>`"codigo": "string",`<br>`"estado": "string",`<br>`"mensaje": "string"`<br>`}`<br><br>**Response in XML format**<br>`<?xml version="1.0" encoding="UTF-8"?>`<br>`<RespuestaConsulta>`<br>`<codigo>string</codigo>`<br>`<estado>string</estado>`<br>`<mensaje>string</mensaje>`<br>`</RespuestaConsulta>` |

**OUTPUT PARAMETER DESCRIPTION:**

- **Codigo:** code associated with the validation status of the received e-CF.
- **Estado:** validation status granted by Internal Taxes to the received e-CF.
- **Mensaje:** message associated with the validation status code of the received e-CF.

**OUTPUT STATUSES:**

- **Not found (0):** implies the receipt was not found in records, possibly because it has not yet been reported.
- **Accepted (1):** implies the e-CF generated by the issuer was accepted and has fiscal validity.
- **Rejected (2):** corresponds to nullity of the receipt generated by the issuer.

**Note:** in addition to the above statuses, the service allows viewing receipts whose status is 'Conditionally Accepted' exclusively for Electronic Consumer Invoices with an amount less than RD$250,000.00.

---

### TrackIds Query (Consulta trackids)

Web service responsible for returning the collection of response numbers (trackId) of an e-NCF that has been received by DGII and their statuses.

To successfully perform the query, the authenticated user is required to be delegated for the issuer, otherwise data cannot be obtained.

#### Service URLs

- **TesteCF:** Pre-certification environment:  
  `https://eCF.dgii.gov.do/testecf/consultatrackids`

- **eCF:** Production environment:  
  `https://eCF.dgii.gov.do/ecf/consultatrackids`

#### METHODS AND PARAMETERS

| Field | Description |
|-------|-------------|
| **METHOD** | GET |
| **RESOURCE (ENDPOINT)** | `/api/trackids/consulta` |
| **REQUEST URL** | `https://ecf.dgii.gov.do/{ambiente}/consultatrackids/api/trackids/consulta?RncEmisor=111111111&ENCF=E310000000001` |
| **CURL EXAMPLE** | `curl -X 'GET' \`<br>`'https://ecf.dgii.gov.do/testecf/consultatrackids/api/trackids/consulta?RncEmisor=111111111&ENCF=E310000000001' \`<br>`-H 'accept: application/json' \`<br>`-H 'Authorization: bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...'` |
| **INPUT** | Input parameters<br>`RncEmisor*`<br>`ENCF*` |
| **OUTPUT FORMATS** | **Response in JSON format**<br>`{`<br>`"detalles": [`<br>`{`<br>`"trackId": "string",`<br>`"codigo": "string",`<br>`"estado": "string",`<br>`"mensaje": "string"`<br>`}`<br>`]`<br>`}`<br><br>**Response in XML format**<br>`<?xml version="1.0" encoding="UTF-8"?>`<br>`<RespuestaConsultaTrackIds>`<br>`<detalles>`<br>`<trackId>string</trackId>`<br>`<codigo>string</codigo>`<br>`<estado>string</estado>`<br>`<mensaje>string</mensaje>`<br>`</detalles>`<br>`</RespuestaConsultaTrackIds>` |

**OUTPUT PARAMETER DESCRIPTION:**

- **TrackId:** unique number generated by Internal Taxes for a received e-CF.
- **Codigo:** code associated with the validation status of the received e-CF.
- **Estado:** validation status granted by Internal Taxes to the received e-CF.
- **Mensaje:** message associated with the validation status code of the received e-CF.

---

### Directory Query (Consulta directorio)

Web service responsible for returning exclusively in the production environment a list of authorized electronic taxpayers and the URLs of their e-CF reception, commercial approval, and authentication (Optional) services.

In the case of pre-certification, this service aims to provide test URLs that were enabled by DGII to simulate being another taxpayer, equally allowing authentication, receiving receipts and/or commercial approvals.

#### Service URLs

- **TesteCF:** Pre-certification environment:  
  `https://eCF.dgii.gov.do/testecf/consultadirectorio`

- **eCF:** Production environment:  
  `https://eCF.dgii.gov.do/ecf/consultadirectorio`

#### METHODS AND PARAMETERS

**Endpoint 1: Complete listing**

| Field | Description |
|-------|-------------|
| **METHOD** | GET |
| **RESOURCE (ENDPOINT)** | `/api/consultas/listado` |
| **REQUEST URL** | `https://ecf.dgii.gov.do/{ambiente}/consultadirectorio/api/consultas/listado` |
| **CURL EXAMPLE** | `curl -X 'GET' \`<br>`'https://ecf.dgii.gov.do/testecf/consultadirectorio/api/consultas/listado' \`<br>`-H 'accept: application/json' \`<br>`-H 'Authorization: bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...'` |
| **INPUT** | N/A |
| **OUTPUT FORMATS** | **Response in JSON format**<br>`{`<br>`"contribuyentes": [`<br>`{`<br>`"rnc": "string",`<br>`"razonSocial": "string",`<br>`"urlRecepcion": "string",`<br>`"urlAceptacion": "string",`<br>`"urlOpcional": "string"`<br>`}`<br>`]`<br>`}` |

**Endpoint 2: Query by RNC**

| Field | Description |
|-------|-------------|
| **METHOD** | GET |
| **RESOURCE (ENDPOINT)** | `/api/consultas/rnc` |
| **REQUEST URL** | `https://ecf.dgii.gov.do/{ambiente}/consultadirectorio/api/consultas/rnc?rnc=111111111` |
| **CURL EXAMPLE** | `curl -X 'GET' \`<br>`'https://ecf.dgii.gov.do/testecf/consultadirectorio/api/consultas/rnc?rnc=111111111' \`<br>`-H 'accept: application/json' \`<br>`-H 'Authorization: bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...'` |
| **INPUT** | Input parameters<br>`rnc*` |
| **OUTPUT FORMATS** | **Response in JSON format**<br>`{`<br>`"rnc": "string",`<br>`"razonSocial": "string",`<br>`"urlRecepcion": "string",`<br>`"urlAceptacion": "string",`<br>`"urlOpcional": "string"`<br>`}` |

**OUTPUT PARAMETER DESCRIPTION:**

- **RNC:** taxpayer's national registry number.
- **RazonSocial:** taxpayer's name or business name.
- **UrlRecepcion:** URL of taxpayer's e-CF reception service.
- **UrlAceptacion:** URL of taxpayer's commercial approval service.
- **UrlOpcional:** URL of taxpayer's authentication service (optional).

---

### Services Status Query (Consulta estatus servicios)

Web service responsible for providing the status and availability of electronic invoicing services, as well as their maintenance windows.

#### Service URLs

- **TesteCF:** Pre-certification environment:  
  `https://eCF.dgii.gov.do/testecf/estatusservicios`

- **eCF:** Production environment:  
  `https://eCF.dgii.gov.do/ecf/estatusservicios`

#### METHODS AND PARAMETERS

| Field | Description |
|-------|-------------|
| **METHOD** | GET |
| **RESOURCE (ENDPOINT)** | `/api/consultas/estatus` |
| **REQUEST URL** | `https://ecf.dgii.gov.do/{ambiente}/estatusservicios/api/consultas/estatus` |
| **CURL EXAMPLE** | `curl -X 'GET' \`<br>`'https://ecf.dgii.gov.do/testecf/estatusservicios/api/consultas/estatus' \`<br>`-H 'accept: application/json'` |
| **INPUT** | N/A |
| **OUTPUT FORMATS** | **Response in JSON format**<br>`{`<br>`"servicios": [`<br>`{`<br>`"nombre": "string",`<br>`"estado": "string",`<br>`"mensaje": "string",`<br>`"mantenimiento": {`<br>`"fechaInicio": "yyyy-MM-ddTHH:mm:ssZ",`<br>`"fechaFin": "yyyy-MM-ddTHH:mm:ssZ"`<br>`}`<br>`}`<br>`]`<br>`}` |

**OUTPUT PARAMETER DESCRIPTION:**

- **Nombre:** service name.
- **Estado:** service status (Available, Not Available, Under Maintenance).
- **Mensaje:** descriptive status message.
- **Mantenimiento:** information about scheduled maintenance windows.

---

### Commercial Approval (Aprobación comercial)

Web service responsible for receiving an electronic commercial approval receipt (digitally signed XML) corresponding to acceptance or rejection by the electronic receiver of an e-CF previously received, and a token associated with a valid session.

Only those commercial approvals associated with e-CFs that have been previously validated and accepted by Internal Taxes are valid.

#### Service URLs

- **TesteCF:** Pre-certification environment:  
  `https://eCF.dgii.gov.do/testecf/aprobacioncomercial`

- **CerteCF:** Certification environment:  
  `https://eCF.dgii.gov.do/certecf/aprobacioncomercial`

- **eCF:** Production environment:  
  `https://eCF.dgii.gov.do/ecf/aprobacioncomercial`

#### METHODS AND PARAMETERS

| Field | Description |
|-------|-------------|
| **METHOD** | POST |
| **RESOURCE (ENDPOINT)** | `/api/aprobacioncomercial` |
| **REQUEST URL** | `https://ecf.dgii.gov.do/{ambiente}/aprobacioncomercial/api/aprobacioncomercial` |
| **CURL EXAMPLE** | `curl -X 'POST' \`<br>`'https://ecf.dgii.gov.do/testecf/aprobacioncomercial/api/aprobacioncomercial' \`<br>`-H 'accept: application/json' \`<br>`-H 'Authorization: bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...' \`<br>`-H 'Content-Type: multipart/form-data' \`<br>`-F 'xml=@aprobacion_comercial.xml;type=text/xml'` |
| **INPUT** | Input parameters<br>`xml*` |
| **OUTPUT FORMATS** | **Response in JSON format**<br>`{`<br>`"codigo": "string",`<br>`"estado": "string",`<br>`"mensaje": "string"`<br>`}`<br><br>**Response in XML format**<br>`<?xml version="1.0" encoding="UTF-8"?>`<br>`<RespuestaAprobacion>`<br>`<codigo>string</codigo>`<br>`<estado>string</estado>`<br>`<mensaje>string</mensaje>`<br>`</RespuestaAprobacion>` |

**OUTPUT PARAMETER DESCRIPTION:**

- **Codigo:** code associated with commercial approval reception status.
- **Estado:** reception status (Accepted, Rejected).
- **Mensaje:** descriptive result message.

---

### Range Annulment (Anulación rangos)

Web service responsible for receiving an electronic e-NCF range or sequence annulment receipt (digitally signed XML) and a token associated with a valid session.

Through this service, the following can be annulled:
- Unused sequence ranges
- e-CFs that have been signed but not sent (neither to DGII nor to receiver)

#### Service URLs

- **TesteCF:** Pre-certification environment:  
  `https://eCF.dgii.gov.do/testecf/anulacionrangos`

- **eCF:** Production environment:  
  `https://eCF.dgii.gov.do/ecf/anulacionrangos`

#### METHODS AND PARAMETERS

| Field | Description |
|-------|-------------|
| **METHOD** | POST |
| **RESOURCE (ENDPOINT)** | `/api/operaciones/anularrango` |
| **REQUEST URL** | `https://ecf.dgii.gov.do/{ambiente}/anulacionrangos/api/operaciones/anularrango` |
| **CURL EXAMPLE** | `curl -X 'POST' \`<br>`'https://ecf.dgii.gov.do/testecf/anulacionrangos/api/operaciones/anularrango' \`<br>`-H 'accept: application/json' \`<br>`-H 'Authorization: bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...' \`<br>`-H 'Content-Type: multipart/form-data' \`<br>`-F 'xml=@anulacion.xml;type=text/xml'` |
| **INPUT** | Input parameters<br>`xml*` |
| **OUTPUT FORMATS** | **Response in JSON format**<br>`{`<br>`"codigo": "string",`<br>`"estado": "string",`<br>`"mensaje": "string"`<br>`}`<br><br>**Response in XML format**<br>`<?xml version="1.0" encoding="UTF-8"?>`<br>`<RespuestaAnulacion>`<br>`<codigo>string</codigo>`<br>`<estado>string</estado>`<br>`<mensaje>string</mensaje>`<br>`</RespuestaAnulacion>` |

**OUTPUT PARAMETER DESCRIPTION:**

- **Codigo:** code associated with annulment status.
- **Estado:** process status (Accepted, Rejected).
- **Mensaje:** descriptive result message.

---

### Issuer-Receiver (P2P Communication) (Emisor-Receptor)

Service exclusively available in the pre-certification environment, responsible for simulating being an issuer and/or receiver before a taxpayer and based on this allowing them to test the operability they would have in the production environment for authentication (Optional), receipt reception and issuance, acknowledgments of receipt, and commercial approvals.

#### Service URLs

- **TesteCF:** Pre-certification environment:  
  `https://eCF.dgii.gov.do/testecf/emisorreceptor/help/index.html`

This service simulates the following P2P operations:

**1. Authentication (Optional)**
- Endpoint: `/api/autenticacion/semilla`
- Endpoint: `/api/autenticacion/validarsemilla`

**2. e-CF Reception**
- Endpoint: `/api/recepcionecf`
- Allows receiving test e-CFs from other taxpayers

**3. Acknowledgment of Receipt Query**
- Endpoint: `/api/consulta/acuse`
- Allows querying issued acknowledgments of receipt

**4. Commercial Approval Reception**
- Endpoint: `/api/aprobacioncomercial`
- Allows receiving commercial approvals/rejections

---

## Issuer-Receiver Communication Standard (Estándar de Comunicación Emisor-Receptor)

This section details the requirements that the electronic issuer must meet to communicate both with DGII and with other electronic taxpayers (receivers).

### General Requirements (Requerimientos Generales)

1. **REST web services implementation**
   - Electronic issuers/receivers must implement REST web services for:
     - e-CF reception
     - Commercial Approval reception
     - Authentication (optional)

2. **Response format**
   - Services must return responses in JSON or XML format
   - Appropriate HTTP status codes

3. **Security**
   - Mandatory use of HTTPS (TLS 1.2 or higher)
   - Digital certificate validation
   - JWT token authentication (optional for P2P)

4. **Case sensitivity**
   - Services must NOT be case-sensitive in parameters

5. **Network ports**
   - Use of traditional network ports (80 for HTTP, 443 for HTTPS)
   - Avoid non-standard ports to facilitate interoperability

6. **Timeout and retries**
   - Recommended timeout: 30 seconds
   - Implement retry logic with exponential backoff

### Service Creation and Parameterization (Creación y Parametrización De Servicios)

Electronic taxpayers must register their service URLs in the Virtual Office (OFV - Oficina Virtual) through the "FE Directory Maintenance" option.

**Fields to register:**
- **e-CF Reception URL**: Endpoint to receive e-CFs from other issuers
- **Commercial Approval URL**: Endpoint to receive commercial approvals
- **Authentication URL (Optional)**: Authentication endpoint if required

 **URL examples:**
```
https://mi-empresa.com.do/api/recepcion/ecf
https://mi-empresa.com.do/api/aprobacion-comercial
https://mi-empresa.com.do/api/autenticacion (optional)
```

### Content and/or Character Restrictions in XML (Restricciones de Contenido y/o Caracteres en los XML)

1. **Mandatory encoding**: UTF-8

2. **Empty tags**: Empty tags should not be included in XMLs. If an optional field has no value, it should be completely omitted.

   **Incorrect:**
   ```xml
   <DescripcionDescuento></DescripcionDescuento>
   ```
   
   **Correct:**
   ```xml
   <!-- Completely omit the tag -->
   ```

3. **Special characters**: Must be properly escaped:

| Character | XML Entity | Decimal | Hexadecimal |
|----------|-------------|---------|-------------|
| `<` | `&lt;` | `&#60;` | `&#x3C;` |
| `>` | `&gt;` | `&#62;` | `&#x3E;` |
| `&` | `&amp;` | `&#38;` | `&#x26;` |
| `"` | `&quot;` | `&#34;` | `&#x22;` |
| `'` | `&apos;` | `&#39;` | `&#x27;` |

4. **Security code in QR**: For URL composition in QR codes, security code characters must comply with URL-safe restrictions:

| Character | URL Encoding |
|----------|-----------------|
| Space | `%20` |
| `+` | `%2B` |
| `/` | `%2F` |
| `?` | `%3F` |
| `%` | `%25` |
| `#` | `%23` |
| `&` | `%26` |

### XML File Naming Format (Formato de Nombre de los Archivos XML)

XML files representing e-CFs and other electronic documents must strictly follow the following format:

**General format:**
```
[RNC][Serie][TipoComprobante][Secuencia].xml
```

**Components:**
- **RNC**: 11 digits of issuer's RNC
- **Serie**: 1 letter (E for electronic, B for contingency)
- **TipoComprobante**: 2 digits (31, 32, 33, 34, etc.)
- **Secuencia**: 10 digits of sequential number

**Examples:**
```
131880738E31000000001.xml    (Electronic Tax Credit Invoice - Factura de Crédito Fiscal Electrónica)
131880738E32000000001.xml    (Electronic Consumer Invoice - Factura de Consumo Electrónica)
131880738E34000000001.xml    (Electronic Credit Note - Nota de Crédito Electrónica)
```

**Formats for other documents:**

- **Commercial Approval (ACECF):**
  ```
  [RNC]ACECF[eNCFReferenciado].xml
  Example: 131880738ACECFE31000000001.xml
  ```

- **Acknowledgment of Receipt (ARECF):**
  ```
  [RNC]ARECF[eNCFReferenciado].xml
  Example: 131880738ARECFE31000000001.xml
  ```

- **Annulment (ANECF):**
  ```
  [RNC]ANECF[Timestamp].xml
  Example: 131880738ANECF20231226140500.xml
  ```

- **Consumer Invoice Summary (RFCE):**
  ```
  [RNC][Serie][TipoComprobante][Secuencia].xml
  Example: 131880738E32000000001.xml
  ```

### XML Signing (Firmado de XML)

**Mandatory standard**: XMLDSig (XML Digital Signature)

**Signing requirements:**

1. **Signature algorithm**: RSA-SHA256 or higher

2. **Digest algorithm**: SHA-256 or higher

3. **Digital certificate**:
   - Must be issued by a trust service provider accredited by INDOTEL
   - The **SubjectName (SN)** field of the certificate must contain the issuer's RNC
   - Validity current at time of signature

4. **Signature structure**:
   - Digital signature must be the last element of the XML
   - Must sign ALL prior content (all e-CF sections)
   - Use C14N canonicalization (Canonical XML)

5. **Signature validation**:
   - Signature CANNOT be modified after creation
   - Any change in XML (even spaces) invalidates signature
   - DGII validates signature at reception

**Critical points to consider:**

- **Whitespace**: Maintain consistency in spaces and line breaks before signing
- **Encoding**: Ensure UTF-8 without BOM (Byte Order Mark)
- **Immutability**: Once signed, XML CANNOT be modified
- **Timestamp**: Signature date/time must correspond to e-CF issuance date

### Recommendations (Recomendaciones)

1. **Local validation before submission**
   - Validate XML against XSD before signing
   - Verify totals balance
   - Confirm all mandatory fields are present

2. **Logging and auditing**
   - Maintain logs of all submissions and responses
   - Store copies of signed XMLs
   - Record received TrackIds

3. **Error handling**
   - Implement robust HTTP error handling
   - Properly process 4xx and 5xx status codes
   - Retry logic for temporary errors (503, 504)

4. **Performance**
   - Implement authentication token caching (valid 1 hour)
   - Use persistent HTTP connections (keep-alive)
   - Consider asynchronous processing for large volumes

5. **Preservation**
   - Preserve e-CFs and related documents for 10 years (Law 11-92, Art. 50)
   - Maintain in original electronic format
   - Regular fiscal database backup

6. **Exhaustive testing**
   - Test in pre-certification environment before certification
   - Validate all e-CF types (31, 32, 33, 34, etc.)
   - Test error and rejection cases
   - Simulate P2P communication with Issuer-Receiver service

---

**End of document**

**For more information:**
- DGII Portal: https://dgii.gov.do
- XML Formats: Available on the portal
