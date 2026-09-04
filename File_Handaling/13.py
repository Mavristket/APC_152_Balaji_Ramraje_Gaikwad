#!/usr/bin/env python3

file_name = input("Enter file name: ")
search_word = input("Enter word to search: ").lower()
total = 0
line_numbers = []

with open(file_name, "r") as file:
    for line_number, line in enumerate(file, start=1):
        words = line.lower().split()
        count = sum(word.strip(".,!?;:") == search_word for word in words)
        if count:
            total += count
            line_numbers.append(line_number)

print("Occurrences:", total)
print("Line numbers:", line_numbers)
