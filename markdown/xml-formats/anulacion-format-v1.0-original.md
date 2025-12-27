# Formato Anulación de e-NCF

**Versión 1.0**

---

## Bitácora

**Versión 1.0**

Actualizaciones al 24-05-2022  
Modificaciones no implican cambio de versión

• Se elimina de la validación e) de la sección "Detalle de Anulación" lo siguiente: El e-NCF es mayor que el colocado en el campo "Secuencia de e-NCF Desde" de cualquier formato de anulación remitido previamente.

---

## 1. Introducción

El contribuyente podrá anular secuencias autorizadas de comprobantes fiscales electrónicos, si la factura emitida no ha sido enviada a la DGII ni al receptor o si la secuencia no ha sido utilizada, para lo cual deberá emitir un formato XML de anulación de e-NCF descrito en el presente documento.

Si la factura fue enviada a la DGII y/o al receptor, el contribuyente anulará la secuencia emitiendo una Nota de Crédito Electrónica, con las especificaciones establecidas en el formato XML de e-CF.

---

## 2. Contenido del archivo anulación de e-NCF

**a) Encabezado:** esta sección contiene los datos de quién anula, la cantidad de secuencias anuladas y la fecha en que se genera el archivo.

**b) Detalle de Anulación:** en esta sección se informan las secuencias de e-NCF que serán anuladas.

**c) Firma Digital:** que avala la integridad del archivo y autenticidad del emisor.

---

## 3. Códigos de obligatoriedad

**0** - No corresponde: significa que el dato no debe ir en el archivo.

**1** - Dato obligatorio: el dato debe estar siempre en el archivo.

### Secciones del Reporte

| Secciones del Reporte | Obligatoriedad de la Sección |
|-----------------------|------------------------------|
| Encabezado | 1 |
| Detalle de Anulación | 1 |
| Firma Digital | 1 |

A continuación, se describe el contenido de cada sección, las especificaciones de formato para cada campo y los códigos de obligatoriedad para cada uno, que debe tener el archivo de anulación de secuencias.

---

## 4. Formato Anulación de Secuencias de e-NCF

### a) Encabezado

| No. | Nombre del Campo | Descripción | Tipo | Largo Máx. | Validación | Obligatoriedad |
|-----|------------------|-------------|------|------------|------------|----------------|
| | ÁREA `<Encabezado>` | ENCABEZADO | | | | 1 |
| 1 | Versión | Versión del Formato Anulación de e-NCF. | NUM | 3 | Valor: 1.0 | 1 |
| 2 | RNC Emisor<br>`<RncEmisor>` | Corresponde al Número de Registro Nacional del contribuyente que emite la factura electrónica. | NUM | 9 u 11 | a) RNC cumple con la estructura de formato.<br>b) RNC está autorizado como Facturador Electrónico.<br>c) RNC tiene secuencias autorizadas del tipo de e-NCF que está anulando. | 1 |
| 3 | Cantidad de e-NCF Anulados<br>`<CantidadeNCFAnulados>` | Sumatoria de la cantidad de e-NCF que se está reportando en la sección Detalle, de este formato. | NUM | 10 | a) Cantidad de e-NCF Anulados=∑ cantidad de e-NCF anulados por tipo de e-NCF, de la sección Detalle. | 1 |
| 4 | Fecha y Hora Generación Anulación de e-NCF<br>`<FechaHoraAnulacioneNCF>` | Fecha y hora en que se generó el archivo de anulación de secuencias de e-NCF, en formato Formato dd-MM-AAAA HH:mm:ss | ALFA NUM | 19 | a) Formato de fecha y hora cumple con formato dd-MM-AAAA HH:mm:ss | 1 |
| | FIN ÁREA | ENCABEZADO | | | | |

---

### b) Detalle de Anulación

Atendiendo al tipo de comprobante fiscal que se desee anular, la sección puede tener hasta 8 repeticiones.

