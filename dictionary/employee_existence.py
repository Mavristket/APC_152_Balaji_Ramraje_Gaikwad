
employees = {
    "E101": "Amit",
    "E102": "Bina",
    "E103": "Chirag",
    "E104": "Divya"
}


search_id = input("Enter Employee ID to search: ")


if search_id in employees:
    print(f"Employee found: {employees[search_id]}")
else:
    print("Employee ID does not exist.")
