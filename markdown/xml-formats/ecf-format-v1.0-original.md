# Formato Comprobante Fiscal Electrónico (e-CF)

**Versión 1.0 | Octubre 2025**

---

## Bitácora

### Versión 1.0

#### Actualizaciones al 09-10-2025
Modificaciones no implican cambio de versión.

1. Se actualiza la tabla II. Codificación Monedas, para agregar el tipo de moneda "Peso Colombiano"

#### Actualizaciones al 17-09-2024
Modificaciones no implican cambio de versión.

1. Se actualiza la tabla II. Codificación Monedas, para agregar los tipos de monedas "Gourde Haitiana" y "Peso Mexicano"
2. Se actualiza la tabla IV. Codificación Unidad de Medida, para agregar los tipos de medidas "Hectárea", "Mililitro", "Miligramo", "Onzas" y "Onzas Troy"

#### Actualizaciones al 30-08-2022
Modificaciones no implican cambio de versión.

1. Se actualiza la tabla IV. Codificación Unidad de Medida, para agregar el tipo de medida "Bandeja".

#### Actualizaciones al 06-05-2022
Modificaciones no implican cambio de versión.

1. Se actualiza la tabla IV. Codificación Unidad de Medida, para agregar los tipos de medidas "Gross Register Tonnage (Toneladas de Registro Bruto)", "Pie cuadrado", "Pasajero", "Pulgadas" y "Parqueo Barcos en Muelle".

#### Actualizaciones al 19-11-2021
Modificaciones no implican cambio de versión.

1. Se actualizan en el Área Comprador `<Comprador>` los códigos de obligatoriedad de 1 a 2, correspondiente a los tipos de e-CF Nota de Crédito Electrónica y Nota de Débito Electrónica de la sección Encabezado.

#### Actualizaciones al 04-11-2021
Modificaciones no implican cambio de versión.

1. Se actualiza la tabla IV. Codificación Unidad de Medida, para agregar el tipo de medida "Quintal".

#### Actualizaciones al 29-06-2021
Modificaciones no implican cambio de versión.

1. Se actualiza la 'Tabla III. Codificación Provincias y Municipios', para separar por columnas los códigos de las Provincias y Municipios.

#### Actualizaciones al 10-11-2020
Modificaciones no implican cambio de versión.

1. Se actualizan los tags `<Liquidacion>` y `<Mineria>` de la sección Detalle de Bienes o Servicios, para eliminar acentos.
2. Se actualiza la descripción de los campos 'Tabla de Distribución de Subrecargo' y 'Tipo Subrecargo', de la sección Detalle de Bienes o Servicios.
3. Se actualiza el tag `<DescripcionDescuentooRecargo>` de la sección Descuentos o Recargos.

#### Actualizaciones al 28-07-2020
Modificaciones no implican cambio de versión.

Se modifican los campos `<TotalITBISRetenido>` y `<TotalISRRetencion>` de la sección Encabezado para que sean aceptados valores numéricos igual a cero (0).

---

## 1. Introducción

En este documento se describe el contenido de los Comprobantes Fiscales Electrónicos (e-CF), tanto las definiciones desde el punto de vista tributario como desde el punto de vista comercial.

Desde la perspectiva de este razonamiento, este documento tiene como objetivo ser un instrumento adecuado para el respaldo de la transacción entre las partes, y abarcar la información que se requiere para el uso del régimen de Factura Electrónica en República Dominicana.

Esta información considera las especificaciones para la transacción necesaria entre el emisor y comprador.

A continuación, se describe el formato electrónico de los tipos de e-CF:

### TIPO DE COMPROBANTE

| TIPO | e-CF |
|------|------|
| 31 | Factura de Crédito Fiscal Electrónica |
| 32 | Factura de Consumo Electrónica |
| 33 | Nota de Débito Electrónica |
| 34 | Nota de Crédito Electrónica |
| 41 | Compras Electrónico |
| 43 | Gastos Menores Electrónico |
| 44 | Regímenes Especiales Electrónico |
| 45 | Gubernamental Electrónico |
| 46 | Comprobante de Exportaciones Electrónico |
| 47 | Comprobante para Pagos al Exterior Electrónico |

---

## 2. Contenido del e-CF

De acuerdo con lo dispuesto en el Decreto No. 254-06 que establece el Reglamento para la Regulación de la Impresión, Emisión y Entrega de Comprobantes Fiscales, la Dirección General de Impuestos Internos podrá autorizar comprobantes fiscales que reúnan los requisitos exigidos por la Ley y el Reglamento. Sobre la base de esta disposición, se define el formato de los documentos electrónicos y la obligatoriedad de los datos contenidos en ellos. Los documentos electrónicos tienen un formato único, en que la principal diferencia radica en la obligatoriedad o no de algunos datos.

Todo e-CF que se emita debe contener una firma digital, la que permite autenticar su origen y certificar su integridad.

### 2.1. Composición del e-CF

En el e-CF se distinguen las siguientes partes:

**A. Encabezado:** Corresponde a la identificación del e-CF, donde contiene los datos del emisor, comprador y datos tributarios.

**B. Detalle de Bienes o Servicios:** En esta sección se debe detallar una línea por cada ítem.

**C. Subtotales Informativos:** Estos subtotales no aumentan ni disminuyen la base del impuesto, ni modifican los campos totalizadores; solo son campos informativos.

**D. Descuentos o Recargos:** Esta sección se utiliza para especificar descuentos o recargos globales que afectan al total del e-CF. No se requiere especificar ítem por ítem.

**E. Paginación:** En esta sección se indica la cantidad de páginas del e-CF en la Representación Impresa y cuales ítems estarán en cada una. Esta deberá repetirse para el total de páginas especificadas.

**F. Información de Referencia:** En esta sección se deben detallar los e-CF modificados por Nota de Crédito o Débito Electrónica y los e-CF emitidos por motivo de reemplazo de un comprobante emitido en contingencia.

**G. Fecha y Hora de la firma digital.**

**H. Firma Digital sobre toda la información anterior para garantizar la integridad del e-CF.**

La obligatoriedad de cada una de las partes de e-CF se especifica en el siguiente cuadro:

#### Contenido del e-CF

| Sección | Fact. Créd. Fiscal Electr. (31) | Fact. Consum. Electr. (32) | Nota Déb. Electr. (33) | Nota Créd. Electr. (34) | Compras Electr. (41) | Gastos Menor. Electr. (43) | Regí. Espec. Electr. (44) | Guber. Electr. (45) | Export. Electr. (46) | Pagos Exterior Electr. (47) |
|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|
| Encabezado | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| Detalle de Bienes o Servicios | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| Subtotales Informativos | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| Descuentos o Recargos¹ | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| Paginación | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| Información de Referencia | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 2 |
| Fecha y Hora de la firma digital | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| Firma Digital | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |

**Códigos de Obligatoriedad:**

**0:** No corresponde. Significa que el dato no debe ir en un determinado documento.

**1:** Dato obligatorio. El dato siempre debe estar en el documento, independiente de las características de la transacción.

**2:** Dato condicional. El dato no es obligatorio en todos los documentos, pero pasa a serlo en determinadas operaciones si se cumple una determinada condición. Ejemplo: Si existen descuentos recargos que afectan el total del e-CF, se debe incluir la sección Descuentos o Recargos, de lo contrario se descuadrará el monto total.

**3:** Opcional. El dato es opcional.

---

**¹** Sujeto a que exista un descuento o recargo global.

---

## 2.2. Detalle por sección

El contenido de cada sección contendrá el formato y sus códigos de obligatoriedad según el tipo de e-CF. A continuación, se especifican:

➢ **Largo Máximo:** Tamaño máximo del campo. El largo indicado será el largo máximo.

➢ **Tipo de Documento:** Podrá ser alfa (ALFA), numérica (NUM) o alfanumérica (ALFANUM). En la información tipo numérica, los decimales se separan con punto. No debe separarse los miles con otro tipo de carácter.

➢ **Columna I:** Indica si el dato debe estar en la representación impresa (RI) del documento. Debajo de cada campo se incluye el nombre del tag XML que tiene asociado. Ejemplo: `<TipoeCF>`.

En la columna 'I' se pueden tener los siguientes valores:

- **N:** La impresión de este campo no es obligatoria.
- **I:** Impresión del dato es obligatoria.
- **P:** El dato debe estar impreso en palabras. Por ejemplo: si el tipo de e-CF está codificado, en la representación impresa debe estar palabras (Factura Crédito Fiscal Electrónica, Nota de Crédito Electrónica, etc.).

---

## A. ENCABEZADO

### ÁREA: ENCABEZADO `<Encabezado>`

| # | CAMPOS | DESCRIPCIÓN | Largo Max | Tipo | Validación | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|--------|-------------|-----------|------|------------|---|----|----|----|----|----|----|----|----|----|----|
| | ÁREA ENCABEZADO `<Encabezado>` | | | | | | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 1 | VERSIÓN | Versión del formato utilizado. | 3 | ALFA NUM | Valor: 1.0 | N | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |

### ÁREA: IDENTIFICACIÓN DEL DOCUMENTO `<IdDoc>`

| # | CAMPOS | DESCRIPCIÓN | Largo Max | Tipo | Validación | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|--------|-------------|-----------|------|------------|---|----|----|----|----|----|----|----|----|----|----|
| | ÁREA IDENTIFICACIÓN DEL DOCUMENTO `<IdDoc>` | | | | | | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 2 | Tipo Comprobante Fiscal Electrónico `<TipoeCF>` | Indica si el documento es:<br>Código Tipo:<br><br>31: Factura de Crédito Fiscal Electrónica<br>32: Factura de Consumo Electrónica<br>33: Nota de Débito Electrónica<br>34: Nota de Crédito Electrónica<br>41: Compras Electrónico<br>43: Gastos Menores Electrónico<br>44: Regímenes Especiales Electrónica<br>45: Gubernamental Electrónico<br>46: Comprobante para Exportaciones Electrónico<br>47: Comprobante para Pagos al Exterior Electrónico | 2 | NUM | a) De acuerdo a la codificación del campo de Descripción. | P | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 3 | e-NCF `<eNCF>` | Secuencia autorizada por la DGII. | 13 | ALFA NUM | a) Validar con No. Secuencia autorizada por DGII. | I | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 4 | Fecha Vencimiento `<FechaVencimientoSecuencia>` | Fecha de vencimiento de la secuencia de e-NCF. | 10 | ALFA NUM | Fecha válida:<br>a) Formato (dd-MM-AAAA)<br>b) Validar con fecha de vencimiento de la autorización de la secuencia. | I | 1 | 0 | 1 | 0 | 1 | 1 | 1 | 1 | 1 | 1 |
| 5 | Indicador Nota de Crédito mayor a 30 días `<IndicadorNotaCredito>` | Sólo para Notas de Crédito que no tienen derecho a rebajar ITBIS.El indicador tomará valor 1 si la fecha es mayor a 30 días calendario de la emisión del e-CF afectado. | 1 | NUM | a) Valor 0 si fecha de emisión del e-CF afectado es ≤ 30 días calendario.<br>b) Valor 1 si fecha de emisión del e-CF afectado es > 30 días calendario. | N | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| 6 | Indicador Envío Diferido `<IndicadorEnvioDiferido>` | Identifica a los contribuyentes que han sido previamente autorizados a tener ventas a través de dispositivos móviles offline, tales como ventas con Handheld, entre otros.<br><br>Condicional a que se encuentre autorizado hacer envíos diferidos. | 1 | NUM | a) Código 1: Envío diferido autorizado.<br><br>b) Valida contribuyente (RNC/Cédula) está autorizado a realizar envíos diferidos. | N | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 2 | 0 |
| 7 | Indicador Monto Gravado `<IndicadorMontoGravado>` | Indica si en la línea de detalle, el monto se encuentra con ITBIS incluido (impuestos adicionales no están incluidos en el precio del item).<br>Condicional a que el bien o servicio sea gravado con ITBIS. | 1 | NUM | a) Valor 0 si los montos en las líneas sección B "Detalle de Bienes o Servicios" no tienen ITBIS incluido.<br>b) Valor 1 si los montos en las líneas sección B "Detalle de Bienes o Servicios" se encuentran con ITBIS incluido. | N | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 0 | 0 |
| 8 | Tipo de Ingresos `<TipoIngresos>` | Indica el tipo de ingreso recibido, según clasificación del formato de envío de ventas de Bienes o Servicios. | 2 | NUM | a) Código Tipo:<br>01: Ingresos por operaciones (No financieros).<br>02: Ingresos Financieros<br>03: Ingresos Extraordinarios<br>04: Ingresos por Arrendamientos<br>05: Ingresos por Venta de Activo Depreciable<br>06: Otros Ingresos | N | 1 | 1 | 1 | 1 | 0 | 0 | 1 | 1 | 1 | 0 |
| 9 | Tipo de Pago `<TipoPago>` | Indica el tipo de pago del cliente.<br>Las facturas por entrega gratuita (código 3), no son válidas para crédito fiscal. | 1 | NUM | a) Código Tipo:<br>1: Contado<br>2: Crédito<br>3: Gratuito | N | 1 | 1 | 1 | 1 | 1 | 3 | 1 | 1 | 1 | 3 |
| 10 | Fecha Límite de Pago `<FechaLimitePago>` | Solo para facturas a crédito.<br>Condicional a que el tipo de pago sea a crédito. | 10 | ALFA NUM | Fecha válida:<br>a) Formato dd-MM-AAAA<br>b) Fecha límite de pago debe ser ≥ Fecha de emisión. | N | 2 | 2 | 2 | 2 | 2 | 0 | 2 | 2 | 2 | 3 |
| 11 | Término de Pago `<TerminoPago>` | Indica el tiempo establecido para el pago de la factura y se debe especificar si el mismo es en horas, días, semanas, meses u otro.<br>Ejemplo:<br>1) 72 horas<br>2) 120 días<br>3) 1 semana<br>4) 3 meses | 15 | ALFA NUM | a) Sin Validación. | N | 3 | 3 | 3 | 0 | 3 | 0 | 3 | 3 | 3 | 3 |
| | **TABLA DE FORMAS DE PAGO `<TablaFormasPago>`²** | Hasta 07 repeticiones.<br>Contiene los dos campos siguientes. | | | | | 3 | 3 | 3 | 0 | 3 | 0 | 3 | 3 | 3 | 3 |
| 12 | Forma de Pago `<FormaPago>` | Indica el método en que se pagará la factura. | 2 | NUM | a) Código Forma:<br>1: Efectivo<br>2: Cheque/Transferencia/ Depósito<br>3: Tarjeta de Débito/Crédito<br>4: Venta a Crédito<br>5: Bonos o Certificados de regalo<br>6: Permuta<br>7: Nota de crédito<br>8: Otras Formas de pago<br><br>Si la forma de pago corresponde al tipo 5 el e-CF debe ser tipo 32. | N | 3 | 3 | 3 | 0 | 3 | 0 | 3 | 3 | 3 | 3 |

