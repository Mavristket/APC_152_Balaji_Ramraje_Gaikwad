file_name = input("Enter file name: ")

with open(file_name, "r") as file:
    line_count = sum(1 for line in file)

print("Total lines:", line_count)
