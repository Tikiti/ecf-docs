# Formato Aprobación Comercial (ACECF)

**Versión 1.0 | Enero 2020**

---

## 1. Introducción

La aprobación o rechazo comercial es la respuesta que el comprador deberá enviar al emisor como constancia de su conformidad con la transacción realizada. Al momento de recibir la factura, el comprador (receptor) está obligado a confirmar al emisor la recepción del documento con una respuesta de recepción¹ y de manera opcional podrá remitir la aprobación o rechazo comercial, de la cual deberá expedir una copia a la DGII.²

El presente documento describe el contenido que debe tener el formato XML de la aprobación comercial, incluyendo los mensajes que serán utilizados por los receptores electrónicos.

---

## 2. Contenido del Formato XML de Aprobación Comercial

**a) Detalle de Aprobación Comercial:** especifica el contenido de la respuesta que el receptor debe enviar al emisor y remitir copia a la DGII.

**b) Firma Digital:** que avala la integridad de la respuesta y autenticidad del remitente.

---

## 3. Códigos de Obligatoriedad

**1** - Dato obligatorio: el dato debe estar siempre en el archivo.

**2** - Dato condicional: el dato no es obligatorio pero pasa a serlo en determinados casos, si se cumple una cierta condición.

**3** - Dato opcional: el dato es opcional.

---

**¹** El Acuse de Recibo notifica la recepción de la factura electrónica, es decir, si la misma es recibida o no.

**²** La DGII recibirá aprobación o rechazo comercial de e-CF previamente aceptadas por la DGII.

---

### Contenido del Formato de Aprobación Comercial

| Secciones del Archivo | Obligatoriedad de la Sección |
|-----------------------|------------------------------|
| Detalle Aprobación Comercial | 1 |
| Firma Digital | 1 |

A continuación, se describe el contenido de cada sección, las especificaciones de formato para cada campo y los códigos de obligatoriedad para cada uno. Los nombres y características son similares al formato de e-CF.

---

## 4. Detalle de Aprobación Comercial

### ÁREA: DETALLE APROBACION COMERCIAL `<DetalleAprobacionComercial>`

| No. | Campo | Descripción | Tipo | Largo Máx. | Validación | Obligatoriedad |
|-----|-------|-------------|------|------------|------------|----------------|
| | ÁREA `<DetalleAprobacionComercial>` | DETALLE APROBACION COMERCIAL | | | | 1 |
| 1 | Versión | Versión del formato de Aprobación Comercial. | NUM | 3 | Valor: 1.0 | 1 |
| 2 | RNC del Emisor<br>`<RNCEmisor>` | Número del Registro Nacional del contribuyente que emite el e-CF. | NUM | 9 u 11 | a) RNC cumple con la estructura de formato.<br>b) RNC debe coincidir con el RNC del emisor del e-CF. | 1 |
| 3 | e-NCF<br>`<eNCF>` | Número Comprobante Fiscal Electrónico (e-NCF). | ALFA NUM | 13 | a) e-NCF cumple con la estructura de formato.<br>b) e-NCF debe coincidir con el e-NCF del e-CF remitido por el emisor electrónico. | 1 |
| 4 | Fecha Emisión<br>`<FechaEmision>` | Fecha de emisión del e-CF. | ALFA NUM | 10 | a) Formato fecha cumple con estructura dd-MM-AAAA.<br>b) Fecha de emisión debe coincidir en la aprobación comercial y en el e-CF remitido por el emisor electrónico. | 1 |
| 5 | Monto Total<br>`<MontoTotal>` | Valor indicado en el campo Monto Total del e-CF. | NUM | 18 | a) Monto Total debe coincidir con el valor del campo Monto Total del e-CF emitido. | 1 |
| 6 | RNC del Comprador<br>`<RNCComprador>` | Número del Registro Nacional del contribuyente que emite la Aprobación Comercial del e-CF. | NUM | 9 u 11 | a) RNC cumple con la estructura de formato.<br>b) RNC debe coincidir con RNC del comprador del e-CF. | 1 |
| 7 | Estado<br>`<Estado>` | Código numérico que indica el estado de la Aprobación Comercial. | NUM | 1 | Código numérico del estado de la Aprobación Comercial<br>1: e-CF Aceptado<br>2: e-CF Rechazado | 1 |
| 8 | Detalle Motivo del Rechazo<br>`<DetalleMotivoRechazo>` | Se indica el motivo de rechazo de manera detallada.<br>Condicional a que el campo Estado sea código 2. | ALFA NUM | 250 | Sin validación | 2 |
| 9 | Fecha y Hora Generación Aprobación Comercial<br>`<FechaHoraAprobacionComercial>` | Fecha y hora en formato dd-MM-AAAA HH:mm:ss | ALFA NUM | 19 | Fecha y hora cumplen con el formato indicado | 1 |
| | FIN ÁREA | DETALLE APROBACION COMERCIAL | | | | |

---

## 5. Firma Digital

### ÁREA: SIGNATURE `<Signature>`

| No. | Campo | Descripción | Tipo | Largo Máx. | Validación | Obligatoriedad |
|-----|-------|-------------|------|------------|------------|----------------|
| | ÁREA `<Signature>` | SIGNATURE | | | | 1 |
| 1 | Firma Digital | Firma digital sobre el archivo de Aprobación Comercial | | | | 1 |
| | FIN ÁREA | SIGNATURE | | | | |
