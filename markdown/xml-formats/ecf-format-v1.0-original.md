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

## Sección B: DetallesItem (Detalles de Líneas de Ítems)

Cada elemento `<Item>` describe un ítem de línea (bien o servicio). Hasta 100 ítems por e-CF (hasta 1,000 para tipo 32 ≥DOP$250k, o 10,000 para tipo 32 <DOP$250k).

### B.1 Identificación de Ítem (Campos 1-3)

| # | Elemento | Descripción | Máx | Tipo | Validación | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|----------|-------------|-----|------|------------|:-:|----|----|----|----|----|----|----|----|----|----| 
| 1 | `<NumeroLinea>` | Número de línea | 5 | NUM | Secuencial 1 a n | N | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| — | `<TablaCodigosItem>` | — | — | — | Contenedor (hasta 5 reps) | — | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 2 | `<TipoCodigo>` | Tipo de código | 14 | ALFANUM | EAN, PLU, DUN, Interna | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 3 | `<CodigoItem>` | Código de ítem | 35 | ALFANUM | Hasta 5 códigos | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |

### B.2 Indicador de Impuesto y Retención (Campos 4-7)

| # | Elemento | Descripción | Máx | Tipo | Validación | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|----------|-------------|-----|------|------------|:-:|----|----|----|----|----|----|----|----|----|----| 
| 4 | `<IndicadorFacturacion>` | Indicador de impuesto | 1 | NUM | 0-4 (ver códigos abajo) | P | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| — | `<Retencion>` | — | — | — | Contenedor (si existe retención) | — | 2 | 0 | 2 | 2 | 1 | 0 | 0 | 0 | 0 | 1 |
| 5 | `<IndicadorAgenteRetencionoPercepcion>` | Indicador de agente | 1 | NUM | 1=R (Retención), 2=P (Percepción) | N | 2 | 0 | 2 | 2 | 1 | 0 | 0 | 0 | 0 | 1 |
| 6 | `<MontoITBISRetenido>` | ITBIS retenido | 18 | NUM | ≥0, 2 decimales | N | 2 | 0 | 2 | 2 | 2 | 0 | 0 | 0 | 0 | 0 |
| 7 | `<MontoISRRetenido>` | ISR retenido | 18 | NUM | ≥0, 2 decimales | N | 2 | 0 | 2 | 2 | 2 | 0 | 0 | 0 | 0 | 1 |

**Valores de IndicadorFacturacion:**

| Código | Descripción |
|--------|-------------|
| `0` | No Facturable |
| `1` | Gravado ITBIS Tasa 1 (18%) |
| `2` | Gravado ITBIS Tasa 2 (16%) |
| `3` | Gravado ITBIS Tasa 3 (0%) |
| `4` | Exento |

> [!NOTE]
> **Tipo 43, 44, 47**: IndicadorFacturacion debe = 4 (Exento). **Tipo 46**: debe = 3 (ITBIS 0%).

> [!WARNING]
> Si `IndicadorFacturacion=4` (Exento) Y `IndicadorAgenteRetencionoPercepcion=1` (R), entonces `MontoITBISRetenido` **debe ser 0**.

---

### B.3 Detalles del Ítem (Campos 8-14)

| # | Elemento | Descripción | Máx | Tipo | Validación | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|----------|-------------|-----|------|------------|:-:|----|----|----|----|----|----|----|----|----|----| 
| 8 | `<NombreItem>` | Nombre del ítem | 80 | ALFANUM | — | I | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 9 | `<IndicadorBienoServicio>` | Bien/Servicio | 1 | NUM | 1=Bien, 2=Servicio | N | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 10 | `<DescripcionItem>` | Descripción | 1000 | ALFANUM | — | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 11 | `<CantidadItem>` | Cantidad | 18 | NUM | >0, 2 decimales | I | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 12 | `<UnidadMedida>` | Unidad de medida | 2 | NUM | Códigos Tabla IV | P | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 13 | `<CantidadReferencia>` | Cantidad de referencia | 18 | NUM | ≥0, para ISC 006-022 | N | 2 | 2 | 2 | 2 | 0 | 0 | 0 | 2 | 0 | 0 |
| 14 | `<UnidadReferencia>` | Unidad de referencia | 2 | NUM | Códigos Tabla IV | N | 2 | 2 | 2 | 2 | 0 | 0 | 0 | 2 | 0 | 0 |

