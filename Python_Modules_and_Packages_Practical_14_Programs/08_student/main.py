from student.marks import *
from student.grade import calculate_grade
from student.attendance import eligibility
name=input("Enter name: "); marks=[float(input("Enter marks: ")) for i in range(5)]
present=int(input("Classes attended: ")); total_classes=int(input("Total classes: "))
p=percentage(marks); att,ok=eligibility(present,total_classes)
print("Name =",name); print("Total =",total(marks)); print("Percentage =",p)
print("Grade =",calculate_grade(p)); print("Attendance =",att,"%"); print("Eligible =",ok)
