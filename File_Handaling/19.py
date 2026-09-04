import csv

file_name = "attendance.csv"

with open(file_name, "r", newline="") as file:
    students = list(csv.DictReader(file))

for student in students:
    present = int(student["PresentDays"])
    total = int(student["TotalDays"])
    percentage = present / total * 100
    print(student["RollNo"], student["Name"], f"{percentage:.2f}%")
    if percentage < 75:
        print("Below 75% attendance")
