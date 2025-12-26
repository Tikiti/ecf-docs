# Three-Version Documentation Workflow

## Overview
Every official DGII PDF should be documented in **three versions**, each serving a specific purpose:

1. **Original** (`-original.md`) - Spanish 1:1 from PDF
2. **Complete** (`-complete.md`) - English 1:1 translation
3. **Optimized** (no suffix) - Enhanced English reference

## File Naming Convention

Given a document about "Technical Report e-CF":

```
technical-report-ecf-v1.0-original.md    # Spanish, direct from PDF
technical-report-ecf-v1.0-complete.md    # English, direct translation
technical-report-ecf-v1.0.md              # English, optimized (source of truth)
```

**Rules**:
- Base filename is always in English (lowercase with dashes)
- Original Spanish: add `-original` suffix
- Complete English: add `-complete` suffix  
- Optimized English: no suffix (this is the default for developers)

## Version Purposes

### 1. Original Spanish (`-original.md`)
**Purpose**: Exact 1:1 representation of the PDF in original Spanish

**Characteristics**:
- Matches PDF structure exactly (sections, subsections, numbering)
- Preserves all Spanish text as-is
- Includes all tables, examples, footnotes exactly as they appear
- Maintains PDF formatting conventions (bullet styles, numbering)
- No enhancements or reorganization

**Use case**: Legal verification, exact reference to official document

**Creation**:
- Extract from `/exports/<pdf>_<sha6>/` data
- Cross-verify with `pdf_layout.txt` and extracted tables
- Preserve every detail from PDF

### 2. Complete English (`-complete.md`)
**Purpose**: 1:1 translation of the Original Spanish version

**Characteristics**:
- Translates all Spanish prose to English
- Preserves exact structure from `-original.md`
- Keeps Spanish technical terms (XML tags, legal identifiers)
- Includes bilingual presentation: "Electronic Fiscal Receipt (**Comprobante Fiscal Electrónico** - e-CF)"
- No reorganization or optimization

**Use case**: English-speaking developers who need exact PDF content

**Creation**:
- Translate from `-original.md` version
- Follow `documentation-language.md` rules for term preservation
- Maintain identical structure and section numbering

### 3. Optimized English (no suffix)
**Purpose**: Enhanced, developer-friendly reference (source of truth)

**Characteristics**:
- Reorganized for clarity and usability
- Added cross-references to other documents
- Improved examples with code snippets
- Better formatting (tables, callouts, notes)
- Additional explanations where PDF is unclear
- Indexed for quick reference
- May combine related sections or split complex ones

**Use case**: Primary reference for application development

**Creation**:
- Start from `-complete.md` version
- Enhance structure for developer workflow
- Add cross-references, examples, clarifications
- Improve formatting and organization

## Standard Workflow

### Starting Fresh (New PDF)
```
Step 1: Extract PDF
  └─> /exports/<pdf>_<sha6>/
      ├─ fingerprint.txt
      ├─ pdf_layout.txt
      ├─ camelot/lattice/*.csv
      └─ pdfplumber/tables/*.csv

Step 2: Create Original Spanish
  └─> <filename>-original.md
      (1:1 from PDF, Spanish)

Step 3: Create Complete English  
  └─> <filename>-complete.md
      (1:1 translation from -original.md)

Step 4: Create Optimized English
  └─> <filename>.md
      (Enhanced from -complete.md)
```

### Backfilling Existing Documentation
Most existing files are **optimized versions**. To create missing versions:

**If you have optimized → create complete & original**:
```
Step 1: Create -complete.md
  - Use optimized version as reference
  - Remove enhancements (cross-refs, reorganization)
  - Match original PDF structure from /exports/ data
  - Keep bilingual format

Step 2: Create -original.md
  - Translate -complete.md to Spanish
  - Verify against PDF exports
  - Ensure 1:1 match with PDF structure
```

**If you have original → create complete & optimized**:
```
Step 1: Create -complete.md
  - Translate -original.md to English
  - Preserve structure exactly
  - Follow language preservation rules

Step 2: Create -optimized.md
  - Enhance -complete.md for usability
  - Add developer-friendly improvements
```

## Cross-Version Consistency

When creating or updating any version, use other versions for verification:

**Creating `-original.md`**:
- Check optimized version for field names, calculations
- Verify structure against `/exports/` PDF data
- Ensure no content is missed

**Creating `-complete.md`**:
- Compare to `-original.md` for structural match
- Compare to optimized for technical accuracy
- Ensure all Spanish terms are properly preserved

**Creating optimized**:
- Verify all content from `-complete.md` is included
- Check enhancements don't contradict PDF specs
- Ensure cross-references are accurate

## Migration Strategy for Existing Docs

### Current State
All existing `.md` files in `/markdown/` are **optimized versions**:
- `technical-report-ecf-v1.0.md` ✓ (optimized)
- `ecf-format-v1.0.md` ✓ (optimized)
- `digital-signing-guide.md` ✓ (optimized)
- etc.

### Priority for Backfilling
Focus on high-value documents first:

**Priority 1** (Critical for development):
1. `ecf-format-v1.0.md` - Main XML format
2. `technical-description.md` - API and workflow
3. `technical-report-ecf-v1.0.md` - Tax calculations

**Priority 2** (Referenced formats):
4. `acecf-format-v1.0.md`
5. `rfce-format-v1.0.md`
6. `anulacion-format-v1.0.md`

**Priority 3** (Guides):
7. `digital-signing-guide.md`
8. `certification-process.md`

### Backfill Process
For each document:
1. Verify `/exports/<pdf>_<sha6>/` exists (extract if not)
2. Create `-original.md` from exports + optimized reference
3. Create `-complete.md` from original translation
4. Verify optimized version is still accurate

## Quality Checks

### For `-original.md`
- [ ] Structure matches PDF exactly (section numbers, order)
- [ ] All tables included with correct data
- [ ] All examples and calculations present
- [ ] Footnotes and references preserved
- [ ] No missing content vs PDF

### For `-complete.md`
- [ ] Structure identical to `-original.md`
- [ ] All Spanish technical terms preserved correctly
- [ ] Bilingual format for first mentions
- [ ] Translation is accurate and clear
- [ ] No reorganization or optimization

### For optimized `.md`
- [ ] All content from `-complete.md` included
- [ ] Enhancements improve clarity
- [ ] Cross-references are accurate
- [ ] Examples are correct and helpful
- [ ] Developer-focused organization

## Special Cases

### Documents Without PDF Source
Some guides may not have PDF sources (created directly as Markdown):
- Create only optimized version
- Mark as "No PDF source" in frontmatter

### Multilingual PDFs
If PDF is bilingual:
- `-original.md` includes both languages as in PDF
- `-complete.md` translates to English only
- Note bilingual source in both files

### Version Updates
When PDF is updated:
1. Extract new PDF to new `/exports/` folder (new SHA6)
2. Create new `-original.md` from new PDF
3. Compare with old `-original.md` to identify changes
4. Update `-complete.md` accordingly
5. Update optimized `.md` with changes
6. Document changes in all three versions
