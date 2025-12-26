# Descripción Técnica de Facturación Electrónica

**Versión 1.6**  
**Junio 2023**

**GERENCIA DE TECNOLOGIA DE LA INFORMACION Y COMUNICACIONES**  
**República Dominicana**

---

## Índice

- Bitácora
- Propósito
- Facturación Electrónica Autoridad Tributaria
  - Lenguaje Estándar de Comunicación
  - Descripción de Ambientes
  - Descripción de Servicios Web
- Estándar de Comunicación Emisor-Receptor
  - Requerimientos Generales
  - Creación y Parametrización De Servicios
  - Restricciones de Contenido y/o Caracteres en los XML
  - Formato de Nombre de los Archivos XML
  - Firmado de XML
  - Recomendaciones

---

## Bitácora

### Actualizaciones al 12-06-2023

1. Se agregó un nuevo servicio de consulta de Resúmenes de factura que permite consultar dado un RNC, ENCF y Código de seguridad un comprobante en particular para ver el estado de este.

### Actualizaciones al 18-05-2023

1. Se agregó un nuevo endpoint al servicio de consulta directorio que permite filtrar por un RNC en particular.

2. Se agregaron descripciones de los parámetros de salida de los servicios de Impuestos Internos.

3. Se agregaron nuevos puntos a los requerimientos generales del estándar de comunicación emisor-receptor:
   - Servicios no sensitivos a mayúsculas y minúsculas.
   - Uso de puertos de red tradicionales.

4. Se incluyeron dos parámetros "encf" y "secuencia Utilizada" a la respuesta del servicio de Recepción del resumen de factura de consumo electrónica para retroalimentar cuando el número de comprobante fiscal electrónico (eNCF) puede ser reutilizado.

5. Se incluyó el estado de disponibilidad de los servicios del ambiente de precertificación en el servicio de estatus endpoint ObtenerEstatus.

6. Se agregó una referencia al formato de fecha universal que debe ser utilizado en los parámetros de fecha expedición y expiración del token retornado por el servicio de autenticación.

### Actualizaciones al 18-04-2022

1. Se incluyeron dos parámetros a la respuesta del servicio de Consulta Resultado para retroalimentar cuando el número del comprobante fiscal electrónico (eNCF) puede ser reutilizado.

2. Se especifica el estándar para el formato de codificación de caracteres.

3. Se especifica el estándar para el nombre de archivo de todos los formatos.

4. Se actualiza el periodo de vigencia de los envíos realizados en el ambiente de precertificación.

### Actualizaciones al 28-12-2021

1. Se actualizó la fecha de vencimiento de las secuencias habilitadas a los contribuyentes para fines de prueba en el ambiente de precertificación.

### Actualizaciones al 01-03-2021

1. Se agregaron dos nuevos endpoint al servicio de Emisor/Receptor del ambiente de pruebas para recibir aprobaciones comerciales y autenticarse.

2. Se modificó la descripción del servicio de consulta directorio para destacar la funcionalidad de este según el ambiente de interacción.

### Actualizaciones al 28-12-2020

1. Se modificó el nombre de la subsección 'Restricciones de caracteres' a 'Restricciones de contenido y/o caracteres' y se agregó en la misma él no incluir tags vacíos en los XML.

2. Se quitaron las URL del servicio de anulación rangos, consulta estado, consulta trackids y consulta directorio para el ambiente de certificación conforme a que en el mismo aún no se encuentran disponibles para el público.

3. Se completó la URL del servicio de Emisor Receptor del ambiente de pruebas, agregando al final de la misma los recursos '/help/index.html'.

### Actualizaciones al 02-10-2020

1. Se agregó a modo referencia una barra inclinada al final de la URL del swagger del servicio de Recepción de Facturas de Consumo (FC).

2. Se quitó la URL del servicio de Recepción de Facturas de Consumo (FC) para el ambiente de certificación conforme a que el mismo aún no se encuentra disponible para el público.

3. Se especificó tanto en la descripción del servicio de recepción como en el estándar de facturación electrónica, el formato que debe ser utilizado para el nombre de los archivos (XML).

4. Se agregaron puntos a tomar en cuenta con respecto al firmado de eCF en los requerimientos generales, así como recomendaciones a fines.

5. Se le agregó el parámetro de la URL de autenticación al servicio de Envío de comprobantes en pre-certificación.

6. Se agregó un cuadro con las restricciones de caracteres con respecto al código de seguridad de los QR conforme al uso apropiado para una composición de una URL.

7. Se agregó el nuevo servicio de Emisor-Receptor con la descripción y estructura de los siguientes endpoint para su interacción:
   - EmisionComprobantes
   - Consulta de acuse de recibo
   - RecepcioneCF

8. Se agrego a las URL base la estructura del dominio de los resúmenes de factura de consumo electrónica.

### Actualizaciones al 30-04-2020

1. Se modifican las URL del servicio de recepción del resumen de factura de consumo electrónica y el servicio de consulta timbre de dichas facturas de consumo electrónica conforme a un cambio de dominio.

### Actualizaciones al 22-04-2020

1. Se agregó referencia a informaciones importantes del ambiente de pre-certificación en el acápite de descripción de ambientes.

2. Se agregó la descripción y estructura del nuevo servicio de consulta trackids al acápite de descripción de servicios web.

---

## Propósito

El presente documento tiene por objetivo describir en sentido general los aspectos técnicos que conforman el sistema fiscal de facturación electrónica de la Dirección General de Impuestos Internos (DGII), así como de manera específica, los requerimientos necesarios a disponibilizar por parte de los contribuyentes para entrar en esta modalidad y comunicarse de manera correcta con la autoridad tributaria y otros contribuyentes electrónicos.

---

## Facturación Electrónica Autoridad Tributaria

Cuando se habla de Facturación electrónica, se refiere a la modalidad de negocios que utiliza comprobantes fiscales electrónicos, en ese sentido, la presente sección detalla los aspectos técnicos de la Dirección General de Impuestos Internos (DGII) tales como el lenguaje de comunicación, ambientes y servicios web existentes.

### Lenguaje Estándar de Comunicación

Para el intercambio de información, se tiene establecido el lenguaje extensible de marcas (XML), un estándar que a través de servicios web permite el intercambio de información entre plataformas heterogéneas.

Para cada operación que se estará realizando en Facturación Electrónica, la autoridad tributaria dispone de un formato preestablecido en el portal con la finalidad de describir los datos y validaciones que estas operaciones contemplan, adicional a un XSD a modo de referencia estructural de dichos XML.

Cada formato cuenta con un tag (etiqueta) por el cual se le reconoce, detallado a continuación:

