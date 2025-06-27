# with open("names.csv") as file:
#     for line in sorted(file):
#         name, house = line.rstrip().split(",")
#         print(f"{name} lives in {house}")


# get sorted values of csv by sorting values by name of the student


students = []
with open("names.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)


def get_name(student):
    return student["name"]


# sorting dictionaries
for student in sorted(students, key=lambda studen: studen["name"]):
    # method 2: or we can create a special function for sort function to use them for sorting on specific key
    # for student in sorted(students, key=get_name, reverse=True):
    # method 3: alternatively we can use operator module "key=itemgetter("name")" in sort function to achive the same result
    print(f"{student['name']} lives in {student['house']}")


# one method

# students = []
# with open("names.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student = {"name": name, "house": house}
#         students.append(student)

# for student in students:
#     print(f"{student['name']} lives in {student['house']}")
