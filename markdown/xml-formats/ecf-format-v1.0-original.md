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

1. Se actualiza la tabla II. Codificación Monedas, para agregar los tipos de monedas "Peso Mexicano" y otros
2. Se actualiza la tabla IV. Codificación Unidad de Medida, para agregar los tipos de medidas adicionales

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
| | **ÁREA ENCABEZADO `<Encabezado>`** | | | | | | **1** | **1** | **1** | **1** | **1** | **1** | **1** | **1** | **1** | **1** |
| 1 | VERSIÓN | Versión del formato utilizado. | 3 | ALFA NUM | Valor: 1.0 | N | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |

### ÁREA: IDENTIFICACIÓN DEL DOCUMENTO `<IdDoc>`

| # | CAMPOS | DESCRIPCIÓN | Largo Max | Tipo | Validación | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|--------|-------------|-----------|------|------------|---|----|----|----|----|----|----|----|----|----|----|
| | **ÁREA IDENTIFICACIÓN DEL DOCUMENTO `<IdDoc>`** | | | | | | **1** | **1** | **1** | **1** | **1** | **1** | **1** | **1** | **1** | **1** |
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
| | **TABLA DE FORMAS DE PAGO `<TablaFormasPago>`²** | Hasta 07 repeticiones.<br>Contiene los dos campos siguientes. | | | | | **3** | **3** | **3** | **0** | **3** | **0** | **3** | **3** | **3** | **3** |
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
| | **FIN ÁREA** | **IDENTIFICACIÓN DEL DOCUMENTO** | | | | | | | | | | | | | | |

---

**³** En los casos donde exista más de una forma de pago cheque/transferencia/depósito sólo colocar un tipo cuenta de pago.

---

### ÁREA: EMISOR `<Emisor>`

| # | CAMPOS | DESCRIPCIÓN | Largo Max | Tipo | Validación | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|--------|-------------|-----------|------|------------|---|----|----|----|----|----|----|----|----|----|----|
| | **ÁREA EMISOR `<Emisor>`** | | | | | | **1** | **1** | **1** | **1** | **1** | **1** | **1** | **1** | **1** | **1** |
| 20 | RNC Emisor `<RNCEmisor>` | Corresponde al RNC del emisor. | 9 u 11 | NUM | Validar en el Registro Nacional de contribuyentes.<br>Se tiene que validar:<br>a) RNC cumpla con estructura de formato.<br>b) RNC esté autorizado como Facturador Electrónico.<br>c) RNC se encuentre en estatus "Activo".<br>d) RNC no posea marcas de bloqueos. | I | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 21 | Nombre o Razón Social Emisor `<RazonSocialEmisor>` | Nombre o Razón Social del emisor. | 150 | ALFA NUM | a) Sin validación | I | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 22 | Nombre Comercial `<NombreComercial>` | Nombre Comercial. | 150 | ALFA NUM | a) Sin validación | I | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 23 | Sucursal `<Sucursal>` | Indica nombre de la sucursal que emite el e-CF. Corresponde a un dato administrado por el emisor. | 20 | ALFA NUM | a) Sin validación | I | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 24 | Dirección de Emisor `<DireccionEmisor>` | Datos correspondientes a Domicilio de operación del Emisor. | 100 | ALFA NUM | a) Sin validación | I | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 25 | Municipio `<Municipio>` | Dato correspondiente al domicilio de operación del Emisor. | 6 | NUM | a) Validar con código de la Tabla III (Codificación Provincias Y Municipios) | P | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 26 | Provincia `<Provincia>` | Dato correspondiente al domicilio de operación del Emisor. | 6 | NUM | a) Validar con código de la Tabla III (Codificación Provincias Y Municipios | P | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| | **Tabla de Teléfono Emisor `<TablaTelefonoEmisor>`** | Se pueden incluir 3 repeticiones. | | | | | **3** | **3** | **3** | **3** | **3** | **3** | **3** | **3** | **3** | **3** |
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
| | **FIN ÁREA** | **EMISOR** | | | | | | | | | | | | | | |

---

### ÁREA: COMPRADOR `<Comprador>`

| # | CAMPOS | DESCRIPCIÓN | Largo Max | Tipo | Validación | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|--------|-------------|-----------|------|------------|---|----|----|----|----|----|----|----|----|----|----|
| | **ÁREA COMPRADOR `<Comprador>`** | | | | | | **1** | **1** | **2** | **2** | **1** | **0** | **1** | **1** | **1** | **3** |
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
| | **FIN ÁREA** | **COMPRADOR** | | | | | | | | | | | | | | |

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
| | **ÁREA INFORMACIONES ADICIONALES `<InformacionesAdicionales>`** | | | | | | **3** | **3** | **3** | **3** | **0** | **0** | **3** | **3** | **3** | **0** |
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
| | **FIN ÁREA** | **INFORMACIONES ADICIONALES** | | | | | | | | | | | | | | |

---

### ÁREA: TRANSPORTE `<Transporte>`

| # | CAMPOS | DESCRIPCIÓN | Largo Max | Tipo | Validación | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|--------|-------------|-----------|------|------------|---|----|----|----|----|----|----|----|----|----|----|
| | **ÁREA TRANSPORTE `<Transporte>`** | | | | | | **3** | **3** | **3** | **3** | **0** | **0** | **3** | **3** | **3** | **0** |
| 78 | Vía Transporte `<ViaTransporte>` | Se especifica si el transporte es vía marítima, terrestre o aérea. | 2 | NUM | Se tiene que validar:<br>01: Terrestre<br>02: Marítimo<br>03: Aérea | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 79 | País Origen `<PaisOrigen>` | Corresponde al país de origen de la mercancía. | 60 | ALFA | a) Sin validación | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 80 | Dirección Destino `<DireccionDestino>` | Corresponde a la dirección de destino donde sera realizado el envío del ítem (distinto a la dirección del comprador). | 100 | ALFA NUM | a) Sin validación | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 81 | País Destino `<PaisDestino>` | Corresponde al país destino donde sera realizado el envío del ítem (distinto a país del comprador). | 60 | ALFA | a) Sin validación | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 3 |
| 82 | RNC o Identificación Compañía Transportista `<RNCIdentificacionCompaniaTransportista>` | Corresponde al dato de RNC o de Identificación de la compañía que realiza el transporte. | 20 | ALFA NUM | a) Sin validación | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 83 | Nombre Compañía Transportista `<NombreCompaniaTransportista>` | Corresponde al dato del nombre o razón social de la compañía que realiza el transporte. | 150 | ALFA NUM | a) Sin validación | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 84 | Número de Viaje `<NumeroViaje>` | Corresponde al número de viaje o el número del vuelo. | 20 | ALFA NUM | a) Sin validación | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| | **FIN ÁREA** | **TRANSPORTE** | | | | | | | | | | | | | | |

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
| | **FIN ÁREA** | **TRANSPORTE** | | | | | | | | | | | | | | |

