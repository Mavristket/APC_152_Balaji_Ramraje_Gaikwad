"""
Program 1:
Create a dictionary containing information for 5 students:
- Student ID
- Student Name
- Python Marks
- DBMS Marks
- Mathematics Marks

Convert the dictionary into a Pandas DataFrame and:
1. Display the DataFrame.
2. Calculate total marks for each student.
3. Calculate average marks.
4. Display students who scored more than 75% average.
"""

import pandas as pd

# Create dictionary containing 5 students' details
data = {
    "Student ID": [101, 102, 103, 104, 105],
    "Student Name": ["Aarav Sharma", "Diya Patel", "Rohan Verma", "Ananya Iyer", "Vivaan Reddy"],
    "Python Marks": [85, 68, 92, 55, 78],
    "DBMS Marks": [78, 72, 88, 60, 82],
    "Mathematics Marks": [92, 64, 95, 58, 80]
}

# Convert dictionary to DataFrame
df = pd.DataFrame(data)

# 1. Display the DataFrame
print("1. Student DataFrame:")
print(df)
print("-" * 60)

# 2. Calculate total marks for each student
df["Total Marks"] = df["Python Marks"] + df["DBMS Marks"] + df["Mathematics Marks"]
print("2. DataFrame with Total Marks:")
print(df[["Student ID", "Student Name", "Total Marks"]])
print("-" * 60)

# 3. Calculate average marks
df["Average Marks"] = df["Total Marks"] / 3
print("3. DataFrame with Average Marks:")
print(df[["Student ID", "Student Name", "Total Marks", "Average Marks"]])
print("-" * 60)

# 4. Display students who scored more than 75% average
high_scorers = df[df["Average Marks"] > 75]
print("4. Students with average marks > 75%:")
print(high_scorers[["Student ID", "Student Name", "Average Marks"]])