> [!NOTE]
> **Tipo 47 (Pagos al Exterior)**: Campo 9 `IndicadorBienoServicio` debe = 2 (Servicio).

---

### B.4 Subcantidad para Productos ISC (Campos 15-18)

Para productos de alcohol, tabaco con códigos ISC 006-022 (específico) y 023-039 (ad-valorem).

| # | Elemento | Descripción | Máx | Tipo | Validación | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|----------|-------------|-----|------|------------|:-:|----|----|----|----|----|----|----|----|----|----| 
| — | `<TablaSubcantidad>` | — | — | — | Contenedor (hasta 5 reps) | N | 2 | 2 | 2 | 2 | 0 | 0 | 0 | 2 | 0 | 0 |
| 15 | `<Subcantidad>` | Sub-cantidad | 19 | NUM | ≥0, 3 decimales | N | 2 | 2 | 2 | 2 | 0 | 0 | 0 | 2 | 0 | 0 |
| 16 | `<CodigoSubcantidad>` | Código de unidad | 2 | NUM | Códigos Tabla IV | N | 2 | 2 | 2 | 2 | 0 | 0 | 0 | 2 | 0 | 0 |
| 17 | `<GradosAlcohol>` | Grados de alcohol % | 5 | NUM | >0, 3 ent + 2 dec | I | 2 | 2 | 2 | 2 | 0 | 0 | 0 | 2 | 0 | 0 |
| 18 | `<PrecioUnitarioReferencia>` | Precio unitario de referencia | 18 | NUM | >0 (PVP para cálculo ISC) | I | 2 | 2 | 2 | 2 | 0 | 0 | 0 | 2 | 0 | 0 |

> [!NOTE]
> **Campo 15 (Subcantidad)**: Para alcohol = contenido de alcohol absoluto en litros. Para tabaco = unidades de cigarrillos por paquete.
> **Campo 18 (PrecioUnitarioReferencia)**: Para ISC Ad-Valorem (códigos 023-039), este es el precio de venta al público (PVP) usado como base imponible.

---

### B.5 Fechas del Producto (Campos 19-20)

| # | Elemento | Descripción | Máx | Tipo | Validación | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|----------|-------------|-----|------|------------|:-:|----|----|----|----|----|----|----|----|----|----| 
| 19 | `<FechaElaboracion>` | Fecha de fabricación | 10 | ALFANUM | dd-MM-AAAA | N | 3 | 3 | 3 | 3 | 3 | 0 | 3 | 3 | 3 | 0 |
| 20 | `<FechaVencimientoItem>` | Fecha de vencimiento | 10 | ALFANUM | dd-MM-AAAA | N | 3 | 3 | 3 | 3 | 3 | 0 | 3 | 3 | 3 | 0 |

---

### B.6 Sección Minería (Campos 21-24)

Solo para facturas del sector minero (condicional en transacciones mineras).

