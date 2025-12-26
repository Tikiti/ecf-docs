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
| **10-11-2020** | Se eliminaron acentos de las etiquetas `\u003cLiquidacion\u003e` y `\u003cMineria\u003e`. Se actualizó descriptions de SubDescuento/SubRecargo |
| **28-07-2020** | Se modificó `\u003cTotalITBISRetenido\u003e` y `\u003cTotalISRRetencion\u003e` para aceptar valores cero |

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
\u003cECF\u003e
  \u003cEncabezado\u003e                      \u003c!-- A. Encabezado --\u003e
    \u003cIdDoc\u003e...\u003c/IdDoc\u003e              \u003c!-- Identificación del documento --\u003e
    \u003cEmisor\u003e...\u003c/Emisor\u003e            \u003c!-- Datos del emisor --\u003e
    \u003cComprador\u003e...\u003c/Comprador\u003e      \u003c!-- Datos del comprador --\u003e
    \u003cInformacionesAdicionales\u003e...\u003c/InformacionesAdicionales\u003e  \u003c!-- Exportación/embarque --\u003e
    \u003cTransporte\u003e...\u003c/Transporte\u003e    \u003c!-- Datos de transporte --\u003e
    \u003cTotales\u003e...\u003c/Totales\u003e          \u003c!-- Totales --\u003e
    \u003cOtraMoneda\u003e...\u003c/OtraMoneda\u003e    \u003c!-- Totales en otra moneda --\u003e
  \u003c/Encabezado\u003e
  \u003cDetallesItem\u003e                   \u003c!-- B. Detalles de Ítems --\u003e
    \u003cItem\u003e...\u003c/Item\u003e
  \u003c/DetallesItem\u003e
  \u003cSubtotales\u003e...\u003c/Subtotales\u003e      \u003c!-- C. Subtotales Informativos --\u003e
  \u003cDescuentosORecargos\u003e...\u003c/DescuentosORecargos\u003e  \u003c!-- D. Descuentos o Recargos Globales --\u003e
  \u003cPaginacion\u003e...\u003c/Paginacion\u003e      \u003c!-- E. Paginación --\u003e
  \u003cInformacionReferencia\u003e...\u003c/InformacionReferencia\u003e  \u003c!-- F. Información de Referencia --\u003e
  \u003cFechaHoraFirma\u003e...\u003c/FechaHoraFirma\u003e  \u003c!-- G. Fecha y Hora de Firma --\u003e
  \u003cSignature\u003e...\u003c/Signature\u003e        \u003c!-- H. Firma Digital --\u003e
