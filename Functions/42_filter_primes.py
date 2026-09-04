def prime_numbers(numbers):
    is_prime = lambda number: number > 1 and all(number % divisor for divisor in range(2, int(number ** 0.5) + 1))
    return list(filter(is_prime, numbers))


print(prime_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9]))
