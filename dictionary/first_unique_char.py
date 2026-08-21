
text = "swiss"
print("Input string:", text)

char_counts = {}
for char in text:
    char_counts[char] = char_counts.get(char, 0) + 1


first_unique = None
for char in text:
    if char_counts[char] == 1:
        first_unique = char
        break


if first_unique:
    print(f"The first character that occurs only once is: '{first_unique}'")
else:
    print("There are no unique characters in the string.")