\u003c/ECF\u003e
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
| 1 | `\u003cVersion\u003e` | Versión del formato | 3 | ALFANUM | Valor: "1.0" | N | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 2 | `\u003cTipoeCF\u003e` | Código de tipo de e-CF | 2 | NUM | Tipo válido (31-47) | P | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 3 | `\u003ceNCF\u003e` | Número fiscal electrónico | 13 | ALFANUM | Formato de secuencia válida | I | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 4 | `\u003cFechaVencimientoSecuencia\u003e` | Fecha de vencimiento del e-NCF | 10 | DATE | DD-MM-YYYY | I | 1 | 0 | 1 | 0 | 1 | 1 | 1 | 1 | 1 | 1 |
| 5 | `\u003cIndicadorNotaCredito\u003e` | Nota de crédito \u003e30 días | 1 | NUM | 0=≤30 días, 1=\u003e30 días | N | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| 6 | `\u003cIndicadorEnvioDiferido\u003e` | Envío diferido | 1 | NUM | 0=normal, 1=diferido | N | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 2 | 0 |
| 7 | `\u003cIndicadorMontoGravado\u003e` | ITBIS incluido en precios | 1 | NUM | 0=excluido, 1=incluido | N | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 2 | 0 | 0 |
| 8 | `\u003cTipoIngresos\u003e` | Código de tipo de ingresos | 2 | NUM | Valores 01-06 (Ver Tabla VI) | N | 1 | 1 | 1 | 1 | 0 | 0 | 1 | 1 | 1 | 0 |
| 9 | `\u003cTipoPago\u003e` | Tipo de pago | 1 | NUM | 1=Contado, 2=Crédito, 3=Gratuito | N | 1 | 1 | 1 | 1 | 1 | 3 | 1 | 1 | 1 | 3 |
| 10 | `\u003cFechaLimitePago\u003e` | Fecha límite de pago | 10 | DATE | DD-MM-YYYY, ≥FechaEmision | N | 2 | 2 | 2 | 2 | 2 | 0 | 2 | 2 | 2 | 3 |
| 11 | `\u003cTerminoPago\u003e` | Términos de pago | 15 | ALFANUM | Texto libre | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| — | `\u003cTablaFormasPago\u003e` | Tabla de formas de pago | — | — | Contenedor (ver nota) | — | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 12 | `\u003cFormaPago\u003e` | Código de forma de pago | 2 | NUM | Valores 1-8 (Tabla V) | N | 3 | 3 | 3 | 0 | 3 | 0 | 3 | 3 | 3 | 3 |
| 13 | `\u003cMontoPago\u003e` | Monto del pago | 18 | NUM | 16 ent + 2 dec, ≥0 | N | 2 | 2 | 2 | 0 | 2 | 0 | 2 | 2 | 2 | 3 |
| 14 | `\u003cTipoCuentaPago\u003e` | Tipo de cuenta | 2 | ALFA | CT=Corriente, AH=Ahorro, OT=Otra | N | 3 | 3 | 3 | 0 | 3 | 0 | 3 | 3 | 3 | 3 |
| 15 | `\u003cNumeroCuentaPago\u003e` | Número de cuenta | 28 | ALFANUM | — | N | 3 | 3 | 3 | 0 | 3 | 0 | 3 | 3 | 3 | 3 |
| 16 | `\u003cBancoPago\u003e` | Nombre del banco | 75 | ALFANUM | — | N | 3 | 3 | 3 | 0 | 3 | 0 | 3 | 3 | 3 | 3 |
| 17 | `\u003cFechaDesde\u003e` | Inicio del período de facturación | 10 | ALFANUM | DD-MM-YYYY, ≤FechaHasta | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 3 |
| 18 | `\u003cFechaHasta\u003e` | Fin del período de facturación | 10 | ALFANUM | DD-MM-YYYY, ≥FechaDesde | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 3 |
| 19 | `\u003cTotalPaginas\u003e` | Total de páginas | 3 | NUM | \u003e1, condicional si existe Paginación | I | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |

\u003e [!NOTE]
\u003e **Estructura de `\u003cTablaFormasPago\u003e`**: Cada pago está envuelto en `\u003cFormaDePago\u003e` conteniendo `\u003cFormaPago\u003e` + `\u003cMontoPago\u003e`.
\u003e Para múltiples pagos vía cheque/transferencia (código 2), solo se debe usar UNA entrada `\u003cTipoCuentaPago\u003e`.

\u003e [!NOTE]
\u003e **Nota al pie 1**: La estructura del e-NCF consiste de: Letra de serie (E-Z, excepto P) + código de tipo de 2 dígitos + secuencia de 10 dígitos.
\u003e 
\u003e **Nota al pie 2**: `IndicadorNotaCredito = 1` significa que la nota de crédito pierde el beneficio de crédito fiscal de ITBIS (emitida \u003e30 días después de la original).
\u003e
\u003e **Nota al pie 3**: Facturas con `TipoPago = 3` (Gratuito/Libre) no pueden ser usadas para reclamaciones de crédito fiscal.

---

### A.2 Emisor (Issuer)

