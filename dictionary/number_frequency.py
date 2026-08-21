
numbers_list = [1, 2, 3, 2, 4, 1, 5, 2, 4, 3, 3, 3]
print("Original list:", numbers_list)


frequency = {}
for num in numbers_list:
    frequency[num] = frequency.get(num, 0) + 1

print("Number frequencies:", frequency)
