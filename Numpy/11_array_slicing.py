"""
Program 11:
Create a NumPy array containing numbers from 1 to 20. Using slicing, display:
- First 5 elements
- Last 5 elements
- Alternate elements
- Elements in reverse order
"""

import numpy as np

# Create array with numbers from 1 to 20
arr = np.arange(1, 21)

print("Original Array:\n", arr)
print("-" * 40)

# Slicing operations
print("First 5 elements (arr[:5]):", arr[:5])
print("Last 5 elements (arr[-5:]):", arr[-5:])
print("Alternate elements (arr[::2]):", arr[::2])
print("Elements in reverse order (arr[::-1]):", arr[::-1])
