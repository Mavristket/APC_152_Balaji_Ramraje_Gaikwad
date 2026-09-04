def binary_search(numbers, target, low=0, high=None):
    if high is None:
        high = len(numbers) - 1
    if low > high:
        return -1

    middle = (low + high) // 2
    if numbers[middle] == target:
        return middle
    if target < numbers[middle]:
        return binary_search(numbers, target, low, middle - 1)
    return binary_search(numbers, target, middle + 1, high)


print(binary_search([2, 5, 8, 12, 16, 20], 12))
