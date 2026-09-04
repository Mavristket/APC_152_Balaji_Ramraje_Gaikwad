def largest_number(numbers):
    if not numbers:
        raise ValueError("the list cannot be empty")

    largest = numbers[0]
    for number in numbers[1:]:
        if number > largest:
            largest = number
    return largest


print(largest_number([12, 45, 8, 31]))
