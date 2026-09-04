def sort_employees(employees):
    return sorted(employees, key=lambda employee: employee[1])


print(sort_employees([("Asha", 65000), ("Ravi", 45000), ("Mina", 72000)]))
