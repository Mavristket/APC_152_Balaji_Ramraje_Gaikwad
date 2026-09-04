products = {}


def add_product(name, price, quantity):
    products[name] = {"price": price, "quantity": quantity}


def remove_product(name):
    products.pop(name, None)


def subtotal():
    return sum(item["price"] * item["quantity"] for item in products.values())


def apply_coupon(amount, coupon):
    discounts = {"SAVE10": 10, "SAVE20": 20}
    return amount - amount * discounts.get(coupon, 0) / 100


def calculate_gst(amount, rate=18):
    return amount * rate / 100


def generate_invoice(coupon=None, gst_rate=18):
    before_tax = apply_coupon(subtotal(), coupon)
    gst = calculate_gst(before_tax, gst_rate)
    return {"subtotal": before_tax, "gst": gst, "total": before_tax + gst}



add_product("Notebook", 100, 3)
add_product("Bag", 800, 1)
print(generate_invoice("SAVE10"))
