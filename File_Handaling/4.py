file_name = input("Enter file name: ")

with open(file_name, "r") as file:
    for line in file:
        print(line.rstrip())
