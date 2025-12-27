# QA Review & Workload Strategy
**Created:** 2025-12-27
**Target:** Next LLM Session / QA Engineer

---

## 🧐 Current Status Assessment

The previous session successfully completed the "3-Way Documentation" and "Deep Table Verification" for the **4 auxiliary formats** (`ACECF`, `ARECF`, `ANULACION`, `RFCE`).
However, there are opportunities for improvement and potential gaps regarding the **main ECF format** (`ecf-format-v1.0.md`).

---

## 🛠️ Workload: Immediate Fixes

### 1. Typo Correction
- [x] **File:** `markdown/xml-formats/rfce-format-v1.0.md`
- **Issue:** Line ~247 contains "Foot note 4" (space between Foot and note).
- **Fix:** ~~Change to "**Footnote 4**".~~ ✅ **FIXED by Claude 4 Sonnet**

### 2. Footnote Reference Clarity
- [x] **File:** `markdown/xml-formats/rfce-format-v1.0.md`
- **Issue:** Footnote 5 says "See note 2". In the optimized layout, "Footnote 2" is located in the **Buyer** section (Line 123), which might be far away visually.
- **Suggestion:** ~~Change to "See Footnote 2 in Section A.3 (Comprador)" or repeat the content if brief.~~ ✅ **FIXED by Claude 4 Sonnet** - Added Footnote 2 to the section and updated reference.

---

## 🔍 Verification Gaps (Critical)

### 3. Main ECF Format Deep Verification
**Context:** The recent "Deep Table Verification" report covered the 4 auxiliary formats. It is unclear if the main `ecf-format-v1.0.md` (1,308 lines) received the same rigorous `camelot`/`pdfplumber` field-by-field check today.
- [ ] **Action:** Run the `verify_comprehensive.py` style script on `ecf-format-v1.0.md` vs the main ECF PDF extracts.
- [ ] **Check:** Verify `MontoImpuestoAdicional` and `ImpuestosAdicionales` table structures match the PDF exact layout (repeating rows vs columns).

### 4. "Optimized" Version Alignment
**Context:** The auxiliary files received a new "PDF Specification Footnotes" section today.
- [ ] **Action:** Check `ecf-format-v1.0.md` (Optimized). Does it have the "PDF Specification Footnotes" section at the end?
- [ ] **Action:** If missing, extract all footnotes from the main ECF PDF and add them to `ecf-format-v1.0.md` for completeness.

---

## 💡 Consistency & Improvements

### 5. Header Metadata Standardization
- [x] **Action:** Verify all 5 optimized files (`ecf`, `acecf`, `arecf`, `anulacion`, `rfce`) use the exact same header format:
    ```markdown
    > **Original**: [Spanish Name]
    > **Source**: [Link to PDF]
    > **Pages**: [Count]
    > **Scope**: [Description]
    ```
    ✅ **FIXED by Claude 4 Sonnet** - ECF header now standardized with Scope and clickable Source link.

### 6. XML Structure Examples
- [ ] **Action:** The auxiliary files have excellent XML code blocks showing the structure. Ensure `ecf-format-v1.0.md` has a similar high-level "Skeleton" XML block early in the document.

---

## ❓ Questions for the Next Agent

1. **Table I-VII in ECF:** The main ECF format has large reference tables (Units, Currencies, etc.). Are these hardcoded in the Markdown or referenced?
    *   *Suggestion:* If hardcoded, verify they match the latest "Anexo" CSVs exactly.
2. **Conditional Logic:** In `RFCE`, the "Additional Taxes" fields are listed as `Obligatoriedad: 2`. Are they mutually exclusive?
    *   *Suggestion:* Verify if `<TablaImpuestosAdicionales>` is a container tag in RFCE (similar to ECF) or if they are flat fields. Use `pdfplumber` to check nesting visualization.

---

## 🚀 Execution Plan for Next Session

1. **Apply fixes** to `rfce-format-v1.0.md` (typo & ref).
2. **Audit** `ecf-format-v1.0.md` structure against the new "Gold Standard" of the auxiliary files.
3. **Run Verification** on the main ECF file.
4. **Update** `ecf-format-v1.0.md` with:
    - Missing footnotes section.
    - Improved header.
    - Any table corrections found.

---

## Notes from Codex (GPT-5)

> **Model**: Codex (GPT-5)
> **Provenance**: The beginning of this workload was created by Gemini 3 Pro.
> **Acknowledgement**: I read Gemini's notes before adding these.
> **Context read**: `.agent/rules/README.md`, `.agent/rules/project-overview.md`, `.agent/rules/documentation-workflow.md`, `.agent/rules/documentation-language.md`, `.agent/rules/pdf-extraction-stack.md`

### Files checked
- `markdown/xml-formats/rfce-format-v1.0.md`
- `markdown/xml-formats/ecf-format-v1.0.md`

