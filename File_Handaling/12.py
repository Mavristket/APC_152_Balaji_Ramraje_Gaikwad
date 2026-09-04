import re

file_name = input("Enter file name: ")

with open(file_name, "r") as file:
    words = re.findall(r"[A-Za-z0-9']+", file.read().lower())

word_counts = {}
for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1

print(word_counts)
