"""
Program 10:
Create a 4 x 4 matrix and calculate the sum of each row and each column separately.
"""

import numpy as np

# Create a 4 x 4 matrix
matrix = np.array([
    [10, 20, 30, 40],
    [15, 25, 35, 45],
    [12, 22, 32, 42],
    [18, 28, 38, 48]
])

print("4 x 4 Matrix:\n", matrix)
print("-" * 40)

# Sum of each row (axis=1)
row_sums = np.sum(matrix, axis=1)
print("Sum of each row (axis=1):", row_sums)

for idx, r_sum in enumerate(row_sums, start=1):
    print(f"  Row {idx} sum = {r_sum}")

print("-" * 40)

# Sum of each column (axis=0)
col_sums = np.sum(matrix, axis=0)
print("Sum of each column (axis=0):", col_sums)

for idx, c_sum in enumerate(col_sums, start=1):
    print(f"  Column {idx} sum = {c_sum}")
