import array

numbers1 = array.array('i', [10, 20])
numbers2 = array.array('i', [30, 40, 50])

print("Original array 1:", numbers1)
print("Array 2:", numbers2)

numbers1.extend(numbers2)
print("Array 1 after extend(numbers2):", numbers1)

numbers1.extend([60, 70])
print("Array 1 after extending with list [60, 70]:", numbers1)