| # | Elemento | Descripción | Máx | Tipo | Validación | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|----------|-------------|-----|------|------------|:-:|----|----|----|----|----|----|----|----|----|----| 
| — | `<Mineria>` | — | — | — | Contenedor (sector minero) | — | 0 | 2 | 2 | 2 | 0 | 0 | 0 | 0 | 2 | 0 |
| 21 | `<PesoNetoKilogramo>` | Peso neto (kg) | 19 | NUM | ≥0, 3 decimales | N | 0 | 2 | 2 | 2 | 0 | 0 | 0 | 0 | 2 | 0 |
| 22 | `<PesoNetoMineria>` | Peso neto mineral | 19 | NUM | ≥0, 3 decimales | N | 0 | 2 | 2 | 2 | 0 | 0 | 0 | 0 | 2 | 0 |
| 23 | `<TipoAfiliacion>` | Tipo de afiliación | 1 | NUM | 1=Afiliado, 2=No afiliado | N | 0 | 2 | 2 | 2 | 0 | 0 | 0 | 0 | 2 | 0 |
| 24 | `<Liquidacion>` | Tipo de liquidación | 1 | NUM | 1=Provisional, 2=Final | N | 0 | 2 | 2 | 2 | 0 | 0 | 0 | 0 | 2 | 0 |

---

### B.7 Precio Unitario (Campo 25)

| # | Elemento | Descripción | Máx | Tipo | Validación | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|----------|-------------|-----|------|------------|:-:|----|----|----|----|----|----|----|----|----|----| 
| 25 | `<PrecioUnitarioItem>` | Precio unitario | 20 | NUM | ≥0, 4 decimales | I | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |

> [!NOTE]
> Para productores de alcohol/cerveza: este es el **precio de lista**. Para servicios de seguros: esta es la **prima del seguro**.

---

### B.8 Descuentos (Campos 26-29)

| # | Elemento | Descripción | Máx | Tipo | Validación | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|----------|-------------|-----|------|------------|:-:|----|----|----|----|----|----|----|----|----|----| 
| 26 | `<DescuentoMonto>` | Total descuento | 18 | NUM | ≥0, 2 decimales | I | 2 | 2 | 2 | 2 | 2 | 0 | 2 | 2 | 2 | 0 |
| — | `<TablaSubDescuento>` | — | — | — | Contenedor (hasta 12 reps) | N | 2 | 2 | 2 | 2 | 2 | 0 | 2 | 2 | 2 | 0 |
| 27 | `<TipoSubDescuento>` | Tipo de sub-descuento | 1 | ALFA | "$" o "%" | N | 2 | 2 | 2 | 2 | 2 | 0 | 2 | 2 | 2 | 0 |
| 28 | `<SubDescuentoPorcentaje>` | Porcentaje de descuento | 5 | NUM | >0, 3 ent + 2 dec | N | 2 | 2 | 2 | 2 | 2 | 0 | 2 | 2 | 2 | 0 |
| 29 | `<MontoSubDescuento>` | Monto de sub-descuento | 18 | NUM | ≥0, 2 decimales | N | 2 | 2 | 2 | 2 | 2 | 0 | 2 | 2 | 2 | 0 |

---

### B.9 Recargos (Campos 30-33)

| # | Elemento | Descripción | Máx | Tipo | Validación | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|----------|-------------|-----|------|------------|:-:|----|----|----|----|----|----|----|----|----|----| 
| 30 | `<RecargoMonto>` | Total recargo | 18 | NUM | ≥0, 2 decimales | I | 2 | 2 | 2 | 2 | 2 | 0 | 2 | 2 | 2 | 0 |
| — | `<TablaSubRecargo>` | — | — | — | Contenedor (hasta 12 reps) | N | 2 | 2 | 2 | 2 | 2 | 0 | 2 | 2 | 2 | 0 |
| 31 | `<TipoSubRecargo>` | Tipo de sub-recargo | 1 | ALFA | "$" o "%" | N | 2 | 2 | 2 | 2 | 2 | 0 | 2 | 2 | 2 | 0 |
| 32 | `<SubRecargoPorcentaje>` | Porcentaje de recargo | 5 | NUM | >0, 3 ent + 2 dec | N | 2 | 2 | 2 | 2 | 2 | 0 | 2 | 2 | 2 | 0 |
| 33 | `<MontoSubRecargo>` | Monto de sub-recargo | 18 | NUM | ≥0, 2 decimales | N | 2 | 2 | 2 | 2 | 2 | 0 | 2 | 2 | 2 | 0 |

