"""
Program 9:
Write a program to remove all special characters from a given string while
retaining letters, digits, and spaces.
"""

import re

# Given string with special characters
text = "Hello @World! Python #3 is amazing... (Cost: $500, Discount: 15% & Rating: 4.9*)."
print("Original String:")
print(text)
print("-" * 55)

# Pattern: [^a-zA-Z0-9\s] matches any character that is NOT a letter, digit, or whitespace
cleaned_text = re.sub(r"[^a-zA-Z0-9\s]", "", text)

print("Sanitized String (only letters, digits, and spaces retained):")
print(cleaned_text)
