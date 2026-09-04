file_name = input("Enter file name: ")

with open(file_name, "r") as file:
    character_count = len(file.read())

print("Total characters, including spaces:", character_count)
