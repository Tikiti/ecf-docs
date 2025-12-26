# Formato Comprobante Fiscal Electrónico (e-CF) V1.0

**Versión**: 1.0 | Octubre 2025  
**Páginas**: 87

---

## Bitácora (Version History)

| Fecha | Cambios |
|-------|---------|
| **09-10-2025** | Se agregó "Peso Colombiano" a la Tabla de Monedas (Tabla II) |
| **17-09-2024** | Se agregaron las monedas "Gurda Haitiana" y "Peso Mexicano" a la Tabla II. Se agregaron unidades a la Tabla IV: Hectárea, Mililitro, Miligramo, Onzas, Onzas Troy |
| **30-08-2022** | Se agregó la unidad de medida "Bandeja" a la Tabla IV |
| **06-05-2022** | Se agregaron unidades: Toneladas de Registro Bruto, Pie cuadrado, Pasajero, Pulgadas, Parqueo Barcos en Muelle |
| **19-11-2021** | Se actualizaron códigos de obligatoriedad del Comprador (1→2) para Nota de Crédito/Débito Electrónica |
| **04-11-2021** | Se agregó la unidad de medida "Quintal" |
| **29-06-2021** | Se separaron los códigos de Provincia y Municipio en columnas en la Tabla III |
| **10-11-2020** | Se eliminaron acentos de las etiquetas `<Liquidacion>` y `<Mineria>`. Se actualizó descriptions de SubDescuento/SubRecargo |
| **28-07-2020** | Se modificó `<TotalITBISRetenido>` y `<TotalISRRetencion>` para aceptar valores cero |

---

## 1. Introducción

Este documento describe la estructura XML completa para los Comprobantes Fiscales Electrónicos (e-CF) en el sistema DGII de la República Dominicana, incluyendo definiciones de campos, tipos de datos, reglas de validación y códigos de obligatoriedad para cada tipo de e-CF.

Cada e-CF debe contener una **firma digital** que autentica su origen y certifica su integridad.

---

## 2. Tipos de e-CF

| Código | Tipo | Descripción |
|--------|------|-------------|
| `31` | Factura de Crédito Fiscal Electrónica | Factura B2B con crédito fiscal |
| `32` | Factura de Consumo Electrónica | Factura de consumo/retail |
| `33` | Nota de Débito Electrónica | Nota de débito electrónica |
| `34` | Nota de Crédito Electrónica | Nota de crédito electrónica |
| `41` | Compras Electrónico | Comprobante de compras |
| `43` | Gastos Menores Electrónico | Comprobante de gastos menores |
| `44` | Regímenes Especiales Electrónico | Comprobante de regímenes especiales |
| `45` | Gubernamental Electrónico | Comprobante gubernamental |
| `46` | Comprobante de Exportaciones Electrónico | Comprobante de exportaciones |
| `47` | Comprobante para Pagos al Exterior Electrónico | Comprobante para pagos al exterior |

---

## 3. Estructura del Documento

El e-CF consiste de las siguientes secciones:

```
<ECF>
  <Encabezado>                      <!-- A. Encabezado -->
    <IdDoc>...</IdDoc>              <!-- Identificación del documento -->
    <Emisor>...</Emisor>            <!-- Datos del emisor -->
    <Comprador>...</Comprador>      <!-- Datos del comprador -->
    <InformacionesAdicionales>...</InformacionesAdicionales>  <!-- Exportación/embarque -->
    <Transporte>...</Transporte>    <!-- Datos de transporte -->
    <Totales>...</Totales>          <!-- Totales -->
    <OtraMoneda>...</OtraMoneda>    <!-- Totales en otra moneda -->
  </Encabezado>
  <DetallesItem>                   <!-- B. Detalles de Ítems -->
    <Item>...</Item>
  </DetallesItem>
  <Subtotales>...</Subtotales>      <!-- C. Subtotales Informativos -->
  <DescuentosORecargos>...</DescuentosORecargos>  <!-- D. Descuentos o Recargos Globales -->
  <Paginacion>...</Paginacion>      <!-- E. Paginación -->
  <InformacionReferencia>...</InformacionReferencia>  <!-- F. Información de Referencia -->
  <FechaHoraFirma>...</FechaHoraFirma>  <!-- G. Fecha y Hora de Firma -->
  <Signature>...</Signature>        <!-- H. Firma Digital -->
</ECF>
```

