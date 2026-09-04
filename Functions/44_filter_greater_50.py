def greater_than_50(numbers):
    return list(filter(lambda number: number > 50, numbers))


print(greater_than_50([25, 51, 75, 40, 90]))
