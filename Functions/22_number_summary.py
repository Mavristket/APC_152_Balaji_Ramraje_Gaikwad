def number_summary(numbers):
    if not numbers:
        raise ValueError("the list cannot be empty")
    return {
        "minimum": min(numbers),
        "maximum": max(numbers),
        "sum": sum(numbers),
        "average": sum(numbers) / len(numbers),
    }


print(number_summary([4, 8, 15, 16, 23, 42]))
