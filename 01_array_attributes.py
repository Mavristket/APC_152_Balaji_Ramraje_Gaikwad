"""
Program 1:
Write a Python program using NumPy to create a one-dimensional array
containing 10 integers and display the array, its size, data type,
and number of dimensions.
"""

import numpy as np

# Create a 1D NumPy array containing 10 integers
arr = np.array([10, 25, 30, 45, 50, 65, 70, 85, 90, 100])

print("Array:", arr)
print("Size of array:", arr.size)
print("Data type of array:", arr.dtype)
print("Number of dimensions:", arr.ndim)
