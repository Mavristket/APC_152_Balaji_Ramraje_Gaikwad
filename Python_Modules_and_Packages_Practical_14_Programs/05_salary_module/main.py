import salary
basic=float(input("Enter basic salary: "))
gross=salary.gross_salary(basic)
print("Gross Salary =",gross)
print("Deductions =",salary.deductions(gross))
print("Net Salary =",salary.net_salary(gross))
