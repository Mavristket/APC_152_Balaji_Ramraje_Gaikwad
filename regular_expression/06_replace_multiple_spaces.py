"""
Program 6:
Write a program to replace multiple consecutive spaces with a single space.
"""

import re

# Text containing multiple irregular spaces
original_text = "Python     is   an     interpreted,    high-level,   general-purpose   programming    language."
print("Original String:")
print(f"\"{original_text}\"")
print("-" * 65)

# Pattern: r" +" matches two or more consecutive spaces (or r"\s+" for any consecutive whitespace)
cleaned_text = re.sub(r" +", " ", original_text).strip()

print("Cleaned String (multiple spaces replaced with single space):")
print(f"\"{cleaned_text}\"")