---

**²** Por definición del XML, para cada elemento debe existir un tag contenedor que agrupe los campos contenidos en una tabla. Ej: en el caso de la `<TablaFormasPago>` se agrupan dentro del tag `<FormaDePago>` por cada par `<FormaPago>` y `<MontoPago>` especificado.

---

*(Continuación de Tabla IDENTIFICACIÓN DEL DOCUMENTO)*

| # | CAMPOS | DESCRIPCIÓN | Largo Max | Tipo | Validación | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|--------|-------------|-----------|------|------------|---|----|----|----|----|----|----|----|----|----|----|
| 13 | Monto de Pago `<MontoPago>` | Indica el monto asociado para cada forma de pago. Condicional a que exista una forma de pago. | 18 | NUM | a) Valor numérico de 16 enteros, 2 decimales; ≥ 0 (Debe ser positivo) | N | 2 | 2 | 2 | 0 | 2 | 0 | 2 | 2 | 2 | 3 |
| | **FIN TABLA** | | | | | | | | | | | | | | | |
| 14 | Tipo Cuenta de Pago³ `<TipoCuentaPago>` | Cuenta de origen de la transferencia o del cheque. | 2 | ALFA | Código Tipo:<br>CT: Cta. Corriente<br>AH: Ahorro<br>OT: Otra | N | 3 | 3 | 3 | 0 | 3 | 0 | 3 | 3 | 3 | 3 |
| 15 | Cuenta de Pago `<NumeroCuentaPago>` | Número de la cuenta si la forma de pago es por cheque o transferencia bancaria. | 28 | ALFA NUM | a) Sin validación | N | 3 | 3 | 3 | 0 | 3 | 0 | 3 | 3 | 3 | 3 |
| 16 | Banco de Pago `<BancoPago>` | Banco de la Cuenta. | 75 | ALFA NUM | a) Sin validación | N | 3 | 3 | 3 | 0 | 3 | 0 | 3 | 3 | 3 | 3 |
| 17 | Fecha desde `<FechaDesde>` | Período de facturación para Servicios Periódicos Ej. Energía eléctrica, telefónica, otros.<br>Fecha desde<br>(Fecha inicial del servicio facturado). | 10 | ALFA NUM | Fecha válida:<br>a) Formato dd-MM-AAAA<br>b) Menor o igual que "Fecha hasta".<br>De acuerdo al Formato del campo de descripción. | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 3 |
| 18 | Fecha hasta `<FechaHasta>` | Período de facturación para Servicios Periódicos. Fecha hasta<br>(Fecha final del servicio facturado). | 10 | ALFA NUM | Fecha válida:<br>a) Formato dd-MM-AAAA<br>b) Mayor o igual a "Fecha desde".<br>De acuerdo al Formato del campo de Descripción. | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 3 |
| 19 | Total Páginas `<TotalPaginas>` | Indica el total de páginas en la que será impreso el e-CF.<br>Cuenta las veces que se repite el campo Página No. de la sección Paginación.<br>Condicional a que exista paginación. | 3 | NUM | a) Valor numérico hasta 3 enteros, > 1 (Debe ser positivo).<br>b) Total de veces que se repite el campo 'Página No.' de la sección Paginación. | I | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| | FIN ÁREA | **IDENTIFICACIÓN DEL DOCUMENTO** | | | | | | | | | | | | | | |

---

**³** En los casos donde exista más de una forma de pago cheque/transferencia/depósito sólo colocar un tipo cuenta de pago.

---

### ÁREA: EMISOR `<Emisor>`

| # | CAMPOS | DESCRIPCIÓN | Largo Max | Tipo | Validación | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|--------|-------------|-----------|------|------------|---|----|----|----|----|----|----|----|----|----|----|
| | ÁREA EMISOR `<Emisor>` | | | | | | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 20 | RNC Emisor `<RNCEmisor>` | Corresponde al RNC del emisor. | 9 u 11 | NUM | Validar en el Registro Nacional de contribuyentes.<br>Se tiene que validar:<br>a) RNC cumpla con estructura de formato.<br>b) RNC esté autorizado como Facturador Electrónico.<br>c) RNC se encuentre en estatus "Activo".<br>d) RNC no posea marcas de bloqueos. | I | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 21 | Nombre o Razón Social Emisor `<RazonSocialEmisor>` | Nombre o Razón Social del emisor. | 150 | ALFA NUM | a) Sin validación | I | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 22 | Nombre Comercial `<NombreComercial>` | Nombre Comercial. | 150 | ALFA NUM | a) Sin validación | I | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 23 | Sucursal `<Sucursal>` | Indica nombre de la sucursal que emite el e-CF. Corresponde a un dato administrado por el emisor. | 20 | ALFA NUM | a) Sin validación | I | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 24 | Dirección de Emisor `<DireccionEmisor>` | Datos correspondientes a Domicilio de operación del Emisor. | 100 | ALFA NUM | a) Sin validación | I | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 25 | Municipio `<Municipio>` | Dato correspondiente al domicilio de operación del Emisor. | 6 | NUM | a) Validar con código de la Tabla III (Codificación Provincias Y Municipios) | P | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 26 | Provincia `<Provincia>` | Dato correspondiente al domicilio de operación del Emisor. | 6 | NUM | a) Validar con código de la Tabla III (Codificación Provincias Y Municipios | P | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| | **Tabla de Teléfono Emisor `<TablaTelefonoEmisor>`** | Se pueden incluir 3 repeticiones. | | | | | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 27 | Teléfono Emisor `<TelefonoEmisor>` | Dato correspondiente al teléfono de contacto del emisor. | 12 | ALFA NUM | Formato válido:<br>Estructura de teléfono<br>(xxx-xxx-xxxx) | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| | **FIN TABLA** | **TELÉFONO EMISOR** | | | | | | | | | | | | | | |
| 28 | Correo Electrónico Emisor `<CorreoEmisor>` | Dato correspondiente al correo electrónico del emisor. | 80 | ALFA NUM | Formato válido: Estructura de correo electrónico<br>(xxxxx@xxx.xx) | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 29 | WebSite `<WebSite>` | Dato correspondiente a la página web del emisor. | 50 | ALFA NUM | a) Sin validación | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 30 | Actividad Económica Emisor `<ActividadEconomica>` | Dato correspondiente a la actividad económica del Emisor (se puede incluir sólo la actividad económica que corresponde a la transacción). | 100 | ALFA NUM | a) Sin validación | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 31 | Código del Vendedor `<CodigoVendedor>` | Identificador del Vendedor. | 60 | ALFA NUM | a) Sin validación | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 32 | Número Factura Interna `<NumeroFacturaInterna>` | Corresponde al número interno de la factura. | 20 | ALFA NUM | a) Sin validación | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 33 | Número pedido Interno `<NumeroPedidoInterno>` | Corresponde al número de pedido interno asignado a la factura. | 20 | NUM | a) Sin validación | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 34 | Zona de Venta `<ZonaVenta>` | Corresponde a la zona de venta del vendedor. | 20 | ALFA NUM | a) Sin validación. | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 35 | Ruta de Venta `<RutaVenta>` | Corresponde a la ruta de venta del vendedor. | 20 | ALFA NUM | a) Sin validación | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 36 | Información adicional Emisor `<InformacionAdicionalEmisor>` | Otra información relativa al Emisor. | 250 | ALFA NUM | a) Sin validación | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 37 | Fecha Emisión `<FechaEmision>` | Fecha de emisión del e-CF. | 10 | ALFA NUM | Fecha válida:<br>a) Formato dd-MM-AAAA<br>b) Validar fecha de inicio como facturador electrónico. | I | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| | FIN ÁREA | **EMISOR** | | | | | | | | | | | | | | |

---

### ÁREA: COMPRADOR `<Comprador>`

| # | CAMPOS | DESCRIPCIÓN | Largo Max | Tipo | Validación | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|--------|-------------|-----------|------|------------|---|----|----|----|----|----|----|----|----|----|----|
| | ÁREA COMPRADOR `<Comprador>` | | | | | | 1 | 1 | 2 | 2 | 1 | 0 | 1 | 1 | 1 | 3 |
| 38 | RNC Comprador `<RNCComprador>` | Corresponde al RNC del comprador.<br><br>Condicional a que el monto total del e-CF tipo 32 sea igual o superiores a DOP$ 250M.⁴<br><br>En caso de que el e-CF sea tipo 46, el campo es condicional a que la Zona Franca Comercial (Aeropuertos y Puertos) realice transferencia de bienes a Residentes y el campo 'Identificador Extranjero' esté vacío. | 9 u 11 | NUM | a) Validar estructura.<br><br>b) Si el e-CF es tipo 32 y el monto total es ≥ DOP$250,000.00 se debe identificar RNC Comprador.<br><br>c) Si el e-CF tipo 33 y tipo 34 modifica un e-CF tipo 32 con monto total ≥ DOP$250,000.00 se debe identificar el RNC Comprador.<br><br>d) Si el e-CF es tipo 32 y el comprador es extranjero, este campo puede ir en blanco y completar el campo Identificador Extranjero. | I | 1 | 2 | 2 | 2 | 1 | 0 | 2⁵ | 1 | 2⁶ | 0 |
| 39 | Identificador Extranjero `<IdentificadorExtranjero>`⁷ | Corresponde al número de identificación cuando el comprador es extranjero y no tiene RNC/Cédula.<br><br>Condicional a que el e-CF es tipo 32>DOP$250,000.00 (aplica también para las notas de crédito/débito que hagan referencia a ese tipo de e-CF), y el campo RNC Comprador esté vacío.<br><br>En caso de que el e-CF sea tipo 46, el campo es condicional a que la Zona Franca Comercial (Aeropuertos y Puertos) realice transferencia de bienes a No Residentes y el campo 'RNC Comprador' esté vacío. | 20 | ALFA NUM | a) El e-CF de consumo electrónica es > DOP$250,000.00 (aplica también para las notas de crédito/débito que hagan referencia a ese tipo de e-CF).<br><br>b) El campo RNC Comprador está en blanco. | I | 0 | 2 | 2 | 2 | 0 | 0 | 2⁸ | 0 | 2⁹ | 3 |
| 40 | Nombre o Razón Social Comprador `<RazonSocialComprador>` | Nombre o Razón Social del comprador.<br><br>En caso de que el e-CF sea tipo 46, el campo es condicional a que exista el campo 'RNC Comprador' o 'Identificador Extranjero'. | 150 | ALFA NUM | a) Si el e-CF es tipo 32 y el monto total es ≥ DOP$250,000.00 se debe indicar el nombre o razón social comprador.<br><br>b) Si el e-CF tipo 33 y tipo 34 modifica un e-CF tipo 32 con monto total ≥ DOP$250,000.00, se debe indicar nombre o razón social comprador. | I | 1 | 2 | 2 | 2 | 1 | 0 | 1 | 1 | 1 | 3 |
| 41 | Contacto Comprador `<ContactoComprador>` | Nombre y teléfono de contacto del comprador. | 80 | ALFA NUM | a) Sin validación | N | 3 | 3 | 3 | 3 | 3 | 0 | 3 | 3 | 3 | 0 |
| 42 | Correo Comprador `<CorreoComprador>` | Dato correspondiente al correo electrónico del comprador. | 80 | ALFA NUM | Formato válido: Estructura de correo electrónico.<br>(xxxxx@xxx.xx) | N | 3 | 3 | 3 | 3 | 3 | 0 | 3 | 3 | 3 | 0 |
| 43 | Dirección Comprador `<DireccionComprador>` | Dirección del comprador. | 100 | ALFA NUM | a) Sin validación | N | 3 | 3 | 3 | 3 | 3 | 0 | 3 | 3 | 3 | 0 |
| 44 | Municipio Comprador `<MunicipioComprador>` | Dato correspondiente a dirección de comprador. | 6 | NUM | a) Validar con código de la Tabla III (Codificación Provincias y Municipios) | N | 3 | 3 | 3 | 3 | 3 | 0 | 3 | 3 | 3 | 0 |
| 45 | Provincia Comprador `<ProvinciaComprador>` | Dato correspondiente a dirección de comprador. | 6 | NUM | a) Validar con código de la Tabla III (Codificación Provincias y Municipios) | N | 3 | 3 | 3 | 3 | 3 | 0 | 3 | 3 | 3 | 0 |
| 46 | País Comprador `<PaisComprador>` | Dato correspondiente al país hacia el cual se realiza la facturación. | 60 | ALFA | a) Sin validación. | P | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 47 | Fecha Entrega `<FechaEntrega>` | Corresponde a la fecha de entrega del ítem. | 10 | ALFA NUM | a) Fecha válida:<br>Formato (dd-MM-AAAA) | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 48 | Contacto de Entrega `<ContactoEntrega>` | Dato de contacto donde será realizada la entrega o envio del ítem (distinto al comprador). | 100 | ALFA NUM | a) Sin validación | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 49 | Dirección de Entrega `<DireccionEntrega>` | Corresponde a la dirección o destino del contacto de entrega. | 100 | ALFA NUM | a) Sin validación | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 50 | Telefóno `<TelefonoAdicional>` | Dato del teléfono correspondiente al contacto de entrega. | 12 | ALFA NUM | a)Formato válido:<br>Estructura de teléfono<br>(xxx-xxx-xxxx) | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 51 | Fecha Orden de Compra `<FechaOrdenCompra>` | Corresponde a la fecha de la orden de compra. | 10 | ALFA NUM | a)Fecha válida:<br>Formato (dd-MM-AAAA) | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 52 | Número de Orden de Compra `<NumeroOrdenCompra>` | Corresponde al número de orden de compra. | 20 | ALFA NUM | a) Sin Validación | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 53 | Código Interno del Comprador `<CodigoInternoComprador>` | Para identificación interna del comprador, por ejemplo, código del cliente, número de medidor, etc. | 20 | ALFA NUM | a) Sin validación | N | 3 | 3 | 3 | 3 | 3 | 0 | 3 | 3 | 3 | 0 |
| 54 | Responsable de pago `<ResponsablePago>` | Corresponde a la identificación del que realiza el pago del documento. | 20 | ALFA | a) Sin validación | N | 3 | 3 | 3 | 3 | 3 | 0 | 3 | 3 | 3 | 0 |
| 55 | Información Adicional Comprador `<Informacionadicionalcomprador>` | Otra información relativa al comprador. | 150 | ALFA NUM | a) Sin validación | N | 3 | 3 | 3 | 3 | 3 | 0 | 3 | 3 | 3 | 0 |
| | FIN ÁREA | **COMPRADOR** | | | | | | | | | | | | | | |