| Formato XML | Etiqueta Madre (Obligatoria) |
|-------------|------------------------------|
| Formato e-CF | ECF |
| Formato Aprobación Comercial | ACECF |
| Formato Acuse de recibo | ARECF |
| Formato Anulación de secuencias e-NCF | ANECF |
| Formato de Resumen Factura de Consumo (32 < 250,000.00) | RFCE |

### Descripción de Ambientes

En Facturación Electrónica, un ambiente es un entorno que permite a los contribuyentes interactuar con los servicios de la Autoridad Tributaria en diferentes contextos, contándose actualmente con los siguientes:

**Pre-Certificación:** publica los servicios a efectos de que los contribuyentes puedan realizar pruebas de adecuación e integración de sus sistemas, almacenando los envíos por un periodo de 60 días.

Todo contribuyente habilitado en este ambiente dispone por tipo de comprobante de un rango de secuencias de 1 a 10,000,000, a excepción de las facturas de consumo electrónicas (32) que disponen de un rango de 1 a 50,000,000.

La fecha de vencimiento de estas secuencias corresponde al 31-12-2025, a excepción de las facturas de consumo electrónicas (32) y las notas de crédito electrónica (34) que no llevan fecha de vencimiento de secuencia.

**Certificación:** ambiente que tiene por objetivo validar capacidades por parte del sistema del contribuyente previo a su incorporación productiva al sistema fiscal de facturación electrónica, debiendo para ello agotar un conjunto de pruebas que requieren el uso de los servicios web.

**Producción:** ambiente productivo donde todo envío y operación tiene validez fiscal.

```
                    Pre-Certificación


                       Ambientes


                Producción            Certificación


                   Ilustración de Ambientes
```

En cada URL base de los diferentes ambientes se puede encontrar el documento Swagger (OpenAPI) el cual especifica la lista de recursos disponibles en el API REST y las operaciones (Métodos) a los que se puede invocar en cada uno de ellos, con sus parámetros y posibles respuestas.

A continuación, podrán identificar la estructura definida para la comunicación o invocación de los servicios de facturación electrónica según el ambiente:

**TesteCF:** Ambiente de pre-certificación, ejemplo:
- `https://ecf.dgii.gov.do/testecf/nombredelservicio/help/index.html`
- `https://fc.dgii.gov.do/testecf/nombredelservicio/help/index.html`

**CerteCF:** Ambiente de certificación, ejemplo:
- `https://ecf.dgii.gov.do/certecf/nombredelservicio/help/index.html`
- `https://fc.dgii.gov.do/certecf/nombredelservicio/help/index.html`

**eCF:** Ambiente de producción, ejemplo:
- `https://ecf.dgii.gov.do/ecf/nombredelservicio/help/index.html`
- `https://fc.dgii.gov.do/ecf/nombredelservicio/help/index.html`

*Estructura de los servicios y ambientes de facturación electrónica de la Dirección General de Impuestos Internos (DGII), para mayor detalle dirigirse a la sección de Descripción de Servicios Web.*

---

## Descripción de Servicios Web

Los servicios web, son un conjunto de protocolos y estándares que en este caso mediante el uso del lenguaje extensible de marcas (XML) y API REST, permiten el intercambio de datos entre los softwares de facturación heterogéneos de los contribuyentes y la autoridad tributaria a través de un entorno definido como {Ambiente}, encontrándose en facturación electrónica los siguientes servicios:

### Autenticación

Servicio web responsable de generar una sesión para el contribuyente, validando su identidad mediante el uso de un certificado digital sobre un archivo (Semilla) que obtendrá de una petición y el cual, deberá enviar firmado para recibir un token con una duración determinada (1 hora por el momento).

Con la entrega de dicho token el contribuyente podrá utilizar los restantes servicios de facturación electrónica, especificándolo como header de autorización de los requests (Authorization: Bearer {token}).

#### URLs del servicio

- **TesteCF:** Ambiente de pre-certificación:  
  `https://ecf.dgii.gov.do/testecf/autenticacion`

- **CerteCF:** Ambiente de certificación:  
  `https://ecf.dgii.gov.do/certecf/autenticacion`

- **eCF:** Ambiente de producción:  
  `https://ecf.dgii.gov.do/ecf/autenticacion`

#### Métodos y parámetros

Dentro de la URL, se encontrarán los siguientes dos (2) recursos (Endpoint):

##### OBTENER ARCHIVO SEMILLA

| Campo | Descripción |
|-------|-------------|
| **DESCRIPCIÓN** | Retorna el archivo semilla (en formato XML) que permitirá obtener el token. |
| **MÉTODO** | GET |
| **RECURSO (ENDPOINT)** | `/api/autenticacion/semilla` |
| **REQUEST URL** | `https://eCF.dgii.gov.do/{ambiente}/autenticacion/api/autenticacion/semilla` |
| **EJEMPLO CURL** | `curl -X 'GET' \`<br>`'https://ecf.dgii.gov.do/testecf/autenticacion/api/autenticacion/semilla' \`<br>`-H 'accept: */*' \` |
| **ENTRADA** | Parámetros de entrada<br>N/A |
| **SALIDA** | Respuesta en formato XML<br>`<?xml version="1.0" encoding="utf-8"?>`<br>`<SemillaModel xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">`<br>`<valor>0000000-0000-0000-0000-000000000000</valor>`<br>`<fecha>2019-03-13T14:33:32.8617792-04:00</fecha>`<br>`</SemillaModel>` |
| **DESCRIPCIÓN PARAMETROS DE SALIDA** | - **Valor:** valor de la semilla, secuencia de caracteres encriptados.<br>- **Fecha:** fecha y hora en la cual se generó el archivo semilla. |

##### VALIDACIÓN DE ARCHIVO: VALIDAR SEMILLA

