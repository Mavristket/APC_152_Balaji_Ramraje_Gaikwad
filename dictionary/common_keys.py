
dict_a = {"apple": 5, "banana": 3, "cherry": 7}
dict_b = {"banana": 8, "cherry": 10, "date": 2}


common_keys = set(dict_a.keys()).intersection(set(dict_b.keys()))


print("Dict A:", dict_a)
print("Dict B:", dict_b)
print("Common keys:", common_keys)
