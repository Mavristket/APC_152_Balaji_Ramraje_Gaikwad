"""
Program 17:
Write a program to identify consecutive repeated words in a sentence, ignoring case differences.
"""

import re

# Given sentence with repeated words
sentence = "Paris in the the spring is is very Very beautiful and and peaceful."
print("Input Sentence:\n", sentence)
print("-" * 60)

# Pattern:
# \b(\w+) captures a word into group 1
# \s+ matches one or more whitespace characters
# \1 matches the exact same word as captured in group 1 (backreference)
# \b word boundary
# re.IGNORECASE ensures "Very very" or "The the" are matched
pattern = r"\b(\w+)\s+\1\b"

matches = list(re.finditer(pattern, sentence, re.IGNORECASE))

print(f"Consecutive repeated words found (Count: {len(matches)}):")
for idx, match in enumerate(matches, start=1):
    repeated_word = match.group(1)
    full_span_text = match.group(0)
    print(f"  {idx}. Word '{repeated_word}' repeated as \"{full_span_text}\" at index {match.start()}-{match.end()}")
