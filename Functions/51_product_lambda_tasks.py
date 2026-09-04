def product_values(products):
    return list(map(lambda product: (product[0], product[1], product[2], product[1] * product[2]), products))


def costing_more_than_1000(products):
    return list(filter(lambda product: product[1] * product[2] > 1000, products))


def sort_by_total_value(products):
    return sorted(products, key=lambda product: product[1] * product[2])



products = [("Pen", 20, 10), ("Bag", 800, 2), ("Book", 300, 4)]
print(product_values(products))
print(costing_more_than_1000(products))
print(sort_by_total_value(products))