---

## 4. Códigos de Obligatoriedad

| Código | Significado |
|--------|-------------|
| `1` | **Obligatorio** - Debe estar siempre presente |
| `2` | **Condicional** - Requerido bajo condiciones específicas |
| `3` | **Opcional** - Puede ser incluido |
| `0` | **No Aplica** - No debe ser incluido |

---

## 5. Códigos de Representación Impresa (Columna I)

La especificación PDF incluye una columna \"Representación Impresa\" que indica cómo los campos deben aparecer en la versión impresa del e-CF.

| Código | Significado |
|--------|-------------|
| `N` | **No obligatoria** - La impresión de este campo no es obligatoria |
| `I` | **Impresión obligatoria** - La impresión de este dato es obligatoria |
| `P` | **Impreso en palabras** - Los datos deben ser impresos en palabras (ej: los códigos de tipo deben estar escritos, no solo números) |

---

## 6. Referencia de Tipos de Datos

| Tipo | Significado | Validación |
|------|-------------|------------|
| **NUM** | Numérico | Solo dígitos 0-9 |
| **ALFANUM** | Alfanumérico | Letras, números, espacios y caracteres especiales permitidos |
| **FECHA** | Fecha | Formato: AAAA-MM-DD |
| **DATETIME** | Fecha y Hora | Formato: AAAA-MM-DDTHH:MM:SS (ISO 8601) |
| **DECIMAL** | Decimal | Formato: hasta 2 decimales (ej: 1234.56) |
| **EMAIL** | Correo Electrónico | Debe contener @ y dominio válido |
| **TELEFONO** | Número de Teléfono | 10 dígitos (formato: 809-555-1234) |

**Reglas Generales**:
- Todos los campos numéricos decimales usan **punto (.)** como separador decimal
- No se permiten separadores de miles (comas)
- Los montos monetarios tienen máximo **2 decimales**
- Las tasas de impuesto tienen máximo **2 decimales**

---

## Sección A: Encabezado (Header)

### A.1 IdDoc (Identificación del Documento)

