"""
Program 2:
Accept a sentence and display all words beginning with the letter A or a.
"""

import re

# Accept sentence from user (with fallback for automated runs)
try:
    sentence = input("Enter a sentence: ").strip()
    if not sentence:
        sentence = "An agile alligator ate an apple and an apricot in August."
except (EOFError, KeyboardInterrupt):
    sentence = "An agile alligator ate an apple and an apricot in August."

print(f"Sentence: \"{sentence}\"")
print("-" * 55)

# Pattern: \b denotes a word boundary, [aA] checks if the word starts with 'a' or 'A', \w* captures the rest of the word
words_starting_with_a = re.findall(r"\b[aA]\w*", sentence)

print(f"Words beginning with 'A' or 'a' (Count: {len(words_starting_with_a)}):")
print(words_starting_with_a)
