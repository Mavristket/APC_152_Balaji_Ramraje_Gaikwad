
student_marks = {}


print("Enter details for 5 students:")
for i in range(1, 6):
    name = input(f"Enter name of student {i}: ")
    marks = float(input(f"Enter marks of student {i}: "))
    student_marks[name] = marks

print("\nStored Student Marks:", student_marks)