---

### B.10 Impuestos Adicionales por Ítem (Campo 34)

| # | Elemento | Descripción | Máx | Tipo | Validación | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|----------|-------------|-----|------|------------|:-:|----|----|----|----|----|----|----|----|----|----| 
| — | `<TablaImpuestoAdicional>` | — | — | — | Contenedor (hasta 2 reps) | N | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 0 | 0 |
| 34 | `<TipoImpuesto>` | Código de impuesto | 3 | NUM | Tabla I (001-039) | N | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 0 | 0 |

---

### B.11 OtraMoneda por Ítem (Campos 35-38)

Detalle en moneda extranjera a nivel de ítem.

| # | Elemento | Descripción | Máx | Tipo | Validación | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|----------|-------------|-----|------|------------|:-:|----|----|----|----|----|----|----|----|----|----| 
| — | `<OtraMonedaDetalle>` | — | — | — | Contenedor (detalle ME) | N | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| 35 | `<PrecioOtraMoneda>` | Precio unitario (ME) | 20 | NUM | ≥0, 4 decimales | N | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| 36 | `<DescuentoOtraMoneda>` | Descuento (ME) | 18 | NUM | ≥0, 2 decimales | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 37 | `<RecargoOtraMoneda>` | Recargo (ME) | 18 | NUM | ≥0, 2 decimales | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 38 | `<MontoItemOtraMoneda>` | Total de línea (ME) | 18 | NUM | ≥0, 2 decimales | N | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |

---

### B.12 Total de Línea (Campo 39)

| # | Elemento | Descripción | Máx | Tipo | Validación | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|----------|-------------|-----|------|------------|:-:|----|----|----|----|----|----|----|----|----|----| 
| 39 | `<MontoItem>` | Total de línea | 18 | NUM | =(Precio×Cant)−Descuento+Recargo | I | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |

> [!NOTE]
> `MontoItem` puede ser **0** para notas de crédito de corrección de texto (cuando `CodigoModificacion=2` en Información de Referencia).

---

## Sección C: Subtotales Informativos

Subtotales informativos opcionales (no afectan los totales principales). Se pueden incluir hasta 20 entradas `<Subtotal>`.

**Estructura XML:**
```xml
<Subtotales>
  <Subtotal>...</Subtotal>
  <Subtotal>...</Subtotal>
</Subtotales>
```

| # | Elemento | Descripción | Máx | Tipo | Validación | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|----------|-------------|-----|------|------------|:-:|----|----|----|----|----|----|----|----|----|----| 
| 1 | `<NumeroSubTotal>` | Número de subtotal | 2 | NUM | Secuencial 1 a n | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 2 | `<DescripcionSubtotal>` | Título | 40 | ALFA | — | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 3 | `<Orden>` | Orden de visualización | 2 | NUM | — | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 4 | `<SubTotalMontoGravadoTotal>` | Subtotal total gravado | 18 | NUM | ≥0, 2 decimales | N | 3 | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 0 |
| 5 | `<SubTotalMontoGravadoI1>` | Subtotal al 18% | 18 | NUM | ≥0, 2 decimales | N | 3 | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 0 | 0 |
| 6 | `<SubTotalMontoGravadoI2>` | Subtotal al 16% | 18 | NUM | ≥0, 2 decimales | N | 3 | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 0 | 0 |
| 7 | `<SubTotalMontoGravadoI3>` | Subtotal al 0% | 18 | NUM | ≥0, 2 decimales | N | 3 | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 0 |
| 8 | `<SubTotaITBIS>` | Subtotal ITBIS | 18 | NUM | ≥0, 2 decimales | N | 3 | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 0 |
| 9 | `<SubTotaITBIS1>` | Subtotal ITBIS 18% | 18 | NUM | ≥0, 2 decimales | N | 3 | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 0 | 0 |
| 10 | `<SubTotaITBIS2>` | Subtotal ITBIS 16% | 18 | NUM | ≥0, 2 decimales | N | 3 | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 0 | 0 |
| 11 | `<SubTotaITBIS3>` | Subtotal ITBIS 0% | 18 | NUM | ≥0, 2 decimales | N | 3 | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 0 |
| 12 | `<SubTotalImpuestoAdicional>` | Subtotal impuestos adicionales | 18 | NUM | >0, 2 decimales | N | 3 | 3 | 3 | 3 | 3 | 0 | 3 | 3 | 0 | 0 |
| 13 | `<SubTotalExento>` | Subtotal exento | 18 | NUM | ≥0, 2 decimales | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 0 | 3 |
| 14 | `<MontoSubTotal>` | Monto de subtotal | 18 | NUM | ≥0, 2 decimales | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 15 | `<Lineas>` | Conteo de líneas en subtotal | 2 | NUM | >0 | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |


