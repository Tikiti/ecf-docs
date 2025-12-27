# Formato de Resumen Factura de Consumo Electrónica <DOP250,000 (RFCE)

**Versión 1.0 | Enero 2020**

---

## 1. Introducción

Los contribuyentes que emitan facturas de consumo electrónicas menores a DOP$250 mil mediante el Formato de e-CF, deberán enviar a Impuestos Internos las ventas realizadas mediante este tipo de e-CF, en el formato XML que se establece en este documento.

En relación con la factura de consumo electrónica emitida al receptor, deberá cumplir con las especificaciones del Formato del Comprobante Fiscal Electrónico; asimismo el emisor deberá disponer de un mecanismo electrónico para fines de consulta por parte de sus clientes.

---

## 2. Contenido del formato de Factura de Consumo Electrónica <DOP250,000 (envío a DGII)

| Sección | Factura de Consumo < 250mil (32) |
|---------|----------------------------------|
| Encabezado | 1 |
| Firma Digital | 1 |

### Códigos de obligatoriedad:

**1** - Dato obligatorio: el dato debe estar siempre en el documento, independientemente de las características de la transacción.

**2** - Dato condicional: el dato no es obligatorio pero pasa a serlo en determinadas operaciones, si se cumple una determinada condición.

**3** - Opcional. El dato es opcional.

---

## 1.1. Detalle por sección

El contenido de cada sección contendrá el formato y el código de obligatoriedad. A continuación, se especifican:

- **Largo Máximo:** Tamaño máximo del campo. El largo indicado será el largo máximo.
- **Tipo de Documento:** Podrá ser alfa (ALFA), numérica (NUM) o alfanumérica (ALFANUM). En la información tipo numérica, los decimales se separan con punto. No debe separarse los miles con otro tipo de carácter.

---

## A. Encabezado

