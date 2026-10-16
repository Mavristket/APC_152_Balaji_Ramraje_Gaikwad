"""
Program 3:
Create a dictionary containing:
- Product ID
- Product Name
- Category
- Price
- Quantity

Convert it into a DataFrame.
Calculate:
Total Amount = Price * Quantity
Then find the product having the highest total sales.
"""

import pandas as pd

# Create dictionary containing product details
product_data = {
    "Product ID": ["P01", "P02", "P03", "P04", "P05"],
    "Product Name": ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones"],
    "Category": ["Electronics", "Accessories", "Accessories", "Electronics", "Audio"],
    "Price": [55000, 800, 1500, 12000, 2500],
    "Quantity": [4, 25, 15, 6, 18]
}

# Convert to DataFrame
df = pd.DataFrame(product_data)

# Calculate Total Amount = Price * Quantity
df["Total Amount"] = df["Price"] * df["Quantity"]

print("Product DataFrame with Total Amount:\n", df)
print("-" * 65)

# Find the product having the highest total sales
highest_sales_product = df.loc[df["Total Amount"].idxmax()]
print("Product with the highest total sales:")
print(f"Product ID   : {highest_sales_product['Product ID']}")
print(f"Product Name : {highest_sales_product['Product Name']}")
print(f"Total Sales  : Rs. {highest_sales_product['Total Amount']:,}")
