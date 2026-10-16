"""
Program 3:
Create a NumPy array containing 10 numbers.
Find and display the maximum, minimum, sum, and average of the elements.
"""

import numpy as np

# Create a NumPy array with 10 numbers
arr = np.array([12, 45, 7, 23, 89, 34, 56, 91, 18, 62])

print("Array:", arr)
print("Maximum element:", np.max(arr))
print("Minimum element:", np.min(arr))
print("Sum of elements:", np.sum(arr))
print("Average (Mean) of elements:", np.mean(arr))
