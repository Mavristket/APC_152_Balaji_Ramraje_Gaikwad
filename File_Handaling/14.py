file_name = input("Enter file name: ")
old_word = input("Enter word to replace: ")
new_word = input("Enter new word: ")

with open(file_name, "r") as file:
    text = file.read()

text = text.replace(old_word, new_word)

with open(file_name, "w") as file:
    file.write(text)

print("Replacement completed.")
