def earning_more_than_50000(employees):
    return list(filter(lambda employee: employee[2] > 50000, employees))


def increase_salaries(employees):
    return list(map(lambda employee: (employee[0], employee[1], employee[2] * 1.10), employees))


def sort_by_salary(employees):
    return sorted(employees, key=lambda employee: employee[2])



employees = [("Asha", "IT", 65000), ("Ravi", "HR", 45000), ("Mina", "Sales", 72000)]
print(earning_more_than_50000(employees))
print(increase_salaries(employees))
print(sort_by_salary(employees))
