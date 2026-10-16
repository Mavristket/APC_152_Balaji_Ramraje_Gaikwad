"""
Program 13:
Dataset: students.csv
Columns: Student_ID, Name, Department, Python, DBMS, Maths

Problem Statement:
Read students.csv using Pandas and perform the following:
1. Display the first 5 records.
2. Display the last 5 records.
3. Find the total and average marks of each student.
4. Display students whose average marks are greater than 75.
5. Find the student with the highest average.
6. Find the average marks for each subject.
"""

import os
import pandas as pd

# Load CSV file relative to script location
csv_path = os.path.join(os.path.dirname(__file__), "students.csv")
df = pd.read_csv(csv_path)

# 1. Display first 5 records
print("1. First 5 records:")
print(df.head(5))
print("-" * 65)

# 2. Display last 5 records
print("2. Last 5 records:")
print(df.tail(5))
print("-" * 65)

# 3. Find the total and average marks of each student
df["Total"] = df["Python"] + df["DBMS"] + df["Maths"]
df["Average"] = df["Total"] / 3
print("3. Total and Average Marks of each student:")
print(df[["Student_ID", "Name", "Total", "Average"]])
print("-" * 65)

# 4. Display students whose average marks are greater than 75
above_75 = df[df["Average"] > 75]
print("4. Students with average marks > 75:")
print(above_75[["Student_ID", "Name", "Department", "Average"]])
print("-" * 65)

# 5. Find the student with the highest average
top_student = df.loc[df["Average"].idxmax()]
print("5. Student with the highest average:")
print(f"   Name: {top_student['Name']} (ID: {top_student['Student_ID']}, Dept: {top_student['Department']})")
print(f"   Average Marks: {top_student['Average']:.2f}")
print("-" * 65)

# 6. Find the average marks for each subject
subject_averages = df[["Python", "DBMS", "Maths"]].mean()
print("6. Average marks for each subject:")
for subject, avg in subject_averages.items():
    print(f"   {subject:<8}: {avg:.2f}")
