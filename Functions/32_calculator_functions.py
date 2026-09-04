def add(first, second):
    return first + second


def subtract(first, second):
    return first - second


def multiply(first, second):
    return first * second


def divide(first, second):
    if second == 0:
        raise ZeroDivisionError("cannot divide by zero")
    return first / second


def calculate(first, second, operation):
    return operation(first, second)


print(calculate(12, 4, add))
print(calculate(12, 4, divide))
