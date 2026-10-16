"""
Program 25:
Given a paragraph containing student names, roll numbers, and marks,
extract each field using regular expressions.
"""

import re

# Paragraph containing student details in structured sentences
paragraph = """
Semester Evaluation Summary:
Student Roll No: 101, Name: Aarav Sharma, Marks: 88.
Student Roll No: 102, Name: Diya Patel, Marks: 92.
Student Roll No: 103, Name: Rohan Verma, Marks: 76.
Student Roll No: 104, Name: Ananya Iyer, Marks: 85.
Student Roll No: 105, Name: Vivaan Reddy, Marks: 94.
"""

print("Input Paragraph:\n", paragraph.strip())
print("=" * 65)

# Pattern with named capture groups:
# Roll No: (?P<roll>\d+)
# Name: (?P<name>[A-Za-z\s]+)
# Marks: (?P<marks>\d+)
pattern = r"Roll\s*No[:\s]+(?P<roll>\d+)[,\s]+Name[:\s]+(?P<name>[A-Za-z\s]+?)[,\s]+Marks[:\s]+(?P<marks>\d+)"

matches = list(re.finditer(pattern, paragraph))

print(f"Extracted Student Records (Count: {len(matches)}):")
print(f"{'Roll No':<10} {'Student Name':<20} {'Marks':<8}")
print("-" * 40)

extracted_data = []
for match in matches:
    roll = match.group("roll")
    name = match.group("name").strip()
    marks = match.group("marks")
    extracted_data.append({"Roll": roll, "Name": name, "Marks": marks})
    print(f"{roll:<10} {name:<20} {marks:<8}")

print("-" * 40)
print("Raw Extracted Dictionaries:")
print(extracted_data)
