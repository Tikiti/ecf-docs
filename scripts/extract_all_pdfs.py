#!/usr/bin/env python3
"""
PDF Extraction Script following the pdf-extraction-stack.md workflow.

Uses:
- pdftotext for layout snapshots (reference only)
- camelot-py for table extraction (lattice + stream)
- pdfplumber for verification + edge cases

Follows canonical naming: <stem100>_<sha6>/
"""

import os
import hashlib
import subprocess
import csv
import warnings
from pathlib import Path
from datetime import datetime
import unicodedata

warnings.filterwarnings('ignore')

# Try imports
try:
    import camelot
    CAMELOT_AVAILABLE = True
except ImportError:
    CAMELOT_AVAILABLE = False

try:
    import pdfplumber
    PDFPLUMBER_AVAILABLE = True
except ImportError:
    PDFPLUMBER_AVAILABLE = False

# Configuration
PROJECT_ROOT = Path("/home/romulo/visual/ecf/ecf-docs")
EXPORT_DIR = PROJECT_ROOT / "export"  # Per workflow: ./export/ not ./exports/

# PDF source directories
PDF_SOURCES = [
    PROJECT_ROOT / "Formatos XML",
    PROJECT_ROOT / "Informe y Descripción Técnica",
    PROJECT_ROOT / "Instructivos sobre Facturación Electrónica",
    PROJECT_ROOT / "Documentaciones Proceso de Certificación FE",
]

# Spanish diacritic transliteration table
TRANSLITERATION = str.maketrans({
    'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u', 'ñ': 'n',
    'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U', 'Ñ': 'N',
    'ü': 'u', 'Ü': 'U',
})


def compute_sha256(filepath: Path) -> str:
    """Compute SHA256 hash of a file."""
    sha256_hash = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            sha256_hash.update(chunk)
    return sha256_hash.hexdigest()


def sanitize_stem100(name: str) -> str:
    """
    Sanitize filename to stem100 format per workflow rules.
    
    - Take first 100 chars
    - Preserve ASCII letters/digits plus ._-
    - Convert spaces to -
    - Transliterate Spanish diacritics
    - Replace remaining unsupported chars with -
    - Collapse repeated -
    - Trim leading/trailing - or _
    - Keep original case
    """
    # Remove .pdf extension if present
    if name.lower().endswith('.pdf'):
        name = name[:-4]
    
    # Truncate to 100 characters
    name = name[:100]
    
    # Transliterate Spanish diacritics
    name = name.translate(TRANSLITERATION)
    
    # Convert spaces to dashes
    name = name.replace(' ', '-')
    
    # Keep only ASCII letters, digits, ., _, -
    result = []
    for char in name:
        if char.isascii() and (char.isalnum() or char in '._-'):
            result.append(char)
        else:
            result.append('-')
    name = ''.join(result)
    
    # Collapse repeated dashes
    while '--' in name:
        name = name.replace('--', '-')
    
    # Trim leading/trailing - or _
    name = name.strip('-_')
    
    return name


def get_canonical_folder(pdf_path: Path) -> tuple[str, str]:
    """
    Generate canonical folder name <stem100>_<sha6>.
    Returns (folder_name, full_sha256).
    """
    stem100 = sanitize_stem100(pdf_path.stem)
    sha256 = compute_sha256(pdf_path)
    sha6 = sha256[:6]
    return f"{stem100}_{sha6}", sha256


def find_all_pdfs() -> list[dict]:
    """Find all source PDFs and compute their canonical names."""
    pdfs = []
    for source_dir in PDF_SOURCES:
        if source_dir.exists():
            for pdf_path in sorted(source_dir.glob("*.pdf")):
                folder_name, sha256 = get_canonical_folder(pdf_path)
                pdfs.append({
                    "source_path": pdf_path,
                    "folder_name": folder_name,
                    "sha256": sha256,
                    "original_name": pdf_path.name,
                })
    return pdfs


