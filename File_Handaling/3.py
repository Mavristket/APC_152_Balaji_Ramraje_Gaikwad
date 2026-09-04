file_name = input("Enter file name: ")
extra_info = input("Enter information to append: ")

with open(file_name, "a") as file:
    file.write(extra_info + "\n")

print("Information appended successfully.")
