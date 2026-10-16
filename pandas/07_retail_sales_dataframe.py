"""
Program 7:
A retail shop maintains sales information in a Python dictionary containing:
Product_ID, Product_Name, Category, Price, and Quantity.

Write a Python program to:
1. Convert the dictionary into a Pandas DataFrame.
2. Add a new column Total_Sales.
3. Calculate the total sales using Price * Quantity.
4. Display products with sales greater than Rs. 10,000.
5. Find the product with maximum sales.
6. Calculate the average sales.
"""

import pandas as pd

# Retail shop sales data dictionary
sales_data = {
    "Product_ID": [501, 502, 503, 504, 505],
    "Product_Name": ["Desk Chair", "Wireless Mouse", "Office Desk", "USB Cable", "LED Lamp"],
    "Category": ["Furniture", "Electronics", "Furniture", "Accessories", "Electronics"],
    "Price": [4500, 750, 12000, 250, 1500],
    "Quantity": [3, 20, 2, 30, 8]
}

# 1. Convert dictionary into Pandas DataFrame
df = pd.DataFrame(sales_data)
print("1. Initial Sales DataFrame:\n", df)
print("-" * 65)

# 2 & 3. Add column Total_Sales using Price * Quantity
df["Total_Sales"] = df["Price"] * df["Quantity"]
print("2 & 3. DataFrame with Total_Sales:\n", df)
print("-" * 65)

# 4. Display products with sales greater than 10,000
high_sales = df[df["Total_Sales"] > 10000]
print("4. Products with sales > Rs. 10,000:\n", high_sales)
print("-" * 65)

# 5. Find the product with maximum sales
max_product = df.loc[df["Total_Sales"].idxmax()]
print("5. Product with Maximum Sales:")
print(f"   Product ID   : {max_product['Product_ID']}")
print(f"   Product Name : {max_product['Product_Name']}")
print(f"   Total Sales  : Rs. {max_product['Total_Sales']:,}")
print("-" * 65)

# 6. Calculate the average sales
avg_sales = df["Total_Sales"].mean()
print(f"6. Average Sales: Rs. {avg_sales:,.2f}")