| Campo | Descripción |
|-------|-------------|
| **DESCRIPCIÓN** | Permite el envío del archivo (Semilla) firmado y retorna un objeto que contiene un string de autenticación (token) asociado a una fecha de emisión y una fecha de expiración del token recibido. |
| **MÉTODO** | POST |
| **RECURSO (ENDPOINT)** | `/api/autenticacion/validarsemilla` |
| **REQUEST URL** | `https://ecf.dgii.gov.do/{ambiente}/autenticacion/api/autenticacion/validarsemilla` |
| **EJEMPLO CURL** | `curl -X 'POST' \`<br>`'https://ecf.dgii.gov.do/testecf/autenticacion/api/autenticacion/validarsemilla' \`<br>`-H 'accept: application/json' \`<br>`-H 'Content-Type: multipart/form-data' \`<br>`-F 'xml=@response_1659304894166.xml;type=text/xml'` |
| **ENTRADA** | Parámetros de entrada<br>`xml*` |
| **FORMATOS SALIDA** | **Respuesta en formato JSON**<br>`{`<br>`"token": "string",`<br>`"expira": "yyyy-MM-ddTHH:mm:ssZ",`<br>`"expedido": "yyyy-MM-ddTHH:mm:ssZ"`<br>`}`<br><br>**Respuesta en formato XML**<br>`<?xml version="1.0" encoding="UTF-8"?>`<br>`<RespuestaAutenticacion>`<br>`<token>string</token>`<br>`<expira>yyyy-MM-ddTHH:mm:ssZ</expira>`<br>`<expedido>yyyy-MM-ddTHH:mm:ssZ</expedido>`<br>`</RespuestaAutenticacion>` |
| **DESCRIPCIÓN PARAMETROS DE SALIDA** | - **Token:** valor emitido por Impuestos Internos como llave de seguridad para utilizar los servicios de Facturación Electrónica.<br>- **Expira:** fecha y hora en la cual expira el token recibido.<br>- **Expedido:** fecha y hora en la cual se recibió el token. |

Ver RFC 6750 (https://tools.ietf.org/html/rfc6750) para más información sobre la autenticación por tokens.

---

### Recepción de e-CF

Servicio web responsable de recibir un e-CF tentativo (XML firmado digitalmente) y un token asociado a una sesión válida y en respuesta retornar un objeto que contiene un string denominado TrackId a modo de acuse de recibo, con el cual, el contribuyente podrá consultar el estado de su validación.

La recepción del TrackId y haber recibido un estado de validación satisfactorio, habilita al emisor al envío del e-CF al receptor y en caso de  que este no sea electrónico, la entrega de la correspondiente representación impresa.

Las Facturas de Consumo Electrónica con un monto inferior a los RD$250,000.00, no serán recibidos por este servicio, se deberá remitir un resumen de este al servicio recepción de resumen factura de consumo e-CF.

Adicionalmente, los XML que representan los e-CFs deberán cumplir con el Formato de Nombre de Archivo especificado en la sección "Estándar de Comunicación Emisor-Receptor".

#### URLs del servicio

- **TesteCF:** Ambiente de pre-certificación:  
  `https://ecf.dgii.gov.do/testecf/recepcion`

- **CerteCF:** Ambiente de certificación:  
  `https://ecf.dgii.gov.do/certecf/recepcion`

- **eCF:** Ambiente de producción:  
  `https://ecf.dgii.gov.do/ecf/recepcion`

#### MÉTODOS Y PARÁMETROS

| Campo | Descripción |
|-------|-------------|
| **MÉTODO** | POST |
| **RECURSO (ENDPOINT)** | `/api/facturaselectronicas` |
| **REQUEST URL** | `https://ecf.dgii.gov.do/{ambiente}/recepcion/api/facturaselectronicas` |
| **EJEMPLO CURL** | `curl -X 'POST' \`<br>`'https://ecf.dgii.gov.do/testecf/recepcion/api/facturaselectronicas' \`<br>`-H 'accept: application/json' \`<br>`-H 'Authorization: bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...' \`<br>`-H 'Content-Type: multipart/form-data' \`<br>`-F 'xml=@response_1659304894166.xml;type=text/xml'` |
| **ENTRADA** | Parámetros de entrada<br>`xml*` |
| **FORMATOS SALIDA** | **Respuesta en formato JSON**<br>`{`<br>`"trackId": "string",`<br>`"error": "string",`<br>`"mensaje": "string"`<br>`}`<br><br>**Respuesta en formato XML**<br>`<?xml version="1.0" encoding="UTF-8"?>`<br>`<RespuestaRecepcion>`<br>`<trackId>string</trackId>`<br>`<error>string</error>`<br>`<mensaje>string</mensaje>`<br>`</RespuestaRecepcion>` |
| **DESCRIPCIÓN PARAMETROS DE SALIDA** | - **Trackid:** número único generado por Impuestos Internos a un e-CF recibido.<br>- **Error:** motivo del mensaje de error recibido (Si aplica).<br>- **Mensaje:** mensaje asociado a un error recibido al intentar enviar un e-CF (Si aplica). |

---

### Recepción de resumen factura de consumo e-CF

Servicio web responsable de recibir un resumen que contiene las informaciones principales del e-CF correspondiente a Facturas de Consumo Electrónica con un monto inferior a los RD$250,000.00 (XML firmado digitalmente) y un token asociado a una sesión válida y en respuesta retornar Aceptado en caso de recepción y procesamiento exitoso, Aceptado condicional de encontrarse que no cumplió en algún punto pero que no ameritó el rechazo de este o de lo contrario Rechazado.

A pesar de que estaremos recibiendo un resumen, el contribuyente deberá conservar el e-CF extendido correspondiente a la Factura de Consumo Electrónica para futuros procesos en que se ameriten.

Los e-CF correspondientes a Factura de Consumo Electrónica con un monto superior o igual a los RD$250,000.00 deben ser remitidas en su totalidad (todas las informaciones correspondientes a este e-CF) por el servicio de Recepción de e-CF.

Adicionalmente, los XML que representan estos resúmenes deberán cumplir con el Formato de Nombre de Archivo especificado en la sección "Estándar de Comunicación Emisor-Receptor".

#### URLs del servicio

- **TesteCF:** Ambiente de pre-certificación:  
  `https://fc.dgii.gov.do/testecf/recepcionfc/`

- **eCF:** Ambiente de producción:  
  `https://fc.dgii.gov.do/ecf/recepcionfc/`

#### MÉTODOS Y PARÁMETROS

| Campo | Descripción |
|-------|-------------|
| **MÉTODO** | POST |
| **RECURSO (ENDPOINT)** | `/api/recepcion/ecf` |
| **REQUEST URL** | `https://fc.dgii.gov.do/{ambiente}/recepcionfc/api/recepcion/ecf` |
| **EJEMPLO CURL** | `curl -X POST`<br>`"https://fc.dgii.gov.do/testecf/recepcionfc/api/recepcion/ecf"`<br>`-H "accept: application/json"`<br>`-H "Authorization: bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."`<br>`-H "Content-Type: multipart/form-data"`<br>`-F "xml=@response_1659306932058_180702.xml;type=text/xml"` |
| **ENTRADA** | Parámetros de entrada<br>`xml*` |
| **FORMATOS SALIDA** | **Respuesta en formato JSON**<br>`{`<br>`"codigo": 1,`<br>`"estado": "string",`<br>`"mensajes": [`<br>`{`<br>`"codigo": "string",`<br>`"valor": "string"`<br>`}`<br>`],`<br>`"encf": "string",`<br>`"secuenciaUtilizada": true`<br>`}`<br><br>**Respuesta en formato XML**<br>`<?xml version="1.0" encoding="UTF-8"?>`<br>`<Respuesta>`<br>`<codigo>1</codigo>`<br>`<estado>string</estado>`<br>`<mensajes>`<br>`<codigo>string</codigo>`<br>`<valor>string</valor>`<br>`</mensajes>`<br>`<encf>string</encf>`<br>`<secuenciaUtilizada>true</secuenciaUtilizada>`<br>`</Respuesta>` |

