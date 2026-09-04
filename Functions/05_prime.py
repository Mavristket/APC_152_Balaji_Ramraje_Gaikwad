def is_prime(n):
    if n < 2:
        return False
    for number in range(2, int(n ** 0.5) + 1):
        if n % number == 0:
            return False
    return True


print(is_prime(17))