### Findings, suggestions, and possible fixes
- **RFCE Footnote spacing**: Confirmed `**Foot note 4**` appears in the "PDF Specification Footnotes" block. Suggested fix stands: change to `**Footnote 4**`.
- **RFCE Footnote 5 reference**: Confirmed `**Footnote 5**: See note 2.` In the same "PDF Specification Footnotes" block, **Footnote 2 is missing**. Possible fixes: add Footnote 2 to that block, or rewrite Footnote 5 as "See Footnote 2 in Section A.3 (Comprador)" and repeat the note if short.
- **ECF PDF footnotes section**: I do not see a dedicated "PDF Specification Footnotes" section in `ecf-format-v1.0.md`. There is a "Key Business Rules from Footnotes" list near the end plus footnotes embedded inline. I agree with Gemini that a dedicated footnotes section appears missing if you are standardizing with the auxiliary formats. Possible fix: add a "PDF Specification Footnotes" block at the end (or rename/expand the current "Key Business Rules from Footnotes" to align with the auxiliary format pattern).
- **ECF header metadata consistency**: `ecf-format-v1.0.md` header lacks a `Scope` line, and `Source` is plain text (not a link), unlike `rfce-format-v1.0.md`. I agree with Gemini that the header format is not aligned across the five files. Possible fix: add `Scope` and normalize `Source` to a markdown link.
- **ECF XML skeleton**: `ecf-format-v1.0.md` already contains a top-level XML structure block under "3. Document Structure". If the requirement is simply a high-level skeleton early in the doc, this action looks already satisfied. If the auxiliary files use a different style (e.g., more compact or labeled as "Skeleton"), consider matching that exact format.
- **Verification script mention**: I could not find any `verify_comprehensive.py` (or similar) in the repo. If this step is required, decide on the actual script name/location or add it to `scripts/` so the next agent can run it.
- **ImpuestosAdicionales structure**: In `ecf-format-v1.0.md`, `<ImpuestosAdicionales>` is shown as a container with fields 105-109, and `<MontoImpuestoAdicional>` appears as a separate total line. I cannot confirm table shape vs PDF without cross-checking exports. The workload action to verify layout with camelot/pdfplumber still seems valid.

### Questions / follow-ups for next agent
1. Should the ECF file adopt the same "PDF Specification Footnotes" block as the auxiliary formats, or is the existing "Key Business Rules from Footnotes" section intended to replace it?
2. Which verification tool/script should be used for the "Deep Table Verification" step if `verify_comprehensive.py` does not exist?

---

## 🚨 CRITICAL: Notes from Claude 4 Sonnet (Third Review)

> **Model**: Claude 4 Sonnet  
> **Provenance**: Following up on Gemini 3 Pro → Codex (GPT-5) review chain  
> **Date**: 2025-12-27

### Critical Finding: ECF Optimized Missing ~42 Footnote References

**Problem Statement:**
The `ecf-format-v1.0.md` (optimized) has significantly fewer footnote superscript references than the complete version:

| Version | Footnote References | Difference |
|---------|---------------------|------------|
| **Complete** (`-complete.md`) | **82** | — |
| **Optimized** (`.md`) | **4** | **-78 references!** |

The optimized version only contains footnotes ¹, ¹¹, ¹², and ³¹.
The complete version has footnotes ¹ through ⁸³.

### Specific Example: ImpuestosAdicionales Section

**Optimized (current):**
```markdown
| — | `<ImpuestosAdicionales>` | — | — | — | Container (up to 20 reps) | — | 2 | 2 | ...
```

**Complete (what it should look like):**
```markdown
| | **Additional Taxes Table `<ImpuestosAdicionales>`¹⁷** | Up to 20 repetitions of code-value pairs can be included.<br>Includes the following five fields: | | | a) Conditional on other tax(es) existing in the detail line different from ITBIS. | | 2 | 2 | 2 | 2 | 0 | 0 | **2¹⁸** | 2 | 0 | 0 |
```

**Missing in optimized:**
- ¹⁷ footnote on `<ImpuestosAdicionales>`
- ¹⁸ footnote on obligatoriedad column
- ²⁷, ²⁸, ²⁹ footnotes for detailed calculation rules
- ⁴⁰, ⁴⁶, ⁴⁷ footnotes for OtraMoneda section
- And ~70 more...

### Impact

The optimized version was meant to be the **BEST** version, but instead it **lost critical documentation** during "optimization":
1. **Footnote superscripts** in table cells are gone
2. **Detailed calculation formulas** are truncated
3. **Conditional validation rules** are simplified/missing
4. **Cross-references** between fields are lost

### Recommended Fix Strategy

**Option A: Full Restoration (Recommended)**
- [ ] Systematically compare each table row in optimized vs complete
- [ ] Restore all missing footnote superscripts (¹⁷, ¹⁸, etc.) to table cells
- [ ] Restore detailed validation rules in Description columns
- [ ] Keep the enhanced callouts and examples from optimized version

**Option B: Merge Approach**
- [ ] Start from complete version as base
- [ ] Add the enhanced callouts, examples, and developer notes from optimized
- [ ] This ensures nothing is lost

**Option C: Document as Design Decision**
- [ ] If "optimized" was intentionally simplified, rename to `ecf-format-v1.0-summary.md`
- [ ] Make `ecf-format-v1.0-complete.md` the canonical "optimized" version

### Priority

🔴 **P0 - CRITICAL**

The optimized version is currently **less complete** than the complete version. This violates the 3-way documentation principle where optimized = BEST of all versions.

### Files to Compare

```bash
# To see the gap:
grep -oE "[¹²³⁴⁵⁶⁷⁸⁹⁰]+" markdown/xml-formats/ecf-format-v1.0-complete.md | sort | uniq -c
grep -oE "[¹²³⁴⁵⁶⁷⁸⁹⁰]+" markdown/xml-formats/ecf-format-v1.0.md | sort | uniq -c
```

### Affected Sections (Non-exhaustive)

1. **B.1-B.8 Item Details** - Most footnotes are here (⁴⁸-⁶⁰)
2. **B.4 ImpuestosAdicionales** - Footnotes ¹⁷-²⁹
3. **B.8 OtraMoneda** - Footnotes ⁴⁰-⁴⁷
4. **D Discounts/Surcharges** - Footnotes ⁶⁵-⁷⁴
5. **F Reference Info** - Footnotes ⁷⁵-⁸³