def run_pdftotext(pdf_path: Path, output_dir: Path) -> dict:
    """Extract text using pdftotext with layout and raw modes."""
    results = {"layout": "skipped", "raw": "skipped"}
    
    # Layout mode
    layout_file = output_dir / "pdf_layout.txt"
    try:
        result = subprocess.run(
            ["pdftotext", "-enc", "UTF-8", "-layout", str(pdf_path), str(layout_file)],
            capture_output=True, text=True, timeout=120
        )
        results["layout"] = "✓" if result.returncode == 0 else f"✗ {result.stderr}"
    except Exception as e:
        results["layout"] = f"✗ {e}"
    
    # Raw mode
    raw_file = output_dir / "pdf_raw.txt"
    try:
        result = subprocess.run(
            ["pdftotext", "-enc", "UTF-8", "-raw", str(pdf_path), str(raw_file)],
            capture_output=True, text=True, timeout=120
        )
        results["raw"] = "✓" if result.returncode == 0 else f"✗ {result.stderr}"
    except Exception as e:
        results["raw"] = f"✗ {e}"
    
    return results


def extract_with_camelot(pdf_path: Path, output_dir: Path) -> dict:
    """Extract tables using camelot with lattice and stream modes."""
    if not CAMELOT_AVAILABLE:
        return {"lattice": "skipped (not installed)", "stream": "skipped (not installed)"}
    
    results = {"lattice": "", "stream": ""}
    lattice_dir = output_dir / "camelot" / "lattice"
    stream_dir = output_dir / "camelot" / "stream"
    lattice_dir.mkdir(parents=True, exist_ok=True)
    stream_dir.mkdir(parents=True, exist_ok=True)
    
    lattice_tables = []
    stream_tables = []
    
    # Lattice mode (tables with clear border lines)
    try:
        tables = camelot.read_pdf(str(pdf_path), pages='all', flavor='lattice')
        for i, table in enumerate(tables):
            csv_file = lattice_dir / f"table_{i+1:03d}_p{table.page}.csv"
            table.to_csv(str(csv_file))
            lattice_tables.append({
                "table_num": i + 1,
                "page": table.page,
                "shape": table.shape,
                "accuracy": getattr(table, 'accuracy', 'N/A')
            })
        results["lattice"] = f"✓ {len(tables)} tables"
    except Exception as e:
        results["lattice"] = f"✗ {str(e)[:50]}"
    
    # Stream mode (tables without clear border lines)
    try:
        tables = camelot.read_pdf(str(pdf_path), pages='all', flavor='stream')
        for i, table in enumerate(tables):
            csv_file = stream_dir / f"table_{i+1:03d}_p{table.page}.csv"
            table.to_csv(str(csv_file))
            stream_tables.append({
                "table_num": i + 1,
                "page": table.page,
                "shape": table.shape,
                "accuracy": getattr(table, 'accuracy', 'N/A')
            })
        results["stream"] = f"✓ {len(tables)} tables"
    except Exception as e:
        results["stream"] = f"✗ {str(e)[:50]}"
    
    # Write summary.md
    summary_file = output_dir / "camelot" / "summary.md"
    summary_lines = [
        "# Camelot Extraction Summary",
        "",
        f"**Extracted:** {datetime.now().isoformat()}",
        "",
        "## Lattice Mode (tables with ruling lines)",
        "",
        f"Found {len(lattice_tables)} tables",
        "",
    ]
    if lattice_tables:
        summary_lines.extend([
            "| Table | Page | Shape | Accuracy |",
            "|-------|------|-------|----------|",
        ])
        for t in lattice_tables:
            summary_lines.append(f"| {t['table_num']} | {t['page']} | {t['shape']} | {t['accuracy']} |")
    
    summary_lines.extend([
        "",
        "## Stream Mode (tables without ruling lines)",
        "",
        f"Found {len(stream_tables)} tables",
        "",
    ])
    if stream_tables:
        summary_lines.extend([
            "| Table | Page | Shape | Accuracy |",
            "|-------|------|-------|----------|",
        ])
        for t in stream_tables:
            summary_lines.append(f"| {t['table_num']} | {t['page']} | {t['shape']} | {t['accuracy']} |")
    
    summary_file.write_text("\n".join(summary_lines))
    
    return results


