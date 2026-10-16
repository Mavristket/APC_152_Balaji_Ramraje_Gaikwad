"""
Program 7:
Accept a sentence and display all words containing exactly five characters.
"""

import re

# Accept input with fallback
try:
    sentence = input("Enter a sentence: ").strip()
    if not sentence:
        sentence = "Three green birds fly above their sweet home while great zebra watches."
except (EOFError, KeyboardInterrupt):
    sentence = "Three green birds fly above their sweet home while great zebra watches."

print(f"Sentence: \"{sentence}\"")
print("-" * 55)

# Pattern: \b[a-zA-Z]{5}\b matches any word consisting of exactly 5 letters
five_letter_words = re.findall(r"\b[a-zA-Z]{5}\b", sentence)

print(f"Words containing exactly 5 characters (Count: {len(five_letter_words)}):")
print(five_letter_words)
