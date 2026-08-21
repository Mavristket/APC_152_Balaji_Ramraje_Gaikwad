import array

numbers = array.array('h', [1, 256, 512])
print("Original array:", numbers)

numbers.byteswap()
print("Array after byteswap():", numbers)