**DESCRIPCIÓN PARAMETROS DE SALIDA:**

- **Código:** código asociado al estado de validación del resumen de factura de consumo recibido.
- **Estado:** estado de validación otorgado por Impuestos Internos al resumen de factura de consumo recibido.
- **Mensajes:** mensajes y códigos asociados al estado de validación del resumen de factura de consumo recibido.
- **Encf:** número de secuencia utilizada por el contribuyente en el resumen de factura de consumo.
- **SecuenciaUtilizada:** permite dar a conocer si el número de secuencia que fue recibido por Impuestos Internos puede reutilizarse en otro Resumen de Factura de Consumo en el escenario de que el resultado de la validación haya sido "Rechazado" por los siguientes motivos:

  - Certificado y/o firma inválida.
  - Estructura del comprobante (XML) no es válida.
  - Firmante del comprobante fiscal electrónico no corresponde a un delegado autorizado para hacer transacciones para el RNC Emisor.
  - El e-NCF no está autorizado para el RNC Emisor del comprobante fiscal electrónico.
  - El e-NCF autorizado se encuentra vencido a la fecha de envío del comprobante fiscal electrónico.
  - El RNC Emisor del comprobante no corresponde a un emisor electrónico.
  - El RNC Emisor no existe.
  - El RNC Emisor no se encuentra activo.

  Posibles valores del parámetro:
  - **True** = No puede reutilizarse la secuencia.
  - **False** = Puede reutilizarse la secuencia.

---

### Consulta de Resumen de Factura (RFCE)

Servicio web responsable de responder la validez o estado de un ENCF a un receptor o incluso a un emisor, a través de la presentación del RNC emisor, e-NCF y el código de seguridad.

Para realizar las consultas de los datos previamente descritos, se requiere que el usuario autenticado se encuentre delegado para el emisor.

A través de este servicio también pueden ser consultados los e-CF remitidos por el servicio de recepción de resumen factura de consumo inferiores a los RD$250,000.00.

#### URLs del servicio

- **eCF:** Ambiente de producción:  
  `https://fc.dgii.gov.do/ecf/consultarfce`

#### MÉTODOS Y PARÁMETROS

| Campo | Descripción |
|-------|-------------|
| **MÉTODO** | GET |
| **RECURSO (ENDPOINT)** | `/api/Consultas/Consulta` |
| **REQUEST URL** | `https://fc.dgii.gov.do/ecf/consultarfce/api/Consultas/Consulta?RNC_Emisor=111111111&ENCF=E320000000000&Cod_Seguridad_eCF=XXXXXX` |
| **EJEMPLO CURL** | `curl -X 'GET' \`<br>`'https://fc.dgii.gov.do/ecf/consultarfce/api/Consultas/Consulta?RNC_Emisor=111111111&ENCF=E320000000000&Cod_Seguridad_eCF=XXXXXX' \`<br>`-H 'accept: application/json' \`<br>`-H 'Authorization: bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...'` |
| **ENTRADA** | Parámetros de entrada<br>`RncEmisor*`<br>`ENCF*`<br>`CodigoSeguridad*` |
| **FORMATOS SALIDA** | **Respuesta en formato JSON**<br>`{`<br>`"rnc": "string",`<br>`"encf": "string",`<br>`"secuenciaUtilizada": true,`<br>`"codigo": "string",`<br>`"estado": "string",`<br>`"mensajes": [`<br>`{`<br>`"valor": "string",`<br>`"codigo": 0`<br>`}`<br>`]`<br>`}` |

**DESCRIPCIÓN PARAMETROS DE SALIDA:**

- **Código:** código asociado al estado de validación del e-CF recibido.
- **Estado:** estado de validación otorgado por Impuestos Internos al e-CF recibido.
- **RncEmisor:** número de registro nacional del contribuyente que envió el e-CF.
- **NcfElectronico:** número de secuencia utilizada por el contribuyente en el ENCF.
- **CodigoSeguridad:** extraído de los primeros seis (6) dígitos del hash generado en el SignatureValue de la firma digital que viene en el tag CodigoSeguridadeCF del resumen de factura.

**ESTADOS SALIDA:**

- **No encontrado (0):** implica que no se encontró el comprobante en los registros, pudiendo deberse a que aún no haya sido reportado.
- **Aceptado (1):** implica que el e-CF generado por el emisor fue aceptado y tiene validez fiscal.
- **Rechazado (2):** corresponde a la nulidad del comprobante generado por el emisor.

**Nota:** en adición a los estados anteriores, el servicio permite visualizar comprobantes cuyo estado es 'Aceptado condicional' exclusivamente para Facturas de Consumo Electrónica con un monto inferior a los RD$250,000.00.

---

### Consulta de resultado e-CF

Servicio web responsable de retornar el estado de procesamiento o validez del e-CF tentativo enviado exclusivamente mediante el servicio web de recepción de e-CF, a través de la presentación de un Trackid y un token asociado a una sesión válida.

#### URLs del servicio

- **TesteCF:** Ambiente de pre-certificación:  
  `https://eCF.dgii.gov.do/testecf/consultaresultado`

- **CerteCF:** Ambiente de certificación:  
  `https://eCF.dgii.gov.do/certecf/consultaresultado`

- **eCF:** Ambiente de producción:  
  `https://eCF.dgii.gov.do/ecf/consultaresultado`

#### MÉTODOS Y PARÁMETROS

