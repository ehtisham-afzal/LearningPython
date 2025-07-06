# @properties and decorators
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    @property  # Getter function
    def name(self):
        return self._name

    @name.setter  # Setter function
    def name(self, name):
        if not name:
            raise ValueError("Missing Name")
        self._name = name

    @property  # Getter function
    def house(self):
        return self._house

    @house.setter  # Setter function
    def house(self, house):
        if house not in ["khanpalow", "allahdhand", "islamabad"]:
            raise ValueError("Invalid house name ")
        self._house = house


def main():
    student = get_student()
    print(student)


def get_student():
    name = input("Name ")
    house = input("House ")
    return Student(name, house)


if __name__ == "__main__":
    main()
