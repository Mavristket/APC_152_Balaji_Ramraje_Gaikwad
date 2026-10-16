"""
Program 8:
Create a 3 x 4 matrix and display its transpose.
"""

import numpy as np

# Create a 3 x 4 matrix
matrix = np.arange(1, 13).reshape(3, 4)

print("Original 3 x 4 Matrix:\n", matrix)

# Transpose of the matrix
transposed = matrix.T  # Alternatively np.transpose(matrix)

print("\nTransposed Matrix (shape {}):\n{}".format(transposed.shape, transposed))
