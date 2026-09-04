import re

file_name = input("Enter file name: ")

with open(file_name, "r") as file:
    words = re.findall(r"[A-Za-z0-9']+", file.read())

if words:
    longest_word = max(words, key=len)
    print("Longest word:", longest_word)
else:
    print("The file does not contain any words.")