---

## Sección D: DescuentosORecargos (Descuentos o Recargos Globales)

Descuentos/recargos globales que aplican a toda la factura (no por ítem). Se pueden incluir hasta 20 entradas `<DescuentoORecargo>`.

**Estructura XML:**
```xml
<DescuentosORecargos>
  <DescuentoORecargo>...</DescuentoORecargo>
  <DescuentoORecargo>...</DescuentoORecargo>
</DescuentosORecargos>
```

| # | Elemento | Descripción | Máx | Tipo | Validación | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|----------|-------------|-----|------|------------|:-:|----|----|----|----|----|----|----|----|----|----| 
| 1 | `<NumeroLinea>` | Número de línea | 2 | NUM | 1-20 | N | 2 | 2 | 2 | 2 | 2 | 0 | 2 | 2 | 2 | 0 |
| 2 | `<TipoAjuste>` | D (Descuento) o R (Recargo) | 1 | ALFA | — | N | 2 | 2 | 2 | 2 | 2 | 0 | 2 | 2 | 2 | 0 |
| 3 | `<IndicadorNorma1007>` | Indicador Norma 10-07 | 1 | NUM | 1=Sí | N | 3 | 3 | 3 | 3 | 0 | 0 | 0 | 3 | 0 | 0 |
| 4 | `<DescripcionDescuentooRecargo>` | Descripción | 45 | ALFA | — | I | 3 | 3 | 3 | 3 | 3 | 0 | 3 | 3 | 3 | 0 |
| 5 | `<TipoValor>` | Tipo de valor (% o $) | 1 | ALFA | "%" o "$" | I | 2 | 2 | 2 | 2 | 2 | 0 | 2 | 2 | 2 | 0 |
| 6 | `<ValorDescuentooRecargo>` | Porcentaje de descuento/recargo | 5 | NUM | >0, 3 ent + 2 dec | I | 2 | 2 | 2 | 2 | 2 | 0 | 2 | 2 | 2 | 0 |
| 7 | `<MontoDescuentooRecargo>` | Monto de descuento/recargo | 18 | NUM | ≥0, 2 decimales | I | 2 | 2 | 2 | 2 | 2 | 0 | 2 | 2 | 2 | 0 |
| 8 | `<MontoDescuentooRecargoOtraMoneda>` | Monto (moneda extranjera) | 18 | NUM | ≥0, 2 decimales | N | 3 | 3 | 3 | 3 | 3 | 0 | 3 | 3 | 3 | 0 |
| 9 | `<IndicadorFacturacionDescuentooRecargo>` | Indicador de impuesto | 1 | NUM | 1=ITBIS1, 2=ITBIS2, 3=ITBIS3, 4=Exento | N | 2 | 2 | 2 | 2 | 2 | 0 | 2 | 2 | 2 | 0 |


