file_name = input("Enter file name: ")
alphabets = digits = spaces = special_characters = 0

with open(file_name, "r") as file:
    for character in file.read():
        if character.isalpha():
            alphabets += 1
        elif character.isdigit():
            digits += 1
        elif character.isspace():
            spaces += 1
        else:
            special_characters += 1

print("Alphabets:", alphabets)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special characters:", special_characters)
