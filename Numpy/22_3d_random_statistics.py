"""
Program 22:
Generate a random 3D array of shape (3, 4, 5) and calculate its:
mean, median, standard deviation, variance, minimum, and maximum.
"""

import numpy as np

# Set seed for reproducibility
np.random.seed(42)

# Generate a random 3D array of shape (3, 4, 5)
arr = np.random.randint(1, 101, size=(3, 4, 5))

print("3D Array of shape (3, 4, 5):\n", arr)
print("=" * 45)

# Statistical calculations
print(f"Mean               : {np.mean(arr):.4f}")
print(f"Median             : {np.median(arr):.4f}")
print(f"Standard Deviation : {np.std(arr):.4f}")
print(f"Variance           : {np.var(arr):.4f}")
print(f"Minimum            : {np.min(arr)}")
print(f"Maximum            : {np.max(arr)}")
