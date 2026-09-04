import csv
import os

file_name = "employees.csv"

if not os.path.exists(file_name):
    with open(file_name, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["EmployeeID", "Name", "Department", "Salary"])
        writer.writerows([
            [1, "Anil", "Sales", 35000],
            [2, "Meena", "IT", 55000],
            [3, "Ravi", "HR", 42000],
        ])


def read_employees():
    with open(file_name, "r", newline="") as file:
        return list(csv.DictReader(file))


def display_all(employees):
    for employee in employees:
        print(employee)


def highest_paid(employees):
    return max(employees, key=lambda employee: float(employee["Salary"]))


def average_salary(employees):
    return sum(float(employee["Salary"]) for employee in employees) / len(employees)


employees = read_employees()
print("All employees:")
display_all(employees)
print("Highest-paid employee:", highest_paid(employees))
print("Average salary:", average_salary(employees))

limit = float(input("Enter salary limit: "))
print("Employees earning above the limit:")
for employee in employees:
    if float(employee["Salary"]) > limit:
        print(employee)
