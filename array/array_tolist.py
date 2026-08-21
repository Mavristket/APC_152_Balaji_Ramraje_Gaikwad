import array

numbers = array.array('i', [10, 20, 30])
print("Original array:", numbers)

normal_list = numbers.tolist()
print("Converted to list:", normal_list)
print("Type of output:", type(normal_list))