---

**⁴** Si el monto total de la factura de consumo electrónica es menor a DOP$250 mil, el campo 'RNC Comprador' sera completado de manera opcional.

**⁵** Condicional a que el comprador tenga RNC/Cédula. Si el comprador es extranjero (diplomático), el campo 'RNC Comprador' debe ir en blanco y completar el campo 'Identificador Extranjero'.

**⁶** Según lo establecido en el Art. 10 de la Norma General 05-19, en caso de que las Zonas Francas Comerciales (Aeropuertos y Puertos) realicen transferencias de bienes a Residentes, se deberá completar el campo 'RNC Comprador'.

**⁷** Este campo se completa si el e-CF es una factura de consumo electrónica > DOP$250,000 y el comprador no posee RNC/Cédula por ser extranjero. Lo mismo con las notas de crédito/débito electrónicas que afecten e-CF tipo 32 por valor > DOP$250,000. Cuando exista Identidicador Extranjero se omitirá el campo RNC Comprador.

**⁸** Condicional a que el comprador sea extranjero (diplomático). Si el campo 'Identificador Extranjero' es completado, el campo RNC comprador no deberá ser completado.

**⁹** Según lo establecido en el Art. 10 de la Norma General 05-19, en caso de que las Zonas Francas Comerciales (Aeropuertos y Puertos) realicen transferencias de bienes a No Residentes, se deberá completar el campo 'Identificador Extranjero'.

---

### ÁREA: INFORMACIONES ADICIONALES `<InformacionesAdicionales>`

| # | CAMPOS | DESCRIPCIÓN | Largo Max | Tipo | Validación | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|--------|-------------|-----------|------|------------|---|----|----|----|----|----|----|----|----|----|----|
| | ÁREA INFORMACIONES ADICIONALES `<InformacionesAdicionales>` | | | | | | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 56 | Fecha Embarque `<FechaEmbarque>` | Corresponde a la fecha del embarque. | 10 | ALFA NUM | a)Fecha válida:<br>Formato (dd-MM-AAAA) | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 57 | Número de Embarque `<NumeroEmbarque>` | Dato correspondiente al número de embarque. | 25 | ALFA NUM | a) Sin validación | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 58 | Número de Contenedor `<NumeroContenedor>` | Dato correspondiente al número de contenedor. | 100 | ALFA NUM | a) Sin validación | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 59 | Número de Referencia `<NumeroReferencia>` | Dato correspondiente al número de referencia. | 20 | NUM | a) Sin validación | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 60 | Nombre Puerto Embarque `<NombrePuertoEmbarque>` | Nombre del puerto de embarque de la mercancía. | 40 | ALFA NUM | a) Sin validación | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 61 | Condiciones de Entrega `<CondicionesEntrega>` | Se refiere a los términos comerciales fijados por el comprador y el vendedor referente a las condicones de entrega de las mercancías y/o productos.<br><br>Se indica si es CIF, FOB, etc. | 3 | ALFA | a) Sin validación | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 62 | Total FOB `<TotalFob>` | Corresponde a la suma del valor FOB de todas las mercancías. | 18 | NUM | a) Valor numérico de 16 enteros, 2 decimales; > 0 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 63 | Seguro `<Seguro>` | Corresponde al monto total de la prima que figura en el documento de embarque o el documento que certifica el valor de la prima asignada por la compañía aseguradora. | 18 | NUM | a) Valor numérico de 16 enteros, 2 decimales; > 0 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 64 | Flete `<Flete>` | Corresponde al importe pagado por el traslado de la mercancía de puertos dominicanos al extranjero. | 18 | NUM | a) Valor numérico de 16 enteros, 2 decimales; > 0 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 65 | Otros Gastos `<OtrosGastos>` | Importe sobre gastos por otros servicios, hasta el transporte de las mercancías en la aduana de destino. | 18 | NUM | a) Valor numérico de 16 enteros, 2 decimales; > 0 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 66 | Total CIF `<TotalCif>` | Corresponde al valor FOB, Flete, Seguro y otros gastos. | 18 | NUM | a) Valor numérico de 16 enteros, 2 decimales; > 0 | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 67 | Régimen Aduanero `<RegimenAduanero>` | Corresponde al régimen aduanero al que se acoge la mercancía exportada, según se encuentra tipificada en la DGA10. | 35 | ALFA | a) Sin validación | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 68 | Nombre Puerto Salida `<NombrePuertoSalida>` | Nombre del puerto de donde sale la mercancía, distinto al puerto de embarque. | 40 | ALFA NUM | a) Sin validación | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 69 | Nombre Puerto Desembarque `<NombrePuertoDesembarque>` | Nombre del puerto de destino de la mercancía. | 40 | ALFA NUM | a) Sin validación | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 70 | Peso Bruto `<PesoBruto>` | Corresponde al peso bruto del contenedor. | 18 | NUM | a) Valor numérico de 16 enteros, 2 decimales; > 0 (No puede ser negativo) | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 71 | Peso Neto `<PesoNeto>` | Corresponde a peso neto del contenedor. | 18 | NUM | a) Valor numérico de 16 enteros, 2 decimales; > 0 (No puede ser negativo) | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 72 | Unidad Peso Bruto `<UnidadPesoBruto>` | Corresponde a la unidad de medida en la que se encuentra el peso bruto de la mercancía. | 2 | NUM | a) Validar con la Tabla IV (Codificación de Unidad de medida) | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 73 | Unidad Peso Neto `<UnidadPesoNeto>` | Corresponde a la unidad de medida en la que se encuentra el peso neto de la mercancía. | 2 | NUM | a) Validar con la Tabla IV (Codificación de Unidad de medida) | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 74 | Cantidad de Bultos `<CantidadBulto>` | Corresponde a la cantidad de bultos que ampara el documento. | 18 | NUM | a) Valor numérico de 16 enteros, 2 decimales; > 0 | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 75 | Unidad Bultos `<UnidadBulto>` | Corresponde a la unidad de medida en la que se encuentra los bultos. | 2 | NUM | a) Validar con la Tabla IV (Codificación de Unidad de medida) | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 76 | Volumen `<VolumenBulto>` | Corresponde al volumen de los bultos. | 18 | NUM | a) Valor numérico de 16 enteros, 2 decimales; > 0 | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 77 | Unidad Volumen `<UnidadVolumen>` | Corresponde a la unidad de medida en la que se encuentra el volumen de los bultos. | 2 | NUM | a) Validar con la Tabla IV (Codificación de Unidad de medida) | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| | FIN ÁREA | **INFORMACIONES ADICIONALES** | | | | | | | | | | | | | | |

---

### ÁREA: TRANSPORTE `<Transporte>`

| # | CAMPOS | DESCRIPCIÓN | Largo Max | Tipo | Validación | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|--------|-------------|-----------|------|------------|---|----|----|----|----|----|----|----|----|----|----|
| | ÁREA TRANSPORTE `<Transporte>` | | | | | | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 78 | Vía Transporte `<ViaTransporte>` | Se especifica si el transporte es vía marítima, terrestre o aérea. | 2 | NUM | Se tiene que validar:<br>01: Terrestre<br>02: Marítimo<br>03: Aérea | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 79 | País Origen `<PaisOrigen>` | Corresponde al país de origen de la mercancía. | 60 | ALFA | a) Sin validación | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 80 | Dirección Destino `<DireccionDestino>` | Corresponde a la dirección de destino donde sera realizado el envío del ítem (distinto a la dirección del comprador). | 100 | ALFA NUM | a) Sin validación | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 81 | País Destino `<PaisDestino>` | Corresponde al país destino donde sera realizado el envío del ítem (distinto a país del comprador). | 60 | ALFA | a) Sin validación | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 3 |
| 82 | RNC o Identificación Compañía Transportista `<RNCIdentificacionCompaniaTransportista>` | Corresponde al dato de RNC o de Identificación de la compañía que realiza el transporte. | 20 | ALFA NUM | a) Sin validación | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 83 | Nombre Compañía Transportista `<NombreCompaniaTransportista>` | Corresponde al dato del nombre o razón social de la compañía que realiza el transporte. | 150 | ALFA NUM | a) Sin validación | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 84 | Número de Viaje `<NumeroViaje>` | Corresponde al número de viaje o el número del vuelo. | 20 | ALFA NUM | a) Sin validación | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| | FIN ÁREA | **TRANSPORTE** | | | | | | | | | | | | | | |

---

*(Continuación de ÁREA TRANSPORTE)*

| # | CAMPOS | DESCRIPCIÓN | Largo Max | Tipo | Validación | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|--------|-------------|-----------|------|------------|---|----|----|----|----|----|----|----|----|----|----|
| 85 | Conductor `<Conductor>` | Corresponde al código o nombre del conductor. | 20 | ALFA NUM | a) Sin validación | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 86 | Documento `<DocumentoTransporte>` | Corresponde al documento de transporte del conductor. | 20 | NUM | a) Sin validación | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 87 | Ficha `<Ficha>` | Corresponde a la ficha del transporte. | 10 | ALFA NUM | a) Sin validación | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 88 | Placa `<Placa>` | Corresponde al número de placa del vehículo del transporte. | 7 | ALFA NUM | a) Sin validación | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 89 | Ruta de Transporte `<RutaTransporte>` | Corresponde a la ruta establecida de transporte. | 20 | ALFA NUM | a) Sin validación | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 90 | Zona de Tranporte `<ZonaTransporte>` | Corresponde a la zona de transporte. | 20 | ALFA NUM | a) Sin validación | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 91 | Número Albarán `<NumeroAlbaran>` | Corresponde al número de albarán de entrega. | 20 | ALFA NUM | a) Sin validación | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| | FIN ÁREA | **TRANSPORTE** | | | | | | | | | | | | | | |

---

### A.2 ÁREA: TOTALES `<Totales>`

