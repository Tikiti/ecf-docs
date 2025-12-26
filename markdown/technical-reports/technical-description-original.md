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
