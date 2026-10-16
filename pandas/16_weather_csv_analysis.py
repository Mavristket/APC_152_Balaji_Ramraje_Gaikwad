"""
Program 16:
Dataset: weather.csv
Columns: Date, City, Temperature, Humidity, Rainfall

Problem Statement:
Read the CSV file and:
1. Find the maximum temperature.
2. Find the minimum temperature.
3. Calculate the average temperature.
4. Display records where temperature is above 35 deg C.
5. Calculate city-wise average temperature.
"""

import os
import pandas as pd

# Load CSV file relative to script location
csv_path = os.path.join(os.path.dirname(__file__), "weather.csv")
df = pd.read_csv(csv_path)

print("Weather Dataset Loaded Successfully:")
print(df)
print("-" * 65)

# 1. Find the maximum temperature
max_temp = df["Temperature"].max()
max_temp_row = df.loc[df["Temperature"].idxmax()]
print(f"1. Maximum Temperature: {max_temp}°C (in {max_temp_row['City']} on {max_temp_row['Date']})")

# 2. Find the minimum temperature
min_temp = df["Temperature"].min()
min_temp_row = df.loc[df["Temperature"].idxmin()]
print(f"2. Minimum Temperature: {min_temp}°C (in {min_temp_row['City']} on {min_temp_row['Date']})")

# 3. Calculate the average temperature
avg_temp = df["Temperature"].mean()
print(f"3. Overall Average Temperature: {avg_temp:.2f}°C")
print("-" * 65)

# 4. Display records where temperature is above 35 deg C
hot_days = df[df["Temperature"] > 35]
print("4. Records where temperature is above 35°C:")
print(hot_days)
print("-" * 65)

# 5. Calculate city-wise average temperature
city_avg_temp = df.groupby("City")["Temperature"].mean()
print("5. City-wise Average Temperature:")
for city, avg in city_avg_temp.items():
    print(f"   {city:<12}: {avg:.2f}°C")