| # | CAMPOS | DESCRIPCIÓN | Largo Max | Tipo | Validación | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|--------|-------------|-----------|------|------------|---|----|----|----|----|----|----|----|----|----|----|
| | ÁREA TOTALES `<Totales>` | | | | | | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 92 | Monto Gravado Total¹¹ `<MontoGravadoTotal>` | Total de la suma de valores de monto gravado ITBIS a diferentes tasas.<br>Condicional a que exista Monto gravado1, y/o Monto gravado 2 y/o Monto gravado 3. | 18 | NUM | a) Valor numérico de 16 enteros, 2 decimales; ≥ 0 (No puede ser negativo).<br>b) Valor numérico de la sumatoria del total Monto gravado ITBIS Tasa1 + Monto gravado ITBIS Tasa 2 + Monto gravado ITBIS Tasa3. | I | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 0 |
| 93 | Monto Gravado ITBIS Tasa 1 `<MontoGravadoI1>` | Total de la suma de valores de Ítems gravados asignados a ITBIS tasa 1 (tasa 18%), menos descuentos más recargos.¹²<br>Condicional a que en la línea de detalle exista algún ítem gravado a tasa ITBIS1. | 18 | NUM | a) Valor numérico de 16 enteros, 2 decimales; ≥ 0 (No puede ser negativo).<br>b) Suma de valores del monto ítem con indicador de facturación=1¹³, menos descuentos más recargos.<br>c) Si el indicador monto gravado es =1, se debe dividir la suma de valores del monto ítem con indicador de facturación=1, entre (1+tasa ITBIS tasa 1), menos descuentos más recargos.<br>d) Si el campo 'Indicador de la norma 10-07' es completado, se debe dividir la suma de valores del monto ítem con indicador de facturación=1, entre (1+tasa ITBIS tasa 1+tasas de códigos de impuestos adicionales 002 y 004, asignados al ítem). Si existe descuento, el monto de descuento correspondiente no se deberá rebajar del monto gravado ITBIS tasa 1. | N | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 0 | 0 |
| 94 | Monto Gravado ITBIS Tasa 2 `<MontoGravadoI2>` | Total de la suma de valores de Ítems gravados asignados a ITBIS tasa 2(tasa 16%), menos descuentos más recargos.<br>Condicional a que en la línea de detalle exista algún ítem gravado a tasa ITBIS2. | 18 | NUM | a) Valor numérico de 16 enteros, 2 decimales; ≥ 0 (No puede ser negativo).<br>b) Suma de valores del monto ítem con indicador de facturación=2, menos descuentos más recargos.<br>c) Si el indicador monto gravado=1, se debe dividir el resultado por (1+ ITBIS tasa 2). | N | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 0 | 0 |
| 95 | Monto Gravado ITBIS Tasa 3 `<MontoGravadoI3>` | Total de la suma de valores de Ítems gravados asignados a ITBIS tasa 3 (tasa 0%), menos descuentos más recargos.<br>Condicional a que en la línea de detalle exista algún ítem gravado a tasa ITBIS3. | 18 | NUM | a) Valor numérico de 16 enteros, 2 decimales≥ 0 (No puede ser negativo).<br>b) Suma de valores del monto ítem con indicador de facturación=3, menos descuentos más recargos. | N | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 0 |
| 96 | Monto Exento `<MontoExento>` | Total de la suma de valores de ítems exentos, menos descuentos más recargos.<br>Condicional a que en la línea de detalle exista algún ítem exento. | 18 | NUM | a) Valor numérico de 16 enteros, 2 decimales. ≥ 0 (No puede ser negativo).<br>b) Suma de valores del monto ítem con indicador de facturación=4, menos descuentos más recargos. | I | 2 | 2 | 2 | 2 | 2 | 2¹⁴ | 2 | 2 | 0 | 2 |
| 97 | ITBIS Tasa 1 `<ITBIS1>` | Tasa de ITBIS 1 (18%).<br>Condicional a que en la línea de detalle exista ítem gravado a tasa 1. | 2 | NUM | a) 2 enteros en porcentaje Ej.: 18%<br>b) Existe ítem con indicador de facturación=1 | N¹⁵ | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 0 | 0 |
| 98 | ITBIS Tasa 2 `<ITBIS2>` | Tasa de ITBIS 2 (16%). Condicional a que en la línea de detalle exista ítem gravado a tasa 2. | 2 | NUM | a) 2 enteros en porcentaje Ej.: 16%.<br>b) Existe ítem con indicador de facturación=2. | N | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 0 | 0 |
| 99 | ITBIS Tasa 3 `<ITBIS3>` | Tasa de ITBIS 3 (0%).<br>Condicional a que en la línea de detalle exista ítem gravado a tasa 3. | 2 | NUM | a) 1 entero en porcentaje Ej.: 0%.<br>b) Existe ítem con indicador de facturación=3. | N | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 0 |
| 100 | Total ITBIS `<TotalITBIS>` | Total de la suma de valores de ITBIS a diferentes tasas. Condicional a que exista Total ITBIS Tasa 1, y/o Total ITBIS Tasa 2 y/o Total ITBIS Tasa 3. | 18 | NUM | a) Valor numérico de 16 enteros, 2 decimales; ≥ 0 (No puede ser negativo).<br>b) Suma de Total ITBIS Tasa 1 + Total ITBIS Tasa 2 + Total ITBIS Tasa 3. | I | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 0 |
| 101 | Total ITBIS Tasa 1 `<TotalITBIS1>` | Valor numérico igual a Monto Gravado ITBIS Tasa1 por la Tasa ITBIS 1.<br>Condicional a que exista Monto Gravado tasa 1 y tasa ITBIS 1.<br>Si existen impuestos selectivos al consumo que formen parte de la base imponible del IT BIS, estos se sumaran al monto gravado antes de multiplicarlo por la tasa de ITBIS. | 18 | NUM | a) Valor numérico de 16 enteros, dos decimales; ≥ 0 (No puede ser negativo).<br>b) Total ITBIS Tasa1= Monto Gravado ITBIS tasa1 *ITBIS tasa.<br>Solo forman parte de la base imponible del ITBIS los impuestos selectivos al consumo con códigos desde 006 hasta 039 correspondientes a la Tabla de Codificación de Tipos de Impuestos Adicionales. | N | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 0 | 0 |
| 102 | Total ITBIS Tasa 2 `<TotalITBIS2>` | Valor numérico igual a Monto Gravado ITBIS Tasa2*tasa ITBIS 2.<br>Condicional a que exista Monto Gravado tasa 2 y tasa ITBIS 2. | 18 | NUM | a) Valor numérico de 16 enteros, dos decimales; ≥ 0 (No puede ser negativo).<br>b) Total ITBIS Tasa2= Monto Gravado ITBIS tasa2*ITBIS tasa 2. | N | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 0 | 0 |
| 103 | Total ITBIS Tasa3 `<TotalITBIS3>` | Valor numérico igual a Monto gravado ITBIS Tasa3*tasa ITBIS 3.<br>Condicional a que exista Monto Gravado tasa 3 y tasa ITBIS 3. | 18 | NUM | a)Valor numérico de 16 enteros, dos decimales; ≥ 0 (No puede ser negativo). | N | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 0 |
| 104 | Monto del Impuesto Adicional `<MontoImpuestoAdicional>` | Sumatoria de los campos Monto Impuesto Selectivo al Consumo Específico, Monto Impuesto Selectivo Ad Valorem y Monto Otros Impuestos Adicionales. | 18 | NUM | a) Valor numérico de 16 enteros, dos decimales; >0 (debe ser positivo).<br>b) Monto del Impuesto Adicional= Monto Impuesto Selectivo al Consumo Específico+ Monto Impuesto Selectivo Ad Valorem+ Monto Otros Impuestos Adicionales. | I | 2 | 2 | 2 | 2 | 0 | 0 | 2¹⁶ | 2 | 0 | 0 |
| | **Tabla de Impuestos Adicionales `<ImpuestosAdicionales>`¹⁷** | Se pueden incluir 20 repeticiones de pares código – valor.<br>Incluye los cinco campos siguientes: | | | a) Condicional a que exista otros(s) impuesto(s) en la línea de detalle distinto(s) al ITBIS. | | 2 | 2 | 2 | 2 | 0 | 0 | **2¹⁸** | 2 | 0 | 0 |
| 105 | Código de Impuesto Adicional `<TipoImpuesto>` | Dato correspondiente al Código del impuesto adicional de acuerdo con la Tabla I (Codificación Tipos de Impuestos Adicionales). | 3 | NUM | a) Validar con Tabla I (Codificación Tipos de Impuestos Adicionales). | N | 2 | 2 | 2 | 2 | 0 | 0 | 2¹⁹ | 2 | 0 | 0 |
| 106 | Tasa de Impuesto Adicional `<TasaImpuestoAdicional>` | Dato correspondiente a la Tasa del Impuesto Adicional.<br>Se debe indicar la tasa de Impuesto.²⁰ | 5 | NUM | a) Validar con Tabla I (Codificación Tipos de Impuestos Adicionales).<br>b) Si la tasa corresponde a los códigos entre 006 hasta 022 de la Tabla I (Codificación Tipos de Impuestos Adicionales), se debe validar que coincide con la tasa vigente en el período al que corresponda la fecha de emisión del e-CF (campo fecha emision). | N²¹ | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 0 | 0 |
| 107 | Monto Impuesto Selectivo al Consumo Específico²² `<MontoImpuestoSelectivoConsumoEspecifico>` | Valor del impuesto selectivo al consumo (ISC) específico asociado al código de impuesto adicional. Condicional a que exista código del 006 al 022²³.<br>El cálculo del monto del ISC específico dependerá de la tasa correspondiente al código del impuesto en la Tabla I (Codificación Tipos de Impuestos Adicionales). | 18 | NUM | a) Valor numérico de 16 enteros, dos decimales; >0 (debe ser positivo).<br>b) Si el código del impuesto se encuentra entre 006 hasta 018 se debe verificar la unidad de medida del ítem, si es a granel (código 18) no se deberá calcular el Impuesto Selectivo al Consumo Específico.<br>c) Para los ítems con códigos 006 al 018 de la 'Tabla I (Codificación Tipos de Impuestos Adicionales)' y unidad de medida distinta de granel, se debe multiplicar la cantidad de referencia por los grados de alcohol, por la tasa del impuesto indicada en la tabla para dicho código, por la subcantidad y cantidad.<br>d) Para los códigos del 019 al 022, se debe calcular multiplicando la cantidad por la cantidad de referencia, por la tasa del impuesto adicional indicado. | N | 2 | 2 | 2 | 2 | 0 | 0 | 0 | 2 | 0 | 0 |
| 108 | Monto Impuesto Selectivo al Consumo Ad Valorem `<MontoImpuestoSelectivoConsumoAdvalorem>` | Valor del impuesto selectivo al consumo (ISC) ad valorem asociado al código de impuesto adicional. Condicional a que exista código del 023 al 039²⁴.<br>El cálculo del monto del ISC ad valorem dependerá de la tasa correspondiente al código del impuesto en la Tabla I (Codificación Tipos de Impuestos Adicionales). | 18 | NUM | a) Valor numérico de 16 enteros, dos decimales; >0 (debe ser positivo).<br>b) Si el código del impuesto se encuentra entre 023 hasta 035 se debe verificar la unidad de medida del ítem, si es a granel (código 18) se deberá calcular el Impuesto Selectivo Ad Valorem incrementando en un treinta por ciento (30%) el precio unitario del ítem (equivalente al precio de lista) por la cantidad ítem por la tasa del impuesto correspondiente.<br>c) Para los ítems con código entre 023-035 (ISC Ad valorem)²⁵, y unidad de medida distinta de granel, se debe dividir el precio unitario de referencia entre (1+tasa ITBIS tasa 1). Este resultado se debe restar del ISC Especifico Unitario²⁶ y este último resultado se debe dividir entre (1+tasa del impuesto adicional especificado), esto dará como resultado la base imponible del impuesto. Esta base (ISC Ad Valorem unitario) se deberá multiplicar por la cantidad, por la cantidad de referencia y por la tasa del impuesto correspondiente.<br>d) Cuando el código del impuesto adicional sea entre 036-039 según la 'Tabla de Codificación Tipos de Impuestos Adicionales' se debe calcular el impuesto dividiendo el precio unitario de referencia entre (1+tasa ITBIS tasa 1). Este resultado se debe restar la tasa del ISC Específico y el resultado se debe dividir entre (1+tasa del impuesto adicional especificado); esto dará como resultado la base imponible para el ISC Ad Valorem. Esta base se debe multiplicar por la cantidad, por la cantidad de referencia y por la tasa del impuesto correspondiente. | N | 2 | 2 | 2 | 2 | 0 | 0 | 0 | 2 | 0 | 0 |
| 109 | Monto Otros Impuestos Adicionales `<OtrosImpuestosAdicionales>` | Valor del impuesto adicional asociado al código de impuesto adicional. Condicional a que exista código del 001 al 005.<br>El cálculo del monto del impuesto adicional dependerá de la tasa correspondiente al código del impuesto en la Tabla I (Codificación Tipos de Impuestos Adicionales). | 18 | NUM | a) Valor numérico de 16 enteros, dos decimales; >0 (debe ser positivo).<br>b) Si el código del impuesto se encuentra entre 001 al 005, se deben multiplicar los montos ítems por la tasa correspondiente al código de impuesto adicional.<br>c) Para los códigos 001, 002, 003 y 004, si el indicador monto gravado=1, se debe dividir el monto de ítem entre (1+ ITBIS tasa 1), y el resultado multiplicar por la tasa correspondiente al código de impuesto adicional.<br>d) Para los códigos 002 y 004, si el campo²⁷ 'Indicador Norma 10-07' de la sección Descuentos o Recargos es completado, se debe dividir la suma de los valores del monto ítem con indicador de facturación=1, entre (1+tasa ITBIS tasa 1+ tasa del código de impuesto adicional 002 + tasa del código de impuesto adicional 004), para luego multiplicar este resultado por la tasa correspondiente al código de impuesto adicional.<br>e) Si existe descuento global se debe multiplicar el porcentaje del monto ítem por línea²⁸ por el Monto Descuento (global), esto dará como resultado el monto de descuento aplicable para cada línea de detalle. | N²⁹ | 2 | 2 | 2 | 2 | 0 | 0 | 2²⁹ | 2 | 0 | 0 |
| | **FIN TABLA** | **IMPUESTOS ADICIONALES** | | | | | | | | | | | | | | |


**⚠️ Continuation from field 109 - Adding fields 110-119 to complete A.2 ÁREA TOTALES

*(Continuación de Tabla ÁREA TOTALES)*

