"""
Program 5:
Create a dictionary containing:
- Order_ID
- Customer
- Product
- Quantity
- Price
- Discount

Create a DataFrame and calculate:
Final Amount = Quantity * Price - Discount

Then display:
- All orders
- Orders above Rs. 5,000
- Highest-value order
- Average order value
"""

import pandas as pd

# Create dictionary containing orders
order_data = {
    "Order_ID": ["ORD01", "ORD02", "ORD03", "ORD04", "ORD05"],
    "Customer": ["Amit", "Bhavna", "Chirag", "Deepika", "Eshan"],
    "Product": ["Smartphone", "Power Bank", "Smartwatch", "Earbuds", "Tablet"],
    "Quantity": [1, 2, 2, 3, 1],
    "Price": [18000, 1500, 3500, 1200, 15000],
    "Discount": [1000, 200, 500, 300, 1500]
}

# Create DataFrame
df = pd.DataFrame(order_data)

# Calculate Final Amount = Quantity * Price - Discount
df["Final Amount"] = (df["Quantity"] * df["Price"]) - df["Discount"]

# Display all orders
print("1. All Orders:\n", df)
print("-" * 65)

# Orders above 5,000
high_orders = df[df["Final Amount"] > 5000]
print("2. Orders above Rs. 5,000:\n", high_orders)
print("-" * 65)

# Highest-value order
highest_order = df.loc[df["Final Amount"].idxmax()]
print("3. Highest-Value Order:")
print(f"   Order ID     : {highest_order['Order_ID']}")
print(f"   Customer     : {highest_order['Customer']}")
print(f"   Product      : {highest_order['Product']}")
print(f"   Final Amount : Rs. {highest_order['Final Amount']:,}")
print("-" * 65)

# Average order value
avg_order_value = df["Final Amount"].mean()
print(f"4. Average Order Value: Rs. {avg_order_value:,.2f}")