def extract_with_pdfplumber(pdf_path: Path, output_dir: Path) -> dict:
    """Extract tables and text using pdfplumber."""
    if not PDFPLUMBER_AVAILABLE:
        return {"status": "skipped (not installed)"}
    
    tables_dir = output_dir / "pdfplumber" / "tables"
    tables_dir.mkdir(parents=True, exist_ok=True)
    
    results = {"status": "", "pages": 0, "tables": 0}
    all_tables = []
    page_info = []
    
    try:
        with pdfplumber.open(pdf_path) as pdf:
            results["pages"] = len(pdf.pages)
            
            for page_num, page in enumerate(pdf.pages, 1):
                page_tables = page.extract_tables()
                page_info.append({
                    "page": page_num,
                    "tables_found": len(page_tables) if page_tables else 0,
                    "width": page.width,
                    "height": page.height,
                })
                
                if page_tables:
                    for table_idx, table in enumerate(page_tables):
                        if table:
                            results["tables"] += 1
                            csv_file = tables_dir / f"table_{results['tables']:03d}_p{page_num}.csv"
                            
                            with open(csv_file, 'w', newline='', encoding='utf-8') as f:
                                writer = csv.writer(f)
                                for row in table:
                                    writer.writerow(row)
                            
                            all_tables.append({
                                "table_num": results["tables"],
                                "page": page_num,
                                "rows": len(table),
                                "cols": len(table[0]) if table else 0,
                            })
        
        results["status"] = f"✓ {results['pages']} pages, {results['tables']} tables"
        
    except Exception as e:
        results["status"] = f"✗ {str(e)[:50]}"
        return results
    
    # Write summary.md
    summary_file = output_dir / "pdfplumber" / "summary.md"
    summary_lines = [
        "# pdfplumber Extraction Summary",
        "",
        f"**Extracted:** {datetime.now().isoformat()}",
        f"**Total Pages:** {results['pages']}",
        f"**Total Tables:** {results['tables']}",
        "",
        "## Page-by-Page Summary",
        "",
        "| Page | Tables Found | Dimensions |",
        "|------|--------------|------------|",
    ]
    for p in page_info:
        summary_lines.append(f"| {p['page']} | {p['tables_found']} | {p['width']:.0f} x {p['height']:.0f} |")
    
    if all_tables:
        summary_lines.extend([
            "",
            "## Tables Extracted",
            "",
            "| Table | Page | Rows | Cols |",
            "|-------|------|------|------|",
        ])
        for t in all_tables:
            summary_lines.append(f"| {t['table_num']} | {t['page']} | {t['rows']} | {t['cols']} |")
    
    summary_file.write_text("\n".join(summary_lines))
    
    return results


def create_notes(output_dir: Path, pdf_name: str, pdftotext_results: dict, 
                 camelot_results: dict, pdfplumber_results: dict) -> None:
    """Create notes.md with extraction summary and anomalies."""
    notes_file = output_dir / "notes.md"
    
    content = f"""# Extraction Notes: {pdf_name}

**Extracted:** {datetime.now().isoformat()}

## Extraction Summary

### pdftotext (reference snapshots)
- Layout mode: {pdftotext_results.get('layout', 'N/A')}
- Raw mode: {pdftotext_results.get('raw', 'N/A')}

### Camelot (primary table extraction)
- Lattice mode: {camelot_results.get('lattice', 'N/A')}
- Stream mode: {camelot_results.get('stream', 'N/A')}

### pdfplumber (verification)
- Status: {pdfplumber_results.get('status', 'N/A')}

## Cross-Reference Notes

Compare Camelot and pdfplumber outputs for accuracy:
- Check row/column counts match
- Verify no missing columns or merged cells
- Use pdf_layout.txt as visual truth reference

## Anomalies Detected

(none detected automatically - manual review recommended)

## Discrepancies

(document any tool disagreements here)
"""
    notes_file.write_text(content)


def update_index(pdfs: list[dict], extraction_log: list[dict]) -> None:
    """Update or create the index.md ledger."""
    index_file = EXPORT_DIR / "index.md"
    
    lines = [
        "# PDF Export Index (Ledger)",
        "",
        f"**Last updated:** {datetime.now().isoformat()}",
        "",
        "## Extraction Log",
        "",
        "| PDF Filename | Fingerprint (SHA256) | Export Folder | Date | Tools |",
        "|--------------|----------------------|---------------|------|-------|",
    ]
    
    for entry in extraction_log:
        sha_short = entry['sha256'][:16] + "..."
        lines.append(
            f"| {entry['original_name'][:40]}... | `{sha_short}` | "
            f"`{entry['folder_name']}/` | {entry['timestamp']} | {entry['tools']} |"
        )
    
    lines.extend([
        "",
        "## Folder Structure Convention",
        "",
        "Each folder follows: `<stem100>_<sha6>/`",
        "",
        "Contents per folder:",
        "- `source.pdf` - symlink to original PDF",
        "- `fingerprint.txt` - full SHA256",
        "- `pdf_layout.txt` - pdftotext -layout output",
        "- `pdf_raw.txt` - pdftotext -raw output",
        "- `camelot/lattice/` - Camelot lattice tables (CSV)",
        "- `camelot/stream/` - Camelot stream tables (CSV)",
        "- `camelot/summary.md` - Camelot extraction summary",
        "- `pdfplumber/tables/` - pdfplumber tables (CSV)",
        "- `pdfplumber/summary.md` - pdfplumber extraction summary",
        "- `notes.md` - anomalies and cross-reference notes",
        "",
    ])
    
    index_file.write_text("\n".join(lines))
    print(f"\n📋 Updated: {index_file}")


