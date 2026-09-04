def average_marks(students):
    return sum(student[1] for student in students) / len(students)


def above_75(students):
    return list(filter(lambda student: student[1] > 75, students))


def sort_by_marks(students):
    return sorted(students, key=lambda student: student[1])


students = [("Asha", 88), ("Ravi", 72), ("Mina", 95)]
print(average_marks(students))
print(above_75(students))
print(sort_by_marks(students))
