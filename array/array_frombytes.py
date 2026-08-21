import array

numbers = array.array('i', [10, 20])
print("Original array:", numbers)

new_data_bytes = array.array('i', [30, 40]).tobytes()
print("Bytes to append:", new_data_bytes)

numbers.frombytes(new_data_bytes)
print("Array after frombytes():", numbers)
