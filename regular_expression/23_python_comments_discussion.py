"""
Program 23:
Write a program to identify single-line comments in Python source code.
Discuss why regular expressions alone may not correctly handle every string literal or multiline case.
"""

import re

# Sample Python source code containing comments and tricky edge cases
python_code = '''
# Top-level module comment: Math operations
import math

def calculate_circle_area(radius):
    # Calculate area using pi * r^2
    area = math.pi * (radius ** 2)
    url = "https://example.com/api#section"  # Tricky: string contains #, followed by inline comment
    hex_color = "#FF5733"                    # Hex code string with '#' inside quotes
    return area

"""
Multiline docstring / comment
# This hash inside triple quotes is NOT a comment!
"""
'''

print("Sample Python Source Code:")
print(python_code)
print("=" * 65)

# A naive regular expression to find single-line comments:
# Pattern: r"#.*$" matches '#' up to the end of the line
comments = re.findall(r"#.*$", python_code, re.MULTILINE)

print("Identified Comments using Naive Regex (r'#.*$'):")
for idx, c in enumerate(comments, start=1):
    print(f"  {idx}. {c}")

print("=" * 65)
print("DISCUSSION: Why Regular Expressions Alone Fail for Python Comments:")
print("-" * 65)
discussion = """
1. String Literals Containing '#':
   - In Python, hash symbols inside single or double quotes represent string data,
     e.g., color = "#FF5733" or url = "http://site.com#ref".
   - A naive regex matches the '#' inside the string and mistakenly treats the rest
     of the line as a comment.

2. Triple-Quoted Strings (Docstrings / Multiline Literals):
   - Python uses triple quotes (''' or \"\"\") for multiline strings and docstrings.
   - Any '#' occurring inside a triple-quoted string is part of the string content,
     not a comment. Regular expressions lack the state-tracking to know if they are
     currently inside a multi-line string state.

3. Escaped Quotes:
   - Strings with escaped quotes like \"Hello \\\" # not comment\" further complicate
     regex boundary detection.

4. Correct Solution:
   - Instead of regular expressions alone, accurate source code analysis requires a
     true Lexer / Tokenizer. Python provides the built-in `tokenize` module or the
     `ast` (Abstract Syntax Tree) module, which maintain full parsing state and
     distinguish string tokens from COMMENT tokens accurately.
"""
print(discussion.strip())
