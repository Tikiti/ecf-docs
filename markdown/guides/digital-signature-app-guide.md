# Digital Signature App Guide

> **Original**: Instructivo App Firma Digital  
> **Source**: [Instructivo App Firma Digital.pdf](file:///home/romulo/visual/ecf/ecf-docs/Instructivos%20sobre%20Facturaci%C3%B3n%20Electr%C3%B3nica/Instructivo%20App%20Firma%20Digital.pdf)

---

## Overview

The **App Firma Digital** is a Windows desktop application provided by the DGII to facilitate the signing of XML documents during the certification and setup process. It is primarily used for signing:
- **Delegation Requests** (Solicitud de Delegación)
- **Test XMLs** (if manual signing is needed)

---

## Prerequisites

| Requirement | Details |
|-------------|---------|
| **OS** | Windows |
| **Framework** | .NET Framework 3.5+ |
| **Certificate** | Valid X.509 Digital Certificate (`.p12` or `.pfx`) |
| **Origin** | Must be issued by an Indotel-authorized CA |
| **Access** | You must have the Private Key password |

---

## Step-by-Step Usage

### 1. Installation
1.  Navigate to the DGII Website: `Facturación > Comprobantes Fiscales Electrónicos e-CF > Herramientas recomendadas`.
2.  Download the **App Firma Digital** (.zip).
3.  Extract the contents to a local folder.
4.  Run the executable `App Firma Digital.exe`.

### 2. Loading Files
1.  **Select XML**: Click the `Examinar` button next to the "XML a Firmar" field and select your unsigned XML file.
2.  **Select Certificate**: Click the `Examinar` button next to the "Certificado" field and select your `.p12` or `.pfx` file.
3.  **Enter Password**: Type the certificate's password in the "Contraseña" field.

### 3. Signing
1.  Click the **Descargar XML firmado** button.
2.  A system dialog will appear asking where to save the file.
3.  Choose a location and save. Use a clear name (e.g., `[OriginalName]_signed.xml`).

---

## Troubleshooting

- **Invalid Password**: Ensure the password is correct for the specific `.p12` file.
- **Certificate Error**: The app only supports certificates issued by authorized Dominican CAs (Avansi, Camara de Comercio, ViaFirma, etc.).
- **XML Structure**: If the XML is malformed, the app may crash or show an error. Validate your XML syntax before signing.

> [!TIP]
> This tool is useful for one-off tasks like signing the **Delegation Request** XML. For automated invoicing, you should implement the signing logic directly in your code (see [Digital Signing Guide](../guides/digital-signing-guide.md)).
