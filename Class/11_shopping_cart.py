class ShoppingCart:
    def __init__(self, customer_name, cart_id):
        self.customer_name = customer_name
        self.cart_id = cart_id
        self.products = {}  # product name: price

    def add_product(self, name, price):
        if price >= 0:
            self.products[name] = price
            print(name, "added to cart.")
        else:
            print("Price cannot be negative.")

    def remove_product(self, name):
        if name in self.products:
            del self.products[name]
            print(name, "removed from cart.")
        else:
            print("Product not found.")

    def total_bill(self):
        return sum(self.products.values())

    def display_cart(self):
        print("Customer:", self.customer_name)
        print("Cart ID:", self.cart_id)
        print("Products:", self.products)
        print("Total Bill: Rs.", self.total_bill())

    def __del__(self):
        print("Shopping cart object destroyed.")


cart = ShoppingCart("Amit", "C101")
cart.add_product("Notebook", 50)
cart.add_product("Pen", 10)
cart.add_product("Bag", 700)
cart.display_cart()
cart.remove_product("Pen")
cart.display_cart()
del cart
