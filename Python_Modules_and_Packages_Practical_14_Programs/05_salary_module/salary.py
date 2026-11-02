def gross_salary(basic): return basic + basic*.20 + basic*.10
def deductions(gross): return gross*.10
def net_salary(gross): return gross-deductions(gross)
