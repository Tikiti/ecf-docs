# Informe Técnico Comprobante Fiscal Electrónico

**Versión 1.0**  
**Gerencia de Facturación**  
**Dirección General de Impuestos Internos (DGII)**

---

## Bitácora

### Actualizaciones al 16-03-2021

• Fueron agregados en la sección 4. Comunicaciones y Web Service los servicios de Recepción RFCE, Comunicación Emisor-Receptor, Consulta Estatus Servicios y Consulta de TrackId e-CF.

• Se limitó el contenido de los diferentes servicios indicados en la sección 4. Comunicaciones y WebService, a una descripción funcional general y se incluyó la referencia de la descripción técnica para ver más detalle de la estructura y funcionamiento de cada uno de los servicios.

• Se actualiza el ejemplo de la URL que compone el timbre electrónico de una Factura de Consumo Electrónica menor a DOP$250 mil.

### Actualizaciones al 17-08-2022

• Se actualiza el ejemplo del cálculo del impuesto adicional para los códigos que se encuentra entre 023-035 y la unidad de medida es distinta de granel.

• Se actualiza el ejemplo del cálculo del impuesto adicional para los códigos que se encuentra entre 036-039.

• Actualización del tope máximo de la cantidad de líneas de los e-CF con un máximo de mil (1,000) líneas.

• Se excluye el término "Timbre Electrónico" en el documento de referencia.

---

## Definiciones

**Aprobación o Rechazo Comercial:** es la respuesta que emite el Receptor Electrónico sobre un e-CF recibido donde informa, tanto al emisor electrónico del e-CF como a la DGII, la conformidad o no, respectivamente, con el documento recibido, la cual es enviada a través del Servicio Web de Aprobación Comercial, en el formato estándar XML definido.

**Acuse de Recibo:** es una respuesta automática que indica que el e-CF fue recibido por el receptor electrónico; esta no implica una respuesta positiva o negativa respecto de la transacción comercial.

**Certificado Digital:** es un documento digital emitido y firmado digitalmente por una entidad de certificación, que identifica inequívocamente a un suscriptor durante el período de vigencia del certificado y que se constituye en prueba de que dicho suscriptor es fuente u originador del contenido de un documento digital o mensaje de datos que incorpore su certificado asociado.

**Contingencia:** es el estado que define las situaciones excepcionales que podrían impedir el curso normal del ciclo de facturación electrónica y para el cual se encuentran definidas acciones específicas que deben seguir los actores del modelo en cada situación.

**Firma Digital:** se entenderá como un valor numérico que se adhiere a un mensaje de datos y que, utilizando un procedimiento matemático conocido, vinculado a la clave del iniciador y al texto del mensaje, permite determinar que este valor se ha obtenido exclusivamente con la clave del iniciador y el texto del mensaje, y que el mensaje inicial no ha sido modificado después de efectuada la transmisión.

**INDOTEL (Instituto Dominicano de las Telecomunicaciones):** órgano regulador de las telecomunicaciones y del comercio electrónico, documentos y firmas digitales, de conformidad con las leyes No. 153-98 General de Telecomunicaciones y No. 126-02 de Comercio Electrónico, Documentos y Firmas Digitales de la República Dominicana, respectivamente.

**Lenguaje de Marcas Expansible (XML):** es un lenguaje estándar que estructura el intercambio de información entre diferentes plataformas, permitiendo la organización y el etiquetado de documentos. Algunos de sus campos de aplicación son las bases de datos, los documentos de texto, las hojas de cálculo y las páginas web.

**Mensajes de Datos:** es la información generada, enviada, recibida, almacenada o comunicada por medios electrónicos, ópticos o similares, como pudieran ser, entre otros, el intercambio electrónico de datos (EDI, por sus siglas en inglés), el correo electrónico, el telegrama, el télex o el telefax.

**Número de Comprobante Fiscal Electrónico (e-NCF):** secuencia alfanumérica que identifica un comprobante fiscal electrónico otorgado por la Dirección General de Impuestos Internos (DGII).

**Oficina Virtual (OFV):** es un espacio telemático donde los contribuyentes pueden ejecutar procedimientos tributarios, con el fin de facilitar y reducir los costos del cumplimiento de estos. Está ubicada dentro del portal de esta Dirección General y para su acceso es imprescindible cumplir con los mecanismos de autenticación definidos por la DGII para el acceso.

**Prestadora de servicios de confianza:** entidad de certificación conforme a lo establecido en la citada Ley núm. 126-02 y en la normativa emitida por el INDOTEL.

**Representación Impresa (RI) de e-CF:** es la versión impresa en papel del formato XML de un e-CF, que será entregada tanto a receptores no electrónicos para que puedan reportar sus transacciones de compras ante la DGII, sustentar crédito fiscal y conservar dichos documentos según lo establece la legislación vigente, como a quienes lo requieran por vender bienes que incluyen transportación. A tales fines, esta debe contener todos los campos establecidos como obligatorios por el Decreto núm. 254-06, según las especificaciones de la Norma General núm. 06-2018.

**Signatario o Firmante:** contribuyente que actúa en nombre propio o persona que actúa por cuenta de éste, y que habiendo obtenido previamente un certificado digital para uso tributario tiene la capacidad de firmar un documento digital y de autenticarse ante la DGII para realizar operaciones relacionadas con los e-CF.

**Web Service (en inglés):** es una tecnología que utiliza un conjunto de protocolos y estándares que sirven para intercambiar datos entre aplicaciones. Distintas aplicaciones de software desarrolladas en lenguajes de programación diferentes y ejecutadas sobre cualquier plataforma pueden utilizar los servicios web para intercambiar datos en redes como Internet.

---

## 1. Introducción

El presente documento tiene como propósito principal informar acerca de las particularidades que los contribuyentes deben conocer, conforme se vayan incorporando en el régimen de emisión de Comprobantes Fiscales Electrónicos (e-CF).

