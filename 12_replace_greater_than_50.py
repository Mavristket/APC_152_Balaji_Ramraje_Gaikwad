"""
Program 12:
Create an array of 10 integers.
Replace all elements greater than 50 with 0 using NumPy Boolean indexing.
"""

import numpy as np

# Create an array of 10 integers
arr = np.array([15, 62, 34, 88, 45, 99, 23, 51, 10, 75])

print("Original Array:\n", arr)

# Replace elements greater than 50 with 0 using Boolean indexing
arr[arr > 50] = 0

print("\nArray after replacing elements > 50 with 0:\n", arr)