| # | Elemento | Descripción | Máx | Tipo | Validación | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|----------|-------------|-----|------|------------|:-:|----|----|----|----|----|----|----|----|----|----| 
| 1 | `<Version>` | Versión del formato | 3 | ALFANUM | Valor: "1.0" | N | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 2 | `<TipoeCF>` | Código de tipo de e-CF | 2 | NUM | Tipo válido (31-47) | P | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 3 | `<eNCF>` | Número fiscal electrónico | 13 | ALFANUM | Formato de secuencia válida | I | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 4 | `<FechaVencimientoSecuencia>` | Fecha de vencimiento del e-NCF | 10 | DATE | DD-MM-YYYY | I | 1 | 0 | 1 | 0 | 1 | 1 | 1 | 1 | 1 | 1 |
| 5 | `<IndicadorNotaCredito>` | Nota de crédito >30 días | 1 | NUM | 0=≤30 días, 1=>30 días | N | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| 6 | `<IndicadorEnvioDiferido>` | Envío diferido | 1 | NUM | 0=normal, 1=diferido | N | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 2 | 0 |
| 7 | `<IndicadorMontoGravado>` | ITBIS incluido en precios | 1 | NUM | 0=excluido, 1=incluido | N | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 0 | 0 |
| 8 | `<TipoIngresos>` | Código de tipo de ingresos | 2 | NUM | Valores 01-06 (Ver Tabla VI) | N | 1 | 1 | 1 | 1 | 0 | 0 | 1 | 1 | 1 | 0 |
| 9 | `<TipoPago>` | Tipo de pago | 1 | NUM | 1=Contado, 2=Crédito, 3=Gratuito | N | 1 | 1 | 1 | 1 | 1 | 3 | 1 | 1 | 1 | 3 |
| 10 | `<FechaLimitePago>` | Fecha límite de pago | 10 | DATE | DD-MM-YYYY, ≥FechaEmision | N | 2 | 2 | 2 | 2 | 2 | 0 | 2 | 2 | 2 | 3 |
| 11 | `<TerminoPago>` | Términos de pago | 15 | ALFANUM | Texto libre | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| — | `<TablaFormasPago>` | Tabla de formas de pago | — | — | Contenedor (ver nota) | — | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 12 | `<FormaPago>` | Código de forma de pago | 2 | NUM | Valores 1-8 (Tabla V) | N | 3 | 3 | 3 | 0 | 3 | 0 | 3 | 3 | 3 | 3 |
| 13 | `<MontoPago>` | Monto del pago | 18 | NUM | 16 ent + 2 dec, ≥0 | N | 2 | 2 | 2 | 0 | 2 | 0 | 2 | 2 | 2 | 3 |
| 14 | `<TipoCuentaPago>` | Tipo de cuenta | 2 | ALFA | CT=Corriente, AH=Ahorro, OT=Otra | N | 3 | 3 | 3 | 0 | 3 | 0 | 3 | 3 | 3 | 3 |
| 15 | `<NumeroCuentaPago>` | Número de cuenta | 28 | ALFANUM | — | N | 3 | 3 | 3 | 0 | 3 | 0 | 3 | 3 | 3 | 3 |
| 16 | `<BancoPago>` | Nombre del banco | 75 | ALFANUM | — | N | 3 | 3 | 3 | 0 | 3 | 0 | 3 | 3 | 3 | 3 |
| 17 | `<FechaDesde>` | Inicio del período de facturación | 10 | ALFANUM | DD-MM-YYYY, ≤FechaHasta | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 3 |
| 18 | `<FechaHasta>` | Fin del período de facturación | 10 | ALFANUM | DD-MM-YYYY, ≥FechaDesde | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 3 |
| 19 | `<TotalPaginas>` | Total de páginas | 3 | NUM | >1, condicional si existe Paginación | I | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |

> [!NOTE]
> **Estructura de `<TablaFormasPago>`**: Cada pago está envuelto en `<FormaDePago>` conteniendo `<FormaPago>` + `<MontoPago>`.
> Para múltiples pagos vía cheque/transferencia (código 2), solo se debe usar UNA entrada `<TipoCuentaPago>`.

> [!NOTE]
> **Nota al pie 1**: La estructura del e-NCF consiste de: Letra de serie (E-Z, excepto P) + código de tipo de 2 dígitos + secuencia de 10 dígitos.
> 
> **Nota al pie 2**: `IndicadorNotaCredito = 1` significa que la nota de crédito pierde el beneficio de crédito fiscal de ITBIS (emitida >30 días después de la original).
>
> **Nota al pie 3**: Facturas con `TipoPago = 3` (Gratuito/Libre) no pueden ser usadas para reclamaciones de crédito fiscal.

---

### A.2 Emisor (Issuer)

| # | Elemento | Descripción | Máx | Tipo | Validación | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|----------|-------------|-----|------|------------|:-:|----|----|----|----|----|----|----|----|----|----| 
| 20 | `<RNCEmisor>` | RNC del Emisor | 9/11 | NUM | 9 u 11 dígitos válidos | I | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 21 | `<RazonSocialEmisor>` | Razón social | 150 | ALFANUM | — | I | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 22 | `<NombreComercial>` | Nombre comercial | 150 | ALFANUM | — | I | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 23 | `<Sucursal>` | Código de sucursal | 20 | ALFANUM | — | I | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 24 | `<DireccionEmisor>` | Dirección | 100 | ALFANUM | — | I | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 25 | `<Municipio>` | Código de municipio | 6 | NUM | Tabla III | P | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 26 | `<Provincia>` | Código de provincia | 6 | NUM | Tabla III | P | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| — | `<TablaTelefonoEmisor>` | Contenedor de teléfonos (hasta 3) | — | — | — | — | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 27 | `<TelefonoEmisor>` | Número de teléfono (hasta 3) | 12 | ALFANUM | Formato: xxx-xxx-xxxx | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 28 | `<CorreoEmisor>` | Correo electrónico | 80 | ALFANUM | Formato de email válido | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 29 | `<WebSite>` | Sitio web | 50 | ALFANUM | — | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 30 | `<ActividadEconomica>` | Actividad económica | 100 | ALFANUM | — | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 31 | `<CodigoVendedor>` | Código de vendedor | 60 | ALFANUM | Referencia interna | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 32 | `<NumeroFacturaInterna>` | Número de factura interna | 20 | ALFANUM | — | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 33 | `<NumeroPedidoInterno>` | Número de pedido interno | 20 | NUM | — | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 34 | `<ZonaVenta>` | Zona de venta | 20 | ALFANUM | — | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 35 | `<RutaVenta>` | Ruta de venta | 20 | ALFANUM | — | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 36 | `<InformacionAdicionalEmisor>` | Información adicional | 250 | ALFANUM | — | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 37 | `<FechaEmision>` | Fecha de emisión | 10 | ALFANUM | DD-MM-YYYY, validar fecha inicio emisor electrónico | I | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |

