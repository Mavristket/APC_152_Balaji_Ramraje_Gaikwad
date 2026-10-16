"""
Program 10:
Create a Pandas Series using a dictionary containing product names and prices.
Perform:
- Display all products and prices.
- Increase every price by 10%.
- Find the most expensive product.
- Find products costing more than Rs. 1,000.
"""

import pandas as pd

# Dictionary containing product names and prices
products_dict = {
    "Wireless Mouse": 650.0,
    "Mechanical Keyboard": 2500.0,
    "USB Flash Drive": 450.0,
    "Gaming Headset": 3200.0,
    "Webcam HD": 1800.0,
    "Mousepad": 300.0
}

# Create Pandas Series
series = pd.Series(products_dict)

# 1. Display all products and prices
print("1. Original Product Prices:")
print(series)
print("-" * 50)

# 2. Increase every price by 10%
increased_prices = series * 1.10
print("2. Product Prices after 10% Increase:")
print(increased_prices.round(2))
print("-" * 50)

# 3. Find the most expensive product
most_expensive_product = series.idxmax()
print(f"3. Most Expensive Product: {most_expensive_product} (Rs. {series.max():,})")
print("-" * 50)

# 4. Find products costing more than 1,000
expensive_products = series[series > 1000]
print("4. Products costing more than Rs. 1,000:")
print(expensive_products)