**Valores de TipoDescuentoRecargo:**

| Código | Descripción |
|--------|-------------|
| `1` | Descuento |
| `2` | Recargo |

**Valores de TipoValor (campo ALFA):**

| Código | Descripción |
|--------|-------------|
| `%` | Porcentaje |
| `$` | Monto (Cantidad fija) |

> [!WARNING]
> **Usar caracteres literales**: `TipoValor` es un campo ALFA. Enviar los caracteres reales `%` o `$`, no valores numéricos. El PDF define explícitamente estos como "%" o "$".

**Valores de IndicadorFacturacionDescuentooRecargo:**

| Código | Descripción |
|--------|-------------|
| `1` | ITBIS Tasa 1 (18%) |
| `2` | ITBIS Tasa 2 (16%) |
| `3` | ITBIS Tasa 3 (0%) |
| `4` | Exento (mostrado como "E" en documentación DGII, pero enviar valor `4`) |

> [!CAUTION]
> **No enviar "E"**: Aunque la documentación DGII etiqueta Exento como "E", el campo es tipo NUM. Debe enviar el valor numérico `4`, no la letra "E".

---

## Sección E: Paginacion (Paginación)

Para representación impresa, indica qué ítems aparecen en cada página.

> [!NOTE]
> Cada elemento `<Pagina>` está envuelto dentro del contenedor `<Paginacion>`.
> Estructura: `<Paginacion><Pagina>...</Pagina></Paginacion>`

| # | Elemento | Descripción | Máx | Tipo | Validación | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|----------|-------------|-----|------|------------|:-:|----|----|----|----|----|----|----|----|----|----:|
| 1 | `<PaginaNo>` | Número de página | 3 | NUM | 1-100, secuencial | I | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| 2 | `<NoLineaDesde>` | Línea inicial | 3 | NUM | >0, ≤NoLineaHasta | N | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| 3 | `<NoLineaHasta>` | Línea final | 3 | NUM | >0, ≥NoLineaDesde | N | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| 4 | `<SubtotalMontoGravadoPagina>` | Subtotal gravado de página | 18 | NUM | ≥0, 2 decimales | I | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 0 |
| 5 | `<SubtotalMontoGravado1Pagina>` | Subtotal página 18% | 18 | NUM | ≥0, 2 decimales | N | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 0 | 0 |
| 6 | `<SubtotalMontoGravado2Pagina>` | Subtotal página 16% | 18 | NUM | ≥0, 2 decimales | N | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 0 | 0 |
| 7 | `<SubtotalMontoGravado3Pagina>` | Subtotal página 0% | 18 | NUM | ≥0, 2 decimales | N | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 0 |
| 8 | `<SubtotalExentoPagina>` | Subtotal exento de página | 18 | NUM | ≥0, 2 decimales | I | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 2 |
| 9 | `<SubtotalItbisPagina>` | Subtotal ITBIS de página | 18 | NUM | ≥0, 2 decimales | I | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 0 |
| 10 | `<SubtotalItbis1Pagina>` | ITBIS página 18% | 18 | NUM | ≥0, 2 decimales | N | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 0 | 0 |
| 11 | `<SubtotalItbis2Pagina>` | ITBIS página 16% | 18 | NUM | ≥0, 2 decimales | N | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 0 | 0 |
| 12 | `<SubtotalItbis3Pagina>` | ITBIS página 0% | 18 | NUM | ≥0, 2 decimales | N | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 0 |
| 13 | `<SubtotalImpuestoAdicionalPagina>` | Impuestos adicionales de página | 18 | NUM | >0, 2 decimales | I | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 0 | 0 |
| — | `<SubtotalImpuestoAdicional>` | Contenedor impuestos adicionales (AREA) | — | — | — | — | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 0 | 0 |
| 14 | `<SubtotalImpuestoSelectivoConsumoEspecificoPagina>` | ISC específico de página | 18 | NUM | >0, 2 decimales | N | 2 | 2 | 2 | 2 | 0 | 0 | 0 | 2 | 0 | 0 |
| 15 | `<SubtotalOtrosImpuesto>` | Otros impuestos de página | 18 | NUM | >0, 2 decimales | N | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 0 | 0 |
| 16 | `<MontoSubtotalPagina>` | Subtotal de página | 18 | NUM | ≥0, 2 decimales | I | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| 17 | `<SubtotalMontoNoFacturablePagina>` | No facturable de página | 18 | NUM | ≥0, 2 decimales | N | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |

