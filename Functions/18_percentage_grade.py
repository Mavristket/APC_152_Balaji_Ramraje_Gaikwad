def percentage_and_grade(*marks):
    if len(marks) != 5:
        raise ValueError("exactly five marks are required")

    percentage = sum(marks) / 5
    if percentage >= 90:
        grade = "A"
    elif percentage >= 75:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 40:
        grade = "D"
    else:
        grade = "F"
    return percentage, grade


print(percentage_and_grade(85, 78, 92, 88, 90))
