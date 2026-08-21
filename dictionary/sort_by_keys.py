
my_dict = {
    "zebra": 5,
    "apple": 10,
    "mango": 12,
    "banana": 8
}
print("Original dictionary:", my_dict)


sorted_dict = dict(sorted(my_dict.items()))
print("Sorted by keys:", sorted_dict)