| Campo | Descripción |
|-------|-------------|
| **MÉTODO** | GET |
| **RECURSO (ENDPOINT)** | `/api/consultas/estado` |
| **REQUEST URL** | `https://ecf.dgii.gov.do/{ambiente}/consultaresultado/api/consultas/estado?trackId=XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX` |
| **EJEMPLO CURL** | `curl -X 'GET' \`<br>`'https://ecf.dgii.gov.do/testecf/consultaresultado/api/consultas/estado?trackId=XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX' \`<br>`-H 'accept: application/json' \`<br>`-H 'Authorization: bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...'` |
| **ENTRADA** | Parámetros de entrada<br>`trackId*` |
| **FORMATOS SALIDA** | **Respuesta en formato JSON**<br>`{`<br>`"codigo": "string",`<br>`"estado": "string",`<br>`"mensaje": "string",`<br>`"encf": "string",`<br>`"secuenciaUtilizada": true`<br>`}`<br><br>**Respuesta en formato XML**<br>`<?xml version="1.0" encoding="UTF-8"?>`<br>`<RespuestaConsulta>`<br>`<codigo>string</codigo>`<br>`<estado>string</estado>`<br>`<mensaje>string</mensaje>`<br>`<encf>string</encf>`<br>`<secuenciaUtilizada>true</secuenciaUtilizada>`<br>`</RespuestaConsulta>` |

**DESCRIPCIÓN PARAMETROS DE SALIDA:**

- **Código:** código asociado al estado de validación del e-CF recibido.
- **Estado:** estado de validación otorgado por Impuestos Internos al e-CF recibido.
- **Mensaje:** mensaje asociado al código del estado de validación del e-CF recibido.
- **Encf:** número de secuencia utilizada por el contribuyente en el e-CF.
- **SecuenciaUtilizada:** permite dar a conocer si el número de secuencia que fue recibido por Impuestos Internos puede reutilizarse en otro e-CF (recuérdese que puede ser enviado más de una vez el mismo e-CF), en el escenario de que el resultado de la validación haya sido "Rechazado" (por los mismos motivos establecidos en el servicio de Recepción del resumen de factura de consumo electrónica).

**ESTADOS SALIDA:**

- **No encontrado (0):** implica que no se encontró el trackId proporcionado en los registros.
- **Aceptado (1):** implica que el e-CF generado por el emisor fue aceptado y tiene validez fiscal.
- **Rechazado (2):** corresponde a la nulidad del comprobante generado por el emisor.
- **En proceso (3):** implica que el comprobante se encuentra en verificación por parte de Impuestos Internos.
- **Aceptado Condicional (4):** implica que el e-CF generado por el emisor cumple con las especificaciones establecidas sin embargo existen condiciones que deben ser revisadas y corregidas las cuales durante el proceso de validación no ameritaron ser rechazados.

---

### Consulta estado e-CF

Servicio web responsable de responder la validez o estado de un e-NCF a un receptor o incluso a un emisor, a través de la presentación del RNC del emisor, RNC del comprador (cuando aplique), e-NCF y código de seguridad.

Para realizar las consultas de los datos previamente descritos, se requiere que el usuario autenticado se encuentre delegado para el emisor o para el receptor.

A través de este servicio también pueden ser consultados los e-CF remitidos por el servicio de recepción de resumen factura de consumo inferiores a los RD$250,000.00.

#### URLs del servicio

- **TesteCF:** Ambiente de pre-certificación:  
  `https://eCF.dgii.gov.do/testecf/consultaestado`

- **CerteCF:** Ambiente de certificación:  
  `https://eCF.dgii.gov.do/certecf/consultaestado`

- **eCF:** Ambiente de producción:  
  `https://eCF.dgii.gov.do/ecf/consultaestado`

#### MÉTODOS Y PARÁMETROS

| Campo | Descripción |
|-------|-------------|
| **MÉTODO** | GET |
| **RECURSO (ENDPOINT)** | `/api/consultas/estado` |
| **REQUEST URL** | `https://ecf.dgii.gov.do/{ambiente}/consultaestado/api/consultas/estado?RncEmisor=111111111&NcfElectronico=E310000000001&RncComprador=222222222&CodigoSeguridad=XXXXXX` |
| **EJEMPLO CURL** | `curl -X 'GET' \`<br>`'https://ecf.dgii.gov.do/testecf/consultaestado/api/consultas/estado?RncEmisor=111111111&NcfElectronico=E310000000001&RncComprador=222222222&CodigoSeguridad=XXXXXX' \`<br>`-H 'accept: application/json' \`<br>`-H 'Authorization: bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...'` |
| **ENTRADA** | Parámetros de entrada<br>`RncEmisor*`<br>`NcfElectronico*`<br>`RncComprador`<br>`CodigoSeguridad*` |
| **FORMATOS SALIDA** | **Respuesta en formato JSON**<br>`{`<br>`"codigo": "string",`<br>`"estado": "string",`<br>`"mensaje": "string"`<br>`}`<br><br>**Respuesta en formato XML**<br>`<?xml version="1.0" encoding="UTF-8"?>`<br>`<RespuestaConsulta>`<br>`<codigo>string</codigo>`<br>`<estado>string</estado>`<br>`<mensaje>string</mensaje>`<br>`</RespuestaConsulta>` |

**DESCRIPCIÓN PARAMETROS DE SALIDA:**

- **Código:** código asociado al estado de validación del e-CF recibido.
- **Estado:** estado de validación otorgado por Impuestos Internos al e-CF recibido.
- **Mensaje:** mensaje asociado al código del estado de validación del e-CF recibido.

**ESTADOS SALIDA:**

- **No encontrado (0):** implica que no se encontró el comprobante en los registros, pudiendo deberse a que aún no haya sido reportado.
- **Aceptado (1):** implica que el e-CF generado por el emisor fue aceptado y tiene validez fiscal.
- **Rechazado (2):** corresponde a la nulidad del comprobante generado por el emisor.

**Nota:** en adición a los estados anteriores, el servicio permite visualizar comprobantes cuyo estado es 'Aceptado condicional' exclusivamente para Facturas de Consumo Electrónica con un monto inferior a los RD$250,000.00.

---

### Consulta trackids

Servicio web responsable de retornar la colección de números de respuesta (trackId) de un e-NCF que haya sido recibido por DGII y los estados de estos.

Para poder realizar la consulta satisfactoriamente, se requiere que el usuario autenticado se encuentre delegado para el emisor, de lo contrario, no podrá obtener los datos.

#### URLs del servicio

- **TesteCF:** Ambiente de pre-certificación:  
  `https://eCF.dgii.gov.do/testecf/consultatrackids`

- **eCF:** Ambiente de producción:  
  `https://eCF.dgii.gov.do/ecf/consultatrackids`

#### MÉTODOS Y PARÁMETROS

