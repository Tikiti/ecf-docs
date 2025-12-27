#!/usr/bin/env python3
"""
Helper script to extract and build sections from camelot CSV tables
for the ecf-format-v1.0-original.md document
"""

import csv
import os
import json
from pathlib import Path

# Base directory
BASE_DIR = Path("/home/romulo/visual/ecf/ecf-docs")
EXPORT_DIR = BASE_DIR / "exports/Formato-Comprobante-Fiscal-Electronico-e-CF-V1.0_c811c9"
CAMELOT_DIR = EXPORT_DIR / "camelot/lattice"

def read_csv_table(table_num):
    """Read a specific camelot table CSV file"""
    # Find the file matching the table number
    files = list(CAMELOT_DIR.glob(f"table_{table_num:03d}_p*.csv"))
    if not files:
        return None
    
    with open(files[0], 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)
    return rows

def extract_field_from_table(rows, field_num):
    """Extract a single field row from table data"""
    if not rows:
        return None
    
    # Find row starting with field_num
    for i, row in enumerate(rows):
        if row and str(row[0]).strip() == str(field_num):
            return row
    return None

# List all available tables
def list_tables():
    """List all camelot table files"""
    tables = sorted(CAMELOT_DIR.glob("table_*.csv"))
    for t in tables:
        print(f"{t.name} - {t.stat().st_size} bytes")

def get_table_range(start_page, end_page):
    """Get all tables within a page range"""
    tables = []
    for p in range(start_page, end_page + 1):
        files = list(CAMELOT_DIR.glob(f"table_*_p{p}.csv"))
        if files:
            tables.extend(files)
    return sorted(tables)

if __name__ == "__main__":
    # Quick test
    print("Camelot tables available:")
    tables = sorted(CAMELOT_DIR.glob("table_*.csv"))
    print(f"Total: {len(tables)} tables")
    
    # Show first few
    for t in tables[:5]:
        print(f"  {t.name}")
    
    print(f"\n... and {len(tables) - 5} more")
    
    # Show page range
    pages = set()
    for t in tables:
        # Extract page number from filename like table_001_p3.csv
        parts = t.stem.split('_p')
        if len(parts) == 2:
            pages.add(int(parts[1]))
    
    print(f"\nPages covered: {min(pages)} to {max(pages)}")
