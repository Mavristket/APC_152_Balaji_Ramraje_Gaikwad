
python_students = {"Alice", "Bob", "Charlie", "David"}
java_students = {"Charlie", "David", "Emma", "Frank"}

both_courses = python_students.intersection(java_students)

only_one_course = python_students.symmetric_difference(java_students)


print("Students enrolled in both Python and Java:", both_courses)
print("Students enrolled in only one course:", only_one_course)