---

### A.3 Comprador (Buyer)

| # | Elemento | Descripción | Máx | Tipo | Validación | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|----------|-------------|-----|------|------------|:-:|----|----|----|----|----|----|----|----|----|----| 
| 38 | `<RNCComprador>` | RNC del Comprador | 11 | NUM | 9 u 11 dígitos válidos | I | 1 | 2 | 2 | 2 | 1 | 0 | 1 | 1 | 2 | 2 |
| 39 | `<IdentificadorExtranjero>` | Identificación extranjera | 20 | ALFANUM | Para no residentes | I | 0 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 2 | 2 |
| 40 | `<RazonSocialComprador>` | Razón social | 150 | ALFANUM | — | I | 2 | 2 | 2 | 2 | 2 | 0 | 2 | 2 | 2 | 2 |
| 41 | `<ContactoComprador>` | Nombre/teléfono de contacto | 80 | ALFANUM | — | N | 3 | 3 | 3 | 3 | 3 | 0 | 3 | 3 | 3 | 0 |
| 42 | `<CorreoComprador>` | Correo electrónico | 80 | ALFANUM | Email válido | N | 3 | 3 | 3 | 3 | 3 | 0 | 3 | 3 | 3 | 3 |
| 43 | `<DireccionComprador>` | Dirección | 100 | ALFANUM | — | N | 3 | 3 | 3 | 3 | 3 | 0 | 3 | 3 | 3 | 3 |
| 44 | `<MunicipioComprador>` | Municipio | 6 | NUM | Tabla III | N | 3 | 3 | 3 | 3 | 3 | 0 | 3 | 3 | 3 | 3 |
| 45 | `<ProvinciaComprador>` | Provincia | 6 | NUM | Tabla III | N | 3 | 3 | 3 | 3 | 3 | 0 | 3 | 3 | 3 | 3 |
| 46 | `<PaisComprador>` | Nombre del país | 60 | ALFA | Nombre completo del país | P | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 47 | `<FechaEntrega>` | Fecha de entrega | 10 | DATE | DD-MM-YYYY | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 48 | `<ContactoEntrega>` | Contacto de entrega | 100 | ALFANUM | — | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 49 | `<DireccionEntrega>` | Dirección de entrega | 100 | ALFANUM | — | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 50 | `<TelefonoAdicional>` | Teléfono de entrega | 12 | ALFANUM | — | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 51 | `<FechaOrdenCompra>` | Fecha de orden de compra | 10 | DATE | DD-MM-YYYY | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 52 | `<NumeroOrdenCompra>` | Número de orden de compra | 20 | ALFANUM | — | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 53 | `<CodigoInternoComprador>` | Código interno del comprador | 20 | ALFANUM | Referencia interna | N | 3 | 3 | 3 | 3 | 3 | 0 | 3 | 3 | 3 | 0 |
| 54 | `<ResponsablePago>` | Responsable del pago | 20 | ALFA | — | N | 3 | 3 | 3 | 3 | 3 | 0 | 3 | 3 | 3 | 0 |
| 55 | `<Informacionadicionalcomprador>` | Notas | 150 | ALFANUM | — | N | 3 | 3 | 3 | 3 | 3 | 0 | 3 | 3 | 3 | 0 |

