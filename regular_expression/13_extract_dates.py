"""
Program 13:
Write a program to extract dates in DD-MM-YYYY format from a given paragraph.
"""

import re

# Given paragraph containing various dates
paragraph = """
Important University Schedule:
The semester examinations will commence on 15-11-2026 and finish by 05-12-2026.
Fee payment deadline was 31-10-2026. Note that project submission is due on 20-01-2027.
Invalid formats such as 2026-11-15 or 15/11/2026 should not match this pattern.
"""

print("Input Paragraph:\n", paragraph.strip())
print("-" * 60)

# Pattern: \b(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(\d{4})\b
# Validates realistic 2-digit day (01-31), 2-digit month (01-12), and 4-digit year separated by hyphens
date_pattern = r"\b(?:0[1-9]|[12][0-9]|3[01])-(?:0[1-9]|1[0-2])-\d{4}\b"
extracted_dates = re.findall(date_pattern, paragraph)

print(f"Dates extracted in DD-MM-YYYY format (Count: {len(extracted_dates)}):")
for idx, d in enumerate(extracted_dates, start=1):
    print(f"  {idx}. {d}")
