"""
Program 4:
Create a dictionary containing:
- Patient ID
- Patient Name
- Age
- Disease
- Medical Charges

Convert the dictionary into a DataFrame and:
1. Display patients above 60 years.
2. Find the average medical charge.
3. Find the maximum medical charge.
4. Display patients whose medical charges are greater than Rs. 50,000.
"""

import pandas as pd

# Create patient dictionary
patient_data = {
    "Patient ID": [1001, 1002, 1003, 1004, 1005],
    "Patient Name": ["Ramesh Gupta", "Shanti Devi", "Arjun Kapoor", "Leela Roy", "Suresh Raina"],
    "Age": [65, 72, 35, 68, 54],
    "Disease": ["Diabetes", "Hypertension", "Asthma", "Arthritis", "Diabetes"],
    "Medical Charges": [45000, 58000, 22000, 64000, 38000]
}

# Convert to DataFrame
df = pd.DataFrame(patient_data)
print("Patient DataFrame:\n", df)
print("-" * 65)

# 1. Display patients above 60 years
seniors = df[df["Age"] > 60]
print("1. Patients above 60 years:\n", seniors)
print("-" * 65)

# 2. Find the average medical charge
avg_charge = df["Medical Charges"].mean()
print(f"2. Average Medical Charge: Rs. {avg_charge:,.2f}")
print("-" * 65)

# 3. Find the maximum medical charge
max_charge = df["Medical Charges"].max()
print(f"3. Maximum Medical Charge: Rs. {max_charge:,.2f}")
print("-" * 65)

# 4. Display patients whose medical charges are greater than 50,000
high_charge_patients = df[df["Medical Charges"] > 50000]
print("4. Patients with Medical Charges > Rs. 50,000:\n", high_charge_patients)
