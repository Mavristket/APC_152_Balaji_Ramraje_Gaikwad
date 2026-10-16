"""
Program 17:
Take marks of 20 students, calculate the class average
and display the marks of students who scored above the average.
"""

import numpy as np

# Marks of 20 students
marks = np.array([78, 85, 92, 67, 74, 88, 59, 90, 82, 71,
                  95, 63, 80, 77, 89, 66, 83, 72, 91, 55])

print("Marks of 20 students:\n", marks)

# Calculate class average
class_avg = np.mean(marks)
print(f"\nClass Average: {class_avg:.2f}")

# Boolean indexing to filter marks above average
above_avg_marks = marks[marks > class_avg]

print("\nMarks of students scoring above the average:")
print(above_avg_marks)
print(f"Total count of students above average: {len(above_avg_marks)}")
