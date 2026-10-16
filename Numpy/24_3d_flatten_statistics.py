"""
Program 24:
Create a 3D array containing integers from 1 to 27.
Flatten the array and calculate:
- Sum
- Average
- Maximum
- Minimum
"""

import numpy as np

# Create 3D array containing integers from 1 to 27 (shape: 3 x 3 x 3)
arr_3d = np.arange(1, 28).reshape(3, 3, 3)
print("Original 3D Array (shape {}):\n{}".format(arr_3d.shape, arr_3d))
print("-" * 45)

# Flatten the array
flat_arr = arr_3d.flatten()
print("Flattened Array:\n", flat_arr)
print("-" * 45)

# Calculate statistics on the flattened array
total_sum = np.sum(flat_arr)
average = np.mean(flat_arr)
maximum = np.max(flat_arr)
minimum = np.min(flat_arr)

print(f"Sum     : {total_sum}")
print(f"Average : {average:.2f}")
print(f"Maximum : {maximum}")
print(f"Minimum : {minimum}")
