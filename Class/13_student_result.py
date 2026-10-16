class StudentResult:
    def __init__(self, student_name, marks):
        self.student_name = student_name
        self.marks = marks  # list of marks in five subjects

    def total(self):
        return sum(self.marks)

    def percentage(self):
        return self.total() / 5  # each subject is out of 100

    def grade(self):
        percent = self.percentage()
        if percent >= 90:
            return "A+"
        elif percent >= 80:
            return "A"
        elif percent >= 70:
            return "B"
        elif percent >= 60:
            return "C"
        elif percent >= 40:
            return "D"
        else:
            return "Fail"

    def display(self):
        print("Student Name:", self.student_name)
        print("Marks:", self.marks)
        print("Total Marks:", self.total(), "/ 500")
        print("Percentage:", self.percentage(), "%")
        print("Grade:", self.grade())

    def __del__(self):
        print("Student result object destroyed.")


name = input("Enter student name: ")
marks = []
for i in range(1, 6):
    mark = float(input("Enter marks for subject " + str(i) + " (out of 100): "))
    marks.append(mark)

if all(0 <= mark <= 100 for mark in marks):
    result = StudentResult(name, marks)
    result.display()
    del result
else:
    print("Marks must be between 0 and 100.")
