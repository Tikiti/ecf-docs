# Formato Acuse de Recibo (ARECF)

**Versión 1.0**

---

## Bitácora de actualizaciones

**Versión 1.0**

1. Se actualiza la etiqueta del área 'DETALLE ACUSE DE RECIBO'.

---

## 1. Introducción

El acuse de recibo es la respuesta que el receptor deberá enviar al emisor como constancia de recepción del Comprobante Fiscal Electrónico; el mismo no implica aceptación ni rechazo del e-CF, sólo indica si fue o no recibido.

Al momento de recibir la factura, el receptor está obligado a confirmar al em isor la recepción del documento con una respuesta de recepción¹, previo a la aprobación comercial.

El presente documento describe el contenido que debe tener el formato XML del acuse de recibo, incluyendo los mensajes que serán utilizados por los receptores electrónicos.

---

## 2. Contenido del Formato XML del Acuse de Recibo

**a) Detalle del Acuse de Recibo:** especifica el contenido de la respuesta que el receptor debe enviar al emisor.

**b) Firma Digital:** que avala la integridad de la respuesta y autenticidad del remitente.

---

## 3. Códigos de Obligatoriedad

**1** - Dato obligatorio: el dato debe estar siempre en el archivo.

**2** - Dato condicional: el dato no es obligatorio pero pasa a serlo en determinados casos, si se cumple una cierta condición.

---

**¹** El Acuse de Recibo confirma que el documento corresponde a una factura electrónica y ha sido recibida.

---

### Contenido del Formato del Acuse de Recibo

| Secciones del Archivo | Obligatoriedad de la Sección |
|-----------------------|------------------------------|
| Detalle Acuse de Recibo | 1 |
| Firma Digital | 1 |

A continuación, se describe el contenido de cada sección, las especificaciones de formato para cada campo y el código de obligatoriedad de cada uno. Los nombres y características son similares al formato de e-CF.

---

## A. Detalle de Acuse de Recibo

| No. | Campo | Descripción | Tipo | Largo Máx. | Validación | Obligatoriedad |
|-----|-------|-------------|------|------------|------------|----------------|
| | ÁREA `<DetalleAcusedeRecibo>` | DETALLE ACUSE DE RECIBO | | | | 1 |
| 1 | Versión | Versión del formato de Acuse de Recibo. | NUM | 3 | Valor: 1.0 | 1 |
| 2 | RNC del Emisor<br>`<RNCEmisor>` | Número del Registro Nacional del contribuyente que emite el e-CF. | NUM | 9 u 11 | RNC/Cédula cumple con la estructura de formato. | 1 |
| 3 | RNC del Comprador<br>`<RNCComprador>` | Número del Registro Nacional del contribuyente que emite el Acuse de Recibo del e-CF. | NUM | 9 u 11 | RNC/Cédula cumple con la estructura de formato. | 1 |
| 4 | e-NCF<br>`<eNCF>` | Número Comprobante Fiscal Electrónico (e-NCF) | ALFA NUM | 13 | e-NCF cumple con la estructura de formato. | 1 |
| 5 | Estado<br>`<Estado>` | Código de respuesta del Acuse de Recibo. | NUM | 1 | 0: e-CF Recibido<br>1: e-CF No Recibido | 1 |
| 6 | Código Motivo No Recibido<br>`<CodigoMotivoNoRecibido>` | Código numérico que indica el motivo de rechazo del e-CF.<br>Condicional a que el Estado tenga valor 1. | NUM | 1 | Código motivo de No Recibido<br>1: Error de especificación.<br>2: Error de Firma Digital.<br>3: Envío duplicado<br>4: RNC Comprador no corresponde | 2 |
| 7 | Fecha y Hora Generación Acuse de Recibo<br>`<FechaHoraAcuseRecibo>` | Fecha y hora en formato dd-MM-AAAA HH:mm:ss | ALFA NUM | 19 | Fecha y hora cumplen con el formato indicado. | 1 |
| | FIN ÁREA | DETALLE ACUSE DE RECIBO | | | | |

---

## B. Firma Digital

| No. | Campos | Descripción | Tipo | Largo Máx. | Validación | Obligatoriedad |
|-----|--------|-------------|------|------------|------------|----------------|
| | ÁREA `<Signature>` | SIGNATURE | | | | 1 |
| 1 | Firma Digital | Firma digital sobre el archivo de Acuse de Recibo | | | | 1 |
| | FIN ÁREA | SIGNATURE | | | | |
