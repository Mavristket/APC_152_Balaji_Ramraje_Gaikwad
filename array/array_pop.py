import array

numbers = array.array('i', [10, 20, 30, 40])
print("Original array:", numbers)

last_item = numbers.pop()
print(f"Popped item (default index -1): {last_item}")
print("Array after pop():", numbers)

item_at_1 = numbers.pop(1)
print(f"Popped item at index 1: {item_at_1}")
print("Array after pop(1):", numbers)
