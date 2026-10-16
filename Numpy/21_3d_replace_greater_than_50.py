"""
Program 21:
Create a 3D array of random integers between 1 and 100.
Replace all values greater than 50 with 0.
"""

import numpy as np

# Set seed for reproducible results (optional)
np.random.seed(42)

# Create a 3D array of random integers between 1 and 100
arr_3d = np.random.randint(1, 101, size=(2, 3, 4))

print("Original 3D Array:\n", arr_3d)
print("-" * 45)

# Replace values greater than 50 with 0 using Boolean indexing
arr_3d[arr_3d > 50] = 0

print("3D Array after replacing elements > 50 with 0:\n", arr_3d)
