import array

numbers = array.array('i', [10, 20, 30, 40, 20, 50])
print("Array:", numbers)

first_index = numbers.index(20)
print("Index of first 20:", first_index)

next_index = numbers.index(20, 2)
print("Index of 20 (starting search from index 2):", next_index)