| No. | Campos | Descripción | Largo Máx. | Tipo | Validación | Factura de Consumo Electrónica (<250mil) 32 |
|-----|--------|-------------|------------|------|------------|---------------------------------------------|
| | ÁREA `<Encabezado>` | ENCABEZADO | | | | 1 |
| 1 | VERSIÓN | Versión del formato utilizado. | 3 | ALFANUM | a) Valor: 1.0 | 1 |
| | ÁREA `<IdDoc>` | IDENTIFICACIÓN DEL DOCUMENTO | | | | 1 |
| 2 | Tipo Comprobante Fiscal Electrónico<br>`<TipoeCF>` | Indica si el documento es:<br>Código Tipo:<br>32: Factura de Consumo Electrónica | 2 | NUM | a) Código Tipo:<br>32: Factura de Consumo Electrónica | 1 |
| 3 | e-NCF<br>`<eNCF>` | Secuencia autorizada por la DGII. | 13 | ALFANUM | a) Número de secuencia autorizada por DGII. | 1 |
| 4 | Tipo de Ingresos<br>`<TipoIngresos>` | Indica el tipo de ingreso recibido, según clasificación del formato de envío de ventas de Bienes o Servicios. | 2 | NUM | Código Tipo:<br>01: Ingresos por operaciones (No financieros).<br>02: Ingresos Financieros<br>03: Ingresos Extraordinarios<br>04: Ingresos por Arrendamientos<br>05: Ingresos por Venta de Activo Depreciable<br>06: Otros Ingresos | 1 |
| 5 | Tipo de Pago<br>`<TipoPago>` | Indica el tipo de pago del cliente. | 1 | NUM | Código Tipo:<br>1: Contado<br>2: Crédito<br>3: Gratuito | 1 |
| | TABLA DE FORMAS DE PAGO¹<br>Hasta 07 repeticiones.<br>Contiene los dos campos siguientes. | | | | | 3 |
| 6 | Forma de Pago<br>`<FormaPago>` | Indica el método en que se pagará la factura. | 2 | NUM | Código Forma:<br>1: Efectivo<br>2: Cheque/Transferencia/Depósito<br>3: Tarjeta de Débito/Crédito<br>4: Venta a Crédito<br>5: Bonos o Certificados de regalo<br>6: Permuta<br>7: Nota de crédito<br>8: Otras Formas de pago | 3 |
| 7 | Monto de Pago<br>`<MontoPago>` | Indica el monto asociado para cada forma de pago.<br>Condicional a que exista una forma de pago. | 18 | NUM | a) Valor numérico de 16 enteros, 2 decimales; ≥ 0 (Debe ser positivo) | 2 |
| | FIN ÁREA | IDENTIFICACIÓN DEL DOCUMENTO | | | | |
| | ÁREA `<Emisor>` | EMISOR | | | | 1 |
| 8 | RNC Emisor<br>`<RNCEmisor>` | Corresponde al RNC del emisor. | 9 u 11 | NUM | Validar en el Registro Nacional de contribuyentes.<br>Se tiene que validar:<br>a) RNC cumpla con estructura de formato.<br>b) RNC esté autorizado como Facturador Electrónico.<br>c) RNC se encuentre en estatus "Activo".<br>d) RNC no posea marcas de bloqueos. | 1 |
| 9 | Nombre o Razón Social Emisor<br>`<RazonSocialEmisor>` | Nombre o Razón Social del emisor. | 150 | ALFANUM | a) Sin validación | 1 |
| 10 | Fecha Emisión<br>`<FechaEmision>` | Fecha de emisión del e-CF. | 10 | ALFANUM | Fecha válida:<br>a) Formato dd-MM-AAAA<br>b) Validar fecha de inicio como facturador electrónico. | 1 |
| | FIN ÁREA | EMISOR | | | | |
| | ÁREA `<Comprador>` | COMPRADOR | | | | 3 |
| 11 | RNC Comprador<br>`<RNCComprador>` | Corresponde al RNC del comprador. | 9 u 11 | NUM | a) Sin validación | 3 |
| 12 | Identificador Extranjero<br>`<IdentificadorExtranjero>`³ | Corresponde al número de identificación cuando el comprador es extranjero y no tiene RNC/Cédula. Condicional a que el comprador sea extranjero. | 20 | ALFA NUM | a) Sin validación | 2 |
| 13 | Nombre o Razón Social<br>`<RazonSocialComprador>` | Nombre o Razón Social del comprador. | 150 | ALFANUM | a) Sin validación | 3 |
| | FIN ÁREA | COMPRADOR | | | | |
| | ÁREA `<Totales>` | TOTALES | | | | 1 |
| 14 | Monto Gravado Total⁴<br>`<MontoGravadoTotal>` | Total de la suma de valores de monto gravado ITBIS a diferentes tasas.<br>Condicional a que exista Monto gravado1, y/o Monto gravado 2 y/o Monto gravado 3. | 18 | NUM | a) Valor numérico de 16 enteros, 2 decimales; ≥ 0 (No puede ser negativo).<br>b) Valor de la suma del Monto Gravado ITBIS Tasa 1 + Monto Gravado ITBIS Tasa 2 + Monto Gravado ITBIS Tasa 3. | 2 |
| 15 | Monto Gravado ITBIS Tasa 1<br>`<MontoGravadoI1>` | Corresponde al total de los montos de ITBIS al 18%, asignados en la factura de consumo electrónica.<br>Condicional a que en la línea de detalle exista algún ítem gravado al 18%. | 18 | NUM | a) Valor numérico de 16 enteros, 2 decimales; ≥ 0 (No puede ser negativo). | 2 |
| 16 | Monto Gravado ITBIS Tasa 2<br>`<MontoGravadoI2>` | Corresponde al total de los montos de ITBIS al 16%, asignados en la factura de consumo electrónica.<br>Condicional a que en la línea de detalle exista algún ítem gravado al 16%. | 18 | NUM | a) Valor numérico de 16 enteros, 2 decimales; ≥ 0 (No puede ser negativo). | 2 |
| 17 | Monto Gravado ITBIS Tasa 3<br>`<MontoGravadoI3>` | Corresponde al total de los montos de ITBIS a tasa cero (0), asignados en la factura de consumo electrónica.<br>Condicional a que en la línea de detalle exista algún ítem gravado a tasa 0. | 18 | NUM | a) Valor numérico de 16 enteros, 2 decimales≥ 0 (No puede ser negativo). | 2 |
| 18 | Monto Exento<br>`<MontoExento>` | Corresponde al total de los montos exentos, asignados en la factura de consumo electrónica.<br>Condicional a que en la línea de detalle exista algún ítem exento. | 18 | NUM | a) Valor numérico de 16 enteros, 2 decimales≥ 0 (No puede ser negativo). | 2 |
| 19 | Total ITBIS<br>`<TotalITBIS>` | Corresponde a la sumatoria total de los montos de ITBIS (en sus diferentes tasas), asignados en la factura de consumo electrónica emitida.<br>Condicional a que el contribuyente indique que existe montos de ITBIS al menos a una de las tasas (1, 2 y/o 3). | 18 | NUM | a) Valor numérico de 16 enteros, 2 decimales; ≥ 0 (No puede ser negativo).<br>b) Valor de la suma del Total ITBIS Tasa1 + Total ITBIS Tasa 2 + Total ITBIS Tasa3. | 2 |
| 20 | Total ITBIS Tasa 1<br>`<TotalITBIS1>` | Corresponde al total de los montos de ITBIS al 18%, asignados en la factura de consumo electrónica.<br>Condicional a que en la línea de detalle exista algún ítem gravado al 18%. | 18 | NUM | a) Valor numérico de 16 enteros, dos decimales; ≥ 0 (No puede ser negativo). | 2 |
| 21 | Total ITBIS Tasa 2<br>`<TotalITBIS2>` | Corresponde al total de los montos de ITBIS al 16%, asignados en la factura de consumo electrónica.<br>Condicional a que en la línea de detalle exista algún ítem gravado al 16% | 18 | NUM | a) Valor numérico de 16 enteros, dos decimales; ≥ 0 (No puede ser negativo). | 2 |
| 22 | Total ITBIS Tasa3<br>`<TotalITBIS3>` | Corresponde al total de los montos de ITBIS tasa cero (0%), asignados en la factura de consumo electrónica.<br>Condicional a que en la línea de detalle exista algún ítem gravado a tasa 0. | 18 | NUM | a) Valor numérico de 16 enteros, dos decimales; ≥ 0 (No puede ser negativo). | 2 |
| 23 | Monto del Impuesto Adicional<br>`<MontoImpuestoAdicional>` | Corresponde a la suma de los campos Monto Impuesto Selectivo al Consumo Específico y Ad Valorem y Monto Otros Impuestos Adicionales, asignados en la factura de consumo electrónica.<br>Condicional a que exista Monto Impuesto Selectivo al Consumo. | 18 | NUM | a)Valor numérico de 16 enteros, dos decimales; >0 (debe ser positivo).<br>b)Valor de la suma del Monto Impuesto Selectivo al Consumo Específico+ Monto Impuesto Selectivo Ad Valorem+ Monto Otros Impuestos Adicionales. | 2 |
| | Tabla de Impuestos Adicionales<br>`<ImpuestosAdicionales>`⁵<br>Se pueden incluir 20 repeticiones de pares código –valor. Incluye los cinco campos siguientes:<br>Condicional a que exista impuestos adicionales en la factura de consumo electrónica. | | | | | 2 |
| 24 | Código de Impuesto Adicional<br>`<TipoImpuesto>` | Dato correspondiente al Código del impuesto adicional de acuerdo con la Tabla I (Codificación Tipos de Impuestos Adicionales) del formato de comprobante fiscal electrónico (e-CF), asignada a la factura de consumo electrónica. | 3 | NUM | a) Validar con Tabla I (Codificación Tipos de Impuestos Adicionales)⁶ | 2 |
| 25 | Monto Impuesto Selectivo al Consumo Específico<br>`<MontoImpuestoSelectivoConsumoEspecifico>` | Valor del impuesto selectivo al consumo (ISC) específico asociado al código de impuesto adicional.<br>Condicional a que el contribuyente indique que existe impuesto selectivo al consumo específico, en la factura de consumo electrónica emitida. | 18 | NUM | a) Valor numérico de 16 enteros, dos decimales; >0 (debe ser positivo). | 2 |
| 26 | Monto Impuesto Selectivo al Consumo Ad Valorem<br>`<MontoImpuestoSelectivoConsumoAdvalorem>` | Valor del impuesto selectivo al consumo (ISC) Ad-Valorem asociado al código de impuesto adicional.<br>Condicional a que el contribuyente indique que existe impuesto selectivo Ad-valorem, en la factura de consumo electrónica emitida. | 18 | NUM | a) Valor numérico de 16 enteros, dos decimales; >0 (debe ser positivo). | 2 |
| 27 | Monto Otros Impuestos Adicionales<br>`<OtrosImpuestosAdicionales>` | Valor de Otros Impuestos Adicionales asociado al código de impuesto adicional.<br>Condicional a que el contribuyente indique que existe otros impuestos adicionales, en la factura de consumo electrónica emitida. | 18 | NUM | a) Valor numérico de 16 enteros, dos decimales; >0 (debe ser positivo). | 2 |
| | FIN TABLA | IMPUESTOS ADICIONALES | | | | |
| 28 | Monto Total<br>`<MontoTotal>` | Valor de la suma de los campos Monto Gravado Total + Monto exento +Total ITBIS + Monto del Impuesto adicional, asignados a la factura de consumo electrónica. | 18 | NUM | a) Valor numérico de 16 enteros, dos decimales; ≥ 0 (No puede ser negativo)<br>b) Valor de la suma del Monto Gravado Total + Monto Exento +Total ITBIS + Monto del Impuesto Adicional. | 1 |
| 29 | Monto no Facturable<br>`<MontoNoFacturable>` | Corresponde al total del monto no facturable, asignados en la factura de consumo electrónica.<br>Condicional a que el contribuyente indique que existe monto no facturable, en la factura de consumo electrónica emitida. | 18 | NUM | a) Valor numérico de 16 enteros, dos decimales. (Puede ser negativo) | 2 |
| 30 | Monto Período<br>`<MontoPeriodo>` | Corresponde al total del monto periodo, asignados en la factura de consumo electrónica. | 18 | NUM | a) Valor numérico de 16 enteros, dos decimales. (Puede ser negativo)<br>b) Monto período= Monto Total+Monto No Facturable. | 3 |
| | FIN ÁREA | TOTALES | | | | |
| 31 | Código Seguridad Factura de Consumo DOP$<250 M<br>`<CodigoSeguridadeCF>` | Corresponde a los 6 primeros caracteres del Hash de la firma digital correspondiente a la factura de consumo electrónica emitida, menor a DOP$250 M. | 6 | ALFANUM | a) Sin validación | 1 |
| | FIN ÁREA | ENCABEZADO | | | | |

---

**¹** Por definición del XML, para cada elemento debe existir un tag contenedor que agrupe los campos contenidos en una tabla. Ejemplo: en el caso de la `<TablaFormasPago>` se agrupan dentro del tag `<FormaDePago>` por cada par `<FormaPago>` y `<MontoPago>` especificado.

**³** Si es completado el campo 'Identificador Extranjero', el campo 'RNC Comprador' debe ir en blanco.

**⁴** En los campos donde existan valores numéricos de 16 enteros y 2 decimales, se debe aplicar la regla de redondeos según el Informe Técnico de e-CF.

**⁵** Ver nota 2.

**⁶** De acuerdo con la Tabla de 'Codificación Tipos de Impuestos Adicionales', incluida en el documento del Formato de e-CF.

---

## B. FIRMA DIGITAL

| No. | Campos | Descripción | Largo Máx. | Tipo | Validación | Obligatoriedad |
|-----|--------|-------------|------------|------|------------|----------------|
| | ÁREA `<Signature>` | SIGNATURE | | | | 1 |
| 1 | Firma Digital | Firma digital sobre todo el documento. | | | | 1 |
| | FIN ÁREA | SIGNATURE | | | | |
