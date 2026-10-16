"""
Program 5:
Create a one-dimensional array containing numbers from 1 to 12. Reshape it into:
- 2 x 6 matrix
- 3 x 4 matrix
- 4 x 3 matrix
"""

import numpy as np

# Create 1D array from 1 to 12
arr = np.arange(1, 13)
print("Original 1D Array:\n", arr)

# Reshape into 2 x 6 matrix
matrix_2x6 = arr.reshape(2, 6)
print("\nReshaped to 2 x 6 Matrix:\n", matrix_2x6)

# Reshape into 3 x 4 matrix
matrix_3x4 = arr.reshape(3, 4)
print("\nReshaped to 3 x 4 Matrix:\n", matrix_3x4)

# Reshape into 4 x 3 matrix
matrix_4x3 = arr.reshape(4, 3)
print("\nReshaped to 4 x 3 Matrix:\n", matrix_4x3)
