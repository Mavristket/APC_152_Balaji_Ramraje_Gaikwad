"""
Program 20:
Create a (2, 3, 4) array and calculate:
- Sum of all elements
- Sum of each layer
- Sum along rows
- Sum along columns
"""

import numpy as np

# Create 3D array of shape (2, 3, 4)
arr = np.arange(1, 25).reshape(2, 3, 4)

print("3D Array (shape (2, 3, 4)):\n", arr)
print("=" * 45)

# 1. Sum of all elements
total_sum = np.sum(arr)
print("1. Sum of all elements:", total_sum)
print("-" * 45)

# 2. Sum of each layer (axis=(1, 2))
layer_sums = np.sum(arr, axis=(1, 2))
print("2. Sum of each layer (axis=(1, 2)):", layer_sums)
for i, l_sum in enumerate(layer_sums):
    print(f"   Layer {i} sum = {l_sum}")
print("-" * 45)

# 3. Sum along rows (axis=1 collapses rows, yielding sum across rows)
sum_along_rows = np.sum(arr, axis=1)
print("3. Sum along rows (axis=1, shape (2, 4)):\n", sum_along_rows)

# Layer-wise row sums for detailed view
for i, layer in enumerate(arr):
    print(f"   Layer {i} row-wise sum (across columns for each row): {layer.sum(axis=1)}")
print("-" * 45)

# 4. Sum along columns (axis=2 collapses columns, yielding sum across columns)
sum_along_cols = np.sum(arr, axis=2)
print("4. Sum along columns (axis=2, shape (2, 3)):\n", sum_along_cols)

# Layer-wise column sums for detailed view
for i, layer in enumerate(arr):
    print(f"   Layer {i} column-wise sum (down rows for each column): {layer.sum(axis=0)}")