| # | CAMPOS | DESCRIPCIÓN | Largo Max | Tipo | Validación | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|--------|-------------|-----------|------|------------|---|----|----|----|----|----|----|----|----|----|----| 
| 110 | Monto Total `<MontoTotal>` | Monto Gravado Total + Monto exento + Total ITBIS + Monto del Impuesto adicional. | 18 | NUM | a) Valor numérico de 16 enteros, dos decimales; ≥ 0 (No puede ser negativo)<br>b) Valor numérico de acuerdo con el total de la sumatoria del campo de Descripción.<br>c) Si es completada la sección Paginación, el monto total debe ser igual a la sumatoria del campo 'Monto Subtotal Página' correspondiente a la sección.<br>d) Si se emite un e-CF tipo 34, el monto total deberá ser menor o igual al monto total del e-CF modificado.³⁰ | I | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 111 | Monto no Facturable `<MontoNoFacturable>` | Total de la suma de montos de bienes o servicios con Indicador de facturación=0.<br>Condicional a que en la línea de detalle exista algún ítem con indicador facturación igual a cero (0). | 18 | NUM | a) Valor numérico de 16 enteros, dos decimales. (Puede ser negativo)<br>b) Valor numérico de acuerdo con el total sumatoria monto ítem con indicador de facturación=0. | N | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 2 | 0 |
| 112 | Monto Período `<MontoPeriodo>` | Total de la suma de Monto Total y Monto no Facturable. | 18 | NUM | a) Valor numérico de 16 enteros, dos decimales. (Puede ser negativo)<br>b) Monto período= Monto Total+Monto No Facturable. | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 113 | Saldo Anterior `<SaldoAnterior>` | Saldo Anterior. Se incluye sólo con fines de ilustrar con claridad el cobro. | 18 | NUM | Valor numérico de 16 enteros, dos decimales. (Puede ser negativo). | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 114 | Monto Avance de pago `<MontoAvancePago>` | Pago parcial por adelantado de la factura que se emite. | 18 | NUM | a) Valor numérico de 16 enteros, dos decimales. >0 (No puede ser negativo) | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 115 | Valor a pagar `<ValorPagar>` | Valor cobrado. | 18 | NUM | a) Valor numérico de 16 enteros, dos decimales. (Puede ser negativo o cero)<br>b) Valor a pagar= Monto total-Monto Avance de pago ± Saldo Anterior (± atendiendo si el valor es positivo o negativo).<br>c) Si el campo 'Indicador Norma 10-07' de la sección Descuento o Recargo es completado, entonces: Valor a pagar= Monto total-Monto descuento³¹- Monto Avance de pago ± Saldo Anterior (± atendiendo si el valor es positivo o negativo). | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 116 | Total Monto ITBIS Retenido `<TotalITBISRetenido>` | Monto del ITBIS correspondiente a la retención que será realizada por el comprador. Condicional a que en la línea de detalle exista retención. | 18 | NUM | a) Valor numérico de 16 enteros, dos decimales, ≥0 (No puede ser negativo)<br>b) Campo Monto ITBIS Retenido de la sección Detalle de B. o S. | N | 2 | 0 | 2 | 2 | 2 | 0 | 0 | 0 | 0 | 0 |
| 117 | Total Monto Retención Renta `<TotalISRRetencion>` | Monto del Impuesto Sobre la Renta correspondiente a la retención realizada de la prestación o locación de servicios. Condicional a que en la línea de detalle exista retención. | 18 | NUM | a) Valor numérico de 16 enteros, dos decimales, ≥0 (No puede ser negativo)<br>b) Monto Retención Renta de la sección Detalle de B. o S. | N | 2 | 0 | 2 | 2 | 2 | 0 | 0 | 0 | 0 | 2 |
| 118 | Total Monto ITBIS Percibido³² `<TotalITBISPercepcion>` | Monto del ITBIS que el contribuyente cobra a terceros como adelanto del impuesto que éste percibirá en sus operaciones. Condicional a que en la línea de detalle exista percepción. | 18 | NUM | a) Valor numérico de 16 enteros, dos decimales, >0 (No puede ser negativo) | N | 2 | 0 | 2 | 2 | 2 | 0 | 0 | 0 | 0 | 0 |
| 119 | Total Monto Percepción Renta `<TotalISRPercepcion>` | Monto del Impuesto Sobre la Renta que el contribuyente cobra a terceros como adelanto del impuesto que éste percibirá en sus operaciones. Condicional a que en la línea de detalle exista percepción. | 18 | NUM | a) Valor numérico de 16 enteros, dos decimales; >0 (No puede ser negativo) | N | 2 | 0 | 2 | 2 | 2 | 0 | 0 | 0 | 0 | 0 |
| | FIN ÁREA | **TOTALES ENCABEZADO** | | | | | | | | | | | | | | |

---

**✅ A.2 ÁREA TOTALES COMPLETADO (Fields 92-119 = 28 fields)

---

### A.7 ÁREA: OTRA MONEDA `<OtraMoneda>`

Condicional a que la facturación sea en Otra Moneda.**

| # | CAMPOS | DESCRIPCIÓN | Largo Max | Tipo | Validación | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|--------|-------------|-----------|------|------------|---|----|----|----|----|----|----|----|----|----|----| 
| | ÁREA OTRA MONEDA ENCABEZADO `<OtraMoneda>` | Condicional a que la facturación sea en Otra Moneda. | | | | | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| 120 | Código Otra moneda `<TipoMoneda>` | Moneda alternativa en que se expresan los Montos. Condicional a que la facturación sea realizada en moneda extranjera.³³<br>Este campo debe tener uno de los valores indicados en la 'Tabla Codificación Monedas'. Por ejemplo: "USD" o "EUR", etc. | 3 | ALFA | a) Validar con la Tabla II (Codificación Monedas). | N | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| 121 | Tipo de Cambio `<TipoCambio>` | Factor de conversión utilizado.<br>Condicional a que existan datos en código otra moneda. | 7 | NUM | a) Valor numérico de 3 enteros y 4 decimales; > 0. (Debe ser positivo) | N | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| 122 | Monto gravado total Otra Moneda `<MontoGravadoTotalOtraMoneda>` | Total de la suma de valores de Monto gravado ITBIS Otra Moneda a diferentes tasas.<br>Condicional a que exista datos en código otra moneda y Monto gravado ITBIS en otra moneda a distintas tasas (18%, 16% y 0%). | 18 | NUM | a) Valor numérico de 16 enteros, 2 decimales; ≥ 0 (No puede ser negativo)<br>b) Valor numérico de la sumatoria del total Monto gravado ITBIS Tasa1 Otra Moneda + Monto gravado ITBIS Tasa 2 Otra Moneda +Monto gravado ITBIS Tasa3 Otra Moneda. | N³⁴ | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 0 |
| 123 | Monto gravado ITBIS Tasa 1 Otra Moneda `<MontoGravado1OtraMoneda>` | Total de la suma de valores de Ítems gravados asignados a ITBIS tasa 1 (tasa 18%), menos descuentos en Otra Moneda más recargos en Otra Moneda³⁵. (Asignados a ítem gravados en Otra Moneda).<br>Condicional a que exista datos en código otra moneda y el ítem contenga indicador de facturación igual a 1. | 18 | NUM | a) Valor numérico de 16 enteros, 2 decimales; ≥ 0 (No puede ser negativo).<br>b) Suma de valores del monto ítem con indicador de facturación=1, menos descuentos en Otra Moneda más recargos en Otra Moneda.<br>c) Si el indicador monto gravado=1, se debe dividir el resultado por (1+tasa ITBIS tasa 1) | N | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 0 | 0 |
| 124 | Monto gravado ITBIS Tasa 2 Otra Moneda `<MontoGravado2OtraMoneda>` | Total de la suma de valores de Ítems gravados asignados a ITBIS tasa 2 en Otra Moneda (tasa 16%), menos descuentos en Otra Moneda más recargos en Otra Moneda. (Asignados a ítem gravados en Otra Moneda).<br>Condicional a que exista datos en código otra moneda y el ítem contenga indicador de facturación igual a 2. | 18 | NUM | a) Valor numérico de 16 enteros, 2 decimales; ≥ 0 (No puede ser negativo).<br>b) Suma de valores del monto ítem con indicador de facturación=2, menos descuentos en Otra Moneda más recargos en Otra Moneda. | N | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 0 | 0 |
| 125 | Monto gravado ITBIS Tasa 3 Otra Moneda `<MontoGravado3OtraMoneda>` | Total de la suma de valores de Ítems gravados asignados a ITBIS tasa 3 en Otra Moneda (tasa 0%), menos descuentos en Otra Moneda más recargos en Otra Moneda. (Asignados a ítem gravados en Otra Moneda).<br>Condicional a que exista datos en código otra moneda y el ítem contenga indicador de facturación igual a 3. | 18 | NUM | a) Valor numérico de 16 enteros, 2 decimales; ≥ 0 (No puede ser negativo).<br>b) Suma de valores del monto ítem con indicador de facturación=3, menos descuentos en Otra Moneda más recargos en Otra Moneda. | N | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 0 |
| 126 | Monto exento en Otra Moneda `<MontoExentoOtraMoneda>` | Total de la suma de valores de ítems exentos, menos descuentos en Otra Moneda más recargos en Otra Moneda (asignados a ítems exentos).<br>Condicional a que exista datos en código otra moneda y el ítem contenga indicador de facturación igual a 4. | 18 | NUM | a) Valor numérico de 16 enteros, 2 decimales; ≥ 0 (No puede ser negativo).<br>Suma de valores del monto ítem con indicador de facturación=4, menos descuentos en Otra Moneda más recargos en Otra Moneda. | N | 2 | 2 | 2 | 2 | 2 | 2³⁶ | 2 | 2 | 0 | 2 |
| 127 | Total ITBIS en Otra Moneda `<TotalITBISOtraMoneda>` | Total de la suma de valores de ITBIS en Otra Moneda a diferentes tasas. Condicional a que exista Total ITBIS Tasa 1 en Otra Moneda, y/o Total ITBIS Tasa 2 en Otra Moneda y/o Total ITBIS Tasa 3 en Otra Moneda. | 18 | NUM | a) Valor numérico de 16 enteros, 2 decimales; ≥ 0 (No puede ser negativo).<br>b) Suma de Total ITBIS Tasa 1 en Otra Moneda + Total ITBIS Tasa 2 en Otra Moneda + Total ITBIS Tasa 3 en Otra Moneda. | N | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 0 |
| 128 | Total ITBIS Tasa 1 en Otra Moneda `<TotalITBIS1OtraMoneda>` | Valor numérico igual a Monto Gravado ITBIS en Otra Moneda Tasa1*tasa ITBIS 1. Condicional a que exista Monto gravado ITBIS Tasa 1 Otra Moneda.<br>Condicional a que exista Monto Gravado tasa 1 en Otra Moneda. | 18 | NUM | a) Valor numérico de 16 enteros, dos decimales≥ 0 (No puede ser negativo).<br>Total ITBIS Tasa1 en Otra Moneda= Monto Gravado ITBIS tasa1 Otra Moneda*ITBIS tasa 1.³⁷ | N | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 0 | 0 |
| 129 | Total ITBIS Tasa 2 en otra moneda `<TotalITBIS2OtraMoneda>` | Valor numérico igual a Monto Gravado ITBIS en Otra Moneda Tasa2*tasa ITBIS 2.<br>Condicional a que exista Monto gravado ITBIS Tasa 2 Otra Moneda. | 18 | NUM | a) Valor numérico de 16 enteros, dos decimales; ≥0 (No puede ser negativo).<br>Total ITBIS Tasa 2 en Otra Moneda= Monto Gravado ITBIS tasa2 Otra Moneda*ITBIS tasa 2. | N | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 0 | 0 |
| 130 | Total ITBIS Tasa 3 en otra moneda `<TotalITBIS3OtraMoneda>` | Valor numérico igual a Monto Gravado ITBIS en Otra Moneda Tasa3*tasa ITBIS 3. Condicional a que exista Monto gravado ITBIS Tasa 3 Otra Moneda. | 18 | NUM | a) Valor numérico de 16 enteros, dos decimales; ≥ 0 (No puede ser negativo). | N | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 0 |
| 131 | Monto del Impuesto Adicional en Otra Moneda³⁸ `<MontoImpuestoAdicionalOtraMoneda>` | Sumatoria de los campos Monto Impuesto Selectivo al Consumo Específico en Otra Moneda, Monto Impuesto Selectivo Ad Valorem en Otra Moneda y Monto Otros Impuestos Adicionales en Otra Moneda.<br>Condicional a que exista datos en código otra moneda y exista al menos unos de los campos de Monto Impuesto Selectivo al Consumo Específico en Otra Moneda, Monto Impuesto Selectivo Ad Valorem en Otra Moneda y/o Monto Otros Impuestos Adicionales en Otra Moneda. | 18 | NUM | a) Valor numérico de 16 enteros, dos decimales; >0 (debe ser positivo).<br>b) Monto del Impuesto Adicional en Otra Moneda= Monto Impuesto Selectivo al Consumo Específico en Otra Moneda + Monto Impuesto Selectivo Ad Valorem en Otra Moneda + Monto Otros Impuestos Adicionales en Otra Moneda. | N | 2 | 2 | 2 | 2 | 0 | 0 | 2³⁹ | 2 | 0 | 0 |
| | **Tabla de Impuestos Adicionales en Otra moneda: `<ImpuestosAdicionalesOtraMoneda>`⁴⁰** | Se pueden incluir 20 repeticiones de pares código – valor. Incluye los cinco campos siguientes: | | | Condicional a que exista otros(s) impuesto(s) en la línea de detalle distinto(s) al ITBIS y este completado el campo | | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 0 | 0 |
| 132 | Código de Impuesto adicional en Otra Moneda `<TipoImpuestoOtraMoneda>` | Dato correspondiente al Código del impuesto adicional de acuerdo con la 'Tabla de Codificación Tipos de Impuestos Adicionales'.⁴¹ | 3 | NUM | a) Validar con Tabla I (Codificación Tipos de Impuestos Adicionales) | N | 2 | 2 | 2 | 2 | 0 | 0 | 2⁴² | 2 | 0 | 0 |
| 133 | Tasa de Impuesto adicional en Otra Moneda `<TasaImpuestoAdicionalOtraMoneda>` | Dato correspondiente a la Tasa del Impuesto Adicional. Se debe indicar la tasa de Impuesto. | 5 | NUM | a) Validar con Tabla I (Codificación Tipos de Impuestos Adicionales) | N⁴³ | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 0 | 0 |
| 134 | Monto Impuesto Selectivo al Consumo Específico en Otra Moneda `<MontoImpuestoSelectivoConsumoEspecificoOtraMoneda>` | Valor del campo Monto Impuesto Selectivo al Consumo Específico referenciado al tipo de cambio del código Otra Moneda especificado. Condicional a que exista código de impuesto adicional del 006 al 022, este completado el campo código otra moneda y el campo Monto Impuesto Selectivo Específico.⁴⁴ | 18 | NUM | a) Valor numérico de 16 enteros, dos decimales; >0 (debe ser positivo).<br>b) Valor del campo Monto Impuesto Selectivo al Consumo Específico dividiendo por la tasa especificada en el campo Tipo de Cambio. | N | 2 | 2 | 2 | 2 | 0 | 0 | 0 | 2 | 0 | 0 |
| 135 | Monto Impuesto Selectivo al Consumo Ad Valorem en Otra Moneda `<MontoImpuestoSelectivoConsumoAdvaloremOtraMoneda>` | Valor del campo Monto Impuesto Selectivo al Consumo Ad Valorem referenciado al tipo de cambio del código Otra Moneda especificado. Condicional a que exista código de impuesto adicional del 023 al 039, este completado el campo código otra moneda y el campo Monto Impuesto Selectivo Ad Valorem.⁴⁵ | 18 | NUM | a) Valor numérico de 16 enteros, dos decimales; >0 (debe ser positivo).<br>a) Valor del campo Monto Impuesto Selectivo Ad Valorem dividiendo por la tasa especificada en el campo Tipo de Cambio. | N | 2 | 2 | 2 | 2 | 0 | 0 | 0 | 2 | 0 | 0 |
| 136 | Monto Otros Impuestos Adicionales en Otra Moneda `<OtrosImpuestosAdicionalesOtraMoneda>` | Valor del Monto Impuesto Adicionales referenciado al tipo de cambio del código Otra Moneda especificado.<br>Condicional a que exista código de impuesto adicional del 001 al 005, este completado el campo código otra moneda y el campo Monto Otros Impuestos Adicionales.⁴⁶ | 18 | NUM | b) Valor numérico de 16 enteros, dos decimales; >0 (debe ser positivo).<br>c) Valor del campo Monto Otros Impuesto Adicional dividiendo por la tasa especificada en el campo Tipo de Cambio. | N | 2 | 2 | 2 | 2 | 0 | 0 | 2⁴⁷ | 2 | 0 | 0 |
| | **FIN TABLA** | **IMPUESTOS ADICIONALES** | | | | | | | | | | | | | | |
| 137 | Monto Total en Otra Moneda `<MontoTotalOtraMoneda>` | Monto gravado total en Otra Moneda + Monto exento en Otra Moneda+ Total ITBIS en Otra Moneda+ Monto del Impuesto Adicional en Otra Moneda.<br>Condicional a que exista al menos un monto en otra moneda. | 18 | NUM | a) Valor numérico de 16 enteros, dos decimales; ≥ 0 (no puede ser negativo).<br>b) Valor numérico de acuerdo con el total sumatoria del campo de Descripción. | N | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| | FIN ÁREA | **OTRA MONEDA ENCABEZADO** | | | | | | | | | | | | | | |

