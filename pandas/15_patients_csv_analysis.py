"""
Program 15:
Dataset: patients.csv
Columns: Patient_ID, Name, Age, Gender, Disease, Medical_Expense

Problem Statement:
Read the CSV file and:
1. Display patients above 60 years.
2. Calculate average medical expense.
3. Find the patient with the highest medical expense.
4. Count patients for each disease.
5. Display patients whose medical expense exceeds Rs. 50,000.
"""

import os
import pandas as pd

# Load CSV file relative to script location
csv_path = os.path.join(os.path.dirname(__file__), "patients.csv")
df = pd.read_csv(csv_path)

print("Patients Dataset Loaded Successfully:")
print(df)
print("-" * 65)

# 1. Display patients above 60 years
seniors = df[df["Age"] > 60]
print("1. Patients above 60 years:")
print(seniors[["Patient_ID", "Name", "Age", "Disease", "Medical_Expense"]])
print("-" * 65)

# 2. Calculate average medical expense
avg_expense = df["Medical_Expense"].mean()
print(f"2. Average Medical Expense: Rs. {avg_expense:,.2f}")
print("-" * 65)

# 3. Find the patient with the highest medical expense
top_expense_patient = df.loc[df["Medical_Expense"].idxmax()]
print("3. Patient with the highest medical expense:")
print(f"   Name: {top_expense_patient['Name']} (ID: {top_expense_patient['Patient_ID']})")
print(f"   Expense: Rs. {top_expense_patient['Medical_Expense']:,} (Disease: {top_expense_patient['Disease']})")
print("-" * 65)

# 4. Count patients for each disease
disease_counts = df["Disease"].value_counts()
print("4. Count of patients for each disease:")
for disease, count in disease_counts.items():
    print(f"   {disease:<16}: {count}")
print("-" * 65)

# 5. Display patients whose medical expense exceeds 50,000
high_expense_patients = df[df["Medical_Expense"] > 50000]
print("5. Patients whose medical expense exceeds Rs. 50,000:")
print(high_expense_patients[["Patient_ID", "Name", "Disease", "Medical_Expense"]])
