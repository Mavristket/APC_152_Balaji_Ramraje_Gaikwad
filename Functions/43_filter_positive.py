def positive_numbers(numbers):
    return list(filter(lambda number: number > 0, numbers))


print(positive_numbers([-3, 0, 4, -1, 8]))
