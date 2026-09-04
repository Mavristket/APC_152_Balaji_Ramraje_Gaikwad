def count_occurrences(items, element):
    return sum(1 for item in items if item == element)


print(count_occurrences([1, 2, 1, 3, 1], 1))
