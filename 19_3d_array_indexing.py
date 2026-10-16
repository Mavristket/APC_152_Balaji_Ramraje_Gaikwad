"""
Program 19:
Create a 3D array of shape (2, 3, 4) and write a program to access:
- First element
- Last element
- Element at index [0, 1, 2]
- Element at index [1, 2, 3]
"""

import numpy as np

# Create 3D array of shape (2, 3, 4)
arr_3d = np.arange(1, 25).reshape(2, 3, 4)

print("3D Array:\n", arr_3d)
print("-" * 40)

# Accessing specified elements
first_elem = arr_3d[0, 0, 0]
last_elem = arr_3d[-1, -1, -1]
elem_012 = arr_3d[0, 1, 2]
elem_123 = arr_3d[1, 2, 3]

print(f"First element (index [0, 0, 0])     : {first_elem}")
print(f"Last element (index [-1, -1, -1])    : {last_elem}")
print(f"Element at index [0, 1, 2]           : {elem_012}")
print(f"Element at index [1, 2, 3]           : {elem_123}")
