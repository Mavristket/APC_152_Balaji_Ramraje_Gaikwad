def second_largest(numbers):
    unique_numbers = sorted(set(numbers))
    if len(unique_numbers) < 2:
        raise ValueError("at least two different numbers are required")
    return unique_numbers[-2]


print(second_largest([12, 45, 8, 31, 45]))
