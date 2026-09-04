from itertools import zip_longest

first_file = input("Enter first file name: ")
second_file = input("Enter second file name: ")

with open(first_file, "r") as first, open(second_file, "r") as second:
    for line_number, lines in enumerate(zip_longest(first, second), start=1):
        first_line, second_line = lines
        if first_line != second_line:
            print("Files are different.")
            print("First different line:", line_number)
            break
    else:
        print("Files are identical.")
