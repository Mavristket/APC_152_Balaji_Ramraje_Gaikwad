"""
Program 8:
Write a program to identify all words ending with the letter s.
"""

import re

# Given sentence
text = "The curious cats and dogs chase squirrels across various streets and parks."
print("Input Text:\n", text)
print("-" * 55)

# Pattern: \b\w*[sS]\b matches words ending with 's' or 'S'
words_ending_with_s = re.findall(r"\b[a-zA-Z]+[sS]\b", text)

print(f"Words ending with the letter 's'/'S' (Count: {len(words_ending_with_s)}):")
print(words_ending_with_s)
