# e-CF XML Schema Definitions (XSD) Reference

> **Source**: `Documentación Técnica (XSD)/`  
> **Total Files**: 15 XSDs

---

## Overview

The XML Schema Definitions (XSD) validate the structure, data types, and mandatory fields of the e-CF XML documents. You should use these files to validate your XML *before* sending it to the DGII API.

---

## Core Schemas

| XSD File | e-CF Type | Description |
|----------|-----------|-------------|
| `e-CF 31 v.1.0.xsd` | **31** | Factura de Crédito Fiscal (Tax Credit Invoice) |
| `e-CF 32 v.1.0.xsd` | **32** | Factura de Consumo (Consumer Invoice) |
| `e-CF 33 v.1.0.xsd` | **33** | Nota de Débito (Debit Note) |
| `e-CF 34 v.1.0.xsd` | **34** | Nota de Crédito (Credit Note) |
| `e-CF 41 v.1.0.xsd` | **41** | Comprobante de Compras (Purchases) |
| `e-CF 43 v.1.0.xsd` | **43** | Gastos Menores (Minor Expenses) |
| `e-CF 44 v.1.0.xsd` | **44** | Regímenes Especiales (Special Regimes) |
| `e-CF 45 v.1.0.xsd` | **45** | Gubernamental (Government) |
| `e-CF 46 v.1.0.xsd` | **46** | Exportaciones (Exports) |
| `e-CF 47 v.1.0.xsd` | **47** | Pagos al Exterior (Foreign Payments) |

---

## Response & Utility Schemas

| XSD File | Usage | Description |
|----------|-------|-------------|
| `ACECF v.1.0.xsd` | B2B Response | **Aprobación Comercial** (Commercial Approval/Rejection) |
| `ARECF v1.0.xsd` | B2B Response | **Acuse de Recibo** (Acknowledgment of Receipt) |
| `ANECF v.1.0.xsd` | Process | **Anulación** (Cancellation of unused sequences) |
| `RFCE 32 v.1.0.xsd` | Summary | **Resumen Factura Consumo** (Daily summary for <250k) |
| `Semilla v.1.0.xsd` | Auth | **Semilla** (Authentication Seed structure) |

---

## Validation Strategy

1. **Identify Type**: Check the `<TipoeCF>` element or root element name.
2. **Select XSD**: Load the corresponding schema from the list above (files are in `Documentación Técnica (XSD)/`).
3. **Validate**: Run XML validation.
   * **Success**: Proceed to signing.
   * **Failure**: Fix structure/types. Do *not* sign invalid XMLs.

### Python Validation Example

```python
from lxml import etree

def validate_ecf(xml_path: str, xsd_path: str) -> bool:
    schema = etree.XMLSchema(etree.parse(xsd_path))
    xml_doc = etree.parse(xml_path)
    return schema.validate(xml_doc)

# Usage
is_valid = validate_ecf('invoice.xml', 'e-CF 31 v.1.0.xsd')
```

### C# Validation Example

```csharp
using System.Xml;
using System.Xml.Schema;

XmlSchemaSet schemas = new XmlSchemaSet();
schemas.Add("", "e-CF 31 v.1.0.xsd");

XmlDocument doc = new XmlDocument();
doc.Load("invoice.xml");
doc.Schemas = schemas;
doc.Validate((sender, e) => Console.WriteLine(e.Message));
```

> [!TIP]
> The `Semilla v.1.0.xsd` validates the authentication seed structure (`<SemillaModel><valor>...</valor><fecha>...</fecha></SemillaModel>`) which is crucial for the authentication handshake.
