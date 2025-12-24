# DGII Electronic Invoicing (e-CF) Documentation

This directory contains markdown conversions of the official DGII PDF documentation for electronic fiscal documents (e-CF) in the Dominican Republic.

> **Last Updated**: December 2024  
> **Documentation Version**: e-CF v1.0

---

## 📁 Directory Structure

```
markdown/
├── technical-reports/     # System overview and specifications
├── xml-formats/           # XML schema documentation
├── guides/                # Implementation guides
└── schemas/               # XSD reference documentation
```

---

## 📋 Technical Reports

| Document | Description |
|----------|-------------|
| [Technical Description](technical-reports/technical-description.md) | System overview, integration modes, business flows |
| [Technical Report e-CF v1.0](technical-reports/technical-report-ecf-v1.0.md) | Complete e-CF specification and data structure |
| [Printed Representation Models](technical-reports/printed-representation-models.md) | Visual/layout requirements for printed invoices |

---

## 📄 XML Format Specifications

### Main Document Types

| Document | Description |
|----------|-------------|
| [e-CF Format v1.0](xml-formats/ecf-format-v1.0.md) | Complete e-CF XML structure (87 pages) |
| [RFCE Format v1.0](xml-formats/rfce-format-v1.0.md) | Consumer invoice summary (< RD$250k) |

### Response Documents

| Document | Description |
|----------|-------------|
| [ARECF Format v1.0](xml-formats/arecf-format-v1.0.md) | Acknowledgment of receipt |
| [ACECF Format v1.0](xml-formats/acecf-format-v1.0.md) | Commercial approval/rejection |
| [Anulación Format v1.0](xml-formats/anulacion-format-v1.0.md) | e-NCF cancellation |

---

## 📖 Implementation Guides

| Guide | Description |
|-------|-------------|
| [Digital Signing Guide](guides/digital-signing-guide.md) | XMLDSig implementation with code examples (C#, Java, PHP, TypeScript) |
| [Digital Signature App Guide](guides/digital-signature-app-guide.md) | DGII desktop tool for one-off signing |
| [Role Delegation Guide](guides/role-delegation-guide.md) | Delegating Signer/Approver roles in Virtual Office |
| [Admin User Request Guide](guides/admin-user-request-guide.md) | Designating the Usuario Administrador |
| [Certification Process](guides/certification-process.md) | 15-step DGII certification flow |
| [XSD Reference](schemas/xsd-reference.md) | Consolidated XML schema documentation |

---

## 🔑 Quick Reference

### e-CF Type Codes

| Code | Type | Description |
|------|------|-------------|
| 31 | E31 | Factura de Crédito Fiscal Electrónica |
| 32 | E32 | Factura de Consumo Electrónica |
| 33 | E33 | Nota de Débito Electrónica |
| 34 | E34 | Nota de Crédito Electrónica |
| 41 | E41 | Comprobante de Compras Electrónico |
| 43 | E43 | Comprobante de Gastos Menores |
| 44 | E44 | Comprobante de Regímenes Especiales |
| 45 | E45 | Comprobante Gubernamental |
| 46 | E46 | Comprobante para Exportaciones |
| 47 | E47 | Comprobante para Pagos al Exterior |

### ITBIS Tax Rates

| Rate | Type |
|------|------|
| 18% | Standard rate |
| 16% | Reduced rate |
| 0% | Zero rate / Exempt |

### Integration Modes

| Mode | Description |
|------|-------------|
| Synchronous | Real-time validation |
| Large Issuer | Simplified flows for high volume |

### Key Business Thresholds

| Threshold | Rule |
|-----------|------|
| **RD$250,000** | Consumer invoices ≥ this amount require buyer identification |
| **RD$250,000** | Consumer invoices < this amount use RFCE summary format |
| **1,000 items** | Maximum line items per e-CF document |
| **1 hour** | Bearer token validity period |

### Environment URLs

| Environment | Standard (ecf) | Consumer Summary (fc) |
|-------------|----------------|----------------------|
| Pre-cert | `ecf.dgii.gov.do/testecf/` | `fc.dgii.gov.do/testecf/` |
| Cert | `ecf.dgii.gov.do/certecf/` | `fc.dgii.gov.do/certecf/` |
| Production | `ecf.dgii.gov.do/ecf/` | `fc.dgii.gov.do/ecf/` |

---

## 📂 Source Files

All markdown files were converted from PDFs in:
- `Informe y Descripción Técnica/`
- `Formatos XML/`
- `Instructivos sobre Facturación Electrónica/`
- `Documentaciones Proceso de Certificación FE/`

XSD schemas are available in `Documentación Técnica (XSD)/`.
