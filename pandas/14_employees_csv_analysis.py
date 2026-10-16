"""
Program 14:
Dataset: employees.csv
Columns: Employee_ID, Name, Department, Experience, Salary

Problem Statement:
Read the CSV file and:
1. Display employees from the CSE department.
2. Find the average salary.
3. Find the highest and lowest salary.
4. Display employees having salary greater than Rs. 50,000.
5. Calculate department-wise average salary.
"""

import os
import pandas as pd

# Load CSV file relative to script location
csv_path = os.path.join(os.path.dirname(__file__), "employees.csv")
df = pd.read_csv(csv_path)

print("Employee Dataset Loaded Successfully:")
print(df)
print("-" * 65)

# 1. Display employees from the CSE department
cse_employees = df[df["Department"] == "CSE"]
print("1. Employees from CSE Department:")
print(cse_employees)
print("-" * 65)

# 2. Find the average salary
avg_salary = df["Salary"].mean()
print(f"2. Average Salary: Rs. {avg_salary:,.2f}")
print("-" * 65)

# 3. Find the highest and lowest salary
max_sal = df["Salary"].max()
min_sal = df["Salary"].min()
print(f"3. Highest Salary: Rs. {max_sal:,} (by {df.loc[df['Salary'].idxmax()]['Name']})")
print(f"   Lowest Salary : Rs. {min_sal:,} (by {df.loc[df['Salary'].idxmin()]['Name']})")
print("-" * 65)

# 4. Display employees having salary greater than 50,000
above_50k = df[df["Salary"] > 50000]
print("4. Employees with salary > Rs. 50,000:")
print(above_50k[["Employee_ID", "Name", "Department", "Salary"]])
print("-" * 65)

# 5. Calculate department-wise average salary
dept_avg_salary = df.groupby("Department")["Salary"].mean()
print("5. Department-wise Average Salary:")
for dept, avg in dept_avg_salary.items():
    print(f"   {dept:<12}: Rs. {avg:,.2f}")
