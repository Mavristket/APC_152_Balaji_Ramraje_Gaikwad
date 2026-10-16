"""
Program 11:
Write a program to validate a 10-digit Indian mobile number using a regular expression.
"""

import re

def validate_indian_mobile(number_str):
    """
    Validates a 10-digit Indian mobile number:
    - Starts with 6, 7, 8, or 9
    - Exactly 10 digits
    - Optionally prefixed with '+91 ' or '+91-' or '0'
    Pattern: ^(?:\+91[\-\s]?|0)?[6-9]\d{9}$
    """
    pattern = r"^(?:\+91[\-\s]?|0)?[6-9]\d{9}$"
    return bool(re.match(pattern, number_str.strip()))

# Test cases
test_numbers = [
    "9876543210",        # Valid 10 digits
    "+91 9123456789",    # Valid with +91
    "08765432109",       # Valid with leading 0
    "+91-7890123456",    # Valid with +91-
    "5123456789",        # Invalid: starts with 5
    "987654321",         # Invalid: only 9 digits
    "987654321012",      # Invalid: 12 digits
    "98765abcde"         # Invalid: contains letters
]

print("Validating Indian Mobile Numbers:")
print("-" * 55)
for num in test_numbers:
    is_valid = validate_indian_mobile(num)
    status = "VALID" if is_valid else "INVALID"
    print(f"{num:<18} -> {status}")
