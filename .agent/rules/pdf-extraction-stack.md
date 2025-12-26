# PDF extraction stack (table-heavy PDFs) for this workspace

## Assumptions
- These PDFs are **table-heavy** and messy.
- `pdftotext` is **never enough by itself**. It is a *reference snapshot*, not the source of truth.
- We want **repeatable extractions**, **cross-tool verification**, **cache reuse**, and **consistent exports**.

## Tooling available
- Python is installed.
- `camelot-py[cv]` and `pdfplumber` are available (installed via pipx on this system).
- `pdftotext` is available and should be used for layout-preserved text snapshots.

## Export/caching policy (mandatory)
- Use a project folder named: `./exports/` as the extraction dumpster.
- For each PDF, create a dedicated subfolder using the canonical naming convention:
  - `./exports/<stem100>_<sha6>/`

Before extracting anything:
1) Compute the PDF fingerprint (SHA256 of the PDF bytes).
2) Compute `<stem100>_<sha6>` (rules below).
3) If `./exports/<stem100>_<sha6>/` already exists, reuse prior outputs and **do not re-extract** unless explicitly requested.

### Canonical folder naming convention (mandatory)
Given a PDF named `<pdf_stem>.pdf`:

1) `stem100`:
   - Take the first 100 characters of `<pdf_stem>` (truncate).
   - Sanitize to filesystem-safe while keeping Spanish readability:
     - Preserve ASCII letters/digits plus `._-`
     - Convert spaces to `-`
     - **Transliterate Spanish diacritics to plain letters**:
       - `áéíóúñÁÉÍÓÚÑ` → `aeiounAEIOUN`
     - After transliteration, replace remaining unsupported characters with `-`
     - Collapse repeated `-` into a single `-`
     - Trim leading/trailing `-` or `_`
     - Keep original letter case (do NOT force lowercase), so names stay readable.

2) `sha6`:
   - Compute SHA256 of the PDF bytes.
   - Take the first 6 hex characters.

Canonical folder name:
- `./exports/<stem100>_<sha6>/`

Example:
- `Cotización Ñandú Ácido Útil v2.pdf`
- `stem100` → `Cotizacion-Nandu-Acido-Util-v2`
- sha6 → `a1b2c3`
- folder → `./exports/Cotizacion-Nandu-Acido-Util-v2_a1b2c3/`

### Fingerprint rule
- Store the full SHA256 in:
  - `./exports/<stem100>_<sha6>/fingerprint.txt`

## Indexing policy (mandatory)
- Maintain an `./exports/index.md` file as the extraction ledger.
- On each new extraction, append an entry with:
  - PDF filename
  - fingerprint (full SHA256)
  - export subfolder path (`./exports/<stem100>_<sha6>/`)
  - date/time of extraction
  - tools used + key settings (camelot lattice/stream params, pages processed)
  - notes about detected issues (merged cells, broken lines, rotated tables, repeated headers/footers, etc.)

## Extraction strategy (default order)
We do **multi-tool extraction** and cross-reference outputs:

### 1) `pdftotext` snapshots (reference only)
- Always produce:
  - `pdftotext -enc UTF-8 -layout "<PDF>" "<OUT>/pdf_layout.txt"`
  - `pdftotext -enc UTF-8 -raw "<PDF>" "<OUT>/pdf_raw.txt"`
- These are **reference snapshots**. Never treat them as the sole source of truth.

### 2) Camelot first (tables are the point)
- Prefer Camelot whenever tables are present.
- Try **lattice** first when ruling lines exist.
- Fall back to **stream** when lines are missing or inconsistent.
- Save outputs:
  - CSVs (one per table)
  - plus `camelot/summary.md` (or JSON) mapping: page → tables found → shape → settings

### 3) pdfplumber for verification + edge cases
Use pdfplumber to:
- confirm table boundaries and row/column counts
- extract text around tables (headers, footnotes, multi-line cells)
- detect repeated headers/footers and pagination artifacts
Save:
- `pdfplumber/tables/` per-page dumps
- `pdfplumber/summary.md` page-by-page notes

## Cross-referencing rules (non-negotiable)
- Never trust a single tool output.
- Compare:
  - Camelot tables vs pdfplumber tables (row/column counts, missing columns, merged cells)
  - `pdftotext -layout` as the “visual truth” for what appears on the page
- If tools disagree:
  - call it out explicitly
  - prefer the interpretation that best matches the page layout snapshot and table structure
  - document the discrepancy in `notes.md` and in `exports/index.md`.

## Output conventions (mandatory structure)
Inside each PDF export folder `./exports/<stem100>_<sha6>/`:

- `source.pdf` (copy or symlink if appropriate)
- `fingerprint.txt` (full SHA256)
- `pdf_layout.txt`
- `pdf_raw.txt`
- `camelot/`
  - `lattice/`
  - `stream/`
  - `summary.md`
- `pdfplumber/`
  - `tables/`
  - `summary.md`
- `notes.md` (human-readable anomalies + decisions)

## Failure handling
- If `import camelot` / `import pdfplumber` fails:
  - assume the wrong Python environment is being used (pipx isolation vs project venv).
  - prefer using a project `.venv` with pinned requirements for repeatability.
- Always surface the failure reason and the exact command used.

## Important limitation (intentional)
- Do **not** attempt to “repair” or restructure an existing messy `./exports/` tree automatically.
- If `./exports/index.md` is missing or the export tree is inconsistent:
  - create a fresh, correct export folder for the current PDF (using the canonical naming rules),
  - and continue normally.
