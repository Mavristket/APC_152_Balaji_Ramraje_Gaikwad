def sort_by_length(words):
    return sorted(words, key=lambda word: len(word))


print(sort_by_length(["banana", "fig", "apple", "kiwi"]))
