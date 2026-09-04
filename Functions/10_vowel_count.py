def count_vowels(text):
    return sum(1 for character in text.lower() if character in "aeiou")


print(count_vowels("Hello World"))