---

### A.2 ÁREA: TOTALES `<Totales>`

| # | CAMPOS | DESCRIPCIÓN | Largo Max | Tipo | Validación | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|--------|-------------|-----------|------|------------|---|----|----|----|----|----|----|----|----|----|----|
| | **ÁREA TOTALES `<Totales>`** | | | | | | **1** | **1** | **1** | **1** | **1** | **1** | **1** | **1** | **1** | **1** |
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
| | **Tabla de Impuestos Adicionales `<ImpuestosAdicionales>`¹⁷** | Se pueden incluir 20 repeticiones de pares código – valor.<br>Incluye los cinco campos siguientes: | | | a) Condicional a que exista otros(s) impuesto(s) en la línea de detalle distinto(s) al ITBIS. | | **2** | **2** | **2** | **2** | **0** | **0** | **2¹⁸** | **2** | **0** | **0** |
| 105 | Código de Impuesto Adicional `<TipoImpuesto>` | Dato correspondiente al Código del impuesto adicional de acuerdo con la Tabla I (Codificación Tipos de Impuestos Adicionales). | 3 | NUM | a) Validar con Tabla I (Codificación Tipos de Impuestos Adicionales). | N | 2 | 2 | 2 | 2 | 0 | 0 | 2¹⁹ | 2 | 0 | 0 |
| 106 | Tasa de Impuesto Adicional `<TasaImpuestoAdicional>` | Dato correspondiente a la Tasa del Impuesto Adicional.<br>Se debe indicar la tasa de Impuesto.²⁰ | 5 | NUM | a) Validar con Tabla I (Codificación Tipos de Impuestos Adicionales).<br>b) Si la tasa corresponde a los códigos entre 006 hasta 022 de la Tabla I (Codificación Tipos de Impuestos Adicionales), se debe validar que coincide con la tasa vigente en el período al que corresponda la fecha de emisión del e-CF (campo fecha emision). | N²¹ | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 0 | 0 |
| 107 | Monto Impuesto Selectivo al Consumo Específico²² `<MontoImpuestoSelectivoConsumoEspecifico>` | Valor del impuesto selectivo al consumo (ISC) específico asociado al código de impuesto adicional. Condicional a que exista código del 006 al 022²³.<br>El cálculo del monto del ISC específico dependerá de la tasa correspondiente al código del impuesto en la Tabla I (Codificación Tipos de Impuestos Adicionales). | 18 | NUM | a) Valor numérico de 16 enteros, dos decimales; >0 (debe ser positivo).<br>b) Si el código del impuesto se encuentra entre 006 hasta 018 se debe verificar la unidad de medida del ítem, si es a granel (código 18) no se deberá calcular el Impuesto Selectivo al Consumo Específico.<br>c) Para los ítems con códigos 006 al 018 de la 'Tabla I (Codificación Tipos de Impuestos | N | 2 | 2 | 2 | 2 | 0 | 0 | 0 | 2 | 0 | 0 |

---

**⚠️ CONTINUATION POINT:** A.2 ÁREA TOTALES incomplete. **Resume at field 108** (Monto Impuesto Selectivo al Consumo Ad Valorem).

**Remaining in A.2:** Fields 108-119 (12 fields) - includes complex tax calculations, retentions, and final totals.

---

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

---

**END OF CURRENT WORK SESSION**

---