| Campo | Descripción |
|-------|-------------|
| **MÉTODO** | GET |
| **RECURSO (ENDPOINT)** | `/api/trackids/consulta` |
| **REQUEST URL** | `https://ecf.dgii.gov.do/{ambiente}/consultatrackids/api/trackids/consulta?RncEmisor=111111111&ENCF=E310000000001` |
| **EJEMPLO CURL** | `curl -X 'GET' \`<br>`'https://ecf.dgii.gov.do/testecf/consultatrackids/api/trackids/consulta?RncEmisor=111111111&ENCF=E310000000001' \`<br>`-H 'accept: application/json' \`<br>`-H 'Authorization: bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...'` |
| **ENTRADA** | Parámetros de entrada<br>`RncEmisor*`<br>`ENCF*` |
| **FORMATOS SALIDA** | **Respuesta en formato JSON**<br>`{`<br>`"detalles": [`<br>`{`<br>`"trackId": "string",`<br>`"codigo": "string",`<br>`"estado": "string",`<br>`"mensaje": "string"`<br>`}`<br>`]`<br>`}`<br><br>**Respuesta en formato XML**<br>`<?xml version="1.0" encoding="UTF-8"?>`<br>`<RespuestaConsultaTrackIds>`<br>`<detalles>`<br>`<trackId>string</trackId>`<br>`<codigo>string</codigo>`<br>`<estado>string</estado>`<br>`<mensaje>string</mensaje>`<br>`</detalles>`<br>`</RespuestaConsultaTrackIds>` |

**DESCRIPCIÓN PARAMETROS DE SALIDA:**

- **TrackId:** número único generado por Impuestos Internos a un e-CF recibido.
- **Código:** código asociado al estado de validación del e-CF recibido.
- **Estado:** estado de validación otorgado por Impuestos Internos al e-CF recibido.
- **Mensaje:** mensaje asociado al código del estado de validación del e-CF recibido.

---

### Consulta directorio

Servicio web responsable de retornar exclusivamente en el ambiente productivo un listado de los contribuyentes electrónicos autorizados y las URL de sus servicios de recepción de e-CF, aprobación comercial y autenticación (Opcional).

En el caso de precertificación, este servicio tiene por objetivo proveer unas URL de prueba que fueron habilitadas por DGII para simular ser otro contribuyente, permitiendo de igual forma autenticarse, recibir comprobantes y/o aprobaciones comerciales.

#### URLs del servicio

- **TesteCF:** Ambiente de pre-certificación:  
  `https://eCF.dgii.gov.do/testecf/consultadirectorio`

- **eCF:** Ambiente de producción:  
  `https://eCF.dgii.gov.do/ecf/consultadirectorio`

#### MÉTODOS Y PARÁMETROS

**Endpoint 1: Listado completo**

| Campo | Descripción |
|-------|-------------|
| **MÉTODO** | GET |
| **RECURSO (ENDPOINT)** | `/api/consultas/listado` |
| **REQUEST URL** | `https://ecf.dgii.gov.do/{ambiente}/consultadirectorio/api/consultas/listado` |
| **EJEMPLO CURL** | `curl -X 'GET' \`<br>`'https://ecf.dgii.gov.do/testecf/consultadirectorio/api/consultas/listado' \`<br>`-H 'accept: application/json' \`<br>`-H 'Authorization: bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...'` |
| **ENTRADA** | N/A |
| **FORMATOS SALIDA** | **Respuesta en formato JSON**<br>`{`<br>`"contribuyentes": [`<br>`{`<br>`"rnc": "string",`<br>`"razonSocial": "string",`<br>`"urlRecepcion": "string",`<br>`"urlAceptacion": "string",`<br>`"urlOpcional": "string"`<br>`}`<br>`]`<br>`}` |

**Endpoint 2: Consulta por RNC**

| Campo | Descripción |
|-------|-------------|
| **MÉTODO** | GET |
| **RECURSO (ENDPOINT)** | `/api/consultas/rnc` |
| **REQUEST URL** | `https://ecf.dgii.gov.do/{ambiente}/consultadirectorio/api/consultas/rnc?rnc=111111111` |
| **EJEMPLO CURL** | `curl -X 'GET' \`<br>`'https://ecf.dgii.gov.do/testecf/consultadirectorio/api/consultas/rnc?rnc=111111111' \`<br>`-H 'accept: application/json' \`<br>`-H 'Authorization: bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...'` |
| **ENTRADA** | Parámetros de entrada<br>`rnc*` |
| **FORMATOS SALIDA** | **Respuesta en formato JSON**<br>`{`<br>`"rnc": "string",`<br>`"razonSocial": "string",`<br>`"urlRecepcion": "string",`<br>`"urlAceptacion": "string",`<br>`"urlOpcional": "string"`<br>`}` |

**DESCRIPCIÓN PARAMETROS DE SALIDA:**

- **RNC:** número de registro nacional del contribuyente.
- **RazonSocial:** nombre o razón social del contribuyente.
- **UrlRecepcion:** URL del servicio de recepción de e-CF del contribuyente.
- **UrlAceptacion:** URL del servicio de aprobación comercial del contribuyente.
- **UrlOpcional:** URL del servicio de autenticación (opcional) del contribuyente.

---

### Consulta estatus servicios

Servicio web responsable de proporcionar el estatus y disponibilidad de los servicios de facturación electrónica, como también las ventanas de mantenimientos de estos.

#### URLs del servicio

- **TesteCF:** Ambiente de pre-certificación:  
  `https://eCF.dgii.gov.do/testecf/estatusservicios`

- **eCF:** Ambiente de producción:  
  `https://eCF.dgii.gov.do/ecf/estatusservicios`

#### MÉTODOS Y PARÁMETROS

| Campo | Descripción |
|-------|-------------|
| **MÉTODO** | GET |
| **RECURSO (ENDPOINT)** | `/api/consultas/estatus` |
| **REQUEST URL** | `https://ecf.dgii.gov.do/{ambiente}/estatusservicios/api/consultas/estatus` |
| **EJEMPLO CURL** | `curl -X 'GET' \`<br>`'https://ecf.dgii.gov.do/testecf/estatusservicios/api/consultas/estatus' \`<br>`-H 'accept: application/json'` |
| **ENTRADA** | N/A |
| **FORMATOS SALIDA** | **Respuesta en formato JSON**<br>`{`<br>`"servicios": [`<br>`{`<br>`"nombre": "string",`<br>`"estado": "string",`<br>`"mensaje": "string",`<br>`"mantenimiento": {`<br>`"fechaInicio": "yyyy-MM-ddTHH:mm:ssZ",`<br>`"fechaFin": "yyyy-MM-ddTHH:mm:ssZ"`<br>`}`<br>`}`<br>`]`<br>`}` |

**DESCRIPCIÓN PARAMETROS DE SALIDA:**

- **Nombre:** nombre del servicio.
- **Estado:** estado del servicio (Disponible, No Disponible, En Mantenimiento).
- **Mensaje:** mensaje descriptivo del estado.
- **Mantenimiento:** información sobre ventanas de mantenimiento programado.

---

### Aprobación comercial

Servicio web responsable de recibir un comprobante electrónico de aprobación comercial (XML firmado digitalmente) correspondiente a la aprobación o rechazo por parte del receptor electrónico sobre un e-CF que haya recibido previamente, y un token asociado a una sesión válida.

Solo son validas aquellas aprobaciones comerciales asociadas a e-CF que previamente han sido validados y aceptados por Impuestos Internos.

#### URLs del servicio

- **TesteCF:** Ambiente de pre-certificación:  
  `https://eCF.dgii.gov.do/testecf/aprobacioncomercial`

