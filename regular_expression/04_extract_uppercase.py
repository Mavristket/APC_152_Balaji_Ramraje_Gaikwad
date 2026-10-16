"""
Program 4:
Write a program to extract all uppercase letters from a given string.
"""

import re

# Given string
text = "The Python Programming Language was created by Guido van Rossum in the Netherlands (NL)."
print("Input String:\n", text)
print("-" * 55)

# Pattern: [A-Z] matches any single uppercase ASCII letter
uppercase_letters = re.findall(r"[A-Z]", text)

print(f"Uppercase letters found (Count: {len(uppercase_letters)}):")
print(uppercase_letters)
print("Joined uppercase string:", "".join(uppercase_letters))