Es decir, que este Informe Técnico permitirá a tales contribuyentes obtener las directrices necesarias para la correcta implementación y uso de los e-CF en la República Dominicana.

## 2. Actores del Sistema

En el sistema de facturación electrónica de la República Dominicana se identifican los siguientes actores:

- **Dirección General de Impuestos Internos (DGII):** como entidad facultada para la administración y aplicación de los tributos conforme lo establecen los artículos 32, 34 y 35 del Código Tributario de la República Dominicana (Ley 11-92).

- **Emisor electrónico:** es todo aquel contribuyente autorizado por la DGII a emitir comprobantes fiscales electrónicos.

- **Receptor electrónico:** es todo contribuyente que recibe comprobantes fiscales electrónicos y que se encuentra autorizado por la DGII para emitirlos, es decir, que todo receptor electrónico es a su vez emisor electrónico.

## 3. Autenticidad del Emisor e Integridad de los e-CF

La autenticidad del emisor electrónico y la integridad de los e-CF remitidos están dados por:

- Uso de certificados digitales para firmado digital y para la autenticación en los servicios web.
- La autenticación en la OFV por medio de usuario y clave de acceso vinculados.

El emisor electrónico es responsable absoluto de su firma digital, la cual garantiza que la transacción se haga dentro de un entorno de seguridad y confianza entre las partes que interactúan.

### Estándar de Certificado Digital

Para la emisión de e-CF en la República Dominicana, todos los emisores electrónicos deberán disponer de un certificado digital para procesos tributarios¹, acreditado por una prestadora de servicios de confianza, emitido digitalmente, el cual será utilizado para validar la identidad del signatario que opera en nombre del contribuyente, delegar la firma, la autenticación de los servicios web y la firma digital de archivo XML, el cual deberá cumplir con los requisitos establecidos por el INDOTEL y la normativas relacionadas.

> ¹ En lo que se aplica la normativa de INDOTEL correspondiente a estos certificados, se podrán utilizar los certificados de persona física acreditado por una prestadora de servicios de confianza.

## 4. Comunicaciones y Web Service

El formato de cada documento electrónico utilizado en las comunicaciones de los diferentes web services, está basado en el lenguaje XML, el cual sigue un estándar definido "schema XML" con extensión ".xsd". Estos archivos constan de un formato específico con nombres de tags que conforman dichos documentos electrónicos.

La comunicación de los archivos XML se realizarán mediante Web Service REST, para lo cual la DGII dispondrá de los siguientes:

### 4.1. Web Service – Autenticación

Servicio responsable de validar la identidad del contribuyente mediante el uso de un certificado digital sobre un archivo base y una vez validado entregarle un token que utilizará para el consumo de los restantes servicios de Facturación Electrónica.

### 4.2. Web Service - Recepción e-CF

A través de este servicio, el emisor electrónico envía el XML del e-CF a la DGII y, esta a su vez, lo recibe y entrega de vuelta un TrackId, con el cual el emisor podrá consultar posteriormente el estado del documento enviado.

### 4.3. Web Service – Recepción RFCE

Servicio responsable de recibir un resumen que contiene las informaciones principales de un e-CF correspondiente a una Factura de Consumo Electrónica con un monto inferior a los RD$250,000.00, factura la cual no es enviada a DGII pero debe ser conservado en su totalidad por el contribuyente para futuros procesos.

### 4.4. Web Service - Recepción de Aprobación Comercial

Este servicio es utilizado por el receptor electrónico para enviar a la DGII el XML de Aprobación o Rechazo Comercial firmado, donde notifica su conformidad con el e-CF recibido.

### 4.5. Web Service - Consulta de Resultado de e-CF (emisores)

Mediante este servicio, el emisor electrónico puede consultar el estado de un e-CF, utilizando el TrackId entregado por la DGII a través del servicio de recepción e-CF.

### 4.6. Web Service - Consulta de Estado de e-CF (receptores)

Servicio que permite responder acerca de la validez de un e-CF, siendo necesario para realizar la consulta que el usuario autenticado se encuentre delegado para el emisor o para el receptor.

A través de este servicio también pueden ser consultados los e-CF remitidos por el servicio de recepción de resumen factura de consumo inferiores a los RD$250,000.00.

### 4.7. Web Service - Consulta de Trackid e-CF

Servicio responsable de retornar la colección de números de respuesta (TrackId) de un e-NCF que haya sido recibido por DGII y los estados de estos. Para poder realizar la consulta satisfactoriamente, se requiere que el usuario autenticado se encuentre delegado para el emisor, de lo contrario, no podrá obtener los datos.

### 4.8. Web Service - Consulta Directorio Facturadores

Este servicio es responsable de retornar exclusivamente en el ambiente productivo un listado de los contribuyentes electrónicos autorizados y las URL de sus servicios de recepción de e-CF, aprobación comercial y autenticación (Opcional). En el caso de precertificación, este servicio tiene por objetivo proveer unas URL de prueba que fueron habilitadas por DGII para simular ser otro contribuyente, permitiendo de igual forma autenticarse, recibir comprobantes y/o aprobaciones comerciales.

### 4.9. Web Service - Consulta Estatus Servicios

Servicio responsable de proporcionar el estatus y disponibilidad de los servicios de facturación electrónica, como también las ventanas de mantenimientos de estos.

### 4.10. Web Service - Anulación de e-NCF

Con este servicio y utilizando el XML de anulación de e-NCF, el emisor electrónico puede anular rangos de secuencias no utilizadas o e-CF que hayan sido firmados, pero no enviados ni al receptor electrónico ni a la DGII.

### 4.11. Web Service - Comunicación Emisor-Receptor