| No. | Campo | Descripción | Tipo | Largo Máx. | Validación | Obligatoriedad |
|-----|-------|-------------|------|------------|------------|----------------|
| | ÁREA `<DetalleAnulacion>` | DETALLE ANULACIÓN | | | | 1 |
| | ÁREA `<Anulacion>` | ANULACIÓN<br>Se pueden incluir hasta 10 repeticiones. | | | | 1 |
| 1 | Número de Línea<br>`<NoLinea>` | Número de la línea o secuencial. Desde 1 hasta 10 repeticiones. | NUM | 2 | | 1 |
| 2 | Tipo de e-CF<br>`<TipoeCF>` | Tipo Comprobante Fiscal Electrónico (e-CF) | NUM | 2 | a) El tipo de e-CF es:<br>31: Factura de Crédito Fiscal Electrónica<br>32: Factura de Consumo Electrónica<br>33: Nota de Débito Electrónica<br>34: Nota de Crédito Electrónica<br>41: Compras Electrónico<br>43: Gastos Menores Electrónico<br>44: Regímenes Especiales Electrónica<br>45: Gubernamental Electrónico<br>46: Comprobante para Exportaciones Electrónico<br>47: Comprobante para Pagos al Exterior Electrónico | 1 |
| | Tabla Rango de Secuencias Anuladas de e-NCF<br>`<TablaRangoSecuenciasAnuladaseNCF>` | Tabla que contiene un rango de las secuencias anuladas de manera consecutiva, de acuerdo con el tipo de e-CF. Se pueden incluir hasta 10,000 repeticiones. | | | | 1 |
| 3 | Secuencia de e-NCF Desde<br>`<SecuenciaeNCFDesde>` | Se refiere al Número de Comprobante Fiscal Electrónico (e-NCF) con el secuencial que inicia el rango de secuencias que será anulado. | ALFA NUM | 13 | a) El e-NCF cumple con la estructura de formato de número de comprobante fiscal (13 posiciones)¹. Ej.: E310000000001.<br>b) El primer carácter del e-NCF (Serie) está comprendido entre E-Z²<br>c) El tipo de e-CF de la secuencia debe corresponder al indicado en el campo 'Tipo de e-CF'.<br>d) Se debe colocar la secuencia inicial del rango que será anulado. Ej.: Si el rango de secuencias que será anulado es desde E310000000001 hasta E310000000005, se completará el campo 'Secuencia de e-NCF Desde' con el e-NCF E310000000001.<br>e) El e-NCF es menor o igual que la "Secuencia de e-NCF Hasta" y es mayor a cero (>0). | 1 |
| 4 | Secuencia de e-NCF Hasta<br>`<SecuenciaeNCFHasta>` | Se refiere al Número de Comprobante Fiscal Electrónico (e-NCF) con el secuencial que finaliza el rango de secuencias que será anulado. | ALFA NUM | 13 | a) El e-NCF cumple con la estructura de formato de número de comprobante fiscal (13 posiciones)³. Ej.: E310000000001.<br>b) El e-NCF tiene la misma serie y tipo de comprobante fiscal que el colocado en el campo "Secuencia de e-NCF Desde".<br>c) El e-NCF es mayor o igual que el colocado en el campo "Secuencia de e-NCF Desde" y es mayor a cero (>0). | 1 |
| | FIN TABLA | RANGO SECUENCIAS | | | | |
| 5 | Cantidad de e-NCF Anulados<br>`<CantidadeNCFAnulados>` | Cantidad de secuencias de e-NCF que se está anulando.<br>En este campo se deberá sumar las secuencias colocados en la tabla de rangos de secuencias anuladas de e-NCF. | NUM | 10 | a) ∑ cantidad de e-NCF anulados por tipo de e-CF. | 1 |
| | FIN ÁREA | ANULACIÓN | | | | |
| | FIN ÁREA | DETALLE ANULACIÓN | | | | |

---

**¹** La estructura del número de comprobante fiscal electrónico (e-NCF) está compuesta por una serie o letra entre E-Z (exceptuando la letra P), el tipo de comprobante fiscal especificado con 2 dígitos, seguidos del secuencial de 10 dígitos con valor numérico, los cuales indican la cantidad de comprobantes utilizados.

**²** Se exceptúa la letra P.

**³** La estructura del número de comprobante fiscal electrónico (e-NCF) está compuesta por una serie o letra entre E-Z (exceptuando la letra P, el tipo de comprobante fiscal especificado con 2 dígitos, seguidos del secuencial de 10 dígitos con valor numérico, los cuales indican la cantidad de comprobantes utilizados.

---

### c) Firma Digital

| No. | Campos | Descripción | Tipo | Largo Máx. | Validación | Obligatoriedad |
|-----|--------|-------------|------|------------|------------|----------------|
| | ÁREA `<Signature>` | SIGNATURE | | | | 1 |
| 1 | Firma Digital | Firma digital sobre el archivo de Anulación de e-NCF. | | | | 1 |
| | FIN ÁREA | SIGNATURE | | | | |

---

## Anexo I

Ejemplo del formato de anulación de secuencias de e-NCF en las secciones Encabezado y sección Detalle de Anulación.

### A. Encabezado

| No. | Campo | Valor |
|-----|-------|-------|
| 1 | Versión | 1.00 |
| 2 | RNC Emisor | 123456789 |
| 3 | Cantidad de e-NCF Anulados | 84 |
| 4 | Fecha y Hora de la Firma Digital del Archivo de Anulación | 01-01-2019 08:50:15 |

### B. Detalle de Anulación

| No. | Campo | Valor |
|-----|-------|-------|
| 1 | Número de Línea | 1 |
| 2 | Tipo de e-CF | 31 |
| | **Tabla Rango de Secuencias Anuladas** | |
| 3 | Secuencia de e-NCF Desde | E310000000001 |
| 4 | Secuencia de e-NCF Hasta | E310000000001 |
| 3 | Secuencia de e-NCF Desde | E310000000005 |
| 4 | Secuencia de e-NCF Hasta | E310000000050 |
| 5 | Cantidad de e-NCF Anulados | 47 |
| 1 | Número de Línea | 2 |
| 2 | Tipo de e-CF | 44 |
| | **Tabla Rango de Secuencias Anuladas** | |
| 3 | Secuencia de e-NCF Desde | E440000000010 |
| 4 | Secuencia de e-NCF Hasta | E440000000046 |
| 5 | Cantidad de e-NCF Anulados | 37 |
