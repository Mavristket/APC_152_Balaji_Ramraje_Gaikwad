import student
name = input("Enter student name: ")
marks = []
for i in range(5): marks.append(float(input("Enter marks: ")))
p = student.percentage(marks)
print("Name =", name)
print("Total =", student.total_marks(marks))
print("Percentage =", p)
print("Grade =", student.grade(p))
