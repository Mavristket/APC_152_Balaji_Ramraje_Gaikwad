def decimal_to_binary(number):
    if number < 0:
        raise ValueError("number must be non-negative")
    if number < 2:
        return str(number)
    return decimal_to_binary(number // 2) + str(number % 2)
