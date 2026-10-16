"""
Program 15:
Create two NumPy arrays and concatenate them horizontally and vertically.
"""

import numpy as np

# Create two 2D NumPy arrays of same shape (2, 3)
arr1 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

arr2 = np.array([
    [7, 8, 9],
    [10, 11, 12]
])

print("Array 1 (shape {}):\n{}".format(arr1.shape, arr1))
print("\nArray 2 (shape {}):\n{}".format(arr2.shape, arr2))
print("-" * 40)

# Horizontal Concatenation (axis=1 / np.hstack)
h_concat = np.hstack((arr1, arr2))
print("Horizontal Concatenation (np.hstack, shape {}):\n{}".format(h_concat.shape, h_concat))

print("-" * 40)

# Vertical Concatenation (axis=0 / np.vstack)
v_concat = np.vstack((arr1, arr2))
print("Vertical Concatenation (np.vstack, shape {}):\n{}".format(v_concat.shape, v_concat))
