emp1_skills = {"Python", "SQL", "Git", "HTML"}
emp2_skills = {"SQL", "Java", "Docker", "Git"}


common_skills = emp1_skills.intersection(emp2_skills)


unique_emp1 = emp1_skills.difference(emp2_skills)

unique_emp2 = emp2_skills.difference(emp1_skills)


all_skills = emp1_skills.union(emp2_skills)


print("Employee 1 skills:", emp1_skills)
print("Employee 2 skills:", emp2_skills)
print("Common skills:", common_skills)
print("Skills unique to Employee 1:", unique_emp1)
print("Skills unique to Employee 2:", unique_emp2)
print("All available skills:", all_skills)
