#!/usr/bin/env python3
"""
Extract complete reference table data from camelot CSV files.
"""

import csv
from pathlib import Path

CAMELOT_DIR = Path("exports/Formato-Comprobante-Fiscal-Electronico-e-CF-V1.0_c811c9/camelot/lattice")

def extract_provinces_municipalities():
    """Extract all province and municipality codes from tables 069-081."""
    data = []
    
    for page in range(73, 86):  # pages 73-85
        csv_files = list(CAMELOT_DIR.glob(f"table_*_p{page}.csv"))
        
        for csv_file in csv_files:
            try:
                with open(csv_file, 'r', encoding='utf-8') as f:
                    reader = csv.reader(f)
                    rows = list(reader)
                    
                    for row in rows[1:]:  # Skip header
                        if len(row) >= 3:
                            prov_code = row[0].strip()
                            mun_code = row[1].strip()
                            description = row[2].strip()
                            
                            if prov_code and description:
                                # Format: province code, municipality code, description
                                full_code = f"{prov_code}-{mun_code}" if mun_code else prov_code
                                data.append((full_code, description))
            except Exception as e:
                pass
    
    return data

def extract_units_of_measure():
    """Extract unit of measure codes from tables 082-083."""
    data = []
    
    for page in [86, 87]:  # pages 86-87
        csv_files = list(CAMELOT_DIR.glob(f"table_*_p{page}.csv"))
        
        for csv_file in csv_files:
            try:
                with open(csv_file, 'r', encoding='utf-8') as f:
                    reader = csv.reader(f)
                    rows = list(reader)
                    
                    for row in rows[1:]:  # Skip header
                        if len(row) >= 3:
                            code = row[0].strip()
                            abbrev = row[1].strip()
                            measure = row[2].strip()
                            
                            if code and measure:
                                data.append((code, abbrev, measure))
            except Exception as e:
                pass
    
    return data

def format_provinces_markdown(data):
    """Format province/municipality data as markdown table."""
    md = "| Código | Provincia/Municipio |\n"
    md += "|--------|---------------------|\n"
    
    for code, description in data:
        # Bold province names (those without dashes or with -00)
        if '-' not in code or code.endswith('-00'):
            description = f"**{description}**"
        md += f"| {code} | {description} |\n"
    
    return md

def format_units_markdown(data):
    """Format units of measure as markdown table."""
    md = "| Código | Abrev. | Unidad de Medida |\n"
    md += "|--------|--------|------------------|\n"
    
    for code, abbrev, measure in data:
        md += f"| {code.zfill(2)} | {abbrev} | {measure} |\n"
    
    return md

def main():
    print("Extracting reference table data...")
    
    print("\n=== Provinces and Municipalities ===")
    prov_data = extract_provinces_municipalities()
    print(f"Found {len(prov_data)} entries")
    prov_md = format_provinces_markdown(prov_data)
    print("First 10 entries:")
    print('\n'.join(prov_md.split('\n')[:12]))
    
    with open('markdown/xml-formats/.tablas-provincias.md', 'w', encoding='utf-8') as f:
        f.write(prov_md)
    print(f"\nSaved to .tablas-provincias.md")
    
    print("\n=== Units of Measure ===")
    units_data = extract_units_of_measure()
    print(f"Found {len(units_data)} entries")
    units_md = format_units_markdown(units_data)
    print("First 10 entries:")
    print('\n'.join(units_md.split('\n')[:12]))
    
    with open('markdown/xml-formats/.tablas-unidades.md', 'w', encoding='utf-8') as f:
        f.write(units_md)
    print(f"\nSaved to .tablas-unidades.md")

if __name__ == "__main__":
    main()
