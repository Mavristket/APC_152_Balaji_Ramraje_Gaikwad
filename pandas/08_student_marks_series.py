"""
Program 8:
Create a Pandas Series using a dictionary where the student names are keys
and their marks are values.
Perform:
- Display the Series.
- Display marks of a particular student.
- Find maximum and minimum marks.
- Calculate the average marks.
- Display students who scored more than 75.
"""

import pandas as pd

# Create dictionary of student marks
student_dict = {
    "Aarav": 85,
    "Diya": 72,
    "Rohan": 94,
    "Ananya": 65,
    "Vivaan": 88,
    "Ishita": 78
}

# Create Pandas Series
series = pd.Series(student_dict)

# 1. Display the Series
print("1. Student Marks Series:")
print(series)
print("-" * 50)

# 2. Display marks of a particular student
student_name = "Rohan"
print(f"2. Marks of '{student_name}': {series[student_name]}")
print("-" * 50)

# 3. Find maximum and minimum marks
print(f"3. Maximum Marks: {series.max()} (by {series.idxmax()})")
print(f"   Minimum Marks: {series.min()} (by {series.idxmin()})")
print("-" * 50)

# 4. Calculate the average marks
print(f"4. Average Marks: {series.mean():.2f}")
print("-" * 50)

# 5. Display students who scored more than 75
above_75 = series[series > 75]
print("5. Students who scored more than 75:")
print(above_75)
