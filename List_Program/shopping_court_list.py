cart = ["Pen", "Book", "Bag"]

cart.append("Pencil")

cart.remove("Pen")

item = "Book"

if item in cart:
    print("Item found")
else:
    print("Item not found")

print("Shopping cart:", cart)
print("Total items:", len(cart))
