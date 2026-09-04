def corresponding_sums(first_list, second_list):
    return list(map(lambda values: values[0] + values[1], zip(first_list, second_list)))


print(corresponding_sums([1, 2, 3], [4, 5, 6]))
