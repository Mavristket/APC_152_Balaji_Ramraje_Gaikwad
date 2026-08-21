
students = {"Alice", "Bob", "Charlie", "David", "Emma"}


search_name = input("Enter a student's name to check: ")


if search_name in students:
    print(f"Yes, {search_name} exists in the set.")
else:
    print(f"No, {search_name} does not exist in the set.")