> [!IMPORTANT]
> **Reglas de Identificación del Comprador:**
> - Tipo 31 (Crédito Fiscal): `RNCComprador` siempre obligatorio
> - Tipo 32 (Consumo) ≥ RD$250,000: `RNCComprador` o `IdentificadorExtranjero` obligatorio
> - Tipo 32 (Consumo) < RD$250,000: `RNCComprador` opcional
> - Tipo 46 (Exportaciones): Usar `RNCComprador` para residentes, `IdentificadorExtranjero` para no residentes

---

### A.4 InformacionesAdicionales (Información de Exportación/Embarque)

Esta sección se utiliza principalmente para **Tipo 46 (Exportaciones)** y facturas relacionadas con embarques.

| # | Elemento | Descripción | Máx | Tipo | Validación | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|----------|-------------|-----|------|------------|:-:|----|----|----|----|----|----|----|----|----|----| 
| 56 | `<FechaEmbarque>` | Fecha de embarque | 10 | DATE | DD-MM-YYYY | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 57 | `<NumeroEmbarque>` | Número de embarque | 25 | ALFA | — | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 58 | `<NumeroContenedor>` | Número de contenedor | 100 | ALFA | — | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 59 | `<NumeroReferencia>` | Número de referencia | 20 | NUM | — | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 60 | `<NombrePuertoEmbarque>` | Puerto de carga | 40 | ALFA | — | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 61 | `<CondicionesEntrega>` | Términos de entrega | 3 | ALFA | CIF/FOB/EXW etc. | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 62 | `<TotalFob>` | Valor total FOB | 18 | DEC | ≥0, 2 decimales | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 63 | `<Seguro>` | Monto del seguro | 18 | DEC | ≥0, 2 decimales | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 64 | `<Flete>` | Monto del flete | 18 | DEC | ≥0, 2 decimales | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 65 | `<OtrosGastos>` | Otros gastos | 18 | DEC | ≥0, 2 decimales | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 66 | `<TotalCif>` | Valor total CIF | 18 | DEC | FOB+Seguro+Flete+Otros | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 67 | `<RegimenAduanero>` | Régimen aduanero | 35 | ALFA | Según clasificación DGA | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 68 | `<NombrePuertoSalida>` | Puerto de salida | 40 | ALFANUM | — | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 69 | `<NombrePuertoDesembarque>` | Puerto de destino | 40 | ALFANUM | — | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 70 | `<PesoBruto>` | Peso bruto | 18 | DEC | ≥0, 2 decimales | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 71 | `<PesoNeto>` | Peso neto | 18 | DEC | ≥0, 2 decimales | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 72 | `<UnidadPesoBruto>` | Unidad de peso bruto | 2 | NUM | Tabla IV | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 73 | `<UnidadPesoNeto>` | Unidad de peso neto | 2 | NUM | Tabla IV | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 74 | `<CantidadBulto>` | Número de paquetes | 18 | DEC | >0, 2 decimales | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 75 | `<UnidadBulto>` | Unidad de paquete | 2 | NUM | Tabla IV | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 76 | `<VolumenBulto>` | Volumen | 18 | DEC | >0, 2 decimales | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 77 | `<UnidadVolumen>` | Unidad de volumen | 2 | NUM | Tabla IV | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |

> [!NOTE]
> **Distinción de Etiquetas de Puerto**: Según especificación DGII, estos son 3 puertos diferentes:
> - `NombrePuertoEmbarque` (#60) = Puerto donde se cargan las mercancías
> - `NombrePuertoSalida` (#68) = Puerto de partida (puede diferir del puerto de carga)
> - `NombrePuertoDesembarque` (#69) = Puerto de destino (descarga)

---

### A.5 Transporte (Transport)

| # | Elemento | Descripción | Máx | Tipo | Validación | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|----------|-------------|-----|------|------------|:-:|----|----|----|----|----|----|----|----|----|----| 
| 78 | `<ViaTransporte>` | Modo de transporte | 2 | NUM | 01=Terrestre, 02=Marítimo, 03=Aérea | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 79 | `<PaisOrigen>` | País de origen de la mercancía | 60 | ALFA | — | N |  0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 80 | `<DireccionDestino>` | Dirección de destino | 100 | ALFANUM | — | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 81 | `<PaisDestino>` | País de destino | 60 | ALFA | — | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 3 |
| 82 | `<RNCIdentificacionCompaniaTransportista>` | RNC/ID del transportista | 20 | ALFANUM | — | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 83 | `<NombreCompaniaTransportista>` | Nombre de compañía transportista | 150 | ALFANUM | — | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 84 | `<NumeroViaje>` | Número de viaje/vuelo | 20 | ALFANUM | — | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 85 | `<Conductor>` | Código o nombre del conductor | 20 | ALFANUM | — | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 86 | `<DocumentoTransporte>` | Documento de transporte | 20 | NUM | — | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 87 | `<Ficha>` | Ficha/registro de transporte | 10 | ALFANUM | — | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 88 | `<Placa>` | Número de placa del vehículo | 7 | ALFANUM | — | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 89 | `<RutaTransporte>` | Ruta de transporte establecida | 20 | ALFANUM | — | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 90 | `<ZonaTransporte>` | Zona de transporte | 20 | ALFANUM | — | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 91 | `<NumeroAlbaran>` | Número de albarán de entrega | 20 | ALFANUM | — | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |

---
### A.6 Totales

| # | Elemento | Descripción | Máx | Tipo | Validación | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|----------|-------------|-----|------|------------|:-:|----|----|----|----|----|----|----|----|----|----| 
| 92 | `<MontoGravadoTotal>` | Monto total gravado | 18 | DEC | Suma de montos gravados | I | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 0 |
| 93 | `<MontoGravadoI1>` | Monto gravado ITBIS 18% | 18 | DEC | ≥0, 2 decimales | N | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 0 | 0 |
| 94 | `<MontoGravadoI2>` | Monto gravado ITBIS 16% | 18 | DEC | ≥0, 2 decimales | N | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 0 | 0 |
| 95 | `<MontoGravadoI3>` | Monto gravado ITBIS 0% | 18 | DEC | ≥0, 2 decimales | N | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 0 |
| 96 | `<MontoExento>` | Monto exento | 18 | DEC | ≥0, 2 decimales | I | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 2 |
| 97 | `<ITBIS1>` | Tasa ITBIS 1 | 2 | NUM | Tasa 18% (valor: 18) | N | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 0 | 0 |
| 98 | `<ITBIS2>` | Tasa ITBIS 2 | 2 | NUM | Tasa 16% (valor: 16) | N | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 0 | 0 |
| 99 | `<ITBIS3>` | Tasa ITBIS 3 | 2 | NUM | Tasa 0% (valor: 0) | N | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 0 |
| 100 | `<TotalITBIS>` | Total ITBIS | 18 | DEC | Suma de ITBIS | I | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 0 |
| 101 | `<TotalITBIS1>` | ITBIS al 18% | 18 | DEC | MontoGravadoI1 × 0.18 | N | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 0 | 0 |
| 102 | `<TotalITBIS2>` | ITBIS al 16% | 18 | DEC | MontoGravadoI2 × 0.16 | N | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 0 | 0 |
| 103 | `<TotalITBIS3>` | ITBIS al 0% | 18 | DEC | MontoGravadoI3 × 0 = 0 | N | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 0 |
| 104 | `<MontoImpuestoAdicional>` | Total impuestos adicionales | 18 | DEC | Suma de ISC + Otros | I | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 0 | 0 |
| — | `<ImpuestosAdicionales>` | — | — | — | Contenedor (hasta 20 reps) | — | 2 | 2 | 2 | 2 | 0 | 0 | 0 | 2 | 0 | 0 |
| 105 | `<TipoImpuesto>` | Código de tipo de impuesto | 3 | NUM | Tabla I (001-039) | N | 2 | 2 | 2 | 2 | 0 | 0 | 0 | 2 | 0 | 0 |
| 106 | `<TasaImpuestoAdicional>` | Tasa de impuesto | 5 | NUM | Según Tabla I | N | 2 | 2 | 2 | 2 | 0 | 0 | 0 | 2 | 0 | 0 |
| 107 | `<MontoImpuestoSelectivoConsumoEspecifico>` | ISC Específico | 18 | DEC | ≥0 | N | 2 | 2 | 2 | 2 | 0 | 0 | 0 | 2 | 0 | 0 |
| 108 | `<MontoImpuestoSelectivoConsumoAdvalorem>` | ISC Ad-Valorem | 18 | DEC | ≥0, **ver regla Granel** | N | 2 | 2 | 2 | 2 | 0 | 0 | 0 | 2 | 0 | 0 |
| 109 | `<OtrosImpuestosAdicionales>` | Otros impuestos | 18 | DEC | ≥0 | N | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 0 | 0 |

> [!CAUTION]
> **Regla del 30% de Recargo "Granel" para ISC Ad-Valorem** (Códigos 023-035):
> Cuando la unidad de medida es **Granel** (Código 18), el precio base debe ser **incrementado en 30%** antes de calcular el impuesto Ad-Valorem.
> Fórmula: `ISC = (PrecioBase × 1.30) × TasaAdValorem`

> [!WARNING]
> **Códigos de ISC (006-039)**: Estos requieren lógica de cálculo estricta. Si `TipoImpuesto` está en el rango 006-039, debe calcular ISC Específico O ISC Ad-Valorem según el tipo de código de impuesto. Consulte las fórmulas DGII en Tabla I.

| # | Elemento | Descripción | Máx | Tipo | Validación | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|----------|-------------|-----|------|------------|:-:|----|----|----|----|----|----|----|----|----|----:|
| 110 | `<MontoTotal>` | Monto total general | 18 | DEC | ≥0, suma de componentes | I | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 111 | `<MontoNoFacturable>` | Montos no facturables | 18 | DEC | Puede ser negativo | N | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 2 | 0 |
| 112 | `<MontoPeriodo>` | Monto del período | 18 | DEC | MontoTotal+MontoNoFacturable | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 113 | `<SaldoAnterior>` | Saldo anterior | 18 | DEC | Puede ser ± (positivo o negativo) | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 114 | `<MontoAvancePago>` | Monto de anticipo | 18 | DEC | >0 (debe ser positivo) | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 115 | `<ValorPagar>` | Valor a pagar | 18 | DEC | Puede ser ±  o 0 | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 116 | `<TotalITBISRetenido>` | Total ITBIS retenido | 18 | DEC | ≥0 | N | 2 | 0 | 2 | 2 | 2 | 0 | 0 | 0 | 0 | 0 |
| 117 | `<TotalISRRetencion>` | Total ISR retenido | 18 | DEC | ≥0 | N | 2 | 0 | 2 | 2 | 2 | 0 | 0 | 0 | 0 | 2 |
| 118 | `<TotalITBISPercepcion>` | Total ITBIS percibido | 18 | DEC | >0 (debe ser positivo) | N | 2 | 0 | 2 | 2 | 2 | 0 | 0 | 0 | 0 | 0 |
| 119 | `<TotalISRPercepcion>` | Total ISR percibido | 18 | DEC | >0 (debe ser positivo) | N | 2 | 0 | 2 | 2 | 2 | 0 | 0 | 0 | 0 | 0 |

> [!NOTE]
> **Régimen de Percepción**: El PDF nota "Régimen de percepción no está vigente" (régimen de percepción no está actualmente en vigencia). Los campos 118-119 están incluidos para uso futuro.

> [!NOTE]
> **Fórmula**: `MontoTotal` = `MontoGravadoTotal` + `MontoExento` + `TotalITBIS` + `MontoImpuestoAdicional`
> Nota: Los descuentos/recargos se manejan en la sección global DescuentosORecargos, no en esta fórmula.

---

### A.7 OtraMoneda (Totales en Otra Moneda en el Encabezado)

Cuando las transacciones son en moneda extranjera, esta sección refleja la estructura de Totales en la moneda alternativa.

| # | Elemento | Descripción | Máx | Tipo | Validación | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|----------|-------------|-----|------|------------|:-:|----|----|----|----|----|----|----|----|----|----| 
| 120 | `<TipoMoneda>` | Código de moneda | 3 | ALFA | Tabla II | N | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| 121 | `<TipoCambio>` | Tasa de cambio | 7 | NUM | 3 ent + 4 dec, >0 | N | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| 122 | `<MontoGravadoTotalOtraMoneda>` | Total gravado (ME) | 18 | DEC | ≥0, 2 decimales | N | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 0 |
| 123 | `<MontoGravado1OtraMoneda>` | Monto ITBIS 18% (ME) | 18 | DEC | ≥0, 2 decimales | N | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 0 | 0 |
| 124 | `<MontoGravado2OtraMoneda>` | Monto ITBIS 16% (ME) | 18 | DEC | ≥0, 2 decimales | N | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 0 | 0 |
| 125 | `<MontoGravado3OtraMoneda>` | Monto ITBIS 0% (ME) | 18 | DEC | ≥0, 2 decimales | N | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 0 |
| 126 | `<MontoExentoOtraMoneda>` | Exento (ME) | 18 | DEC | ≥0, 2 decimales | N | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 2 |
| 127 | `<TotalITBISOtraMoneda>` | Total ITBIS (ME) | 18 | DEC | ≥0, 2 decimales | N | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 0 |
| 128 | `<TotalITBIS1OtraMoneda>` | ITBIS 18% (ME) | 18 | DEC | ≥0, 2 decimales | N | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 0 | 0 |
| 129 | `<TotalITBIS2OtraMoneda>` | ITBIS 16% (ME) | 18 | DEC | ≥0, 2 decimales | N | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 0 | 0 |
| 130 | `<TotalITBIS3OtraMoneda>` | ITBIS 0% (ME) | 18 | DEC | ≥0, 2 decimales | N | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 0 |
| 131 | `<MontoImpuestoAdicionalOtraMoneda>` | Impuestos adicionales (ME) | 18 | DEC | ≥0, 2 decimales | N | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 0 | 0 |
| — | `<ImpuestosAdicionalesOtraMoneda>` | — | — | — | Contenedor (hasta 20 reps) | — | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 0 | 0 |
| 132 | `<TipoImpuestoOtraMoneda>` | Código de impuesto (ME) | 3 | NUM | Tabla I (001-039) | N | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 0 | 0 |
| 133 | `<TasaImpuestoAdicionalOtraMoneda>` | Tasa de impuesto (ME) | 5 | NUM | Según Tabla I | N | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 0 | 0 |
| 134 | `<MontoImpuestoSelectivoConsumoEspecificoOtraMoneda>` | ISC Específico (ME) | 18 | DEC | >0, 2 decimales | N | 2 | 2 | 2 | 2 | 0 | 0 | 0 | 2 | 0 | 0 |
| 135 | `<MontoImpuestoSelectivoConsumoAdvaloremOtraMoneda>` | ISC Ad-Valorem (ME) | 18 | DEC | >0, 2 decimales | N | 2 | 2 | 2 | 2 | 0 | 0 | 0 | 2 | 0 | 0 |
| 136 | `<OtrosImpuestosAdicionalesOtraMoneda>` | Otros impuestos adicionales (ME) | 18 | DEC | >0, 2 decimales | N | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 0 | 0 |
| 137 | `<MontoTotalOtraMoneda>` | Monto total general (ME) | 18 | DEC | ≥0, 2 decimales | N | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |

> [!NOTE]
> **OtraMoneda ImpuestosAdicionales**: Cuando se factura en moneda extranjera con impuestos adicionales (ISC, etc.), esta estructura refleja la estructura DOP `ImpuestosAdicionales` pero en los montos de moneda extranjera. Se permiten **hasta 20 repeticiones** de entradas `<ImpuestosAdicionalesOtraMoneda>`.

---

