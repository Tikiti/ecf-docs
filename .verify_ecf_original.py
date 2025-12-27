#!/usr/bin/env python3
"""
Fixed verification script to properly compare ecf-format-v1.0-original.md
against camelot PDF extractions.
"""

import csv
import re
from pathlib import Path
from collections import defaultdict

# Paths
CAMELOT_DIR = Path("exports/Formato-Comprobante-Fiscal-Electronico-e-CF-V1.0_c811c9/camelot/lattice")
MD_FILE = Path("markdown/xml-formats/ecf-format-v1.0-original.md")
ERROR_REPORT = Path("markdown/xml-formats/.verification-errors.md")

def extract_obligatoriedad_from_csv(csv_file):
    """Extract obligatoriedad codes from a CSV file."""
    obligatoriedad_data = []
    
    try:
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            rows = list(reader)
            
            if len(rows) < 3:
                return obligatoriedad_data
            
            # Look for OBLIGATORIEDAD header row
            for i, row in enumerate(rows):
                if any('OBLIGATORIEDAD' in str(cell) for cell in row):
                    header_row = i
                    
                    # Process data rows
                    for data_row in rows[header_row+1:]:
                        if len(data_row) > 0 and data_row[0].strip():
                            first_col = data_row[0].strip()
                            # Skip if first column is empty or contains markers
                            if not first_col or 'FIN' in first_col or 'ÁREA' in first_col:
                                continue
                            
                            # Only process rows where first column is a field number
                            if first_col.isdigit():
                                field_info = {
                                    'field_num': first_col,
                                    'field_name': data_row[1] if len(data_row) > 1 else '',
                                    'obligatoriedad': {
                                        '31': data_row[7].strip() if len(data_row) > 7 else '',
                                        '32': data_row[8].strip() if len(data_row) > 8 else '',
                                        '33': data_row[9].strip() if len(data_row) > 9 else '',
                                        '34': data_row[10].strip() if len(data_row) > 10 else '',
                                        '41': data_row[11].strip() if len(data_row) > 11 else '',
                                        '43': data_row[12].strip() if len(data_row) > 12 else '',
                                        '44': data_row[13].strip() if len(data_row) > 13 else '',
                                        '45': data_row[14].strip() if len(data_row) > 14 else '',
                                        '46': data_row[15].strip() if len(data_row) > 15 else '',
                                        '47': data_row[16].strip() if len(data_row) > 16 else '',
                                    },
                                    'source_file': csv_file.name
                                }
                                obligatoriedad_data.append(field_info)
                    break
                    
    except Exception as e:
        pass
    
    return obligatoriedad_data

def extract_obligatoriedad_from_markdown():
    """Extract obligatoriedad codes from markdown tables - FIXED VERSION."""
    md_content = read_markdown_file()
    md_fields = {}
    
    # Split into lines for better parsing
    lines = md_content.split('\n')
    
    in_table = False
    for line in lines:
        # Check if this is a table row with obligatoriedad codes
        # Format: | field_number | field_name | ... | 31 | 32 | 33 | 34 | 41 | 43 | 44 | 45 | 46 | 47 |
        if line.strip().startswith('|') and line.count('|') >= 13:
            cols = [c.strip() for c in line.split('|')]
            
            # First column should be field number (digit)
            if len(cols) > 0 and cols[1].strip().isdigit():
                field_num = cols[1].strip()
                
                # Last 10 columns should be obligatoriedad codes
                # They should be at indices -11 to -2 (excluding first and last empty strings from split)
                if len(cols) >= 13:
                    # Get the last 10 values before the final empty string
                    obl_values = cols[-11:-1]
                    
                    # Clean up: remove markdown formatting, footnote markers, etc.
                    clean_obl = []
                    for val in obl_values:
                        # Remove footnote markers like ¹⁴, ²¹, etc
                        cleaned = re.sub(r'[¹²³⁴⁵⁶⁷⁸⁹⁰]+', '', val)
                        # Remove **bold** markers
                        cleaned = re.sub(r'\*\*', '', cleaned)
                        cleaned = cleaned.strip()
                        clean_obl.append(cleaned)
                    
                    if len(clean_obl) == 10:
                        md_fields[field_num] = {
                            '31': clean_obl[0],
                            '32': clean_obl[1],
                            '33': clean_obl[2],
                            '34': clean_obl[3],
                            '41': clean_obl[4],
                            '43': clean_obl[5],
                            '44': clean_obl[6],
                            '45': clean_obl[7],
                            '46': clean_obl[8],
                            '47': clean_obl[9],
                        }
    
    return md_fields

def read_markdown_file():
    """Read the markdown file and extract field information."""
    with open(MD_FILE, 'r', encoding='utf-8') as f:
        return f.read()

def find_csv_files():
    """Find all camelot CSV files."""
    csv_files = sorted(CAMELOT_DIR.glob("table_*.csv"))
    return csv_files

