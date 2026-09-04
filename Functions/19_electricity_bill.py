def electricity_bill(units):
    if units <= 100:
        return units * 1.50
    if units <= 200:
        return 100 * 1.50 + (units - 100) * 2.50
    if units <= 300:
        return 100 * 1.50 + 100 * 2.50 + (units - 200) * 4.00
    return 100 * 1.50 + 100 * 2.50 + 100 * 4.00 + (units - 300) * 6.00


print(electricity_bill(250))
