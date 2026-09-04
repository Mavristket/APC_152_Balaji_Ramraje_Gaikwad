import csv
import os

file_name = "student_records.csv"

if not os.path.exists(file_name):
    with open(file_name, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["RollNo", "Name", "Marks"])
        writer.writerows([
            [101, "Amit", 85],
            [102, "Priya", 92],
            [103, "Rahul", 78],
        ])

with open(file_name, "r", newline="") as file:
    records = list(csv.DictReader(file))

print("All records:")
for record in records:
    print(record["RollNo"], record["Name"], record["Marks"])

highest = max(records, key=lambda record: int(record["Marks"]))
average = sum(int(record["Marks"]) for record in records) / len(records)

print("Highest marks:", highest["Name"])
print("Average marks:", average)
print("Students scoring more than 80:")
for record in records:
    if int(record["Marks"]) > 80:
        print(record["Name"])
