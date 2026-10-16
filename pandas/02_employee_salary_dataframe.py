"""
Program 2:
Create a dictionary containing:
- Employee ID
- Employee Name
- Department
- Salary
- Experience

Convert it into a Pandas DataFrame and:
1. Display employees with salary greater than Rs. 50,000.
2. Find the average salary.
3. Find the highest salary.
4. Find the employee with the highest experience.
"""

import pandas as pd

# Create dictionary containing employee details
employee_data = {
    "Employee ID": ["E101", "E102", "E103", "E104", "E105"],
    "Employee Name": ["Rajesh Kumar", "Priya Singh", "Amitabh Sen", "Neha Deshmukh", "Sunil Rao"],
    "Department": ["CSE", "HR", "CSE", "Finance", "ECE"],
    "Salary": [65000, 42000, 95000, 48000, 55000],
    "Experience": [5, 3, 9, 4, 7]
}

# Convert to DataFrame
df = pd.DataFrame(employee_data)
print("Complete Employee DataFrame:\n", df)
print("-" * 60)

# 1. Display employees with salary greater than 50,000
high_salary_emp = df[df["Salary"] > 50000]
print("1. Employees with salary > Rs. 50,000:\n", high_salary_emp)
print("-" * 60)

# 2. Find the average salary
avg_salary = df["Salary"].mean()
print(f"2. Average Salary: Rs. {avg_salary:,.2f}")
print("-" * 60)

# 3. Find the highest salary
max_salary = df["Salary"].max()
print(f"3. Highest Salary: Rs. {max_salary:,.2f}")
print("-" * 60)

# 4. Find the employee with the highest experience
max_exp_emp = df.loc[df["Experience"].idxmax()]
print("4. Employee with the highest experience:")
print(f"   Name: {max_exp_emp['Employee Name']}, Experience: {max_exp_emp['Experience']} years, Dept: {max_exp_emp['Department']}")
