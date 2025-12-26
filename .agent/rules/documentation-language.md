# Documentation Language Standards

## Primary Language
**All documentation must be written in English** to ensure maximum accessibility and compatibility with international development tools.

## Spanish Term Preservation
Preserve the following Spanish elements to maintain legal and technical accuracy:

### Legal and Official Terms
- Official document names: `Comprobante Fiscal Electrónico`, `Factura de Crédito Fiscal Electrónica`, `Nota de Débito Electrónica`, etc.
- Legal entity names: `Dirección General de Impuestos Internos (DGII)`, `Oficina Virtual (OFV)`
- Official identifiers: `RNC`, `e-NCF`, `e-CF`

### Technical Elements
- **XML Tags and Attributes**: Always preserve exact Spanish XML element names
  - Examples: `<MontoTotal>`, `<RncEmisor>`, `<FechaEmision>`, `<IndicadorFacturacion>`
- **Field Names in Tables**: When documenting XML fields, preserve the Spanish name as the primary identifier
  - Example: `<MontoGravadoITBIS>` (Total Amount Taxed with ITBIS)
- **Code Values**: Preserve Spanish enumeration values that are part of the specification
  - Example: `<IndicadorFacturacion>` values like "E" for "Exento"

## Documentation Structure
When documenting Spanish terms:

1. **First mention**: Provide both Spanish and English
   - Example: "Electronic Fiscal Receipt (**Comprobante Fiscal Electrónico** - e-CF)"

2. **Subsequent mentions**: Use abbreviation or English term with Spanish in parentheses where clarity is needed
   - Example: "The e-CF must contain the `<MontoTotal>` (Total Amount) field"

3. **Tables**: Include both languages in headers where appropriate
   | Spanish Name | English Name | Type | Description |
   |--------------|--------------|------|-------------|
   | `<MontoTotal>` | Total Amount | Numeric | The final amount including all taxes |

## Rationale
This approach ensures:
- Documentation is accessible to international developers
- Technical accuracy is maintained (XML specs cannot be translated)
- Legal terminology remains unambiguous
- Developers can copy-paste exact field names from documentation to code
