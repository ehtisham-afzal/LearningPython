# Returning string value with __str__ method
class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing Name")
        if house not in ["khanpalow", "allahdhand", "islamabad"]:
            raise ValueError("Invalid house name ")
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"


def main():
    print(get_student())


def get_student():
    name = input("Name ")
    house = input("House ")
    return Student(name, house)


# --------------------------------------------------------------------------------------------- #


# error raising and handling on classes
# class Student:
#     def __init__(self, name, house):
#         if not name:
#             raise ValueError("Missing Name")
#         self.name = name
#         if house not in ["khanpalow", "allahdhand","islamabad"]:
#             raise ValueError("Invalid house name ")
#         self.house = house


# def main():
#     student = get_student()
#     print(f"{student.name} from {student.house}")


# def get_student():
#     name = input("Name ")
#     house = input("House ")
#     student = Student(name, house)
#     return student


# --------------------------------------------------------------------------------------------- #

# with class instance method
# class Student:
#     def __init__(self, name, house):
#         self.name = name
#         self.house = house


# def main():
#     student = get_student()
#     print(f"{student.name} from {student.house}")


# def get_student():
#     name = input("Name ")
#     house = input("House ")
#     student = Student(name, house)
#     return student

# --------------------------------------------------------------------------------------------- #


# class method
# class Student: ...


# def main():
#     student = get_student()
#     print(f"{student.name} from {student.house}")


# def get_student():
#     student = Student()
#     student.name = input("Name ")
#     student.house = input("House ")
#     return student


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #


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
