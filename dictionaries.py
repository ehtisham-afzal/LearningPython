def dictionary():
    students = {
        "Hermione": "Graffindore",
        "Harry": "Graffindore",
        "Draco": "Graffindore",
        "Ron": "Slythenren",
    }

    for student in students:
        print(student, students[student], sep=", ")


def list_of_dictionaries():
    students = [
        {"name": "Hermione", "house": "Graffindore", "patrounus": "otter"},
        {"name": "Harry", "house": "Stag", "patrounus": "otter"},
        {"name": "Rone", "house": "Jack russel terrior", "patrounus": "otter"},
        {"name": "Draco", "house": "Slytherin", "patrounus": None},
    ]

    for student in students:
        print(
            f"the name of student is {student['name']} living on {student['house']} and has {student['patrounus']} patrounus"
        )


# dictionary()
list_of_dictionaries()
