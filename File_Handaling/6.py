file_name = input("Enter file name: ")

with open(file_name, "r") as file:
    word_count = len(file.read().split())

print("Total words:", word_count)