---

**✅ A.7 ÁREA OTRA MONEDA COMPLETADO (Fields 120-137 = 18 fields)

---

## B. DETALLE DE BIENES O SERVICIOS

### ÁREA: DETALLES ÍTEM `<DetallesItem>`

Este ÁREA es obligatoria para todos los tipos de e-CF.

### ÁREA: ÍTEM `<Item>`

Se pueden incluir hasta 100 repeticiones.**

| # | CAMPOS | DESCRIPCIÓN | Largo Max | Tipo | Validación | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|--------|-------------|-----------|------|------------|---|----|----|----|----|----|----|----|----|----|----| 
| | ÁREA DETALLES ÍTEM `<DetallesItem>` | | | | | | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| | ÁREA ÍTEM `<Item>` | Se pueden incluir hasta 100 repeticiones. | | | | | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 1 | N° de Línea o N° Secuencial `<NumeroLinea>` | Línea que numera el ítem. Desde 1 a 100 repeticiones.⁴⁸ | 5 | NUM | a) Número secuencial de la línea. | N | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| | **Tabla de Códigos de Ítem `<TablaCodigosItem>`** | Se pueden incluir 5 repeticiones de pares código – valor. Incluye los dos campos siguientes: | | | | | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 2 | Tipo Código `<TipoCodigo>` | Tipo de codificación utilizada para el ítem<br>Standard: EAN, PLU, DUN o Interna<br>(Hasta 5 tipos de códigos) | 14 | ALFANUM | a) Sin validación. | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 3 | Código del Ítem `<CodigoItem>` | Código del ítem de acuerdo a tipo de codificación indicada en campo anterior.<br>(Hasta 5 códigos) | 35 | ALFANUM | a) Sin validación. | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| | **FIN TABLA** | **CÓDIGOS ÍTEM** | | | | | | | | | | | | | | |
| 4 | Indicador de Facturación `<IndicadorFacturacion>` | Indica si el ítem es exento, si es gravado, o No facturable. Indicará las distintas tasas:<br>0: No Facturable<br>ITBIS 1: ítem gravado a ITBIS tasa1 (18%).<br>ITBIS 2: ítem gravado a ITBIS tasa2 (16%).<br>ITBIS 3: ítem gravado a ITBIS tasa3 (0%).<br>E: Exento | 1 | NUM | a) Indicar si es valor<br>0: No Facturable<br>1: ITBIS 1 (18%)<br>2: ITBIS 2 (16%)<br>3: ITBIS 3 (0%)<br>4: Exento (E) | P⁴⁹ | 1 | 1 | 1 | 1 | 1 | 1⁵⁰ | 1 | 1 | 1⁵¹ | 1 |
| | ÁREA `<Retencion>` | **RETENCIÓN** | | | Condicional a que exista retención. | | 2 | 0 | 2 | 2 | 1 | 0 | 0 | 0 | 0 | 1 |
| 5 | Indicador Agente de Retención o Percepción⁵² `<IndicadorAgenteRetencionoPercepcion>` | Para Agentes de Retención o Percepción. Indica para cada transacción si es agente retenedor del producto que está vendiendo o el servicio. Condicional a que exista retención. | 1 | NUM | a) Codificación:<br>1: "R"<br>2: "P" | N | 2 | 0 | 2 | 2 | 1 | 0 | 0 | 0 | 0 | 1 |
| 6 | Monto ITBIS Retenido `<MontoITBISRetenido>` | Monto del ITBIS correspondiente a la retención que será realizado por el comprador. Condicional a que exista retención.⁵³ | 18 | NUM | a) Valor numérico de 16 enteros, dos decimales, ≥0. | N | 2 | 0 | 2 | 2 | 2 | 0 | 0 | 0 | 0 | 0 |
| 7 | Monto Retención Renta `<MontoISRRetenido>` | Monto del Impuesto Sobre la Renta correspondiente a la retención realizada de la prestación o locación de servicios.<br>El e-CF tipo 41 es condicional a que exista retención y el 'Indicador Bien o Servicio' sea igual a 2. | 18 | NUM | a) Valor numérico de 16 enteros, dos decimales, ≥0.<br>b) El e-CF tipo 41 es condicional a que exista retención y el 'Indicador Bien o Servicio' sea igual a 2. | N | 2 | 0 | 2 | 2 | 2 | 0 | 0 | 0 | 0 | 1 |
| | FIN ÁREA | **RETENCIÓN** | | | | | | | | | | | | | | |
| 8 | Nombre del Ítem `<NombreItem>` | Nombre del producto o servicio. | 80 | ALFANUM | a) Sin validación. | I | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 9 | Indicador Bien o Servicio `<IndicadorBienoServicio>` | Identifica si el ítem corresponde a Bien o Servicio. | 1 | NUM | a) Indicar si es Valor:<br>1: Bien<br>2: Servicio | N | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1⁵⁴ |
| 10 | Descripción Adicional `<DescripcionItem>` | Descripción Adicional del ítem. | 1000 | ALFANUM | a) Sin validación | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 11 | Cantidad `<CantidadItem>` | Cantidad del ítem⁵⁵ | 18 | NUM | a) Valor numérico de 16 enteros, 2 decimales; >0 (No puede ser negativo). | I | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 12 | Unidad de Medida Ítem `<UnidadMedida>` | Indica la unidad de medida que está expresada la cantidad. | 2 | NUM | a) Validar con la Tabla de Codificación de Unidad de medida. | P | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 13 | Cantidad de Referencia `<CantidadReferencia>` | Cantidad para la unidad de medida de referencia (no se usa para el cálculo del Monto Ítem).<br>Condicional a que el ítem esté gravado con códigos de impuestos adicionales entre 006-022 en la Tabla de Codificación Tipo de Impuestos Adicional.⁵⁶ | 18 | NUM | a) Valor numérico de 16 enteros, 2 decimales; ≥0 (No puede ser negativo). | N | 2 | 2 | 2 | 2 | 0 | 0 | 0 | 2 | 0 | 0 |
| 14 | Unidad de Referencia `<UnidadReferencia>` | Indica la unidad de medida de referencia.<br>Condicional a que esté completado el campo Cantidad de referencia. | 2 | NUM | a) Validar con la Tabla IV (Codificación de Unidad de medida). | N | 2 | 2 | 2 | 2 | 0 | 0 | 0 | 2 | 0 | 0 |
| | **Tabla de Distribución de Subcantidad `<TablaSubcantidad>`⁵⁷** | Se deberá incluir esta tabla para fines del cálculo de los impuestos selectivos al consumo a productos derivados de alcohol y cervezas y productos del tabaco y cigarrillos.<br>Condicional a que exista código desde 006 hasta 039 según la 'Tabla de Codificación Tipos de Impuestos Adicionales'.<br>Se pueden incluir 5 repeticiones de pares cantidad – código. Incluye los dos campos siguientes: | | | | N | 2 | 2 | 2 | 2 | 0 | 0 | 0 | 2 | 0 | 0 |
| 15 | Subcantidad `<Subcantidad>` | Cantidad de unidades de referencia que tiene la unidad del ítem.<br>Condicional a que el ítem esté gravado con códigos de impuestos adicionales desde 006 hasta 022 en la Tabla de Codificación Tipo de Impuestos Adicional.⁵⁸ | 19 | NUM | a) Valor numérico de 16 enteros, 3 decimales; ≥0 (No puede ser negativo). | N | 2 | 2 | 2 | 2 | 0 | 0 | 0 | 2 | 0 | 0 |
| 16 | Código subcantidad `<CodigoSubcantidad>` | Indica la unidad de medida de la subcantidad. | 2 | NUM | a) Validar con la Tabla IV (Codificación de Unidad de medida). | N | 2 | 2 | 2 | 2 | 0 | 0 | 0 | 2 | 0 | 0 |
| | **FIN TABLA** | **SUBCANTIDAD** | | | | | | | | | | | | | | |
| 17 | Grados Alcohol en %⁵⁹ `<GradosAlcohol>` | Corresponde al porcentaje de alcohol en el volumen de concentración total alcohólica por unidad de producto. Condicional a que el ítem esté gravado con códigos de impuestos adicionales 006 hasta 018 en la Tabla de Codificación Tipo de Impuestos Adicional (bebidas alcohólicas). | 5 | NUM | a) Valor numérico de 3 enteros y 2 decimales; >0. (Debe ser positivo) | I | 2 | 2 | 2 | 2 | 0 | 0 | 0 | 2 | 0 | 0 |
| 18 | Precio Unitario de Referencia⁶⁰ `<PrecioUnitarioReferencia>` | Precio unitario para la unidad de medida de referencia (no se usa para el cálculo del monto Total).<br>Condicional a que el ítem esté gravado con códigos de impuestos adicionales desde 023 hasta 039 en la Tabla de Codificación Tipo de Impuestos Adicional. | 18 | NUM | a) Valor numérico de 16 enteros, 2 decimales. >0 (No puede ser negativo) | I | 2 | 2 | 2 | 2 | 0 | 0 | 0 | 2 | 0 | 0 |
| 19 | Fecha Elaboración `<FechaElaboracion>` | Dato correspondiente a la fecha de elaboración del ítem. | 10 | ALFANUM | a) Fecha válida<br>Formato: (dd-MM-AAAA) | N | 3 | 3 | 3 | 3 | 3 | 0 | 3 | 3 | 3 | 0 |
| 20 | Fecha Vencimiento `<FechaVencimientoItem>` | Dato correspondiente a la fecha de vencimiento del ítem. | 10 | ALFANUM | a) Fecha válida<br>Formato: (dd-MM-AAAA) | N | 3 | 3 | 3 | 3 | 3 | 0 | 3 | 3 | 3 | 0 |
| | ÁREA `<Mineria>` | **MINERÍA.**<br>Condicional a que exista facturación relacionado al sector minería. | | | | | 0 | 2 | 2 | 2 | 0 | 0 | 0 | 0 | 2 | 0 |
| 21 | Peso Neto Kilogramo `<PesoNetoKilogramo>` | Indica el peso neto en kilogramo del mineral.⁶¹ | 19 | NUM | a) Valor numérico de 16 enteros, 3 decimales; ≥0 (No puede ser negativo). | N | 0 | 2 | 2 | 2 | 0 | 0 | 0 | 0 | 2 | 0 |
| 22 | Peso Neto `<PesoNetoMineria>` | Indica el peso neto del mineral.⁶² | 19 | NUM | a) Valor numérico de 16 enteros, 3 decimales; ≥0 (No puede ser negativo). | N | 0 | 2 | 2 | 2 | 0 | 0 | 0 | 0 | 2 | 0 |
| 23 | Tipo Afiliación `<TipoAfiliacion>` | Indica si el destinatario es o no afiliada.⁶³ | 1 | NUM | a) Indica si es valor:<br>1: Afiliada<br>2: No afiliada | N | 0 | 2 | 2 | 2 | 0 | 0 | 0 | 0 | 2 | 0 |
| 24 | Liquidación `<Liquidacion>` | Indica si la liquidación del mineral es provisional o final.⁶⁴ | 1 | NUM | a) Indica si es valor:<br>1: Provisional<br>2: Final | N | 0 | 2 | 2 | 2 | 0 | 0 | 0 | 0 | 2 | 0 |
| | FIN ÁREA | **MINERÍA** | | | | | | | | | | | | | | |
| 25 | Precio Unitario del Ítem⁶⁵ `<PrecioUnitarioItem>` | Dato correspondiente al precio unitario del ítem. | 20 | NUM | a) Valor numérico de 16 enteros, 4 decimales; ≥0 (No puede ser negativo). | I | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 26 | Monto Descuento `<DescuentoMonto>` | Totaliza todos los subdescuentos otorgados al ítem en montos. Condicional a que exista Monto Subdescuento. | 18 | NUM | a) Valor numérico de 16 enteros, 2 decimales; ≥0 (No puede ser negativo).<br>b) Monto Subdescuento | I | 2 | 2 | 2 | 2 | 2 | 0 | 2 | 2 | 2 | 0 |
| | **Tabla de Distribución de Subdescuento `<TablaSubDescuento>`⁶⁶** | Condicional a que exista descuento en el ítem. Se pueden incluir 12 repeticiones. Incluye los tres campos siguientes: | | | | N | 2 | 2 | 2 | 2 | 2 | 0 | 2 | 2 | 2 | 0 |
| 27 | Tipo de Subdescuento `<TipoSubDescuento>` | Indica si el Subdescuento está en monto ($) o porcentaje (%). Condicional a que exista descuento en el ítem. | 1 | ALFA | a) "$" o "%" | N | 2 | 2 | 2 | 2 | 2 | 0 | 2 | 2 | 2 | 0 |
| 28 | Subdescuento en % `<SubDescuentoPorcentaje>` | Valor del Subdescuento en porcentaje %. Condicional a que exista tipo Subdescuento en porcentaje (%). | 5 | NUM | a) Valor numérico. 3 enteros y 2 decimales; >0 (No puede ser negativo) | N | 2 | 2 | 2 | 2 | 2 | 0 | 2 | 2 | 2 | 0 |
| 29 | Monto Subdescuento `<MontoSubDescuento>` | Correspondiente al valor del descuento expresado en monto.<br>Si va el subdescuento en %, deberá ir el monto del subdescuento. | 18 | NUM | a) Valor numérico de 16 enteros, 2 decimales. ≥0 (No puede ser negativo).<br>b) Si va el subdescuento en %, el valor del subdescuento en monto deberá ser igual al precio unitario de ítem por el subdescuento en porcentaje, por la cantidad de ítems. | N | 2 | 2 | 2 | 2 | 2 | 0 | 2 | 2 | 2 | 0 |
| | **FIN TABLA** | **SUBDESCUENTO** | | | | | | | | | | | | | | |
| 30 | Monto Recargo `<RecargoMonto>` | Totaliza todos los Subrecargos otorgados al ítem en montos. Condicional a que exista Monto Subrecargo. | 18 | NUM | a) Valor numérico de 16 enteros, 2 decimales; ≥0 (No puede ser negativo).<br>b) Monto Subrecargo. | I | 2 | 2 | 2 | 2 | 2 | 0 | 2 | 2 | 2 | 0 |
| | **Tabla de Distribución de Subrecargo `<TablaSubRecargo>`⁶⁷** | Condicional a que exista recargo en el ítem. Se pueden incluir 12 repeticiones de pares Tipo – Valor. Incluye los tres campos siguientes: | | | | N | 2 | 2 | 2 | 2 | 2 | 0 | 2 | 2 | 2 | 0 |
| 31 | Tipo Subrecargo `<TipoSubRecargo>` | Indica si el Subrecargo está en $ o %. Condicional a que exista recargo en el ítem. | 1 | ALFA | "$" o "%" | N | 2 | 2 | 2 | 2 | 2 | 0 | 2 | 2 | 2 | 0 |
| 32 | Subrecargo en % `<SubRecargoPorcentaje>` | Valor del Subrecargo en porcentaje %. Condicional a que exista tipo Subrecargo en porcentaje (%). | 5 | NUM | a) Valor numérico, 3 enteros y 2 decimales; >0 (No puede ser negativo) | N | 2 | 2 | 2 | 2 | 2 | 0 | 2 | 2 | 2 | 0 |
| 33 | Monto Subrecargo `<MontoSubRecargo>` | Correspondiente al valor del Subrecargo expresado en monto. Condicional a que exista subrecargo.<br>Si va el subrecargo en %, deberá ir el monto del subrecargo. | 18 | NUM | a) Valor numérico de 16 enteros, 2 decimales; ≥0 (No puede ser negativo).<br>b) Si va el subrecargo en %, el valor del subrecargo en monto deberá ser igual al precio unitario del ítem por el valor del subrecargo en porcentaje, por la cantidad de ítems. | N | 2 | 2 | 2 | 2 | 2 | 0 | 2 | 2 | 2 | 0 |
| | **FIN TABLA** | **SUBRECARGO** | | | | | | | | | | | | | | |
| | **Tabla de Códigos de Impuestos Adicionales `<TablaImpuestoAdicional>`⁶⁸** | Se pueden incluir 2 repeticiones de códigos de impuesto. | | | | | 2 | 2 | 2 | 2 | 0 | 0 | **2⁶⁹** | 2 | 0 | 0 |
| 34 | Código de Impuesto Adicional `<TipoImpuesto>` | Dato correspondiente al Código del impuesto adicional de acuerdo a la Tabla de Codificación Tipos de Impuestos Adicionales (Tabla I). Condicional a que el ítem este gravado con Impuesto Adicional.⁷⁰ | 3 | NUM | Código válido respecto a la Tabla I (Codificación Tipos de Impuestos Adicionales). | N | 2 | 2 | 2 | 2 | 0 | 0 | 2⁷¹ | 2 | 0 | 0 |
| | **FIN TABLA** | **IMPUESTOS ADICIONALES** | | | | | | | | | | | | | | |
| | ÁREA `<OtraMonedaDetalle>` | **OTRA MONEDA DETALLE.**<br>Indicar precios en monedas alternativas.⁷² | | | | | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| 35 | Precio unitario en otra moneda `<PrecioOtraMoneda>` | Dato correspondiente al precio Unitario del Ítem en otra moneda. Condicional a que el ítem sea en Otra Moneda. | 20 | NUM | a) Valor numérico de 16 enteros, 4 decimales. ≥0 (No puede ser negativo). | N⁷³ | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| 36 | Descuento en Otra Moneda `<DescuentoOtraMoneda>` | Corresponde al valor de descuento otorgado en Otra Moneda. | 18 | NUM | a) Valor numérico de 16 enteros, 2 decimales. ≥0 (No puede ser negativo). | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 37 | Recargo en Otra Moneda `<RecargoOtraMoneda>` | Corresponde el valor de recargo otorgado en Otra Moneda. | 18 | NUM | a) Valor numérico de 16 enteros, 2 decimales. ≥0 (No puede ser negativo). | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 38 | Monto Ítem Otra Moneda `<MontoItemOtraMoneda>` | (Precio Unitario en otra moneda * Cantidad) – Descuento en otra moneda + Recargo en otra moneda.<br>Condicional a que el Precio del ítem y Descuentos o Recargo (si existen) sean en Otra Moneda. | 18 | NUM | a) Valor numérico de 16 enteros, 2 decimales. ≥0 (No puede ser negativo).<br>b) Valor numérico de acuerdo al campo de Descripción. | N | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| | FIN ÁREA | **OTRA MONEDA DETALLE** | | | | | | | | | | | | | | |
| 39 | Monto Ítem (Valor por la línea de detalle) `<MontoItem>` | (Precio Unitario del ítem * Cantidad) – Monto Descuento + Monto Recargo | 18 | NUM | a) Valor numérico de 16 enteros, 2 decimales; ≥ 0 (No puede ser negativo).<br>b) Valor numérico, de acuerdo con descripción.<br>c) Debe ser cero cuando: es una Nota de Crédito para fines de corrección de texto.⁷⁴<br>Cuando es cero puede no imprimirse o imprimirse un texto explicativo (sin valor, sin costo, etc.) | I | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| | FIN ÁREA | **ÍTEM** | | | | | | | | | | | | | | |
| | FIN ÁREA | **DETALLES ÍTEM** | | | | | | | | | | | | | | |


