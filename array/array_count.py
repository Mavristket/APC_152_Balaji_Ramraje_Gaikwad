import array

numbers = array.array('i', [10, 20, 30, 20, 40, 20])
print("Array:", numbers)

occurrences = numbers.count(20)
print("Count of 20 in the array:", occurrences)
