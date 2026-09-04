file_name = input("Enter file name: ")
vowels = set("aeiouAEIOU")
vowel_count = 0
consonant_count = 0

with open(file_name, "r") as file:
    for character in file.read():
        if character.isalpha():
            if character in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

print("Vowels:", vowel_count)
print("Consonants:", consonant_count)
