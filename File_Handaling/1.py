name = input("Enter student name: ")
roll_no = input("Enter roll number: ")
branch = input("Enter branch: ")
semester = input("Enter semester: ")

with open("student.txt", "w") as file:
    file.write(f"Name: {name}\n")
    file.write(f"Roll number: {roll_no}\n")
    file.write(f"Branch: {branch}\n")
    file.write(f"Semester: {semester}\n")

print("Student details saved in student.txt")
