"""
Program 6:
Create two 3 x 3 NumPy matrices and perform matrix addition.
"""

import numpy as np

# Create two 3x3 matrices
matrix_a = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

matrix_b = np.array([
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
])

print("Matrix A:\n", matrix_a)
print("\nMatrix B:\n", matrix_b)

# Matrix addition
result = matrix_a + matrix_b
print("\nMatrix Addition (A + B):\n", result)
