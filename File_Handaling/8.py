file_name = input("Enter file name: ")

with open(file_name, "r") as file:
    lines = file.readlines()

for line in reversed(lines):
    print(line.rstrip())
