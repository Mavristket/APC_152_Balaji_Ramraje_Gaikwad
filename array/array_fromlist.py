import array

numbers = array.array('f', [1.5, 2.5])
print("Original array:", numbers)

new_list = [3.5, 4.5, 5.5]

numbers.fromlist(new_list)
print("Array after fromlist():", numbers)
