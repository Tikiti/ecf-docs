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
- [ ] **File:** `markdown/xml-formats/rfce-format-v1.0.md`
- **Issue:** Line ~247 contains "Foot note 4" (space between Foot and note).
- **Fix:** Change to "**Footnote 4**".

### 2. Footnote Reference Clarity
- [ ] **File:** `markdown/xml-formats/rfce-format-v1.0.md`
- **Issue:** Footnote 5 says "See note 2". In the optimized layout, "Footnote 2" is located in the **Buyer** section (Line 123), which might be far away visually.
- **Suggestion:** Change to "See Footnote 2 in Section A.3 (Comprador)" or repeat the content if brief.

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
- [ ] **Action:** Verify all 5 optimized files (`ecf`, `acecf`, `arecf`, `anulacion`, `rfce`) use the exact same header format:
    ```markdown
    > **Original**: [Spanish Name]
    > **Source**: [Link to PDF]
    > **Pages**: [Count]
    > **Scope**: [Description]
    ```

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
