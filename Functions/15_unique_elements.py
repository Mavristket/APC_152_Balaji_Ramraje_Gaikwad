def unique_elements(items):
    unique = []
    for item in items:
        if item not in unique:
            unique.append(item)
    return unique


print(unique_elements([1, 2, 2, 3, 1, 4]))
