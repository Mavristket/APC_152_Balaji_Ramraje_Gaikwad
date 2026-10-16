"""
Program 24:
Validate product codes following the pattern ABC-1234-XY,
where letters and digits must appear in the specified positions:
- Exactly 3 uppercase letters
- Followed by a hyphen '-'
- Followed by exactly 4 digits
- Followed by a hyphen '-'
- Followed by exactly 2 uppercase letters
"""

import re

def validate_product_code(code):
    """
    Validates product code format: ^[A-Z]{3}-\d{4}-[A-Z]{2}$
    """
    pattern = r"^[A-Z]{3}-\d{4}-[A-Z]{2}$"
    return bool(re.match(pattern, code.strip()))

# Input with fallback
try:
    user_code = input("Enter product code (e.g. ABC-1234-XY): ").strip()
    if not user_code:
        user_code = "PRD-2026-IN"
except (EOFError, KeyboardInterrupt):
    user_code = "PRD-2026-IN"

print(f"Product Code to Validate: \"{user_code}\"")
print("Result:", "VALID PRODUCT CODE" if validate_product_code(user_code) else "INVALID PRODUCT CODE")
print("-" * 60)

# Test cases
test_codes = [
    ("ABC-1234-XY", True,  "Matches exact pattern"),
    ("PRD-2026-IN", True,  "Valid 3 letters, 4 digits, 2 letters"),
    ("abc-1234-xy", False, "Lowercase letters not allowed"),
    ("AB-1234-XYZ", False, "2 letters in first part, 3 in last part"),
    ("ABCD-1234-XY", False, "4 letters in first part"),
    ("ABC-123-XY",  False, "Only 3 digits in middle part"),
    ("ABC_1234_XY", False, "Underscores instead of hyphens"),
    ("ABC-12A4-XY", False, "Letter inside digit section")
]

print("Test Suite Verification:")
for code, expected, note in test_codes:
    result = validate_product_code(code)
    status = "PASS" if result == expected else "FAIL"
    verdict = "VALID" if result else "INVALID"
    print(f"  {code:<16} -> {verdict:<8} [{status}] ({note})")
