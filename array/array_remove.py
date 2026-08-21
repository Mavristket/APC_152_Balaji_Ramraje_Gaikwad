import array

numbers = array.array('i', [10, 20, 30, 20, 40])
print("Original array:", numbers)

numbers.remove(20)
print("Array after removing first occurrence of 20:", numbers)
