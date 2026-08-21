
user_string = input("Enter a string: ")


frequency = {}
for char in user_string:
    frequency[char] = frequency.get(char, 0) + 1


print("Character frequencies:", frequency)
