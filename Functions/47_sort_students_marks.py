def sort_students(students):
    return sorted(students, key=lambda student: student[1])


print(sort_students([("Asha", 88), ("Ravi", 72), ("Mina", 95)]))
