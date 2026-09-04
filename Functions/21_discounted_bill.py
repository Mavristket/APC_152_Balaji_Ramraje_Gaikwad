def total_bill(prices, quantities, discount=0):
    subtotal = sum(price * quantity for price, quantity in zip(prices, quantities))
    return subtotal - subtotal * discount / 100


print(total_bill([100, 250, 50], [2, 1, 3], 10))
