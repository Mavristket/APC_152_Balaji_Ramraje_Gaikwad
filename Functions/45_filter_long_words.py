def long_words(words):
    return list(filter(lambda word: len(word) > 5, words))


print(long_words(["cat", "orange", "computer", "book"]))