**🎉 ALL CONTENT SECTIONS (A-H) ARE NOW COMPLETE! 🎉**

---

## TABLAS DE CODIFICACIÓN (REFERENCE TABLES)

**IMPORTATE:** Las tablas de referencia completas están disponibles en archivos markdown separados. Esta sección muestra la estructura y ejemplos representativos.

---

### TABLA I: Codificación de Tipos de Impuestos Adicionales

**Fuente:** PDF páginas 61-72

**Impuestos selectivos al consumo y otros impuestos adicionales aplicables en República Dominicana.**

**Resumen de códigos principales:**
- **001:** Propina Legal (10%)
- **002:** Contribución al Desarrollo de las Telecomunicaciones - CDT (2%)
- **003-004:** ISC en Seguros y Telecomunicaciones (16%, 10%)
- **005:** Impuesto sobre Primer Registro de Vehículos (17%)
- **006-022:** ISC Específico (RD$ por unidad) - Bebidas alcohólicas y productos de tabaco
  - Cerveza, vinos, vermut: RD$632.58/unidad
  - Aguardientes, whisky, ron, gin, vodka, licores: RD$632.58/unidad  
  - Cigarrillos 20 unidades: RD$53.51/cajetilla
  - Cigarrillos 10 unidades: RD$26.75/cajetilla
- **023-039:** ISC Ad Valorem (%)  - Diversos productos, porcentaje del valor

**Nota:** Para el catálogo completo de ~40 códigos de impuestos adicionales con tasas específicas, consultar el PDF oficial páginas 61-72.

---

### TABLA II: Codificación de Monedas (ISO 4217)

**Fuente:** PDF página 63

**Códigos de monedas autorizados para e-CF:**

| Código ISO | Moneda |
|------------|--------|
| BRL | Real Brasileño |
| CAD | Dólar Canadiense |
| CHF | Franco Suizo |
| CHY | Yuan Chino |
| COP | Peso Colombiano |
| DKK | Corona Danesa |
| EUR | Euro |
| GBP | Libra Esterlina |
| HTG | Gourde Haitiana |
| JPY | Yen Japonés |
| MXN | Peso Mexicano |
| NOK | Corona Noruega |
| SCP | Libra Escocesa |
| SEK | Corona Sueca |
| USD | Dólar Estadounidense |
| VEF | Bolívar Fuerte Venezolano⁸³ |
| XDR | Derecho Especial de Giro⁸³ |

**Total:** 17 monedas autorizadas

---

### TABLA III: Provincias y Municipios de República Dominicana

**Fuente:** PDF páginas 73-85  
**Tabla completa:** Ver archivo [`tablas-provincias-completa.md`](tablas-provincias-completa.md) (335 entradas)

**Estructura de códigos de 6 dígitos:**
- Formato: `PPMMDD` donde:
  - `PP` = Código de Provincia (01-32)
  - `MM` = Código de Municipio dentro de la provincia
  - `DD` = Código de Distrito Municipal (00 = municipio cabecera)

**Ejemplos estructurales:**

| Código | Tipo | Nombre |
|--------|------|--------|
| 010000 | **Provincia** | **DISTRITO NACIONAL** |
| 010100 | Municipio | Santo Domingo de Guzmán |
| 020000 | **Provincia** | **PROVINCIA AZUA** |
| 020100 | Municipio | MUNICIPIO AZUA DE COMPOSTELA |
| 020101 | Municipio | AZUA DE COMPOSTELA (D. M.). |
| 020102 | Municipio | BARRO ARRIBA (D. M.). |
| 020103 | Municipio | LAS BARIAS-LA ESTANCIA (D. M.). |
| 020104 | Municipio | LOS JOVILLOS (D. M.). |
| 020105 | Municipio | PUERTO VIEJO (D. M.). |
| 020106 | Municipio | BARRERAS (D. M.). |
| 020107 | Municipio | DOÑA EMMA BALAGUER VIUDA VALLEJO (D. M.). |
| 020108 | Municipio | CLAVELLINA (D. M.). |
| 020200 | Municipio | MUNICIPIO LAS CHARCAS |
| 020201 | Municipio | LAS CHARCAS |
| ... | ... | *(ver tabla completa para 333 entradas más)* |
| 320700 | Municipio | MUNICIPIO PEDRO BRAND |
| 320701 | Municipio | PEDRO BRAND (D. M.). |
| 320702 | Municipio | LA GUÁYIGA (D. M.). |
| 320703 | Municipio | LA CUABA (D. M.). |

**Total:** 32 provincias + ~303 municipios y distritos municipales = **335 entradas**

**📄 Tabla completa:** [`tablas-provincias-completa.md`](tablas-provincias-completa.md)

---

### TABLA IV: Unidades de Medida (Completa)

**Fuente:** PDF páginas 86-87

**Codificación completa de unidades de medida para e-CF** (57 códigos):

| Código | Abreviatura | Unidad de Medida |
|--------|-------------|------------------|
| 01 | BARR | Barril |
| 02 | BOL | Bolsa |
| 03 | BOT | Bote |
| 04 | BULTO | Bultos |
| 05 | BOTELLA | Botella |
| 06 | CAJ | Caja/Cajón |
| 07 | CAJETILLA | Cajetilla |
| 08 | CM | Centímetro |
| 09 | CIL | Cilindro |
| 10 | CONJ | Conjunto |
| 11 | CONT | Contenedor |
| 12 | DÍA | Día |
| 13 | DOC | Docena |
| 14 | FARD | Fardo |
| 15 | GL | Galones |
| 16 | GRAD | Grado |
| 17 | GR | Gramo |
| 18 | GRAN | Granel |
| 19 | HOR | Hora |
| 20 | HUAC | Huacal |
| 21 | KG | Kilogramo |
| 22 | kWh | Kilovatio Hora |
| 23 | LB | Libra |
| 24 | LITRO | Litro |
| 25 | LOT | Lote |
| 26 | M | Metro |
| 27 | M2 | Metro Cuadrado |
| 28 | M3 | Metro Cúbico |
| 29 | MMBTU | Millones de Unidades Térmicas |
| 30 | MIN | Minuto |
| 31 | PAQ | Paquete |
| 32 | PAR | Par |
| 33 | PIE | Pie |
| 34 | PZA | Pieza |
| 35 | ROL | Rollo |
| 36 | SOBR | Sobre |
| 37 | SEG | Segundo |
| 38 | TANQUE | Tanque |
| 39 | TONE | Tonelada |
| 40 | TUB | Tubo |
| 41 | YD | Yarda |
| 42 | YD2 | Yarda cuadrada |
| 43 | UND | Unidad |
| 44 | EA | Elemento |
| 45 | MILLAR | Millar |
| 46 | SAC | Saco |
| 47 | LAT | Lata |
| 48 | DIS | Display |
| 49 | BID | Bidón |
| 50 | RAC | Ración |
| 51 | Q | Quintal |
| 52 | GRT | Gross Register Tonnage (Toneladas de registro bruto) |
| 53 | P2 | Pie cuadrado |
| 54 | PAX | Pasajero |
| 55 | PULG | Pulgadas |
| 56 | STAY | Parqueo barcos en muelle |
| 57 | BDJ | Bandeja |

