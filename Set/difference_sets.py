# Create two sets
set_a = {"apple", "banana", "cherry"}
set_b = {"banana", "cherry", "date"}


diff_first_second = set_a.difference(set_b)


diff_second_first = set_b.difference(set_a)

print("Set A:", set_a)
print("Set B:", set_b)
print("Elements present in Set A but not in Set B:", diff_first_second)
print("Elements present in Set B but not in Set A:", diff_second_first)