def process_pdf(pdf_info: dict) -> dict:
    """Process a single PDF following the workflow."""
    pdf_path = pdf_info["source_path"]
    folder_name = pdf_info["folder_name"]
    sha256 = pdf_info["sha256"]
    
    output_dir = EXPORT_DIR / folder_name
    
    # Check if already extracted (cache reuse per workflow)
    if output_dir.exists() and (output_dir / "fingerprint.txt").exists():
        existing_fp = (output_dir / "fingerprint.txt").read_text().strip()
        if existing_fp == sha256:
            print(f"  ⏭️  Already extracted (cache hit)")
            return {
                "original_name": pdf_info["original_name"],
                "folder_name": folder_name,
                "sha256": sha256,
                "timestamp": "cached",
                "tools": "cached",
            }
    
    # Create output directory
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Create source.pdf symlink
    source_link = output_dir / "source.pdf"
    if source_link.exists():
        source_link.unlink()
    source_link.symlink_to(pdf_path)
    
    # Write fingerprint.txt
    (output_dir / "fingerprint.txt").write_text(sha256)
    
    # 1) pdftotext snapshots (reference only)
    print(f"  📄 pdftotext extraction...")
    pdftotext_results = run_pdftotext(pdf_path, output_dir)
    print(f"     Layout: {pdftotext_results['layout']}")
    print(f"     Raw: {pdftotext_results['raw']}")
    
    # 2) Camelot (tables are the point)
    print(f"  📊 Camelot extraction...")
    camelot_results = extract_with_camelot(pdf_path, output_dir)
    print(f"     Lattice: {camelot_results['lattice']}")
    print(f"     Stream: {camelot_results['stream']}")
    
    # 3) pdfplumber (verification + edge cases)
    print(f"  🔍 pdfplumber extraction...")
    pdfplumber_results = extract_with_pdfplumber(pdf_path, output_dir)
    print(f"     {pdfplumber_results['status']}")
    
    # Create notes.md
    create_notes(output_dir, pdf_info["original_name"], 
                 pdftotext_results, camelot_results, pdfplumber_results)
    
    tools_used = "pdftotext"
    if CAMELOT_AVAILABLE:
        tools_used += ", camelot"
    if PDFPLUMBER_AVAILABLE:
        tools_used += ", pdfplumber"
    
    return {
        "original_name": pdf_info["original_name"],
        "folder_name": folder_name,
        "sha256": sha256,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "tools": tools_used,
    }


def main():
    print("=" * 70)
    print("PDF EXTRACTION TOOL")
    print("Following: .agent/rules/pdf-extraction-stack.md")
    print("=" * 70)
    print()
    print(f"📁 Export directory: {EXPORT_DIR}")
    print(f"🐍 Camelot available: {CAMELOT_AVAILABLE}")
    print(f"🐍 pdfplumber available: {PDFPLUMBER_AVAILABLE}")
    print()
    
    # Ensure export directory exists
    EXPORT_DIR.mkdir(parents=True, exist_ok=True)
    
    # Find all PDFs
    print("🔍 Discovering PDFs...")
    pdfs = find_all_pdfs()
    print(f"   Found {len(pdfs)} PDFs\n")
    
    # Process each PDF
    extraction_log = []
    for i, pdf_info in enumerate(pdfs, 1):
        print(f"\n[{i}/{len(pdfs)}] {pdf_info['original_name']}")
        print(f"  → {pdf_info['folder_name']}/")
        print("-" * 60)
        
        result = process_pdf(pdf_info)
        extraction_log.append(result)
    
    # Update index.md
    update_index(pdfs, extraction_log)
    
    print("\n" + "=" * 70)
    print(f"✅ EXTRACTION COMPLETE: {len(pdfs)} PDFs processed")
    print("=" * 70)


if __name__ == "__main__":
    main()