Servicio exclusivamente disponible en el ambiente de precertificación y responsable de simular ser un emisor y/o receptor ante un contribuyente y a partir de esto permitirle probar la operatividad que tendría en el ambiente productivo de autenticación (Opcional), recepción y emisión de comprobantes, acuses de recibo y aprobaciones comerciales.

> Para mayor detalle de la estructura y funcionamiento de estos servicios en los diferentes ambientes acceder a la documentación sobre e-CF, Descripción Técnica de Facturación Electrónica, sección Descripción de Servicios Web.

## 5. Consultas de e-CF

La validez y estado de un e-CF puede ser consultado a través de los distintos canales disponibles por Impuestos Internos, los cuales se detallan a continuación:

### 5.1. Consulta en la página web de DGII

En esta consulta el receptor electrónico puede verificar el estado de un e-CF ingresando el RNC del emisor, el RNC del receptor, el e-NCF del documento y Código de seguridad² (si aplica). Esta consulta presentará los siguientes mensajes de respuesta:

- **Número de Comprobante Fiscal ingresado no es correcto o no corresponde a este RNC:** cuando existe un error en la secuencia del e-NCF o la misma no está autorizada para dicho RNC.

- **e-CF no encontrado:** cuando la secuencia del e-NCF está autorizada pero no se encuentra un e-CF válido asociado a los datos proporcionados.

- **NCF válido:** cuando la secuencia del e-NCF se encuentra autorizada para el RNC ingresado y existe un e-CF asociado, se mostrará uno de los siguientes estados conforme corresponda, siendo estos³:

  - **Aceptado:** indica que el e-CF recibido en la DGII es válido para fines tributarios.
  - **Rechazado:** indica que el e-CF recibido en la DGII, de parte del emisor, no es válido para fines tributarios.

> ² Corresponde a los primeros seis (6) dígitos del hash de firma, encontrados debajo del código QR en la representación impresa del e-CF.
> 
> ³ Los estados de los e-CF serán los mismos para ambos servicios de consulta, ya sea el de envío e-CF como en el de estado e-CF.

### 5.2. Consultas en la Oficina Virtual (OFV)

En la Oficina Virtual (OFV) se encuentra habilitado un menú correspondiente a Facturación Electrónica donde pueden realizar consultas relacionadas a los Comprobantes Fiscales Electrónicos (e-CF), entre otras acciones:

- **Consulta de Anulaciones.** Esta opción permite realizar la búsqueda de Números de Comprobantes Fiscales Electrónicos Anulados, por rangos de fecha.

- **Consulta e-NCF Emitidos.** Esta opción permite realizar la búsqueda de Números de Comprobantes Fiscales Electrónicos emitidos por e-NCF o por rango de fecha; la misma contiene los siguientes filtros de búsqueda:
  - e-NCF
  - RNC Receptor
  - Tipo e-NCF
  - Estado
  - Aprobación Comercial
  - Fecha Emisión

- **Consulta e-NCF Recibidos.** Esta opción permite que el contribuyente (en calidad de receptor electrónico) pueda realizar la búsqueda de los Números de Comprobantes Fiscales Electrónicos Recibidos, colocando el RNC del tercero que generó el e-NCF y un rango de fecha que desee consultar; la misma contiene los siguientes filtros de búsqueda:
  - RNC Emisor
  - Tipo e-NCF
  - Aprobación Comercial
  - Fecha Emisión: Rango de fecha Desde-Hasta

- **Consulta Directorio Electrónico.** Esta opción permite al contribuyente visualizar todos los facturadores electrónicos con sus respectivas URL, para fines de tener comunicación entre ellos.

  Esta consulta, además de mostrar el listado general de emisores electrónicos autorizados, permite al contribuyente realizar filtros por RNC o por Razón Social del emisor electrónico que desee consultar.

- **Mantenimiento Directorio FE.** Esta opción permite al contribuyente agregar o modificar las URL en donde puede recibir las respuestas de Recepción, de Aprobación y de Autenticación (opcional). Esta última es opcional, ya que solo sería utilizada en caso de que el emisor requiera que el receptor se autentique para poder darle acceso a sus URL.

  Los campos a completar en esta opción son:
  - URL Recepción e-CF
  - URL Aprobación Comercial
  - URL Autenticación (Opcional)

### 5.3. Consultas en la App Móvil

En esta aplicación puede ser verificada la validez de un e-CF de dos maneras:

- **Consulta de NCF:** esta opción permite verificar o consultar un e-CF ingresando el RNC emisor, serie del e-NCF y parte secuencial del e-NCF.⁴

- **Validación de Documentos:** esta opción permite la lectura de códigos QR. En el caso del código QR correspondiente a un e-CF, la consulta se realiza a partir de los datos que posee el código QR de dicho e-CF.

Los estados resultantes en ambas consultas son:

- **Aceptado:** indica que el e-CF recibido en la DGII es válido para fines tributarios.
- **Rechazado:** indica que el e-CF no fue recibido en la DGII, por lo que no es válido para fines tributarios.
- **No encontrado:** indica que el e-CF no se encuentra recibido en la DGII.

> ⁴ También permite la consulta de comprobantes fiscales no electrónicos.

## 6. Comprobantes Fiscales Electrónicos (e-CF)

### 6.1. Tipos de Comprobantes Fiscales Electrónicos (e-CF)

El Comprobante Fiscal Electrónico (e-CF) tiene igual validez y efectos legales que el comprobante fiscal no electrónico, sin embargo, difieren de estos en que son emitidos electrónicamente, mantienen un formato estándar (XML) y están firmados electrónicamente, lo que ofrece una mayor seguridad e integridad al documento.

Asimismo, los tipos de comprobantes fiscales electrónicos mantienen las características generales establecidas en el Decreto 254-06, Norma 06-18 y Norma 05-2019, por lo que, son equivalentes a cada tipo de comprobante fiscal no electrónico; se distinguen por estar nombrados con el término "electrónico" y estar codificados de forma distinta. Los tipos de e-CF son:

| Tipo | e-CF |
|------|------|
| 31 | Factura de Crédito Fiscal Electrónica |
| 32 | Factura de Consumo Electrónica |
| 33 | Nota de Débito Electrónica |
| 34 | Nota de Crédito Electrónica |
| 41 | Comprobante Electrónico de Compras |
| 43 | Comprobante Electrónico para Gastos Menores |
| 44 | Comprobante Electrónico para Regímenes Especiales |
| 45 | Comprobante Electrónico Gubernamental |
| 46 | Comprobante Electrónico para Exportaciones |
| 47 | Comprobante Electrónico para Pagos al Exterior |

- **Factura de Crédito Fiscal Electrónica:** Aquellos comprobantes fiscales electrónicos que registran las transacciones comerciales de compra y venta de bienes y/o servicios, y permiten al receptor o usuario que lo solicite, sustentar gastos y costos o crédito fiscal para efecto tributario.

- **Factura de Consumo Electrónica⁵:** Aquellos comprobantes fiscales electrónicos que acreditan la transferencia de bienes, la entrega en uso o la prestación de servicios a consumidores finales.

- **Nota de Débito Electrónica:** Aquellos comprobantes electrónicos que emiten vendedores de bienes y/o prestadores de servicios para recuperar costos y gastos, tales como intereses por mora, fletes u otros, incurridos por el vendedor con posterioridad a la emisión de comprobantes fiscales.

- **Nota de Crédito Electrónica:** Aquellos comprobantes electrónicos que emiten los vendedores de bienes y/o prestadores de servicios por modificaciones posteriores en las condiciones de venta originalmente pactadas, es decir, para anular operaciones, efectuar devoluciones, conceder descuentos y bonificaciones, subsanar errores o casos similares.

- **Comprobante Electrónico de Compras:** Aquellos comprobantes fiscales electrónicos emitidos por las personas físicas y jurídicas cuando adquieran bienes o servicios de personas no registradas como contribuyentes.

- **Comprobante Electrónico para Gastos Menores:** Aquellos comprobantes electrónicos emitidos por las personas físicas o jurídicas para sustentar pagos realizados por su personal, sean éstos efectuados en territorio dominicano o en el extranjero y en ocasión a las actividades relacionadas al trabajo, tales como: consumibles, pasajes y transporte público, tarifas de estacionamiento y peajes.

- **Comprobante Electrónico para Regímenes Especiales:** Aquellos comprobantes fiscales electrónicos utilizados para facturar las transferencias de bienes o prestación de servicios exentos del ITBIS y/o ISC a las personas físicas o jurídicas acogidas a regímenes especiales de tributación mediante leyes especiales, contratos o convenios debidamente ratificados por el Congreso Nacional.

- **Comprobante Electrónico Gubernamental:** Aquellos comprobantes fiscales electrónicos utilizados para facturar la venta de bienes o la prestación de servicios al Gobierno Central, Instituciones Descentralizadas y Autónomas, Instituciones de la Seguridad Social y cualquier entidad gubernamental que no realice una actividad comercial.

- **Comprobante Electrónico para Exportaciones:** Aquellos comprobantes fiscales electrónicos utilizados para reportar ventas de bienes fuera del territorio nacional utilizados por los exportadores nacionales, empresas de zonas francas y Zonas Francas Comerciales.

- **Comprobante Electrónico para Pagos al Exterior:** Aquellos comprobantes fiscales electrónicos emitidos por concepto de pago de rentas gravadas de fuente dominicana a personas físicas o jurídicas no residentes fiscales obligadas a realizar la retención total del Impuesto sobre la Renta, de conformidad a los artículos 297 y 305 del Código Tributario.

> ⁵ Durante el piloto, solo se utilizará este tipo de comprobante en operaciones de facturación masiva o por lote (no retail) después de que se prueben los demás tipos de comprobantes.

## 7. Estructura, Formato y Vencimiento de los Números Comprobantes Fiscales Electrónicos (e-NCF)

La secuencia del comprobante fiscal electrónico dispone de una estructura de trece (13) posiciones alfanuméricas.

**E 31 0000000001**

- **E**: Serie
- **31**: Tipo de Comprobante
- **0000000001**: Secuencia

La letra E corresponde a la serie del e-CF, los dos dígitos siguientes identifican el tipo de e-CF y los últimos diez corresponden al secuencial. Dicha secuencia estará vigente desde la fecha de autorización hasta el 31 de diciembre del año siguiente y no podrá ser usada posterior a su vencimiento.

## 8. Modelo de Operación

Los e-CF son emitidos de forma unitaria, en un formato estándar XML especificado por la DGII y transmitidos mediante una plataforma de servicio web, requiriendo el uso de certificado digital.

### Figura I. Modelo Emisor-Receptor Electrónicos

**Pasos obligatorios:** 1-4  
**Pasos opcionales:** 5-6

El modelo funciona de la siguiente manera:

1. El emisor electrónico envía el e-CF a la DGII al momento de la emisión del documento.
2. La DGII responde entregando un trackId, que el emisor del e-CF puede utilizar para consultar el estado del documento, a través del servicio web habilitado para estos fines⁶.
3. Luego el emisor electrónico envía el e-CF al receptor electrónico.
4. El receptor electrónico debe acusar recibo del e-CF al emisor electrónico.
5. El receptor electrónico podrá dar respuesta de su conformidad, al emisor electrónico, mediante la Aprobación o Rechazo Comercial⁷.
6. En caso de que el receptor envíe la Aprobación o Rechazo Comercial al emisor, notificará de su repuesta a DGII.

