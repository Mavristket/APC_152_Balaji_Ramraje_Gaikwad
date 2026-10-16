"""
Program 4:
Create a NumPy array of integers from 1 to 20.
Use Boolean indexing to separate and display the even and odd numbers.
"""

import numpy as np

# Create an array of integers from 1 to 20
arr = np.arange(1, 21)
print("Original Array:", arr)

# Boolean indexing for even numbers
even_mask = (arr % 2 == 0)
even_numbers = arr[even_mask]

# Boolean indexing for odd numbers
odd_mask = (arr % 2 != 0)
odd_numbers = arr[odd_mask]

print("Even numbers (using Boolean indexing):", even_numbers)
print("Odd numbers (using Boolean indexing):", odd_numbers)
