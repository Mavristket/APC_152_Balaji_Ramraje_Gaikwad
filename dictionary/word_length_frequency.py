
paragraph = input("Enter a paragraph: ")

# Split into words
words = paragraph.split()


length_counts = {}
for word in words:
    
    cleaned_word = word.strip(".,!?\"'()[]{}")
    if cleaned_word:
        length = len(cleaned_word)
        length_counts[length] = length_counts.get(length, 0) + 1


print("\nWord length frequencies:")
for length in sorted(length_counts.keys()):
    print(f"Length {length}: {length_counts[length]} word(s)")
