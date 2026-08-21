
sentence = input("Enter a sentence: ")


words = sentence.lower().split()


word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print("Word frequencies:", word_count)
