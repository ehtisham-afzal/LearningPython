students = ["ehtisham", "zeeshan", "sanan", "muattart gull", "khan"]

# print(students[0])

for student in students:
    print(student)

# print name of students who's name is greater than 5 character using list comprehensions
print([student for student in students if len(student) > 5])
