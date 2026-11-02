from ecommerce.Products.product import add_product
from ecommerce.Products.catalog import show_product
from ecommerce.Customers.customer import add_customer
from ecommerce.Customers.profile import show_customer
from ecommerce.Orders.order import create_order
from ecommerce.Orders.status import order_status
from ecommerce.Payments.payment import make_payment
from ecommerce.Payments.method import payment_method
p=add_product("Laptop",50000); c=add_customer("Amit","amit@gmail.com")
print("Product:"); show_product(p); print("Customer:"); show_customer(c)
print("Order:",create_order(p,1)); print(order_status()); print(payment_method()); make_payment(50000)
