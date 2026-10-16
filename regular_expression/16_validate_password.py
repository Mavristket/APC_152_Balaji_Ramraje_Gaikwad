"""
Program 16:
Write a program to check whether a password contains:
- At least eight characters
- One uppercase letter
- One lowercase letter
- One digit
- One special character
"""

import re

def validate_password(password):
    """
    Checks password strength using individual regex rules and overall lookahead regex.
    """
    reasons = []
    
    if len(password) < 8:
        reasons.append("Must be at least 8 characters long")
    if not re.search(r"[A-Z]", password):
        reasons.append("Missing at least one uppercase letter (A-Z)")
    if not re.search(r"[a-z]", password):
        reasons.append("Missing at least one lowercase letter (a-z)")
    if not re.search(r"\d", password):
        reasons.append("Missing at least one digit (0-9)")
    if not re.search(r"[@$!%*?&#^_\-~+=]", password):
        reasons.append("Missing at least one special character (@$!%*?&#^_-~+=)")

    is_valid = (len(reasons) == 0)
    return is_valid, reasons

# Interactive input with fallback
try:
    user_pass = input("Enter password to validate: ").strip()
    if not user_pass:
        user_pass = "P@ssw0rd2026"
except (EOFError, KeyboardInterrupt):
    user_pass = "P@ssw0rd2026"

valid, errors = validate_password(user_pass)
print(f"Testing Password: \"{user_pass}\"")
if valid:
    print("Result: STRONG & VALID PASSWORD!")
else:
    print("Result: INVALID PASSWORD")
    for err in errors:
        print(f"  - {err}")

print("-" * 60)
print("Testing Sample Passwords:")
sample_passwords = [
    "P@ssw0rd2026",      # Valid
    "weakpass",          # Too short, no upper, no digit, no special
    "AllLettersOnly!",   # No digit
    "12345678#Aa",       # Valid
    "NoSpecialChar123",  # No special char
    "lowercase123#"      # No uppercase
]

for p in sample_passwords:
    v, _ = validate_password(p)
    print(f"  {p:<20} -> {'VALID' if v else 'INVALID'}")
