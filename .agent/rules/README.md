# Agent Rules for DGII e-CF Documentation

This directory contains rules that guide AI agents working on this project.

## Rule Files

### 📋 `project-overview.md`
**Purpose**: High-level project context and structure  
**When to read**: First time working on the project, or when context is needed  
**Contains**:
- Project objectives and scope
- Repository structure explanation
- Key design decisions
- Common workflows and tasks

### 🔄 `documentation-workflow.md` ⭐ **START HERE**
**Purpose**: Complete workflow for creating and managing documentation  
**When to apply**: Converting PDFs, creating new docs, updating existing docs  
**Key concept**: Three-version system
- `-original.md` - Spanish 1:1 from PDF
- `-complete.md` - English 1:1 translation  
- `.md` (no suffix) - Optimized English (source of truth)

### 🌍 `documentation-language.md`
**Purpose**: Language standards for all documentation  
**When to apply**: Creating or modifying any Markdown file  
**Key rules**:
- Write in English (for `-complete` and optimized versions)
- Preserve Spanish technical terms, XML tags, legal identifiers
- Use bilingual approach for first mentions

### 📊 `pdf-extraction-stack.md`
**Purpose**: Complete methodology for extracting data from DGII PDFs  
**When to apply**: Working with any PDF file or verifying documentation accuracy  
**Key rules**:
- Use multi-tool extraction (pdftotext, camelot, pdfplumber)
- Follow canonical naming: `exports/<stem100>_<sha6>/`
- Cross-verify between tools
- Reuse existing extractions (check fingerprint first)

## Quick Reference

### New to the Project?
1. Read `project-overview.md` for context
2. Read `documentation-workflow.md` for the 3-version system
3. Check `documentation-language.md` for language rules
4. Reference `pdf-extraction-stack.md` when working with PDFs

### Common Scenarios

#### 📄 "Convert this PDF to Markdown"
**Primary rule**: `documentation-workflow.md`

**Full process**:
1. Extract PDF (see `pdf-extraction-stack.md`)
   ```
   /exports/<name>_<sha6>/
   ```

2. Create `-original.md` (Spanish 1:1)
   - Use extraction data
   - Match PDF structure exactly

3. Create `-complete.md` (English 1:1)
   - Translate from `-original.md`
   - Keep structure identical
   - Preserve Spanish terms (see `documentation-language.md`)

4. Create `.md` (Optimized)
   - Enhance from `-complete.md`
   - Add cross-references, examples
   - Reorganize for developers

#### ✏️ "Update existing documentation"
**Primary rule**: `documentation-workflow.md`

**Process**:
1. Check which versions exist
2. Extract updated PDF (if applicable)
3. Update `-original.md` first
4. Update `-complete.md` from original
5. Update optimized `.md` last

#### 🔍 "Verify documentation accuracy"
**Primary rules**: `pdf-extraction-stack.md` + `documentation-workflow.md`

**Process**:
1. Check `/exports/` for extraction data
2. Compare `-original.md` to PDF extracts
3. Verify `-complete.md` matches `-original.md` structure
4. Ensure optimized `.md` includes all content

#### 🆕 "Create new technical guide"
**Primary rules**: `documentation-language.md` + `documentation-workflow.md`

**If no PDF source**:
- Create only optimized version (`.md`)
- Mark as "No PDF source" in file

**If PDF source exists**:
- Follow full 3-version workflow

## Current State of Documentation

### Existing Files
All current `.md` files are **optimized versions**:
- ✅ Ready for development use
- ⚠️ Missing `-original.md` and `-complete.md` versions

### Backfilling Priority
See `documentation-workflow.md` for:
- Migration strategy
- Priority order for creating missing versions
- Quality check criteria

## Rule Priority
When rules conflict (rare), priority order:
1. **Accuracy**: Technical correctness above all
2. **Official specs**: PDF specifications are authoritative
3. **Workflow**: Follow the 3-version system
4. **Consistency**: Follow established patterns
5. **Clarity**: Make it understandable for developers

## Visual Workflow Summary

```
┌─────────────────────────────────────────────────────────────┐
│                         PDF Document                         │
└────────────────────────────┬────────────────────────────────┘
                             │
                   ┌─────────▼─────────┐
                   │  Extract to       │
                   │  /exports/        │
                   │  (pdf-extraction- │
                   │   stack.md)       │
                   └─────────┬─────────┘
                             │
                   ┌─────────▼──────────────────┐
                   │  Create -original.md       │
                   │  (Spanish, 1:1 from PDF)   │
                   └─────────┬──────────────────┘
                             │
                   ┌─────────▼──────────────────┐
                   │  Create -complete.md       │
                   │  (English, 1:1 translation)│
                   │  (documentation-language)  │
                   └─────────┬──────────────────┘
                             │
                   ┌─────────▼──────────────────┐
                   │  Create .md (optimized)    │
                   │  (Enhanced, cross-refs)    │
                   │  ⭐ SOURCE OF TRUTH        │
                   └────────────────────────────┘
```

## Updates
These rules are living documents. If you notice:
- Missing scenarios
- Ambiguous guidance  
- Better approaches

Document the improvement and update the relevant rule file.
