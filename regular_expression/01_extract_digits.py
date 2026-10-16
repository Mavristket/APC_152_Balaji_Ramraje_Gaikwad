"""
Program 1:
Write a Python program using regular expressions to extract all digits from a given string.
"""

import re

# Given input string
sample_text = "Order #9842 was placed on 15th October 2026 with 3 items costing 450 rupees each, total 1350."
print("Input String:\n", sample_text)
print("-" * 55)

# 1. Extract individual digits: \d matches any single digit (0-9)
individual_digits = re.findall(r"\d", sample_text)
print("Individual Digits:", individual_digits)

# 2. Extract complete numeric sequences: \d+ matches one or more consecutive digits
numbers = re.findall(r"\d+", sample_text)
print("Extracted Numbers (sequences of digits):", numbers)
