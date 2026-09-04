def grade_from_percentage(percentage):
    if percentage >= 90:
        return "A"
    if percentage >= 75:
        return "B"
    if percentage >= 60:
        return "C"
    if percentage >= 40:
        return "D"
    return "F"


def process_student(student):
    marks = student["marks"]
    total = sum(marks)
    percentage = total / 5
    return {
        "name": student["name"],
        "roll_number": student["roll_number"],
        "total": total,
        "percentage": percentage,
        "grade": grade_from_percentage(percentage),
    }


def process_students(students):
    records = [process_student(student) for student in students]
    percentages = [record["percentage"] for record in records]
    return {
        "records": records,
        "class_average": sum(percentages) / len(percentages),
        "highest_scorer": max(records, key=lambda record: record["percentage"]),
        "lowest_scorer": min(records, key=lambda record: record["percentage"]),
    }



    students = [
        {"name": "Asha", "roll_number": 1, "marks": [85, 90, 78, 88, 92]},
        {"name": "Ravi", "roll_number": 2, "marks": [72, 80, 75, 69, 77]},
    ]
    print(process_students(students))
