"""
Program 2:
Create two NumPy arrays of 5 integers each. Perform and display:
- Addition
- Subtraction
- Multiplication
- Division
- Modulus
"""

import numpy as np

# Create two NumPy arrays of 5 integers each
arr1 = np.array([25, 40, 60, 85, 100])
arr2 = np.array([3, 5, 7, 9, 11])

print("Array 1:", arr1)
print("Array 2:", arr2)
print("-" * 40)

# Arithmetic Operations
print("Addition (arr1 + arr2):", arr1 + arr2)
print("Subtraction (arr1 - arr2):", arr1 - arr2)
print("Multiplication (arr1 * arr2):", arr1 * arr2)
print("Division (arr1 / arr2):", arr1 / arr2)
print("Modulus (arr1 % arr2):", arr1 % arr2)
