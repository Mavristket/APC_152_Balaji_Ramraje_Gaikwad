"""
Program 3:
Write a program to count the occurrences of vowels in a given string using regular expressions.
"""

import re

# Given input string
text = "Antigravity Artificial Intelligence and Machine Learning Engineering"
print("Input String:", text)
print("-" * 55)

# Pattern: [aeiou] with re.IGNORECASE flag matches any vowel
vowels = re.findall(r"[aeiou]", text, re.IGNORECASE)

print(f"Total number of vowels: {len(vowels)}")
print("Vowels found:", vowels)
print("-" * 55)

# Breakdown count for each individual vowel
print("Individual Vowel Frequencies:")
for v in "aeiou":
    count = len(re.findall(re.escape(v), text, re.IGNORECASE))
    print(f"  Vowel '{v}' / '{v.upper()}': {count}")
