"""
Program 19:
Write a program to check whether an input matches a common Indian vehicle registration
format, such as MH12AB1234.
"""

import re

def validate_vehicle_registration(reg_number):
    """
    Validates standard Indian vehicle registration numbers:
    - 2 letters: State code (e.g. MH, DL, KA, TN)
    - 2 digits: RTO district code (e.g. 12, 01)
    - 1 or 2 letters: Series characters (e.g. AB, C, ZZ)
    - 4 digits: Unique vehicle number (e.g. 1234, 0001)
    Optional spaces between segments are handled.
    Pattern: ^[A-Z]{2}\s?[0-9]{2}\s?[A-Z]{1,2}\s?[0-9]{4}$
    """
    pattern = r"^[A-Z]{2}\s?[0-9]{2}\s?[A-Z]{1,2}\s?[0-9]{4}$"
    return bool(re.match(pattern, reg_number.strip().upper()))

# Input with fallback
try:
    user_reg = input("Enter vehicle registration number (e.g. MH12AB1234): ").strip()
    if not user_reg:
        user_reg = "MH12AB1234"
except (EOFError, KeyboardInterrupt):
    user_reg = "MH12AB1234"

print(f"Vehicle Number to Check: \"{user_reg}\"")
print("Validation Result:", "VALID VEHICLE REGISTRATION NUMBER" if validate_vehicle_registration(user_reg) else "INVALID VEHICLE REGISTRATION NUMBER")
print("-" * 65)

# Test cases
test_cases = [
    "MH12AB1234",      # Valid standard
    "DL01A5678",       # Valid 1-letter series
    "KA 05 MN 9999",   # Valid with spaces
    "TN22CZ0007",      # Valid
    "12MHAB1234",      # Invalid state position
    "MH123AB1234",     # Invalid 3-digit RTO
    "MH12ABC1234",     # Invalid 3-letter series
    "MH12AB12"         # Invalid 2-digit vehicle number
]

print("Batch Verification:")
for num in test_cases:
    status = "VALID" if validate_vehicle_registration(num) else "INVALID"
    print(f"  {num:<16} -> {status}")
