"""
Program 9:
Create a Pandas Series using a dictionary containing employee names and their salaries.
Perform:
- Display the Series.
- Find the highest salary.
- Find the lowest salary.
- Calculate average salary.
- Display employees earning more than Rs. 50,000.
"""

import pandas as pd

# Dictionary with employee names and salaries
salary_dict = {
    "Rajesh Kumar": 65000,
    "Priya Singh": 42000,
    "Amitabh Sen": 95000,
    "Neha Deshmukh": 48000,
    "Sunil Rao": 55000,
    "Kavita Nair": 38000
}

# Create Pandas Series
series = pd.Series(salary_dict)

# 1. Display the Series
print("1. Employee Salary Series:")
print(series)
print("-" * 50)

# 2. Find the highest salary
print(f"2. Highest Salary: Rs. {series.max():,} (earned by {series.idxmax()})")

# 3. Find the lowest salary
print(f"3. Lowest Salary : Rs. {series.min():,} (earned by {series.idxmin()})")

# 4. Calculate average salary
print(f"4. Average Salary: Rs. {series.mean():,.2f}")
print("-" * 50)

# 5. Display employees earning more than 50,000
above_50k = series[series > 50000]
print("5. Employees earning more than Rs. 50,000:")
print(above_50k)