def extract_all_obligatoriedad():
    """Extract all obligatoriedad codes from all CSV files."""
    all_data = defaultdict(dict)
    csv_files = find_csv_files()
    
    for csv_file in csv_files:
        data = extract_obligatoriedad_from_csv(csv_file)
        for field in data:
            field_num = field['field_num']
            # Keep the last occurrence (later pages override earlier ones)
            all_data[field_num] = field
    
    print(f"Extracted {len(all_data)} unique fields from CSVs")
    return all_data

def compare_obligatoriedad(csv_data, md_data):
    """Compare obligatoriedad codes and report discrepancies."""
    errors = []
    warnings = []
    
    # Check for fields in CSV but not in MD
    for field_num in csv_data:
        if field_num not in md_data:
            warnings.append(f"Field {field_num} found in CSV but not in markdown (from {csv_data[field_num]['source_file']})")
    
    # Check for fields in MD but not in CSV
    for field_num in md_data:
        if field_num not in csv_data:
            warnings.append(f"Field {field_num} found in markdown but not in CSV files")
    
    # Compare matching fields
    for field_num in csv_data:
        if field_num not in md_data:
            continue
        
        csv_obl = csv_data[field_num]['obligatoriedad']
        md_obl = md_data[field_num]
        
        for etype in ['31', '32', '33', '34', '41', '43', '44', '45', '46', '47']:
            csv_val = csv_obl[etype]
            md_val = md_obl[etype]
            
            # Only report if CSV has a value and it differs from MD
            if csv_val and csv_val != md_val:
                field_name = csv_data[field_num]['field_name']
                errors.append({
                    'field_num': field_num,
                    'field_name': field_name,
                    'etype': etype,
                    'csv_val': csv_val,
                    'md_val': md_val,
                    'source': csv_data[field_num]['source_file']
                })
    
    return errors, warnings

def generate_error_report(errors, warnings):
    """Generate a detailed error report."""
    from datetime import datetime
    
    report = f"""# Verification Errors Report - FIXED VERSION

Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Summary
- **Total obligatoriedad mismatches: {len(errors)}**
- **Total warnings: {len(warnings)}**

## Critical Errors (Obligatoriedad Mismatches)

These are cases where the CSV has a value that differs from the markdown.

"""
    
    # Group errors by field
    by_field = defaultdict(list)
    for error in errors:
        by_field[error['field_num']].append(error)
    
    for field_num in sorted(by_field.keys(), key=int):
        field_errors = by_field[field_num]
        report += f"\n### Field {field_num}: {field_errors[0]['field_name']}\n"
        report += f"Source: {field_errors[0]['source']}\n\n"
        report += "| e-CF Type | CSV Value | MD Value |\n"
        report += "|-----------|-----------|----------|\n"
        for err in field_errors:
            report += f"| {err['etype']} | {err['csv_val']} | {err['md_val']} |\n"
        report += "\n"
    
    if warnings:
        report += "\n## Warnings (Fields Missing in One Source)\n\n"
        for warning in warnings[:20]:  # Limit to first 20
            report += f"- {warning}\n"
        if len(warnings) > 20:
            report += f"\n... and {len(warnings) - 20} more warnings\n"
    
    report += "\n## Next Steps\n\n"
    report += "1. Review and fix critical errors (obligatoriedad mismatches)\n"
    report += "2. Investigate warnings for missing fields\n"
    report += "3. Re-run verification\n"
    report += "4. Remove session markers and add PDF footer\n"
    
    return report

def main():
    print("=" * 80)
    print("ECF Format V1.0 Original - FIXED Verification Script")
    print("=" * 80)
    print()
    
    print("Step 1: Extracting obligatoriedad from CSV files...")
    csv_obligatoriedad = extract_all_obligatoriedad()
    print()
    
    print("Step 2: Extracting obligatoriedad from markdown...")
    md_obligatoriedad = extract_obligatoriedad_from_markdown()
    print(f"  Extracted {len(md_obligatoriedad)} fields from markdown")
    print()
    
    print("Step 3: Comparing data...")
    errors, warnings = compare_obligatoriedad(csv_obligatoriedad, md_obligatoriedad)
    print(f"  Found {len(errors)} obligatoriedad mismatches")
    print(f"  Found {len(warnings)} warnings")
    print()
    
    if errors or warnings:
        print("Step 4: Generating error report...")
        report = generate_error_report(errors, warnings)
        
        with open(ERROR_REPORT, 'w', encoding='utf-8') as f:
            f.write(report)
        
        print(f"  Report saved to: {ERROR_REPORT}")
        print()
        
        if errors:
            print("ERRORS FOUND - Top 10 mismatches:")
            for error in errors[:10]:
                print(f"  Field {error['field_num']} type {error['etype']}: "
                      f"CSV='{error['csv_val']}' vs MD='{error['md_val']}'")
        else:
            print("No obligatoriedad mismatches found!")
    else:
        print("SUCCESS - No errors found!")
    
    print()
    print("=" * 80)
    
    return len(errors)

if __name__ == "__main__":
    error_count = main()
    exit(0 if error_count == 0 else 1)
