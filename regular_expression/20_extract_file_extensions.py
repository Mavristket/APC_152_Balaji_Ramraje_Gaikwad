"""
Program 20:
Write a program to extract file extensions from filenames in a given string.
"""

import re

# String containing various filenames
text = """
The project directory contains multiple source and asset files:
main.py, data_analysis.ipynb, student_report.pdf, annual_budget.xlsx,
profile_pic.jpeg, style.min.css, bundle.js, archive.tar.gz, and README.md.
"""

print("Input Text:\n", text.strip())
print("-" * 60)

# Pattern: \b\w+\.([a-zA-Z0-9]+)\b matches the extension after the dot
# Group 1 captures the extension
extensions = re.findall(r"\b[\w-]+\.([a-zA-Z0-9]+)\b", text)

print(f"Extracted File Extensions (Count: {len(extensions)}):")
print(extensions)
print("-" * 60)

# Also extract filename along with its extension:
file_matches = re.findall(r"\b([\w-]+\.([a-zA-Z0-9]+))\b", text)
print("Filename and Extension Pairs:")
for full_file, ext in file_matches:
    print(f"  Filename: {full_file:<22} -> Extension: .{ext}")
