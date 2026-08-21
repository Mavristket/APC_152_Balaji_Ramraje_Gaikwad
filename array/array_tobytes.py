import array

numbers = array.array('i', [10, 20, 30])
print("Original array:", numbers)

array_bytes = numbers.tobytes()
print("Bytes representation:", array_bytes)
print("Type of output:", type(array_bytes))
print("Restored array from bytes:", array.array('i', array_bytes))
