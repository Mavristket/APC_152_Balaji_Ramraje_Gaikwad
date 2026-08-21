import array
import os

filename = "temp_array_data.bin"

numbers_to_write = array.array('i', [100, 200, 300])
with open(filename, 'wb') as f:
    numbers_to_write.tofile(f)

numbers = array.array('i')
print("Original empty array:", numbers)

with open(filename, 'rb') as f:
    numbers.fromfile(f, 3)

print("Array after fromfile():", numbers)

if os.path.exists(filename):
    os.remove(filename)
