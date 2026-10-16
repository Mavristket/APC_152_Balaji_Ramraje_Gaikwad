"""
Program 6:
Create a dictionary containing:
- Student_ID
- Name
- Department
- Total_Classes
- Classes_Attended

Create a DataFrame and calculate:
Attendance Percentage = (Classes_Attended / Total_Classes) * 100
Display students whose attendance is below 75%.
"""

import pandas as pd

# Create student attendance dictionary
attendance_data = {
    "Student_ID": [201, 202, 203, 204, 205, 206],
    "Name": ["Aarav", "Diya", "Rohan", "Ananya", "Vivaan", "Ishita"],
    "Department": ["CSE", "ECE", "CSE", "IT", "ME", "CSE"],
    "Total_Classes": [60, 60, 60, 60, 60, 60],
    "Classes_Attended": [52, 40, 56, 38, 48, 42]
}

# Create DataFrame
df = pd.DataFrame(attendance_data)

# Calculate Attendance Percentage
df["Attendance Percentage"] = (df["Classes_Attended"] / df["Total_Classes"]) * 100

print("Student Attendance DataFrame:\n", df)
print("-" * 65)

# Display students whose attendance is below 75%
low_attendance = df[df["Attendance Percentage"] < 75]
print("Students with Attendance below 75% (Shortage of Attendance):")
print(low_attendance[["Student_ID", "Name", "Department", "Attendance Percentage"]])
