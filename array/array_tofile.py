import array
import os

numbers = array.array('i', [10, 20, 30, 40])
print("Original array:", numbers)

filename = "temp_output.bin"

with open(filename, "wb") as f:
    numbers.tofile(f)

print(f"Array data has been written to binary file '{filename}'.")

read_array = array.array('i')
with open(filename, "rb") as f:
    read_array.fromfile(f, 4)

print("Verifying contents read back from file:", read_array)

if os.path.exists(filename):
    os.remove(filename)
