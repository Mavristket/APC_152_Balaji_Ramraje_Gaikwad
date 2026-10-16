"""
Program 10:
Write a program to count the number of words in a sentence using regular expressions.
"""

import re

# Given sentence
sentence = "Data science, artificial intelligence, and machine learning are revolutionizing modern industries."
print("Sentence:\n", sentence)
print("-" * 55)

# Pattern: \b[a-zA-Z0-9_]+\b or \b\w+\b matches alphanumeric word tokens
words = re.findall(r"\b[a-zA-Z0-9'-]+\b", sentence)

print(f"Total word count: {len(words)}")
print("List of words extracted:")
print(words)
