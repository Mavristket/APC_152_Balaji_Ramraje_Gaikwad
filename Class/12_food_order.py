class FoodOrder:
    def __init__(self, order_id, customer_name, food_item, quantity, price):
        self.order_id = order_id
        self.customer_name = customer_name
        self.food_item = food_item
        self.quantity = quantity
        self.price = price

    def total_bill(self, tax_percent=5):
        subtotal = self.quantity * self.price
        tax = subtotal * tax_percent / 100
        return subtotal + tax

    def display(self):
        print("Order ID:", self.order_id)
        print("Customer Name:", self.customer_name)
        print("Food Item:", self.food_item)
        print("Quantity:", self.quantity)
        print("Price per item: Rs.", self.price)
        print("Total Bill including 5% tax: Rs.", round(self.total_bill(), 2))

    def __del__(self):
        print("Food order completed.")


order = FoodOrder(501, "Priya", "Pizza", 2, 250)
order.display()
del order
