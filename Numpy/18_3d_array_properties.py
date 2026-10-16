"""
Program 18:
Write a Python program using NumPy to create a 3D array of shape (2, 3, 4)
containing numbers from 1 to 24. Display the array and its:
- Number of dimensions
- Shape
- Size
"""

import numpy as np

# Create 3D array of shape (2, 3, 4) containing numbers 1 to 24
arr_3d = np.arange(1, 25).reshape(2, 3, 4)

print("3D Array (shape (2, 3, 4)):\n", arr_3d)
print("-" * 40)
print("Number of dimensions (ndim):", arr_3d.ndim)
print("Shape of array (shape):", arr_3d.shape)
print("Total number of elements (size):", arr_3d.size)