El e-CF será validado por la DGII, entregando al emisor mediante el web service de envío de e-CF uno de los siguientes estados: "e-CF aceptado", "e-CF aceptado condicional", "e-CF rechazado" o "e-CF en proceso"⁸.

> ⁶ Web Service de Consulta de Resultado de e-CF.
> 
> ⁷ Solo se recibirán aprobaciones comerciales de e-CF previamente aceptadas por la DGII.
> 
> ⁸ Ver descripción de los estados en la sección 4 para el Web Service de Consulta de Envío e-CF.

### Figura II. Modelo Emisor Electrónico - Receptor No Electrónico

**Pasos obligatorios:** 1-3

Cuando el emisor es electrónico pero el receptor no lo es - ver figura II-, el modelo funciona de la siguiente manera:

1. El emisor envía el e-CF a la DGII, al momento de la emisión del documento.
2. La DGII responde entregando un trackId, que el emisor del e-CF puede utilizar para consultar el estado del documento, a través del servicio web habilitado para estos fines.
3. Luego, el emisor electrónico entrega una representación impresa (RI) del e-CF al receptor no electrónico.

El receptor deberá consultar la validez del documento en la consulta disponible en la página web de la DGII y proceder a reportar la compra en el Formato de Envío de Costos y Gastos (Formato 606), de conformidad con lo establecido en la Norma General Núm. 07-18 sobre Remisión de Informaciones y modificaciones que le sucedan.

## 9. Factura de Consumo Electrónica menor a DOP$250 mil

### 9.1. Modelo de operación

Para la emisión de la factura de consumo electrónica menor a DOP250 mil se deberá cumplir con las especificaciones del Formato del Comprobante Fiscal Electrónico (e-CF)⁹.

### Figura III. Modelo emisión Factura de Consumo Electrónica menor a DOP$250 mil

El modelo funciona de la siguiente manera:

1. Una vez emitida la factura de consumo electrónica menor a DOP$250 mil, el emisor deberá guardar en su base de datos dicha factura y remitir a Impuestos Internos un resumen de la factura de consumo electrónica¹⁰, el cual debe cumplir con el formato de resumen establecido.

2. Impuestos Internos retorna la respuesta de la validación del formato de resumen de consumo electrónica remitido, con uno de los siguientes estados:

   - **Aceptado:** indica que el formato de resumen de factura de consumo electrónica cumple con las especificaciones establecidas, por lo que es recibido por la DGII.

   - **Rechazado:** significa que el formato de resumen de factura de consumo electrónica no cumple con las especificaciones establecidas, lo que implica que el archivo no es recibido por la DGII. Ante este estado, el emisor deberá corregir y remitir nuevamente el resumen de factura de consumo electrónica a Impuestos Internos.

   - **Aceptado Condicional:** con esta repuesta la DGII indica que el formato de resumen de factura de consumo electrónica es aceptado, sin embargo existe irregularidad que no amerita el rechazo, pero debe ser observada y corregida para futuras remisiones.

3. Posteriormente, entrega al receptor no electrónico una Representación Impresa de la factura de consumo electrónica menor a DOP$250 mil.

El emisor deberá almacenar y conservar en forma electrónica la factura de consumo emitida al receptor no electrónico, por un período de diez (10) años¹¹, adicional, deberá poner a disposición de este para fines de consulta.

> ⁹ Ver Formato de Comprobante Fiscal Electrónico.
> 
> ¹⁰ Las especificaciones que debe contener el resumen de la factura de consumo electrónica están establecidas en el documento 'Formato de Resumen de Factura Electrónica menores a DOP$250 mil'.
> 
> ¹¹ Según lo establecido en el Artículo 50, literal h del Código Tributario (Ley 11-92).

## 10. Correcciones y Anulación de un e-CF

Las correcciones de un e-CF serán realizadas únicamente mediante el uso de notas de crédito o débito electrónicas, según corresponda. Si la nota de crédito electrónica es emitida con posterioridad a los treinta (30) días, contados a partir del nacimiento de la obligación tributaria, las devoluciones de bienes gravados con el ITBIS podrán conllevar únicamente la restitución del precio pagado, sin incluir la devolución del ITBIS, tal como lo establecen los Arts. 8 y 28 del Reglamento 293-11.

En los casos en que la factura haya sido emitida (firmada digitalmente) y aún no haya sido enviada a la DGII o al receptor, el e-CF puede ser anulado mediante el Web Service de Anulación de e-NCF utilizando el formato XML de Anulación de e-NCF (ANECF)¹². También pueden ser anulados a través de este servicio, aquellos documentos electrónicos que aún no han sido firmados, con la finalidad de anular secuencias no usadas.

Si el e-CF es rechazado por el receptor en la Aprobación Comercial, el emisor electrónico deberá anular la factura enviando una nota de crédito tanto a Impuestos Internos como el receptor, indicando el motivo de la anulación. En tanto, que si el e-CF es aprobado por el receptor en la Aprobación Comercial pero rechazado por la DGII, el e-CF no se considerará válido (ni tampoco lo será la Aprobación Comercial, la cual también será rechazada) y el emisor deberá realizar un nuevo e-CF y sustituir el entregado al receptor.

> ¹² Los detalles del Formato de Anulación de Secuencias de e-NCF están incluidos en el Anexo IV.

## 11. Formato XML del e-CF

### 11.1. Contenido del e-CF

El e-CF debe contener las especificaciones establecidas en el siguiente recuadro¹³:

