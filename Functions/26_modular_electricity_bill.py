def slab_charge(units):
    if units <= 100:
        return units * 2
    if units <= 200:
        return 100 * 2 + (units - 100) * 3
    return 100 * 2 + 100 * 3 + (units - 200) * 5


def electricity_bill(units, fixed_charge=100, tax_rate=5, discount_rate=0):
    amount = slab_charge(units) + fixed_charge
    amount += amount * tax_rate / 100
    return amount - amount * discount_rate / 100


print(electricity_bill(250, discount_rate=5))
