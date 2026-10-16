"""
Program 5:
Write a program to identify all spaces, tabs, and newline characters in a text.
"""

import re

# Text containing standard spaces, tabs (\t), and newlines (\n)
text = "Line 1: Hello World.\nLine 2:\tItem A\tItem B\nLine 3: Goodbye  All!"

print("Raw Representation of Input Text:")
print(repr(text))
print("-" * 55)

# Patterns for specific whitespace characters
spaces = re.findall(r" ", text)
tabs = re.findall(r"\t", text)
newlines = re.findall(r"\n", text)
all_whitespace = re.findall(r"\s", text)

print(f"Number of spaces (' ')         : {len(spaces)}")
print(f"Number of tabs ('\\t')          : {len(tabs)}")
print(f"Number of newlines ('\\n')      : {len(newlines)}")
print(f"Total whitespace characters (\\s): {len(all_whitespace)}")
print("-" * 55)

# Find positions of all whitespace characters
print("Whitespace Positions in Text:")
for match in re.finditer(r"\s", text):
    char_name = "Space" if match.group() == " " else ("Tab" if match.group() == "\t" else "Newline")
    print(f"  Index {match.start():2d}: {char_name}")