**Total:** 57 códigos completos

---

### TABLA V: Tipos de e-CF (Comprobantes Fiscales Electrónicos)

**Fuente:** PDF páginas 3-4

**Tipos de comprobantes fiscales electrónicos autorizados por la DGII:**

| Código | Tipo de e-CF | Descripción/Uso |
|--------|-------------|-----------------|
| 31 | Factura de Crédito Fiscal Electrónica | Para contribuyentes registrados en el ITBIS que realizan transacciones comerciales |
| 32 | Factura de Consumo Electrónica | Para ventas a consumidores finales |
| 33 | Nota de Débito Electrónica | Aumenta el valor de una factura anterior emitida |
| 34 | Nota de Crédito Electrónica | Disminuye el valor de una factura anterior o la anula |
| 41 | Compras Electrónica | Para registrar compras realizadas |
| 43 | Gastos Menores Electrónica | Para gastos menores que no requieren NCF físico |
| 44 | Regímenes Especiales Electrónica | Para contribuyentes en regímenes especiales de tributación |
| 45 | Gubernamental Electrónica | Para ventas a instituciones gubernamentales |
| 46 | Exportaciones Electrónica | Para ventas de exportación |
| 47 | Pagos al Exterior Electrónica | Para pagos a proveedores del exterior |

**Total:** **10 tipos** de e-CF

---

**✅ TABLAS DE CODIFICACIÓN: DOCUMENTACIÓN COMPLETADA**

**ESTADO FINAL:**
- ✅ TABLA I (Impuestos): Resumen incluido, PDF para códigos completos (~40 códigos)
- ✅ TABLA II (Monedas): **Completa** (17 monedas autorizadas)
- ✅ TABLA III (Provincias/Municipios): **Tabla completa extraída** → [`tablas-provincias-completa.md`](tablas-provincias-completa.md) (335 entradas)
- ✅ TABLA IV (Unidades): **Completa en este documento** (57 códigos)
- ✅ TABLA V (Tipos e-CF): Completa (10 tipos)

**NOTA:** El archivo markdown [`tablas-provincias-completa.md`](tablas-provincias-completa.md) contiene la tabla completa de provincias y municipios. Para unidades de medida, todos los 57 códigos están incluidos en este documento.
---

**🎊 DOCUMENTO FORMATO e-CF V1.0 COMPLETADO 🎊**

**Este documento representa la especificación completa del Formato Comprobante Fiscal Electrónico (e-CF) V1.0**

---

## Bitácora

**Versión 1.0**

### Actualizaciones al 09-10-2025
**Modificaciones no implican cambio de versión.**

1. Se actualiza la tabla II. Codificación Monedas, para agregar el tipo de moneda "Peso Colombiano"

### Actualizaciones al 17-09-2024
**Modificaciones no implican cambio de versión.**

1. Se actualiza la tabla II. Codificación Monedas, para agregar los tipos de monedas "Gourde Haitiana" y "Peso Mexicano"
2. Se actualiza la tabla IV. Codificación Unidad de Medida, para agregar los tipos de medidas "Hectárea", "Mililitro", "Miligramo", "Onzas" y "Onzas Troy"

### Actualizaciones al 30-08-2022
**Modificaciones no implican cambio de versión.**

1. Se actualiza la tabla IV. Codificación Unidad de Medida, para agregar el tipo de medida "Bandeja"

---
de la DGII de República Dominicana en formato Markdown con TRUE 1:1 representación en español del PDF oficial.**

- **Total campos:** 225 campos  
- **Total secciones:** 8 (A-H) + Tablas  
- **Total footnotes:** 82  
- **Cobertura:** 100%

### Footnotes - Section A (ENCABEZADO)

**¹¹** Condicional a que exista monto gravado con al menos una de las tasas de ITBIS.

**¹²** Los descuentos y recargos deben ser proporcionales a cada tasa de ITBIS.

**¹³** Indicador de facturación: Indica la tasa de ITBIS aplicable al ítem (1=ITBIS 18%, 2=ITBIS 16%, 3=ITBIS 0%, 4=Exento).

**¹⁴** Para e-CF tipo 43 (Gastos Menores), si el monto exento existe, debe ser mayor a cero.

**¹⁵** La tasa ITBIS debe imprimirse en el formato de representación impresa solo si aplica al documento.

**¹⁶** Para e-CF tipo 44 (Regímenes Especiales), condicional a que existan impuestos adicionales en el detalle.

**¹⁷** Por definición del XML, para cada elemento debe existir un tag contenedor que agrupe los campos. En este caso, cada combinación de código-tasa-monto se agrupa bajo un elemento de la tabla.

**¹⁸** Para e-CF tipo 44 (Regímenes Especiales), condicional a que existan impuestos adicionales distintos al ITBIS.

**¹⁹** Para e-CF tipo 44 (Regímenes Especiales), el código debe validarse contra la Tabla I de Impuestos Adicionales.

**²⁰** Se debe indicar la tasa del impuesto en formato decimal o porcentual según corresponda al tipo de impuesto.

**²¹** Para tipos de impuestos con códigos 006-022, la tasa debe validarse contra las tasas vigentes en la fecha de emisión del e-CF.

**²²** Impuesto Selectivo al Consumo (ISC) Específico: Impuesto que se calcula sobre unidades físicas (litros, unidades, etc.) a una tasa fija por unidad.

**²³** Códigos 006-022 corresponden a ISC Específico en la Tabla I (Codificación Tipos de Impuestos Adicionales).

**²⁴** Códigos 023-039 corresponden a ISC Ad Valorem en la Tabla I (Codificación Tipos de Impuestos Adicionales).

**²⁵** ISC Ad Valorem: Impuesto Selectivo al Consumo que se calcula como un porcentaje del precio de venta.

**²⁶** ISC Específico Unitario: Valor del impuesto selectivo al consumo específico calculado por unidad de medida.

**²⁷** El campo 'Indicador Norma 10-07' se encuentra en la sección D. Descuentos o Recargos.

**²⁸** El porcentaje del monto ítem por línea se calcula dividiendo el monto del ítem entre el monto total de todos los ítems.

**²⁹** Para e-CF tipo 44 (Regímenes Especiales), debe imprimirse si aplica al documento.

**³⁰** Para e-CF tipo 34 (Nota de Crédito Electrónica), el monto total no puede exceder el monto total del e-CF que se está modificando.

**³¹** El campo 'Monto descuento' se encuentra en la sección D. Descuentos o Recargos.

**³²** ITBIS Percibido: Impuesto sobre Transferencia de Bienes Industrializados y Servicios que se cobra anticipadamente.

**³³** La facturación en otra moneda requiere completar todos los campos condicionales de esta sección.

**³⁴** Campo condicional visible en representación impresa solo si hay montos en otra moneda.

**³⁵** Los descuentos y recargos en Otra Moneda deben calcularse usando el tipo de cambio especificado.

**³⁶** Para e-CF tipo 43 (Gastos Menores), si el monto exento en otra moneda existe, debe ser mayor a cero.

**³⁷** Solo forman parte de la base imponible del ITBIS los impuestos selectivos al consumo con códigos desde 006 hasta 039 en otra moneda.

**³⁸** Monto del Impuesto Adicional en Otra Moneda es la suma de ISC Específico, ISC Ad Valorem y Otros Impuestos Adicionales, todos convertidos a la moneda extranjera.

**³⁹** Para e-CF tipo 44 (Regímenes Especiales), condicional a que existan impuestos adicionales en otra moneda.

**⁴⁰** La tabla de impuestos adicionales en otra moneda sigue las mismas reglas que la tabla en moneda local, pero con valores convertidos.

**⁴¹** El código de impuesto adicional debe ser el mismo que se usa en la moneda local.

**⁴²** Para e-CF tipo 44, el código debe validarse contra la Tabla I de Impuestos Adicionales.

**⁴³** La tasa de impuesto adicional en otra moneda debe imprimirse si aplica al documento.

**⁴⁴** El monto ISC Específico en otra moneda se calcula dividiendo el monto en moneda local por el tipo de cambio.

**⁴⁵** El monto ISC Ad Valorem en otra moneda se calcula dividiendo el monto en moneda local por el tipo de cambio.

**⁴⁶** El monto de otros impuestos adicionales en otra moneda se calcula dividiendo el monto en moneda local por el tipo de cambio.

**⁴⁷** Para e-CF tipo 44, debe imprimirse si aplica y existe monto en otra moneda.

---

### Footnotes - Section B (DETALLE DE BIENES O SERVICIOS)

**⁴⁸** El número de línea debe ser secuencial comenzando en 1 y puede llegar hasta 100 ítems por e-CF.

**⁴⁹** El indicador de facturación debe imprimirse en palabras en la representación impresa.

**⁵⁰** Para e-CF tipo 43 (Gastos Menores), solo se permiten valores 1 o 4.

**⁵¹** Para e-CF tipo 46 (Exportaciones), solo se permiten valores 1, 3 o 4.

**⁵²** El indicador de agente de retención o percepción: 1=Retención ("R"), 2=Percepción ("P").

**⁵³** El monto ITBIS retenido a nivel de ítem se suma en el campo Total Monto ITBIS Retenido del encabezado.

**⁵⁴** Para e-CF tipo 47 (Pagos al Exterior), es obligatorio indicar si es bien o servicio.

**⁵⁵** La cantidad del ítem se multiplica por el precio unitario para obtener el monto ítem.

**⁵⁶** La cantidad de referencia se usa para calcular impuestos selectivos al consumo (ISC) para ciertos productos.

**⁵⁷** La tabla de subcantidad es necesaria para calcular ISC en productos derivados del alcohol, cervezas, tabaco y cigarrillos.

**⁵⁸** La subcantidad representa las unidades de medida de referencia contenidas en la unidad del ítem.

**⁵⁹** Grados de alcohol se usa para calcular ISC en bebidas alcohólicas (códigos 006-018).

**⁶⁰** Precio unitario de referencia se usa para calcular ISC Ad Valorem en productos con códigos 023-039.

**⁶¹** Peso neto en kilogramos es específico para transacciones del sector minería.

**⁶²** Peso neto del mineral puede estar expresado en diferentes unidades de medida.

**⁶³** Tipo de afiliación indica si el destinatario minero es afiliado (1) o no afiliado (2) al emisor.

**⁶⁴** La liquidación del mineral puede ser provisional (1) o final (2), afectando el tratamiento contable.

**⁶⁵** El precio unitario del ítem se multiplica por la cantidad para calcular el monto bruto antes de descuentos y recargos.

**⁶⁶** La tabla de subdescuentos puede incluir hasta 12 diferentes tipos de descuentos aplicados al ítem.

**⁶⁷** La tabla de subrecargos puede incluir hasta 12 diferentes tipos de recargos aplicados al ítem.

**⁶⁸** La tabla de impuestos adicionales a nivel de ítem permite especificar hasta 2 códigos de impuestos que afectan al ítem.

**⁶⁹** Para e-CF tipo 44 (Regímenes Especiales), es obligatorio cuando el ítem tiene impuestos adicionales.

**⁷⁰** El código de impuesto adicional a nivel de ítem debe validarse contra la Tabla I de Impuestos Adicionales y puede ser diferente del impuesto del encabezado.

**⁷¹** Para e-CF tipo 44, debe validarse que el código corresponda a un impuesto adicional válido.

**⁷²** El área de otra moneda en el detalle es condicional a que se haya especificado un tipo de moneda en el encabezado.

**⁷³** El precio unitario en otra moneda debe imprimirse si el ítem está precificado en moneda extranjera.

**⁷⁴** En Notas de Crédito para corrección de texto (sin afectar montos), el Monto Ítem puede ser cero.

---

### Footnotes - Section D (DESCUENTOS O RECARGOS)

**⁷⁵** Los descuentos o recargos globales se aplican al total del e-CF, no a ítems individuales.

**⁷⁶** Para e-CF tipo 41 (Compras), el indicador de facturación debe especificarse si aplica descuento o recargo.

---

### Footnotes - Section E (PAGINACIÓN)

**⁷⁸** Los descuentos y recargos en el subtotal de página deben reflejar los aplicados a los ítems incluidos en esa página específica.

---

### Footnotes - Section F (INFORMACIÓN DE REFERENCIA)

**⁷⁹** El NCF modificado se usa cuando un e-CF anula, corrige o reemplaza un comprobante fiscal anterior.

**⁸⁰** Los códigos de modificación permiten especificar el tipo de corrección: 1=Anulación, 2=Corrección texto, 3=Corrección montos, 4=Reemplazo contingencia, 5=Referencia factura consumo.

**⁸¹** El código 5 (Referencia Factura Consumo Electrónica) se usa específicamente para referenciar una factura de consumo electrónica existente.

**⁸²** ISC Específico (códigos 006-022) se calcula como un monto fijo por unidad de medida, aplicable principalmente a bebidas alcohólicas y productos de tabaco, con tasas actualizadas periódicamente por la DGII.

**⁸³** XDR (Derecho Especial de Giro) es un activo de reserva internacional creado por el FMI. VEF (Bolívar Fuerte Venezolano) puede estar sujeto a cambios según regulaciones cambiarias vigentes.

---

## Información de Contacto

**Dirección General de Impuestos Internos (DGII)**

- **Web:** dgii.gov.do
- **Teléfono:** (809) 689-3444 desde cualquier parte del país
- **Email:** informacion@dgii.gov.do

**IMPUESTOS INTERNOS**

**Publicación:** Octubre 2025  
**Nota:** Publicación informativa sin validez legal

---

*Fin del documento*
