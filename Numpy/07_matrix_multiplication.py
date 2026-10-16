"""
Program 7:
Create two compatible matrices using NumPy and perform matrix multiplication
using an appropriate NumPy function.
"""

import numpy as np

# Create two compatible matrices: A of shape (2, 3) and B of shape (3, 2)
matrix_a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

matrix_b = np.array([
    [7, 8],
    [9, 1],
    [2, 3]
])

print("Matrix A (shape {}):\n{}".format(matrix_a.shape, matrix_a))
print("\nMatrix B (shape {}):\n{}".format(matrix_b.shape, matrix_b))

# Matrix multiplication using np.matmul / np.dot
result = np.matmul(matrix_a, matrix_b)
print("\nMatrix Multiplication Result (np.matmul(A, B), shape {}):\n{}".format(result.shape, result))
