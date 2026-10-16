"""
Program 11:
Create a Pandas Series using a dictionary where patient IDs are the index
and patient ages are the values.
Perform:
- Find the average age.
- Find the oldest patient.
- Find the youngest patient.
- Display patients above 60 years.
"""

import pandas as pd

# Dictionary with Patient ID as key and age as value
patient_ages = {
    "P101": 65,
    "P102": 72,
    "P103": 35,
    "P104": 68,
    "P105": 54,
    "P106": 29,
    "P107": 75,
    "P108": 48
}

# Create Pandas Series
series = pd.Series(patient_ages)

print("Patient Age Series (Index = Patient ID, Value = Age):")
print(series)
print("-" * 50)

# 1. Find the average age
print(f"1. Average Age  : {series.mean():.2f} years")

# 2. Find the oldest patient
print(f"2. Oldest Patient  : ID {series.idxmax()} (Age: {series.max()})")

# 3. Find the youngest patient
print(f"3. Youngest Patient: ID {series.idxmin()} (Age: {series.min()})")
print("-" * 50)

# 4. Display patients above 60 years
seniors = series[series > 60]
print("4. Patients above 60 years:")
print(seniors)