| # | Elemento | Descripción | Máx | Tipo | Validación | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|----------|-------------|-----|------|------------|:-:|----|----|----|----|----|----|----|----|----|----| 
| 20 | `\u003cRNCEmisor\u003e` | RNC del Emisor | 9/11 | NUM | 9 u 11 dígitos válidos | I | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 21 | `\u003cRazonSocialEmisor\u003e` | Razón social | 150 | ALFANUM | — | I | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 22 | `\u003cNombreComercial\u003e` | Nombre comercial | 150 | ALFANUM | — | I | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 23 | `\u003cSucursal\u003e` | Código de sucursal | 20 | ALFANUM | — | I | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 24 | `\u003cDireccionEmisor\u003e` | Dirección | 100 | ALFANUM | — | I | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 25 | `\u003cMunicipio\u003e` | Código de municipio | 6 | NUM | Tabla III | P | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 26 | `\u003cProvincia\u003e` | Código de provincia | 6 | NUM | Tabla III | P | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| — | `\u003cTablaTelefonoEmisor\u003e` | Contenedor de teléfonos (hasta 3) | — | — | — | — | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 27 | `\u003cTelefonoEmisor\u003e` | Número de teléfono (hasta 3) | 12 | ALFANUM | Formato: xxx-xxx-xxxx | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 28 | `\u003cCorreoEmisor\u003e` | Correo electrónico | 80 | ALFANUM | Formato de email válido | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 29 | `\u003cWebSite\u003e` | Sitio web | 50 | ALFANUM | — | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 30 | `\u003cActividadEconomica\u003e` | Actividad económica | 100 | ALFANUM | — | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 31 | `\u003cCodigoVendedor\u003e` | Código de vendedor | 60 | ALFANUM | Referencia interna | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 32 | `\u003cNumeroFacturaInterna\u003e` | Número de factura interna | 20 | ALFANUM | — | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 33 | `\u003cNumeroPedidoInterno\u003e` | Número de pedido interno | 20 | NUM | — | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 34 | `\u003cZonaVenta\u003e` | Zona de venta | 20 | ALFANUM | — | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 35 | `\u003cRutaVenta\u003e` | Ruta de venta | 20 | ALFANUM | — | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 36 | `\u003cInformacionAdicionalEmisor\u003e` | Información adicional | 250 | ALFANUM | — | N | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 37 | `\u003cFechaEmision\u003e` | Fecha de emisión | 10 | ALFANUM | DD-MM-YYYY, validar fecha inicio emisor electrónico | I | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |

---

### A.3 Comprador (Buyer)

