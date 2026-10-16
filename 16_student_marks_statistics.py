"""
Program 16:
Store marks of 10 students in a NumPy array. Calculate:
- Highest marks
- Lowest marks
- Average marks
- Median
- Standard deviation
"""

import numpy as np

# Store marks of 10 students
marks = np.array([78, 85, 92, 67, 74, 88, 59, 90, 82, 71])

print("Student Marks:", marks)
print("-" * 40)

# Statistical calculations
highest = np.max(marks)
lowest = np.min(marks)
average = np.mean(marks)
median = np.median(marks)
std_dev = np.std(marks)

print(f"Highest Marks     : {highest}")
print(f"Lowest Marks      : {lowest}")
print(f"Average Marks     : {average:.2f}")
print(f"Median Marks      : {median:.2f}")
print(f"Standard Deviation: {std_dev:.2f}")
