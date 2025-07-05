# class method


class Student: ...


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")


def get_student():
    student = Student
    student.name = input("Name ")
    student.house = input("House ")
    return student


# Dictionry method
# def main():
#     student = get_student()
#     if student["name"] == "ehtisham":
#         student["house"] = "Khanpalow"
#     print(f"{student['name']} from {student['house']}")


# def get_student():
#     student = {}
#     student["name"] = input("Name ")
#     student["house"] = input("House ")
#     return student


# List Method

# def main():
#     student = get_student()
#     if student[0] == "ehtisham":
#         student[1] = "Khanpalow"
#     print(f"{student[0]} from {student[1]}")


# def get_student():
#     name = input("Name ")
#     house = input("House ")
#     return [name, house]


# tubles Method
# def main():
#     student = get_student()
#     # this will return TypeError: 'tuple' object does not support item assignment
#     # if student[0]:
#     #     student[1] = "Khanplalow"
#     print(f"{student[0]} from {student[1]}")


# def get_student():
#     name = input("Name ")
#     house = input("House ")
#     return (name, house)


if __name__ == "__main__":
    main()