- **CerteCF:** Ambiente de certificación:  
  `https://eCF.dgii.gov.do/certecf/aprobacioncomercial`

- **eCF:** Ambiente de producción:  
  `https://eCF.dgii.gov.do/ecf/aprobacioncomercial`

#### MÉTODOS Y PARÁMETROS

| Campo | Descripción |
|-------|-------------|
| **MÉTODO** | POST |
| **RECURSO (ENDPOINT)** | `/api/aprobacioncomercial` |
| **REQUEST URL** | `https://ecf.dgii.gov.do/{ambiente}/aprobacioncomercial/api/aprobacioncomercial` |
| **EJEMPLO CURL** | `curl -X 'POST' \`<br>`'https://ecf.dgii.gov.do/testecf/aprobacioncomercial/api/aprobacioncomercial' \`<br>`-H 'accept: application/json' \`<br>`-H 'Authorization: bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...' \`<br>`-H 'Content-Type: multipart/form-data' \`<br>`-F 'xml=@aprobacion_comercial.xml;type=text/xml'` |
| **ENTRADA** | Parámetros de entrada<br>`xml*` |
| **FORMATOS SALIDA** | **Respuesta en formato JSON**<br>`{`<br>`"codigo": "string",`<br>`"estado": "string",`<br>`"mensaje": "string"`<br>`}`<br><br>**Respuesta en formato XML**<br>`<?xml version="1.0" encoding="UTF-8"?>`<br>`<RespuestaAprobacion>`<br>`<codigo>string</codigo>`<br>`<estado>string</estado>`<br>`<mensaje>string</mensaje>`<br>`</RespuestaAprobacion>` |

**DESCRIPCIÓN PARAMETROS DE SALIDA:**

- **Código:** código asociado al estado de recepción de la aprobación comercial.
- **Estado:** estado de la recepción (Aceptado, Rechazado).
- **Mensaje:** mensaje descriptivo del resultado.

---

### Anulación rangos

Servicio web responsable de recibir un comprobante electrónico de anulación de rangos o secuencias de e-NCF (XML firmado digitalmente) y un token asociado a una sesión válida.

A través de este servicio se pueden anular:
- Rangos de secuencias no utilizadas
- e-CF que hayan sido firmados pero no enviados (ni a DGII ni al receptor)

#### URLs del servicio

- **TesteCF:** Ambiente de pre-certificación:  
  `https://eCF.dgii.gov.do/testecf/anulacionrangos`

- **eCF:** Ambiente de producción:  
  `https://eCF.dgii.gov.do/ecf/anulacionrangos`

#### MÉTODOS Y PARÁMETROS

| Campo | Descripción |
|-------|-------------|
| **MÉTODO** | POST |
| **RECURSO (ENDPOINT)** | `/api/operaciones/anularrango` |
| **REQUEST URL** | `https://ecf.dgii.gov.do/{ambiente}/anulacionrangos/api/operaciones/anularrango` |
| **EJEMPLO CURL** | `curl -X 'POST' \`<br>`'https://ecf.dgii.gov.do/testecf/anulacionrangos/api/operaciones/anularrango' \`<br>`-H 'accept: application/json' \`<br>`-H 'Authorization: bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...' \`<br>`-H 'Content-Type: multipart/form-data' \`<br>`-F 'xml=@anulacion.xml;type=text/xml'` |
| **ENTRADA** | Parámetros de entrada<br>`xml*` |
| **FORMATOS SALIDA** | **Respuesta en formato JSON**<br>`{`<br>`"codigo": "string",`<br>`"estado": "string",`<br>`"mensaje": "string"`<br>`}`<br><br>**Respuesta en formato XML**<br>`<?xml version="1.0" encoding="UTF-8"?>`<br>`<RespuestaAnulacion>`<br>`<codigo>string</codigo>`<br>`<estado>string</estado>`<br>`<mensaje>string</mensaje>`<br>`</RespuestaAnulacion>` |

**DESCRIPCIÓN PARAMETROS DE SALIDA:**

- **Código:** código asociado al estado de la anulación.
- **Estado:** estado del proceso (Aceptado, Rechazado).
- **Mensaje:** mensaje descriptivo del resultado.

---

### Emisor-Receptor (Comunicación P2P)

Servicio exclusivamente disponible en el ambiente de precertificación, responsable de simular ser un emisor y/o receptor ante un contribuyente y a partir de esto permitirle probar la operatividad que tendría en el ambiente productivo de autenticación (Opcional), recepción y emisión de comprobantes, acuses de recibo y aprobaciones comerciales.

#### URLs del servicio

- **TesteCF:** Ambiente de pre-certificación:  
  `https://eCF.dgii.gov.do/testecf/emisorreceptor/help/index.html`

Este servicio simula las siguientes operaciones P2P:

**1. Autenticación (Opcional)**
- Endpoint: `/api/autenticacion/semilla`
- Endpoint: `/api/autenticacion/validarsemilla`

**2. Recepción de e-CF**
- Endpoint: `/api/recepcionecf`
- Permite recibir e-CF de prueba desde otros contribuyentes

**3. Consulta de Acuse de Recibo**
- Endpoint: `/api/consulta/acuse`
- Permite consultar acuses de recibo emitidos

**4. Recepción de Aprobación Comercial**
- Endpoint: `/api/aprobacioncomercial`
- Permite recibir aprobaciones/rechazos comerciales

---

## Estándar de Comunicación Emisor-Receptor

Esta sección detalla los requerimientos que el emisor electrónico debe cumplir para comunicarse tanto con la DGII como con otros contribuyentes electrónicos (receptores).

### Requerimientos Generales

1. **Implementación de servicios web REST**
   - Los emisores/receptores electrónicos deben implementar servicios web REST para:
     - Recepción de e-CF
     - Recepción de Aprobación Comercial
     - Autenticación (opcional)

2. **Formato de respuesta**
   - Los servicios deben retornar respuestas en formato JSON o XML
   - Códigos de estado HTTP apropiados

3. **Seguridad**
   - Uso obligatorio de HTTPS (TLS 1.2 o superior)
   - Validación de certificados digitales
   - Autenticación mediante tokens JWT (opcional para P2P)

4. **Sensibilidad a mayúsculas/minúsculas**
   - Los servicios NO deben ser sensitivos a mayúsculas y minúsculas en los parámetros

