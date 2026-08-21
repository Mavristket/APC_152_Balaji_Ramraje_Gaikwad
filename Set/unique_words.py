
sentence = input("Enter a sentence: ")


words = sentence.lower().split()

unique_words = set(words)

print("Unique words in the sentence:", unique_words)