| Sección | Descripción | Requisito | e-CF |
|---------|-------------|-----------|------|
| **A. Encabezado** | Corresponde a la identificación del e-CF, donde están contenidos los datos del emisor, receptor y datos tributarios. La sección contiene las áreas Identificación del Documento, Emisor, Receptor, Informaciones Adicionales, Transporte, Totales y Otra Moneda. | Obligatorio | Todos |
| **B. Detalle de bienes o Servicios** | Corresponde al detalle de los bienes o servicios. | Obligatorio | Todos |
| **C. Subtotales Informativos** | Corresponde al subtotal informativo. Los campos contenidos en esta sección no modifican los campos totalizadores, ni aumentan o disminuyen la base del impuesto. | Opcional | Todos |
| **D. Descuentos o Recargos** | Esta sección se utiliza para especificar descuentos o recargos globales que afectan al total del e-CF. | Condicional | Todos |
| **E. Paginación** | En esta sección se indica la cantidad de páginas del e-CF en la Representación Impresa y cuales ítems estarán en cada una. | Opcional | Todos |
| **F. Información de Referencia** | En esta sección se deben detallar los e-CF modificados o reemplazados con e-CF. | Obligatorio y condicional. | Obligatorio solo para Notas de Crédito y Débito Electrónica cuando modifica un documento en papel o uno electrónico. Es condicional para el resto de los e-CF, cuando se trate de una sustitución de un NCF por un e-CF (casos de contingencia). |
| **H. Fecha y Hora de la firma digital.** | Indica la fecha y hora de la firma digital. | Obligatorio | Todos |
| **I. Firma Digital** | Corresponde a la firma digital sobre toda la información contenida en las secciones anteriores, para garantizar la integridad del e-CF. | Obligatorio | Todos |

> ¹³ El detalle se encuentra en el documento 'Formato de e-CF'.

#### 11.1.1. Detalle por sección

El contenido de cada sección contendrá el formato y sus códigos de obligatoriedad según el tipo de e-CF¹⁴, siendo estos los siguientes:

- **0: No corresponde.** Significa que el dato no debe ir en un determinado documento.
- **1: Dato obligatorio.** El dato siempre debe estar en el documento, independiente de las características de la transacción.
- **2: Dato condicional.** El dato no es obligatorio en todos los documentos, pero puede serlo en determinadas operaciones si se cumple una determinada condición. Ejemplo: Si existen descuentos recargos que afectan el total del e-CF, se debe incluir la sección Descuentos o Recargos, de lo contrario se descuadrará el monto total.
- **3: Opcional.** El dato es opcional.

> ¹⁴ Incluidos en el 'Formato de e-CF'.

#### 11.1.2. Instrucciones de Formato para las Secciones¹⁵

- Los valores de montos deben ser completados en pesos dominicanos (DOP), excepto los campos correspondientes a otra moneda.
- En los datos tipo numérico, los decimales se separan con punto.
- En los datos tipo numérico, no se separan los miles.
- En la información 'ALFANUM', los siguientes caracteres no deben emplearse dentro del XML, ya que tienen un significado por sí solos y deberán ser remplazados por definiciones estándar especificadas a continuación para dichos caracteres:

| Nombre | Carácter | Referencia Decimal | Referencia Hexadecimal |
|--------|----------|-------------------|----------------------|
| quot | " | &#34; | &#x22; |
| amp | & | &#38; | &#x26; |
| apos | ' | &#39; | &#x27; |
| lt | < | &#60; | &#x3C; |
| gt | > | &#62; | &#x3E; |

> ¹⁵ Instrucciones aplican para el resto de los formatos XML.

## 12. Regla de tolerancia. Cuadratura.

Dado que en toda transacción comercial es necesario que los valores facturados y los pagados coincidan, para efectos del formato XML del e-CF, se define cuadratura como la acción que permite garantizar que los valores en los balances totales coincidan.

En este sentido, para facilitar la cuadratura de estos balances en el XML, se admite una regla de tolerancia para cada línea de la sección Detalle de Bienes o Servicios, que es: una diferencia de ± 1 unidad del `precio * cantidad ítem` en cada línea. Asimismo, se define una tolerancia global sobre el monto total del e-CF, equivalente al total de líneas de la sección Detalle.

Lo anterior implica que tanto los montos de las líneas en la sección Detalle como los del Encabezado deben coincidir o aproximarse a resultados sujetos a la regla de tolerancia indicada. Si la diferencia supera la tolerancia, el e-CF será aceptado condicionalmente.

## 13. Regla de Redondeo

La regla de redondeo establece que los campos de valores numéricos permiten hasta dos (2) dígitos decimales¹⁶, los cuales podrán ser redondeados de la siguiente forma:

El tercer decimal debe redondear el segundo decimal, dejando cifras con dos decimales fijos. Cuando el valor del tercer decimal sea < 5, se mantiene el valor del segundo decimal. Si es >= 5, se incrementa el segundo decimal una unidad.

**Ejemplo 1: Tercer decimal < 5.**  
750.5212 ≈ 750.52

**Ejemplo 2: Tercer decimal >= 5.**  
750.5276 ≈ 750.53

> ¹⁶ Exceptuando `<PrecioUnitarioItem>` y `<PrecioUnitarioItemOtraMoneda>` en la sección Detalle permiten hasta cuatro (4) dígitos decimales, esto incluye `<TipoCambio>` en el Encabezado (según lo establecido por el Banco Central) y `<Subcantidad>` en Detalle (hasta 3 decimales).

## 14. Impuesto Selectivo al Consumo (ISC) de Alcoholes y Cigarrillos

Para el cálculo del ISC de Alcoholes y Cigarrillos, se deberá colocar en la sección Detalle de Bienes y Servicio el código atendiendo al tipo de impuesto adicional especificado en la tabla de Codificación de Tipos de Impuestos Adicionales (incluida en el Formato e-CF), y luego proceder al cálculo según las especificaciones del área de Totales del Encabezado.

### ISC Alcohol (Tasa Específica)

Para el cálculo del ISC específico de alcohol se debe tener en cuenta los siguientes campos:

`<MontoImpuestoSelectivoEspecifico> = <TasaImpuestoAdicional> x <GradosAlcohol> x <CantidadReferencia> x <Subcantidad> x <CantidadItem>`

