"""
Program 9:
Create a 4 x 4 NumPy array and write a program to:
- Display the first row
- Display the last column
- Display the diagonal elements
- Display the elements from the second and third rows
"""

import numpy as np

# Create a 4 x 4 NumPy array
matrix = np.arange(1, 17).reshape(4, 4)

print("4 x 4 Matrix:\n", matrix)
print("-" * 40)

# Display the first row
print("First row:", matrix[0])

# Display the last column
print("Last column:", matrix[:, -1])

# Display diagonal elements
print("Diagonal elements:", np.diag(matrix))

# Display elements from the second and third rows (index 1 and 2)
print("Elements from 2nd and 3rd rows:\n", matrix[1:3, :])