5. **Puertos de red**
   - Uso de puertos de red tradicionales (80 para HTTP, 443 para HTTPS)
   - Evitar puertos no estándar para facilitar interoperabilidad

6. **Timeout y reintentos**
   - Timeout recomendado: 30 segundos
   - Implementar lógica de reintentos con backoff exponencial

### Creación y Parametrización De Servicios

Los contribuyentes electrónicos deben registrar las URL de sus servicios en la Oficina Virtual (OFV) mediante la opción "Mantenimiento Directorio FE".

**Campos a registrar:**
- **URL Recepción e-CF**: Endpoint para recibir e-CF de otros emisores
- **URL Aprobación Comercial**: Endpoint para recibir aprobaciones comerciales
- **URL Autenticación (Opcional)**: Endpoint de autenticación si se requiere

**Ejemplo de URLs:**
```
https://mi-empresa.com.do/api/recepcion/ecf
https://mi-empresa.com.do/api/aprobacion-comercial
https://mi-empresa.com.do/api/autenticacion (opcional)
```

### Restricciones de Contenido y/o Caracteres en los XML

1. **Encoding obligatorio**: UTF-8

2. **Tags vacíos**: No se deben incluir tags vacíos en los XML. Si un campo opcional no tiene valor, debe omitirse completamente.

   **Incorrecto:**
   ```xml
   <DescripcionDescuento></DescripcionDescuento>
   ```
   
   **Correcto:**
   ```xml
   <!-- Omitir el tag completamente -->
   ```

3. **Caracteres especiales**: Deben ser escapados correctamente:

| Carácter | Entidad XML | Decimal | Hexadecimal |
|----------|-------------|---------|-------------|
| `<` | `&lt;` | `&#60;` | `&#x3C;` |
| `>` | `&gt;` | `&#62;` | `&#x3E;` |
| `&` | `&amp;` | `&#38;` | `&#x26;` |
| `"` | `&quot;` | `&#34;` | `&#x22;` |
| `'` | `&apos;` | `&#39;` | `&#x27;` |

4. **Código de seguridad en QR**: Para la composición de URLs en códigos QR, los caracteres del código de seguridad deben cumplir con restricciones URL-safe:

| Carácter | Codificación URL |
|----------|-----------------|
| Espacio | `%20` |
| `+` | `%2B` |
| `/` | `%2F` |
| `?` | `%3F` |
| `%` | `%25` |
| `#` | `%23` |
| `&` | `%26` |

### Formato de Nombre de los Archivos XML

Los archivos XML que representan e-CF y otros documentos electrónicos deben seguir estrictamente el siguiente formato:

**Formato general:**
```
[RNC][Serie][TipoComprobante][Secuencia].xml
```

**Componentes:**
- **RNC**: 11 dígitos del RNC del emisor
- **Serie**: 1 letra (E para electrónico, B para contingencia)
- **TipoComprobante**: 2 dígitos (31, 32, 33, 34, etc.)
- **Secuencia**: 10 dígitos del número secuencial

**Ejemplos:**
```
131880738E31000000001.xml    (Factura de Crédito Fiscal Electrónica)
131880738E32000000001.xml    (Factura de Consumo Electrónica)
131880738E34000000001.xml    (Nota de Crédito Electrónica)
```

**Formatos para otros documentos:**

- **Aprobación Comercial (ACECF):**
  ```
  [RNC]ACECF[eNCFReferenciado].xml
  Ejemplo: 131880738ACECFE31000000001.xml
  ```

- **Acuse de Recibo (ARECF):**
  ```
  [RNC]ARECF[eNCFReferenciado].xml
  Ejemplo: 131880738ARECFE31000000001.xml
  ```

- **Anulación (ANECF):**
  ```
  [RNC]ANECF[Timestamp].xml
  Ejemplo: 131880738ANECF20231226140500.xml
  ```

- **Resumen Factura Consumo (RFCE):**
  ```
  [RNC][Serie][TipoComprobante][Secuencia].xml
  Ejemplo: 131880738E32000000001.xml
  ```

### Firmado de XML

**Estándar obligatorio**: XMLDSig (XML Digital Signature)

**Requisitos del firmado:**

1. **Algoritmo de firma**: RSA-SHA256 o superior

2. **Algoritmo de digestión**: SHA-256 o superior

3. **Certificado digital**:
   - Debe ser emitido por una prestadora de servicios de confianza acreditada por INDOTEL
   - El campo **SubjectName (SN)** del certificado debe contener el RNC del emisor
   - Validez vigente al momento de la firma

4. **Estructura de la firma**:
   - La firma digital debe ser el último elemento del XML
   - Debe firmar TODO el contenido previo (todas las secciones del e-CF)
   - Usar canonicalización C14N (Canonical XML)

5. **Validación de firma**:
   - La firma NO puede ser modificada después de creada
   - Cualquier cambio en el XML (incluso espacios) invalida la firma
   - La DGII valida la firma al momento de recepción

**Puntos críticos a tomar en cuenta:**

- **Whitespace/Espacios en blanco**: Mantener consistencia en espacios y saltos de línea antes de firmar
- **Encoding**: Asegurar UTF-8 sin BOM (Byte Order Mark)
- **Inmutabilidad**: Una vez firmado, el XML NO puede ser modificado
- **Timestamp**: La fecha/hora de firma debe corresponder a la fecha de emisión del e-CF

### Recomendaciones

1. **Validación local antes de envío**
   - Validar el XML contra el XSD antes de firmar
   - Verificar cuadratura de totales
   - Confirmar que todos los campos obligatorios estén presentes

2. **Logging y auditoría**
   - Mantener logs de todos los envíos y respuestas
   - Almacenar copias de los XML firmados
   - Registrar TrackIds recibidos

3. **Manejo de errores**
   - Implementar manejo robusto de errores HTTP
   - Procesar correctamente códigos de estado 4xx y 5xx
   - Retry logic para errores temporales (503, 504)

4. **Performance**
   - Implementar caching de tokens de autenticación (válidos 1 hora)
   - Usar conexiones HTTP persistentes (keep-alive)
   - Considerar procesamiento asíncrono para grandes volúmenes

5. **Conservación**
   - Conservar e-CF y documentos relacionados por 10 años (Ley 11-92, Art. 50)
   - Mantener en formato electrónico original
   - Backup regular de la base de datos fiscal

6. **Testing exhaustivo**
   - Probar en ambiente de precertificación antes de certificación
   - Validar todos los tipos de e-CF (31, 32, 33, 34, etc.)
   - Probar casos de error y rechazo
   - Simular comunicación P2P con el servicio Emisor-Receptor

---

**Fin del documento**

**Para mayor información:**
- Portal DGII: https://dgii.gov.do
- Formatos XML: Disponibles en el portal

