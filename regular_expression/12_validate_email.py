"""
Program 12:
Accept an email address and check whether it follows a reasonable email format.
"""

import re

def is_valid_email(email_str):
    """
    Validates standard email format:
    - Username: alphanumeric and characters (._%+-)
    - @ symbol
    - Domain: alphanumeric with dots/hyphens
    - Top Level Domain (TLD): at least 2 alphabetic characters
    Pattern: ^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$
    """
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email_str.strip()))

# Accept input with fallback
try:
    user_email = input("Enter an email address: ").strip()
    if not user_email:
        user_email = "student.apc@college.edu.in"
except (EOFError, KeyboardInterrupt):
    user_email = "student.apc@college.edu.in"

print(f"Testing input: \"{user_email}\"")
print("Validation Result:", "VALID Email" if is_valid_email(user_email) else "INVALID Email")
print("-" * 55)

# Batch demonstration with multiple sample emails
samples = [
    "john.doe@example.com",
    "user_123@sub.domain.org",
    "invalid-email@",
    "missing_at_domain.com",
    "name@domain",
    "admin@company.co.in"
]
print("Batch Demonstration:")
for sample in samples:
    status = "VALID" if is_valid_email(sample) else "INVALID"
    print(f"  {sample:<28} -> {status}")
