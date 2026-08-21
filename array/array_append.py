import array

numbers = array.array('i', [10, 20, 30])
print("Original array:", numbers)

numbers.append(40)
print("Array after append(40):", numbers)
