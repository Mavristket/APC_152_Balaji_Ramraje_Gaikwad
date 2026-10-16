"""
Program 12:
Create a Pandas Series using a dictionary containing student names and attendance percentages.
Perform:
- Find the average attendance.
- Display students with attendance below 75%.
- Display students with attendance above 90%.
- Find the highest attendance.
"""

import pandas as pd

# Dictionary with student names and attendance percentages
attendance_dict = {
    "Aarav Sharma": 92.5,
    "Diya Patel": 71.0,
    "Rohan Verma": 96.0,
    "Ananya Iyer": 68.5,
    "Vivaan Reddy": 84.0,
    "Ishita Gupta": 91.5,
    "Kabir Mehta": 74.0,
    "Meera Nair": 88.0
}

# Create Pandas Series
series = pd.Series(attendance_dict)

print("Student Attendance Series:")
print(series)
print("-" * 55)

# 1. Find the average attendance
print(f"1. Average Attendance: {series.mean():.2f}%")
print("-" * 55)

# 2. Display students with attendance below 75%
below_75 = series[series < 75]
print("2. Students with attendance below 75% (Shortage):")
print(below_75)
print("-" * 55)

# 3. Display students with attendance above 90%
above_90 = series[series > 90]
print("3. Students with attendance above 90% (Excellent):")
print(above_90)
print("-" * 55)

# 4. Find the highest attendance
print(f"4. Highest Attendance: {series.max()}% (Achieved by {series.idxmax()})")
