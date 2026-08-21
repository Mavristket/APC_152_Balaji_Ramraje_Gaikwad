import array

numbers = array.array('i', [10, 20, 30])
print("Original array:", numbers)

numbers.insert(1, 15)
print("Array after inserting 15 at index 1:", numbers)

numbers.insert(0, 5)
print("Array after inserting 5 at index 0:", numbers)
