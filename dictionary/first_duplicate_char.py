
text = "swiss"
print("Input string:", text)


char_counts = {}
for char in text:
    char_counts[char] = char_counts.get(char, 0) + 1

first_duplicate = None
for char in text:
    if char_counts[char] > 1:
        first_duplicate = char
        break


if first_duplicate:
    print(f"The first character that occurs more than once is: '{first_duplicate}'")
else:
    print("There are no duplicate characters in the string.")
