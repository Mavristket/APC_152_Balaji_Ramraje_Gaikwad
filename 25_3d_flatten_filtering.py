"""
Program 25:
Create a random 3D NumPy array of shape (3, 4, 5). Flatten it and display only
the elements that are:
- Greater than 50
- Even numbers
- Less than the average value
"""

import numpy as np

# Set seed for reproducibility
np.random.seed(42)

# Create a random 3D NumPy array of shape (3, 4, 5) with integers between 1 and 100
arr_3d = np.random.randint(1, 101, size=(3, 4, 5))

print("Original 3D Array of shape (3, 4, 5):\n", arr_3d)
print("=" * 50)

# Flatten the array
flat_arr = arr_3d.flatten()
print("Flattened Array (60 elements):\n", flat_arr)
print("-" * 50)

# 1. Elements greater than 50
greater_than_50 = flat_arr[flat_arr > 50]
print("1. Elements greater than 50:\n", greater_than_50)
print("-" * 50)

# 2. Even numbers
even_elements = flat_arr[flat_arr % 2 == 0]
print("2. Even numbers:\n", even_elements)
print("-" * 50)

# 3. Elements less than the average value
avg_value = np.mean(flat_arr)
less_than_avg = flat_arr[flat_arr < avg_value]
print(f"3. Elements less than average ({avg_value:.2f}):\n", less_than_avg)
