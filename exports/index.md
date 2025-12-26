# PDF Export Index (Ledger)

**Last updated:** 2025-12-25T20:15:51.951224

## Extraction Log

| PDF Filename | Fingerprint (SHA256) | Export Folder | Date | Tools |
|--------------|----------------------|---------------|------|-------|
| Formato Acuse de Recibo v 1.0.pdf... | `d48713b803461b4b...` | `Formato-Acuse-de-Recibo-v-1.0_d48713/` | 2025-12-25 20:12 | pdftotext, camelot, pdfplumber |
| Formato Anulación de e-NCF v1.0.pdf... | `a4f58709c05c3d14...` | `Formato-Anulacion-de-e-NCF-v1.0_a4f587/` | 2025-12-25 20:12 | pdftotext, camelot, pdfplumber |
| Formato Aprobación Comercial v1.0.pdf... | `2fede306878c730a...` | `Formato-Aprobacion-Comercial-v1.0_2fede3/` | 2025-12-25 20:12 | pdftotext, camelot, pdfplumber |
| Formato Comprobante Fiscal Electrónico (... | `c811c91a9e6a61a6...` | `Formato-Comprobante-Fiscal-Electronico-e-CF-V1.0_c811c9/` | 2025-12-25 20:14 | pdftotext, camelot, pdfplumber |
| Formato Resumen Factura Consumo Electrón... | `24f650b527a37fb6...` | `Formato-Resumen-Factura-Consumo-Electronica-v1.0_24f650/` | 2025-12-25 20:14 | pdftotext, camelot, pdfplumber |
| Descripcion-tecnica-de-facturacion-elect... | `6841ddf3d05384f5...` | `Descripcion-tecnica-de-facturacion-electronica_6841dd/` | 2025-12-25 20:14 | pdftotext, camelot, pdfplumber |
| Informe Técnico e-CF v1.0.pdf... | `0299436d18e20826...` | `Informe-Tecnico-e-CF-v1.0_029943/` | 2025-12-25 20:15 | pdftotext, camelot, pdfplumber |
| Representación Impresa (Modelos ilustrat... | `3f8da8532607d691...` | `Representacion-Impresa-Modelos-ilustrativos_3f8da8/` | 2025-12-25 20:15 | pdftotext, camelot, pdfplumber |
| Firmado de e-CF.pdf... | `bb32bb04c170ac3e...` | `Firmado-de-e-CF_bb32bb/` | 2025-12-25 20:15 | pdftotext, camelot, pdfplumber |
| Instructivo App Firma Digital.pdf... | `9ad6e0162b230cad...` | `Instructivo-App-Firma-Digital_9ad6e0/` | 2025-12-25 20:15 | pdftotext, camelot, pdfplumber |
| Instructivo Delegaciones de Roles de Fac... | `bd730c9678bcacdf...` | `Instructivo-Delegaciones-de-Roles-de-Facturacion-Electronica_bd730c/` | 2025-12-25 20:15 | pdftotext, camelot, pdfplumber |
| Solicitud Usuario Administrador de e-CF.... | `3de580ca7db015a7...` | `Solicitud-Usuario-Administrador-de-e-CF_3de580/` | 2025-12-25 20:15 | pdftotext, camelot, pdfplumber |
| Proceso de Certificacion para ser Emisor... | `1e4e53bde9f87dc9...` | `Proceso-de-Certificacion-para-ser-Emisor-Electronico_1e4e53/` | 2025-12-25 20:15 | pdftotext, camelot, pdfplumber |
| Proceso-Certificacion-EmisorElectronico-... | `d46564e625598332...` | `Proceso-Certificacion-EmisorElectronico-Proveedor-Servicios-FECertificado_d46564/` | 2025-12-25 20:15 | pdftotext, camelot, pdfplumber |

## Folder Structure Convention

Each folder follows: `<stem100>_<sha6>/`

Contents per folder:
- `source.pdf` - symlink to original PDF
- `fingerprint.txt` - full SHA256
- `pdf_layout.txt` - pdftotext -layout output
- `pdf_raw.txt` - pdftotext -raw output
- `camelot/lattice/` - Camelot lattice tables (CSV)
- `camelot/stream/` - Camelot stream tables (CSV)
- `camelot/summary.md` - Camelot extraction summary
- `pdfplumber/tables/` - pdfplumber tables (CSV)
- `pdfplumber/summary.md` - pdfplumber extraction summary
- `notes.md` - anomalies and cross-reference notes