| # | Elemento | Descripción | Máx | Tipo | Validación | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|----------|-------------|-----|------|------------|:-:|----|----|----|----|----|----|----|----|----|----| 
| 38 | `\u003cRNCComprador\u003e` | RNC del Comprador | 11 | NUM | 9 u 11 dígitos válidos | I | 1 | 2 | 2 | 2 | 1 | 0 | 1 | 1 | 2 | 2 |
| 39 | `\u003cIdentificadorExtranjero\u003e` | Identificación extranjera | 20 | ALFANUM | Para no residentes | I | 0 | 2 | 2 | 2 | 0 | 0 | 2 | 2 | 2 | 2 |
| 40 | `\u003cRazonSocialComprador\u003e` | Razón social | 150 | ALFANUM | — | I | 2 | 2 | 2 | 2 | 2 | 0 | 2 | 2 | 2 | 2 |
| 41 | `\u003cContactoComprador\u003e` | Nombre/teléfono de contacto | 80 | ALFANUM | — | N | 3 | 3 | 3 | 3 | 3 | 0 | 3 | 3 | 3 | 0 |
| 42 | `\u003cCorreoComprador\u003e` | Correo electrónico | 80 | ALFANUM | Email válido | N | 3 | 3 | 3 | 3 | 3 | 0 | 3 | 3 | 3 | 3 |
| 43 | `\u003cDireccionComprador\u003e` | Dirección | 100 | ALFANUM | — | N | 3 | 3 | 3 | 3 | 3 | 0 | 3 | 3 | 3 | 3 |
| 44 | `\u003cMunicipioComprador\u003e` | Municipio | 6 | NUM | Tabla III | N | 3 | 3 | 3 | 3 | 3 | 0 | 3 | 3 | 3 | 3 |
| 45 | `\u003cProvinciaComprador\u003e` | Provincia | 6 | NUM | Tabla III | N | 3 | 3 | 3 | 3 | 3 | 0 | 3 | 3 | 3 | 3 |
| 46 | `\u003cPaisComprador\u003e` | Nombre del país | 60 | ALFA | Nombre completo del país | P | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 47 | `\u003cFechaEntrega\u003e` | Fecha de entrega | 10 | DATE | DD-MM-YYYY | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 48 | `\u003cContactoEntrega\u003e` | Contacto de entrega | 100 | ALFANUM | — | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 49 | `\u003cDireccionEntrega\u003e` | Dirección de entrega | 100 | ALFANUM | — | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 50 | `\u003cTelefonoAdicional\u003e` | Teléfono de entrega | 12 | ALFANUM | — | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 51 | `\u003cFechaOrdenCompra\u003e` | Fecha de orden de compra | 10 | DATE | DD-MM-YYYY | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 52 | `\u003cNumeroOrdenCompra\u003e` | Número de orden de compra | 20 | ALFANUM | — | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 53 | `\u003cCodigoInternoComprador\u003e` | Código interno del comprador | 20 | ALFANUM | Referencia interna | N | 3 | 3 | 3 | 3 | 3 | 0 | 3 | 3 | 3 | 0 |
| 54 | `\u003cResponsablePago\u003e` | Responsable del pago | 20 | ALFA | — | N | 3 | 3 | 3 | 3 | 3 | 0 | 3 | 3 | 3 | 0 |
| 55 | `\u003cInformacionadicionalcomprador\u003e` | Notas | 150 | ALFANUM | — | N | 3 | 3 | 3 | 3 | 3 | 0 | 3 | 3 | 3 | 0 |

\u003e [!IMPORTANT]
\u003e **Reglas de Identificación del Comprador:**
\u003e - Tipo 31 (Crédito Fiscal): `RNCComprador` siempre obligatorio
\u003e - Tipo 32 (Consumo) ≥ RD$250,000: `RNCComprador` o `IdentificadorExtranjero` obligatorio
\u003e - Tipo 32 (Consumo) \u003c RD$250,000: `RNCComprador` opcional
\u003e - Tipo 46 (Exportaciones): Usar `RNCComprador` para residentes, `IdentificadorExtranjero` para no residentes

---

### A.4 InformacionesAdicionales (Información de Exportación/Embarque)

Esta sección se utiliza principalmente para **Tipo 46 (Exportaciones)** y facturas relacionadas con embarques.

