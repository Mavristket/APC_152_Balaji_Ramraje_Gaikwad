"""
Program 14:
Create an array containing duplicate values. Find and display only the unique elements.
"""

import numpy as np

# Create an array with duplicate values
arr = np.array([10, 20, 10, 30, 40, 20, 50, 30, 60, 40, 10, 70])

print("Original Array with Duplicates:\n", arr)

# Find unique elements using np.unique
unique_elements = np.unique(arr)

print("\nUnique Elements:\n", unique_elements)
