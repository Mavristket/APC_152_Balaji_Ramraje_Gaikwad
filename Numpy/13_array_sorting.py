"""
Program 13:
Create an unsorted NumPy array and display it in:
- Ascending order
- Descending order
"""

import numpy as np

# Create an unsorted NumPy array
arr = np.array([45, 12, 89, 23, 7, 56, 91, 34, 18, 62])

print("Original Unsorted Array:", arr)

# Ascending order
ascending_arr = np.sort(arr)
print("Ascending Order:", ascending_arr)

# Descending order (reversing the ascending sorted array)
descending_arr = np.sort(arr)[::-1]
print("Descending Order:", descending_arr)