| # | Elemento | Descripción | Máx | Tipo | Validación | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|----------|-------------|-----|------|------------|:-:|----|----|----|----|----|----|----|----|----|----| 
| 56 | `\u003cFechaEmbarque\u003e` | Fecha de embarque | 10 | DATE | DD-MM-YYYY | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 57 | `\u003cNumeroEmbarque\u003e` | Número de embarque | 25 | ALFA | — | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 58 | `\u003cNumeroContenedor\u003e` | Número de contenedor | 100 | ALFA | — | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 59 | `\u003cNumeroReferencia\u003e` | Número de referencia | 20 | NUM | — | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 60 | `\u003cNombrePuertoEmbarque\u003e` | Puerto de carga | 40 | ALFA | — | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 61 | `\u003cCondicionesEntrega\u003e` | Términos de entrega | 3 | ALFA | CIF/FOB/EXW etc. | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 62 | `\u003cTotalFob\u003e` | Valor total FOB | 18 | DEC | ≥0, 2 decimales | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 63 | `\u003cSeguro\u003e` | Monto del seguro | 18 | DEC | ≥0, 2 decimales | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 64 | `\u003cFlete\u003e` | Monto del flete | 18 | DEC | ≥0, 2 decimales | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 65 | `\u003cOtrosGastos\u003e` | Otros gastos | 18 | DEC | ≥0, 2 decimales | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 66 | `\u003cTotalCif\u003e` | Valor total CIF | 18 | DEC | FOB+Seguro+Flete+Otros | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 67 | `\u003cRegimenAduanero\u003e` | Régimen aduanero | 35 | ALFA | Según clasificación DGA | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 68 | `\u003cNombrePuertoSalida\u003e` | Puerto de salida | 40 | ALFANUM | — | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 69 | `\u003cNombrePuertoDesembarque\u003e` | Puerto de destino | 40 | ALFANUM | — | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 70 | `\u003cPesoBruto\u003e` | Peso bruto | 18 | DEC | ≥0, 2 decimales | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 71 | `\u003cPesoNeto\u003e` | Peso neto | 18 | DEC | ≥0, 2 decimales | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 72 | `\u003cUnidadPesoBruto\u003e` | Unidad de peso bruto | 2 | NUM | Tabla IV | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 73 | `\u003cUnidadPesoNeto\u003e` | Unidad de peso neto | 2 | NUM | Tabla IV | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 74 | `\u003cCantidadBulto\u003e` | Número de paquetes | 18 | DEC | \u003e0, 2 decimales | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 75 | `\u003cUnidadBulto\u003e` | Unidad de paquete | 2 | NUM | Tabla IV | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 76 | `\u003cVolumenBulto\u003e` | Volumen | 18 | DEC | \u003e0, 2 decimales | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 77 | `\u003cUnidadVolumen\u003e` | Unidad de volumen | 2 | NUM | Tabla IV | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |

\u003e [!NOTE]
\u003e **Distinción de Etiquetas de Puerto**: Según especificación DGII, estos son 3 puertos diferentes:
\u003e - `NombrePuertoEmbarque` (#60) = Puerto donde se cargan las mercancías
\u003e - `NombrePuertoSalida` (#68) = Puerto de partida (puede diferir del puerto de carga)
\u003e - `NombrePuertoDesembarque` (#69) = Puerto de destino (descarga)

---

### A.5 Transporte (Transport)

| # | Elemento | Descripción | Máx | Tipo | Validación | I | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
|---|----------|-------------|-----|------|------------|:-:|----|----|----|----|----|----|----|----|----|----| 
| 78 | `\u003cViaTransporte\u003e` | Modo de transporte | 2 | NUM | 01=Terrestre, 02=Marítimo, 03=Aérea | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 79 | `\u003cPaisOrigen\u003e` | País de origen de la mercancía | 60 | ALFA | — | N |  0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 80 | `\u003cDireccionDestino\u003e` | Dirección de destino | 100 | ALFANUM | — | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 81 | `\u003cPaisDestino\u003e` | País de destino | 60 | ALFA | — | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 3 |
| 82 | `\u003cRNCIdentificacionCompaniaTransportista\u003e` | RNC/ID del transportista | 20 | ALFANUM | — | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 83 | `\u003cNombreCompaniaTransportista\u003e` | Nombre de compañía transportista | 150 | ALFANUM | — | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 84 | `\u003cNumeroViaje\u003e` | Número de viaje/vuelo | 20 | ALFANUM | — | N | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| 85 | `\u003cConductor\u003e` | Código o nombre del conductor | 20 | ALFANUM | — | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 86 | `\u003cDocumentoTransporte\u003e` | Documento de transporte | 20 | NUM | — | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 87 | `\u003cFicha\u003e` | Ficha/registro de transporte | 10 | ALFANUM | — | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 88 | `\u003cPlaca\u003e` | Número de placa del vehículo | 7 | ALFANUM | — | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 89 | `\u003cRutaTransporte\u003e` | Ruta de transporte establecida | 20 | ALFANUM | — | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 90 | `\u003cZonaTransporte\u003e` | Zona de transporte | 20 | ALFANUM | — | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |
| 91 | `\u003cNumeroAlbaran\u003e` | Número de albarán de entrega | 20 | ALFANUM | — | N | 3 | 3 | 3 | 3 | 0 | 0 | 3 | 3 | 3 | 0 |

---
