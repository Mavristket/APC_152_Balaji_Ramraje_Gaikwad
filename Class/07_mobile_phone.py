class MobilePhone:
    def __init__(self, brand, model, storage, price):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.price = price

    def display_specs(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Storage:", self.storage)
        print("Original Price: Rs.", self.price)

    def discounted_price(self, discount_percent):
        return self.price - (self.price * discount_percent / 100)


phone = MobilePhone("Samsung", "Galaxy A55", "128 GB", 30000)
phone.display_specs()
discount = float(input("Enter discount percentage: "))

if 0 <= discount <= 100:
    print("Price after discount: Rs.", round(phone.discounted_price(discount), 2))
else:
    print("Enter a discount from 0 to 100.")
