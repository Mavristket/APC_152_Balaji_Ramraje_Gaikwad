class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks  # marks out of 100

    def percentage(self):
        return self.marks

    def display(self):
        print("Roll No:", self.roll_no)
        print("Name:", self.name)
        print("Marks:", self.marks, "/ 100")
        print("Percentage:", self.percentage(), "%")
        print()


students = [
    Student(1, "Amit", 85),
    Student(2, "Priya", 92),
    Student(3, "Rahul", 78)
]

for student in students:
    student.display()
