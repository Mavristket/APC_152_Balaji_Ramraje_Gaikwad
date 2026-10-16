"""
Program 23:
Create a 3D NumPy array of shape (2, 3, 4) containing numbers from 1 to 24.
Flatten the array into a one-dimensional array and display both the
original and flattened arrays.
"""

import numpy as np

# Create 3D array of shape (2, 3, 4) containing numbers 1 to 24
arr_3d = np.arange(1, 25).reshape(2, 3, 4)

print("Original 3D Array (shape {}):\n{}".format(arr_3d.shape, arr_3d))
print("-" * 45)

# Flatten into a 1D array
flattened_arr = arr_3d.flatten()

print("Flattened 1D Array (shape {}):\n{}".format(flattened_arr.shape, flattened_arr))
