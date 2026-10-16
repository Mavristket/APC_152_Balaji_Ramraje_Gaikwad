class ElectricityBill:
    def __init__(self, consumer_no, consumer_name, units):
        self.consumer_no = consumer_no
        self.consumer_name = consumer_name
        self.units = units

    def calculate_bill(self):
        # Example cumulative slab rates:
        # first 100 units Rs. 1.50/unit, next 100 Rs. 2.50/unit,
        # next 100 Rs. 4/unit, and above 300 Rs. 6/unit.
        remaining = self.units
        bill = 0

        slab = min(remaining, 100)
        bill += slab * 1.50
        remaining -= slab

        slab = min(max(remaining, 0), 100)
        bill += slab * 2.50
        remaining -= slab

        slab = min(max(remaining, 0), 100)
        bill += slab * 4.00
        remaining -= slab

        if remaining > 0:
            bill += remaining * 6.00

        return bill

    def display(self):
        print("Consumer Number:", self.consumer_no)
        print("Consumer Name:", self.consumer_name)
        print("Units Consumed:", self.units)
        print("Electricity Bill: Rs.", round(self.calculate_bill(), 2))


consumer_no = input("Enter consumer number: ")
consumer_name = input("Enter consumer name: ")
units = int(input("Enter units consumed: "))

if units < 0:
    print("Units cannot be negative.")
else:
    bill = ElectricityBill(consumer_no, consumer_name, units)
    bill.display()
