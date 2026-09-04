def fibonacci(n):
    numbers = []
    first, second = 0, 1
    for _ in range(n):
        numbers.append(first)
        first, second = second, first + second
    return numbers


print(fibonacci(8))
