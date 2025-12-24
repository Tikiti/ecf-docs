# Digital Signing Guide for e-CF Documents

> **Original**: Firmado de e-CF  
> **Source**: [Firmado de e-CF.pdf](file:///home/romulo/visual/ecf/ecf-docs/Instructivos%20sobre%20Facturaci%C3%B3n%20Electr%C3%B3nica/Firmado%20de%20e-CF.pdf)

---

## Overview

Digital signatures are **mandatory** for all e-CF documents. They guarantee:
- **Authenticity** - Confirms the issuer's identity
- **Integrity** - Ensures the document hasn't been modified
- **Non-repudiation** - Issuer cannot deny having signed

---

## Technical Standards

| Parameter | Value / URI |
|-----------|-------------|
| **Standard** | XML Signature (XMLDSig) |
| **Reference** | [W3C XML Signature Core](https://www.w3.org/TR/xmldsig-core2/) |
| **Signature Method** | `http://www.w3.org/2001/04/xmldsig-more#rsa-sha256` |
| **Digest Method** | `http://www.w3.org/2001/04/xmlenc#sha256` |
| **Canonicalization** | `http://www.w3.org/TR/2001/REC-xml-c14n-20010315` |
| **Transform** | `http://www.w3.org/2000/09/xmldsig#enveloped-signature` |
| **Reference URI** | `""` (empty - covers entire document) |

> [!CAUTION]
> SHA-1 is **strictly prohibited**. Always use SHA-256.

---

## Certificate Requirements

| Requirement | Description |
|-------------|-------------|
| **Issuer** | Authorized Certification Authority (CA) in Dominican Republic |
| **Regulation** | Indotel-regulated providers |
| **Format** | `.p12` or `.pfx` (PKCS#12) |
| **Contents** | Private key + X.509 certificate chain |
| **Validity** | Must be valid at signing time |

---

## Signing Process

1. **Load the XML** document to be signed
2. **Load Certificate** from PKCS#12 file with password
3. **Configure Signature Engine**:
   - Set Canonicalization Method to C14N (without comments)
   - Set Signature Method to RSA-SHA256
   - Set Digest Method to SHA256
4. **Create Reference**:
   - URI = `""` (empty string)
   - Add Enveloped Signature transform
5. **Compute Signature** - Generate `SignatureValue` and `DigestValue`
6. **Embed Key Info** - Include X.509 certificate in `<KeyInfo>`
7. **Finalize** - Append `<Signature>` as last child of root element

---

## Code Examples

### C# (.NET)

```csharp
using System.Security.Cryptography.Xml;

// Load XML document and certificate
SignedXml signedXml = new SignedXml(xmlDoc);
signedXml.SigningKey = cert.PrivateKey;
signedXml.SignedInfo.SignatureMethod = 
    "http://www.w3.org/2001/04/xmldsig-more#rsa-sha256";

// Create reference covering entire document
Reference reference = new Reference("");
reference.AddTransform(new XmlDsigEnvelopedSignatureTransform());
reference.DigestMethod = "http://www.w3.org/2001/04/xmlenc#sha256";
signedXml.AddReference(reference);

// Add certificate to KeyInfo
KeyInfo keyInfo = new KeyInfo();
keyInfo.AddClause(new KeyInfoX509Data(cert));
signedXml.KeyInfo = keyInfo;

// Compute and append signature
signedXml.ComputeSignature();
xmlDoc.DocumentElement.AppendChild(
    xmlDoc.ImportNode(signedXml.GetXml(), true)
);
```

### VB.NET

```vbnet
Private Function Signed(ByVal xmlDoc As XmlDocument, ByVal pathCert As String, ByVal passCert As String) As XmlDocument
    Dim cert = New X509Certificate2(pathCert, passCert, X509KeyStorageFlags.Exportable)
    Dim exportedKeyMaterial = cert.PrivateKey.ToXmlString(True)
    Dim key = New RSACryptoServiceProvider(New CspParameters(24))
    key.PersistKeyInCsp = False
    key.FromXmlString(exportedKeyMaterial)
    
    Dim signedXml As SignedXml = New SignedXml(xmlDoc)
    signedXml.SigningKey = key
    signedXml.SignedInfo.SignatureMethod = "http://www.w3.org/2001/04/xmldsig-more#rsa-sha256"
    
    Dim reference As Reference = New Reference()
    reference.AddTransform(New XmlDsigEnvelopedSignatureTransform())
    reference.DigestMethod = "http://www.w3.org/2001/04/xmlenc#sha256"
    reference.Uri = ""
    signedXml.AddReference(reference)
    
    Dim keyInfo As KeyInfo = New KeyInfo()
    keyInfo.AddClause(New KeyInfoX509Data(cert))
    signedXml.KeyInfo = keyInfo
    signedXml.ComputeSignature()
    
    Dim xmlFirmaDigital As XmlElement = signedXml.GetXml()
    xmlDoc.DocumentElement.AppendChild(xmlDoc.ImportNode(xmlFirmaDigital, True))
    Return xmlDoc
End Function
```

### Java

> **References**: [Oracle Java SE](https://www.oracle.com/java/technologies/javase-downloads.html), [XML Parser v2](https://repo1.maven.org/maven2/com/oracle/database/xml/xmlparserv2/)

```java
import javax.xml.crypto.dsig.*;
import oracle.xml.parser.v2.DOMParser;
import oracle.xml.parser.v2.XMLDocument;

// Critical: Use Oracle parser with whitespace handling
DOMParser parser = new DOMParser();
parser.setPreserveWhitespace(false);  // REQUIRED!

XMLSignatureFactory fac = XMLSignatureFactory.getInstance("DOM");

// Create reference with enveloped transform
Reference ref = fac.newReference("", 
    fac.newDigestMethod(DigestMethod.SHA256, null),
    Collections.singletonList(
        fac.newTransform(Transform.ENVELOPED, (TransformParameterSpec) null)
    ), null, null);

// Create SignedInfo
SignedInfo si = fac.newSignedInfo(
    fac.newCanonicalizationMethod(
        CanonicalizationMethod.INCLUSIVE, 
        (C14NMethodParameterSpec) null
    ),
    fac.newSignatureMethod(
        "http://www.w3.org/2001/04/xmldsig-more#rsa-sha256", 
        null
    ),
    Collections.singletonList(ref)
);

// Create KeyInfo with certificate
KeyInfoFactory kif = fac.getKeyInfoFactory();
KeyInfo ki = kif.newKeyInfo(
    Collections.singletonList(
        kif.newX509Data(Collections.singletonList(cert))
    )
);

// Sign the document
DOMSignContext dsc = new DOMSignContext(
    keyEntry.getPrivateKey(), 
    xmlDoc.getDocumentElement()
);
XMLSignature signature = fac.newXMLSignature(si, ki);
signature.sign(dsc);
```

### PHP

> **Library**: [selective-php/xmldsig](https://github.com/selective-php/xmldsig)  
> **Tested Version**: PHP 8.1.12+

**Critical Library Modifications Required:**
The official PDF mandates modifying `XmlSigner.php` in the library:
1. Set `$xml->preserveWhiteSpace = false;` (default is true)
2. Change C14N call: `$element->C14N(false, false);` (remove comments)
3. In `appendSignature`, comment out `KeyValue`, `RSAKeyValue`, and `Exponent` tags (lines 154-170 approx).

```php
<?php
use Selective\XmlDSig\PrivateKeyStore;
use Selective\XmlDSig\Algorithm;
use Selective\XmlDSig\CryptoSigner;
use Selective\XmlDSig\XmlSigner;

public function sign(string $p12Content, string $password, string $xmlContent): string
{
    if (!openssl_pkcs12_read($p12Content, $certs, $password)) {
        throw new Exception("Error reading P12");
    }

    $pemContent = $certs['cert'] . $certs['pkey'];
    
    $privateKeyStore = new PrivateKeyStore();
    $privateKeyStore->loadFromPem($pemContent, $password);
    $privateKeyStore->addCertificatesFromX509Pem($pemContent);

    $algorithm = new Algorithm(Algorithm::METHOD_SHA256);
    $cryptoSigner = new CryptoSigner($privateKeyStore, $algorithm);
    
    // Remember: validation is strict on whitespace and C14N!
    $xmlSigner = new XmlSigner($cryptoSigner);
    $xmlSigner->setReferenceUri(''); 

    return $xmlSigner->signXml($xmlContent);
}
?>
```

### TypeScript/Node.js

```typescript
// Using xml-crypto library
import { SignedXml } from 'xml-crypto';
import * as fs from 'fs';

const xml = fs.readFileSync('ecf.xml', 'utf8');
const privateKey = fs.readFileSync('certificate.pem');

const sig = new SignedXml();
sig.signatureAlgorithm = 
    'http://www.w3.org/2001/04/xmldsig-more#rsa-sha256';
sig.addReference(
    '', 
    ['http://www.w3.org/2000/09/xmldsig#enveloped-signature'],
    'http://www.w3.org/2001/04/xmlenc#sha256'
);
sig.signingKey = privateKey;
sig.computeSignature(xml);

const signedXml = sig.getSignedXml();
```

### PHP

```php
<?php
// Using selective-php/xmldsig library
// https://github.com/selective-php/xmldsig

use Selective\XmlDSig\PrivateKeyStore;
use Selective\XmlDSig\Algorithm;
use Selective\XmlDSig\CryptoSigner;
use Selective\XmlDSig\XmlSigner;

// Load certificate from .p12 file
$certStore = file_get_contents('certificate.p12');
$password = 'your_password';

if (!openssl_pkcs12_read($certStore, $certs, $password)) {
    throw new Exception("Could not read certificate");
}

$pemContents = $certs['cert'] . $certs['pkey'];

$privateKeyStore = new PrivateKeyStore();
$privateKeyStore->loadFromPem($pemContents, $password);
$privateKeyStore->addCertificatesFromX509Pem($pemContents);

$algorithm = new Algorithm(Algorithm::METHOD_SHA256);
$cryptoSigner = new CryptoSigner($privateKeyStore, $algorithm);

$xmlSigner = new XmlSigner($cryptoSigner);
$xmlSigner->setReferenceUri('');  // Empty = entire document

$signedXml = $xmlSigner->signXml($xml);
```

> [!WARNING]
> **Critical Whitespace Handling (PHP/Java)**
> 
> When using XML parsers, you **must** set `preserveWhiteSpace = false`:
> - **PHP**: `$xml->preserveWhiteSpace = false;`
> - **Java (Oracle Parser)**: `parser.setPreserveWhitespace(false);`
> 
> Also for PHP: Use `$element->C14N(false, false)` for canonicalization, NOT `C14N(true, false)`.
> 
> Failure to do this will cause **signature validation failures**.

---

## Signature Structure

```xml
<ECF>
  <!-- Document content -->
  <Encabezado>...</Encabezado>
  <DetallesItems>...</DetallesItems>
  
  <!-- Signature appended as last element -->
  <Signature xmlns="http://www.w3.org/2000/09/xmldsig#">
    <SignedInfo>
      <CanonicalizationMethod Algorithm="..."/>
      <SignatureMethod Algorithm="..."/>
      <Reference URI="">
        <Transforms>
          <Transform Algorithm="...enveloped-signature"/>
        </Transforms>
        <DigestMethod Algorithm="..."/>
        <DigestValue>...</DigestValue>
      </Reference>
    </SignedInfo>
    <SignatureValue>...</SignatureValue>
    <KeyInfo>
      <X509Data>
        <X509Certificate>...</X509Certificate>
      </X509Data>
    </KeyInfo>
  </Signature>
</ECF>
```

---

## Security Code Derivation

The **Security Code** (`CodigoSeguridadeCF`) displayed on printed invoices is derived from the signature:

- Take the first **6 characters** of the `<SignatureValue>` hash
- This alphanumeric code is used for quick verification without full signature validation
- The code appears on printed invoices and is used in QR code URLs

> [!TIP]
> When building QR code URLs, remember to URL-encode the security code if it contains special characters.
