# DGII Electronic Invoicing (e-CF) Documentation Project

## Project Scope
This repository contains comprehensive technical documentation for the Dominican Republic's Electronic Fiscal Receipt (Comprobante Fiscal Electrónico - e-CF) system managed by the DGII (Dirección General de Impuestos Internos).

## Objectives
1. **Source of Truth**: Markdown files are the definitive reference for application development
2. **Developer-Friendly**: All documentation must be practical and implementation-ready
3. **1:1 Accuracy**: Markdown must be a complete, accurate representation of official PDF specifications
4. **Multilingual Support**: English documentation with preserved Spanish technical terms

## Repository Structure

### `/markdown/` - Primary Documentation (English)
- **`xml-formats/`**: XML schema documentation for all e-CF types
  - `ecf-format-v1.0.md` - Main e-CF format
  - `acecf-format-v1.0.md` - Commercial approval format
  - `arecf-format-v1.0.md` - Receipt acknowledgment format
  - `anulacion-format-v1.0.md` - Annulment format
  - `rfce-format-v1.0.md` - Consumer invoice summary format
  
- **`technical-reports/`**: Technical implementation guides
  - `technical-description.md` - API endpoints, authentication, workflow
  - `technical-report-ecf-v1.0.md` - Tax calculations, business rules, operations
  - `printed-representation-models.md` - Print specifications, QR codes
  
- **`guides/`**: Implementation guides
  - `digital-signing-guide.md` - Digital signature requirements
  - `certification-process.md` - Certification procedures
  - `role-delegation-guide.md` - User role management

- **`laws/`**: Legal foundation documents
  - `ley-32-23-es.md` - Spanish version of Law 32-23
  - `ley-32-23-en.md` - English translation

### `/exports/` - PDF Extraction Data
Structured extracts from official DGII PDFs using `camelot` and `pdfplumber`:
- Each PDF has a dedicated folder: `exports/<name>_<sha6>/`
- Contains: tables (CSV), text extracts, fingerprints, metadata
- See `pdf-extraction-stack.md` for extraction methodology

### Original PDFs
- Located in various directories (`laws/`, `Formatos XML/`, etc.)
- Serve as verification reference but NOT as primary documentation

## Key Design Decisions

### Markdown as Source of Truth
- Developers should reference Markdown files, not PDFs
- Markdown includes all PDF content plus improvements (better formatting, cross-references, examples)
- PDF extraction data in `/exports/` used for verification and updates

### Language Policy
- **Primary**: English for accessibility
- **Preserved**: Spanish technical terms, XML tags, legal identifiers
- See `documentation-language.md` for detailed rules

### Quality Standards
- **Completeness**: All tables, calculations, examples from PDFs
- **Accuracy**: Cross-verified against multiple extraction tools
- **Usability**: Organized for quick developer reference
- **Maintainability**: Clear structure, consistent formatting

## Workflow

### Adding/Updating Documentation
1. Extract PDF data (if not already in `/exports/`)
2. Create/update Markdown using extraction data as reference
3. Cross-verify critical details (calculations, field types, validation rules)
4. Ensure bilingual elements are properly handled
5. Test code examples if included

### PDF Extraction Process
See `pdf-extraction-stack.md` for complete methodology:
1. Generate fingerprint (SHA256)
2. Check if `exports/<name>_<sha6>/` exists (reuse if present)
3. Extract using `pdftotext`, `camelot`, and `pdfplumber`
4. Cross-verify between tools
5. Document discrepancies in `notes.md`
6. Update `exports/index.md` ledger

## Critical Information

### QR Code Specifications
- **Location**: Bottom left (or center for handhelds)
- **Minimum Size**: 22 x 22 mm
- **Margin**: 3mm on all sides
- **Distance from edge**: Minimum 2 cm
- See `printed-representation-models.md` for complete specs

### XML Validation
- All XML must be digitally signed
- Certificate SN field must match RNC/ID
- Whitespace handling is critical (`preserveWhiteSpace = false`)
- See `digital-signing-guide.md` for requirements

### Environment URLs
- **Production**: `https://ecf.dgii.gov.do/ecf/`
- **Certification**: `https://ecf.dgii.gov.do/certecf/`
- **Pre-Certification**: `https://ecf.dgii.gov.do/testecf/`

## Development Notes

### When Working on This Project
1. Always reference the latest Markdown, not PDFs
2. Preserve Spanish technical terms exactly as specified
3. Cross-verify critical details against `/exports/` data
4. Follow established naming and formatting conventions
5. Document any discrepancies found

### Common Tasks
- **Add new XML format**: Extract PDF → Create Markdown → Verify against exports
- **Update calculations**: Check `technical-report-ecf-v1.0.md` examples
- **Verify API endpoints**: Reference `technical-description.md`
- **Check legal requirements**: See `laws/ley-32-23-*.md`

---

## Three-Version Documentation System

### Version Types
Each official DGII document exists in three versions:

1. **Original Spanish** (`-original.md`)
   - Direct 1:1 from PDF in Spanish
   - Exact structure and content
   - Legal verification reference

2. **Complete English** (`-complete.md`)
   - 1:1 translation from original
   - Preserves structure exactly
   - English-speaking developer reference

3. **Optimized English** (no suffix `.md`)
   - Enhanced for development use
   - Improved organization and examples
   - **Primary source of truth** for implementation

### Why Three Versions?

**Original Spanish**: 
- Legal accuracy and verification
- Required for compliance review
- Matches official government document

**Complete English**:
- Accessible to international developers
- Exact content match for verification
- Translation reference

**Optimized English**:
- Best for actual development work
- Enhanced with cross-references
- Reorganized for clarity
- Includes additional examples

### Example File Set
```
technical-report-ecf-v1.0-original.md    # Spanish PDF match
technical-report-ecf-v1.0-complete.md    # English translation  
technical-report-ecf-v1.0.md             # Enhanced reference ⭐
```

### Current Status
- **Existing files**: All are optimized versions
- **Migration**: Backfilling `-original` and `-complete` versions
- **New files**: Follow full 3-version workflow

See `documentation-workflow.md` for complete details.
