#!/usr/bin/env python3
"""Recalculate an .xlsx file with LibreOffice and list every formula error.

Usage: python3 recalc_check.py model.xlsx

Recalculates a temporary copy (the original file is not changed), then prints
the formula count and each formula cell that shows an Excel error.
Exit code 0 = no errors, 1 = errors found, 2 = could not run.
"""
import os
import shutil
import subprocess
import sys
import tempfile

ERRORS = ("#REF!", "#DIV/0!", "#NAME?", "#VALUE!", "#N/A", "#NUM!", "#NULL!")


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    path = os.path.abspath(sys.argv[1])
    if not os.path.isfile(path):
        print(f"File not found: {path}")
        return 2
    soffice = shutil.which("soffice") or shutil.which("libreoffice")
    if not soffice:
        print("LibreOffice (soffice) not found: formulas were NOT recalculated or checked.")
        return 2
    try:
        import openpyxl
    except ImportError:
        print("openpyxl is missing: run  pip install openpyxl")
        return 2

    with tempfile.TemporaryDirectory() as out, tempfile.TemporaryDirectory() as profile:
        cmd = [soffice, f"-env:UserInstallation=file://{profile}", "--headless",
               "--calc", "--convert-to", "xlsx", "--outdir", out, path]
        subprocess.run(cmd, check=False, capture_output=True, timeout=180)
        result = os.path.join(out, os.path.basename(path))
        if not os.path.isfile(result):
            print("LibreOffice could not recalculate the file.")
            return 2
        values = openpyxl.load_workbook(result, data_only=True)

    formulas = openpyxl.load_workbook(path)
    count, bad = 0, []
    for ws in formulas.worksheets:
        vws = values[ws.title]
        for row in ws.iter_rows():
            for cell in row:
                if isinstance(cell.value, str) and cell.value.startswith("="):
                    count += 1
                    v = vws[cell.coordinate].value
                    if isinstance(v, str) and v.strip() in ERRORS:
                        bad.append(f"{ws.title}!{cell.coordinate}: {v} ({cell.value})")
    print(f"Formulas: {count}")
    print(f"Errors: {len(bad)}")
    for line in bad:
        print("  " + line)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