> [!WARNING]
> **Etiquetas de paginación en moneda extranjera**: Las etiquetas `SubtotalMontoGravadoPaginaOtraMoneda` y `MontoSubtotalPaginaOtraMoneda` de versiones anteriores pueden no estar presentes en todas las versiones del PDF. Verificar contra su versión específica del PDF antes de implementar.

> [!TIP]
> **Tipo "NUM" para campos monetarios**: El PDF usa NUM para todos los campos monetarios. Cuando el campo contiene decimales, la validación especifica "2 decimales". Esta es la convención DGII.

---

## Sección F: InformacionReferencia (Información de Referencia)

Usado para Notas de Débito/Crédito (tipos 33, 34) para referenciar la factura modificada.

| # | Elemento | Descripción | Máx | Tipo | Validacion | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|----------|-------------|-----|------|------------|:-:|----|----|----|----|----|----|----|----|----|----:|
| 1 | `<NCFModificado>` | e-NCF modificado | 11/13/19 | ALFA | Formato NCF/e-NCF válido | I | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2 | `<RNCOtroContribuyente>` | RNC de otro contribuyente | 9/11 | NUM | RNC válido (9 u 11 dígitos) | N | 0 | 0 | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| 3 | `<FechaNCFModificado>` | Fecha del e-CF modificado | 10 | DATE | DD-MM-YYYY | N | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| 4 | `<CodigoModificacion>` | Código de modificación | 1 | NUM | Valores 1-5 | P | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| 5 | `<RazonModificacion>` | Razón de modificación | 90 | ALFA | Texto libre (ej. "error en precio") | N | 0 | 0 | 3 | 3 | 0 | 0 | 0 | 0 | 0 | 0 |

**Códigos de Modificación (CodigoModificacion):**

| Código | Descripción | Aplica A |
|--------|-------------|----------|
| `1` | Anula documento completo | Nota Crédito/Débito |
| `2` | Corrige texto | Nota Crédito/Débito |
| `3` | Corrige montos | Nota Crédito/Débito |
| `4` | Reemplazo NCF emitido en contingencia | Nota Crédito/Débito |
| `5` | Referencia Factura de Consumo Electrónica | Solo Factura Crédito Fiscal |

> [!NOTE]
> **Nota al pie 80**: Los códigos 1, 2, 3 se aplican solo cuando se emite una nota de crédito o débito.
> 
> **Nota al pie 81**: El código 5 se aplica solo para Factura de Crédito Fiscal referenciando una factura de consumo.

---

## Sección G: Fecha y Hora de Firma Digital

| # | Elemento | Descripción | Máx | Tipo | Validación |
|---|----------|-------------|-----|------|------------|
| 1 | `<FechaHoraFirma>` | Marca de tiempo de firma | 19 | ALFANUM | DD-MM-YYYY HH:mm:ss, GMT-4. Debe ser ≤ hora actual. |

---

## Sección H: Firma Digital

| # | Elemento | Descripción | Obligatoriedad |
|---|----------|-------------|----------------|
| 1 | `<Signature>` | Firma envuelta XML-DSig cubriendo todo el documento | 1 (Obligatorio) |

Consulte [Guía de Firma Digital](../guides/digital-signing-guide.md) para detalles de implementación.

---