### ISC Alcohol (Tasa Ad-Valorem)

Para el cálculo del ISC Ad-Valorem de alcohol:

Si el código del impuesto se encuentra entre 023-035, se debe verificar la unidad de medida del ítem. Si es granel (código 18), el cálculo del Ad-Valorem incrementa el precio unitario (equivalente al precio de lista) un 30% multiplicado por la cantidad del ítem multiplicado por la tasa del impuesto.

Si el código del impuesto se encuentra entre 023-035 y la unidad es distinta de granel, aplicar la fórmula correspondiente según las especificaciones del documento.

### ISC Cigarrillos (Tasa Específica)

Para el cálculo del ISC específico de cigarrillos, se debe multiplicar la cantidad del ítem por la cantidad de referencia por la tasa de impuesto adicional.

### ISC Cigarrillos (Tasa Ad-Valorem)

Si el código del impuesto se encuentra entre 036-039, aplicar la fórmula Ad-Valorem correspondiente según las especificaciones del documento.

## 15. Otros impuestos adicionales

Para los impuestos adicionales como Propina Legal, Contribución al Desarrollo de las Telecomunicaciones (CDT), Servicios Generales de Seguros, Servicios de Telecomunicaciones, Emisión Primera Placa:

- Si `<IndicadorMontoGravado>` = 0: `<MontoItem> x <TasaImpuestoAdicional>`
- Si `<IndicadorMontoGravado>` = 1: `<OtrosImpuestosAdicionales> = <MontoItem> / (1+ ITBIS tasa 1) x TasaImpuestoAdicional`

Para CDT y Servicios de Telecomunicaciones, si `<IndicadorNorma1007>` en Descuentos/Recargos = 1, aplicar la fórmula correspondiente considerando la Norma 10-07.

## 16. Tratamiento para e-CF con aplicación de la Norma General 07-07

Las especificaciones para operaciones bajo la Norma General 07-07 indican que la operación debe dividirse en dos ítems: uno correspondiente a la parte exenta (90% del valor) y otro para la parte gravada (10% del valor).

## 17. Representación Impresa (RI) del e-CF

Existen especificaciones mínimas, con carácter de obligatoriedad, que deben presentarse en una Representación Impresa (RI) de e-CF, así como un orden y lugar específico donde debe ser colocadas las informaciones relativas al tipo de comprobante fiscal a la que corresponda. Cabe destacar, que si la RI corresponde a un e-CF que no ha sido recibido por la DGII o se encuentre en estado de rechazado, la misma no podrá ser usada para fines de sustentar crédito fiscal.

Las informaciones de un e-CF, deben estar contenidas dentro de la RI a imprimir y con un máximo de mil líneas (1,000) a ser incluidas en la sección de Detalle de Bienes o Servicios, exceptuando las Facturas de Consumo Electrónicas menor a DOP$250 mil, las cuales tienen un tope de máximo de diez mil (10,000) líneas.

La Representación Impresa (RI) podrá imprimirse en varias páginas en caso de ser requerido, siempre que cumpla con las especificaciones que se indican respecto a la paginación, tanto en el Formato de e-CF como en el presente documento.

### 17.1. Calidad de impresión

La calidad de impresión de una Representación Impresa deberá ser tal que asegure la legibilidad del documento por un tiempo de al menos diez (10) años, conforme lo establecido en el literal f) del Artículo 44 de la Ley 11-92 Código Tributario.

### 17.2. Orden y Distribución de la Información en la Representación Impresa de un e-CF

#### 17.2.1. Encabezado

Corresponde a la identificación del e-CF, donde contiene los datos del emisor, comprador¹⁷ y datos tributarios.

**A. En la parte superior del encabezado, lado derecho del documento, deben estar contenidas las siguientes informaciones:**

- **Tipo de Comprobante Fiscal Electrónico**
- **e-NCF**
- **Fecha Vencimiento**
- **e-NCF Modificado** (aplica para Notas de Débito y Crédito)
- **Código de Modificación** (aplica para Notas de Débito y Crédito)

| Código de Modificación | Descripción del Código |
|------------------------|------------------------|
| 1 | Anula el NCF modificado |
| 2 | Corrige Texto del Comprobante Fiscal modificado |
| 3 | Corrige montos del NCF modificado |
| 4 | Reemplazo NCF emitido en contingencia |

**B. En la parte superior del encabezado, lado izquierdo del documento, deben estar contenidas las siguientes informaciones del emisor:**

- Nombre Comercial (si lo hubiera)
- Nombre o Razón Social
- Sucursal (si aplica)
- Número de Registro Nacional de Contribuyente (RNC)
- Dirección
- Municipio
- Provincia
- Fecha de Emisión

**C. En la parte inferior del encabezado, lado izquierdo, el documento debe contener los datos del cliente o destinatario:**

- Nombre o Razón Social Cliente
- Número de Registro Nacional de Contribuyente (si aplica)

> ¹⁷ En el caso de la factura de consumo electrónico cuando el monto total sea menor a DOP$250 mil el RNC Comprador será completado de manera opcional.

#### 17.2.2. Parte central

En la parte central, el documento debe  contener los datos indicados a continuación, conforme el artículo 8 del Decreto n.o 254-06, la Norma General 06-18 y según el bien o servicio transado.

**Datos del bien o servicio transferido, valor de la transacción y datos de impuestos:**

- Cantidad
- Indicador de Facturación
- Descripción
- Unidad de Medida (si aplica)
- Grados Alcohol en % (si aplica)
- PVP (si aplica)
- Precio
- ISC Específico (si aplica)
- ISC Ad-Valorem (si aplica)
- ITBIS (si aplica)
- Descuento (si aplica)
- Recargo (si aplica)
- Valor
- Subtotal Gravado (si aplica)
- Subtotal Exento (si aplica)
- Total ISC (si aplica)
- Total ITBIS (si aplica)
- CDT (si aplica)
- Propina legal (si aplica)
- Total
- Descripción de Descuento o Recargo (si aplica)
- Descuento o Recargo en % (si aplica)
- Monto de Descuento o Recargo (si aplica)

