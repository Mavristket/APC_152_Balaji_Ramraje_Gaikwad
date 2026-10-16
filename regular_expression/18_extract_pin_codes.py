"""
Program 18:
Write a program to extract six-digit Indian PIN codes from a paragraph.
"""

import re

# Given paragraph
text = """
Our regional headquarters are distributed across India:
- Mumbai Central Office: PIN 400001
- Bengaluru Tech Park Branch: PIN 560001
- New Delhi Administrative Hub: 110001
- Kolkata Regional Center: 700028
- Pune Sector 14: 411038
Please do not confuse PIN codes with 5-digit numbers like 12345 or 012345 (starts with 0, invalid),
or 7-digit IDs like 5600012.
"""

print("Input Paragraph:\n", text.strip())
print("-" * 60)

# Pattern: \b[1-9][0-9]{5}\b
# Valid Indian PIN code has exactly 6 digits, and the first digit cannot be 0 (1-9).
pin_pattern = r"\b[1-9]\d{5}\b"
extracted_pins = re.findall(pin_pattern, text)

print(f"Extracted 6-Digit Indian PIN Codes (Count: {len(extracted_pins)}):")
for idx, pin in enumerate(extracted_pins, start=1):
    print(f"  {idx}. {pin}")
