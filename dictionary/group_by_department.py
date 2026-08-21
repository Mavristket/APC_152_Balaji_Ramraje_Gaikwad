
students_dept = {
    "Alice": "Computer Science",
    "Bob": "Electrical",
    "Charlie": "Computer Science",
    "David": "Mechanical",
    "Emma": "Electrical"
}
print("Original dictionary:", students_dept)


grouped = {}
for student, dept in students_dept.items():
    if dept not in grouped:
        grouped[dept] = []
    grouped[dept].append(student)


print("Grouped by department:", grouped)
