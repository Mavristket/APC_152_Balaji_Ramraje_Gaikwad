def word_lengths(words):
    return list(map(lambda word: len(word), words))


def words_longer_than_five(words):
    return list(filter(lambda word: len(word) > 5, words))


def sort_by_length(words):
    return sorted(words, key=lambda word: len(word))



words = ["apple", "computer", "pen", "notebook"]
print(word_lengths(words))
print(words_longer_than_five(words))
print(sort_by_length(words))