#### 17.2.3. Datos adicionales para incluirse en la RI

**Informaciones de consulta de un e-CF:**

- **Código QR:** deberá colocarse en el lado inferior izquierdo¹⁸ del e-CF, conservar una distancia mínima de dos (2) centímetros desde el borde de la hoja hasta el lugar donde inicia el código QR y tener un tamaño mínimo de 22 x 22 mm, con un margen de 3mm en los lados de este.

  El código QR en su composición deberá contener los siguientes parámetros¹⁹:
  - RncEmisor
  - RncComprador
  - ENCF
  - FechaEmision (dd-MM-aaaa)
  - MontoTotal
  - FechaFirma (dd-MM-aaaa HH:mm:ss)
  - CodigoSeguridad: corresponde a los primeros seis (6) dígitos del hash generado en el SignatureValue de la firma digital del e-CF.

  **Ejemplo URL:**  
  `https://ecf.dgii.gov.do/ecf/ConsultaTimbre?RncEmisor=XXXXXXXXXXX&RncComprador=XXXXXXXXXXXX&ENCF=XXXXXXXXXXXXX&FechaEmision=dd-MMyyyy&MontoTotal=XXXX.XX&FechaFirma=dd-MMyyyy%20HH:mm:ss&CodigoSeguridad=XXXXXX`

- **Código de Seguridad:** Debe ser indicado en palabras los primeros seis (6) dígitos del hash del SignatureValue de la firma, debajo del código QR.

- **Fecha de Firma Digital:** Debe colocar la fecha y hora de la firma digital en formato dd-MM-yyyy HH:mm:ss.

**Informaciones de consulta para la Factura de Consumo Electrónica menor a DOP$250 mil:**

En el caso del código QR para una factura de consumo electrónica menor a DOP$250 mil, en su composición, deberá contener los siguientes parámetros:
- RncEmisor
- ENCF
- MontoTotal
- CodigoSeguridad

**Ejemplo URL:**  
`https://fc.dgii.gov.do/eCF/ConsultaTimbreFC?RncEmisor=XXXXXXXXXXX&ENCF=XXXXXXXXXXXXX&MontoTotal=XXXX.XX&CodigoSeguridad=XXXXXX`

> ¹⁸ Excepto para dispositivos Handheld, en los cuales podrá ser también en el lado inferior central de la parte final del e-CF.
> 
> ¹⁹ Se exceptúan de estos parámetros las facturas de consumo menor a DOP$250 mil.

### 17.3. Modelos ilustrativos

- 17.3.1. Modelo ilustrativo con totales al final de la factura.
- 17.3.2. Modelo ilustrativo incluyendo el ITBIS en el campo 'Valor' del detalle de bienes o servicios.
- 17.3.3. Modelo ilustrativo incluyendo el ITBIS en el campo 'Valor' y totales en la parte del detalle de bienes o servicios.
- 17.3.4. Modelo ilustrativo de un e-FCF realizado a través de Papel Continuo.
- 17.3.5. Modelo ilustrativo de e-FCF para Impuesto Selectivo al Consumo.
- 17.3.6. Modelo ilustrativo de la Nota de Crédito Electrónica.
- 17.3.7. Modelo ilustrativo incluyendo Paginación (e-CF con dos páginas).
- 17.3.8. Modelo ilustrativo de la Factura de Consumo Electrónica con monto total igual o mayor a DOP$ 250 mil.
- 17.3.9. Modelo ilustrativo de la Factura de Consumo Electrónica con monto total menor a DOP$ 250 mil.
- 17.3.10. Modelo ilustrativo de la Factura de Consumo Electrónica con monto menor a DOP$250 mil, realizado a través de Papel Continuo.

## 18. Operación en Contingencia

Se considera el estado de contingencia cuando existen las siguientes condiciones:

- **No existe conexión:** Si no es posible el envío de e-CF a Impuestos Internos a través del web service, debido a que no existe conexión, se deberán enviar los e-CF que sean emitidos cuando se reestablezca la misma.

- **No es posible emitir e-CF:** Cuando no sea posible la emisión de e-CF, se dispondrá de secuencias serie B, que podrán ser utilizadas solo en caso de contingencia. Una vez sea solucionada la situación, se deben reemplazar los comprobantes emitidos serie B por los de serie E (e-CF) correspondientes, sin enviarlos al receptor, únicamente a la DGII.

**Notificación del estado contingencia**

El estado de contingencia debe ser informado de inmediato. En el caso de la DGII, esta realizará la notificación por los canales habilitados para estos fines. Por su parte, el emisor deberá informarlo a la DGII a través del módulo de contingencia disponible en la Oficina Virtual (OFV) o comunicándose Centro de Atención al Contribuyente.

### 18.1. Tipos de contingencia

- **Contingencia total:** existe una falla de sistema que afecta la operación total del contribuyente (emisión de e-CF). En este caso, el mismo deberá indicar la fecha de inicio de la contingencia y el motivo del estado. Este estado será inactivado automáticamente cuando la DGII reciba el primer e-CF posterior a la fecha de inicio de la contingencia o cuando el contribuyente notifique que la falla fue solucionada, lo que suceda primero.

- **Contingencia parcial:** existe una falla de sistema que afecta solo una parte de las operaciones del contribuyente, es decir, que una o varias de sus sucursales o unidades de negocio no puede facturar electrónicamente pero el resto continúa operando de forma habitual, emitiendo comprobantes electrónicos.

---

**Fin del documento**
