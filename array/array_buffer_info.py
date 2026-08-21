import array

numbers = array.array('i', [10, 20, 30, 40])
print("Array:", numbers)

info = numbers.buffer_info()
print("Buffer info (address, length):", info)
print(f"Memory Address: {info[0]}")
print(f"Number of elements: {info[1]}")
