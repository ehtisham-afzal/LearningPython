import csv

students = []
with open("names_and_home.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append(
            {"name": row["name"], "home": row["home"], "house": row["house"]}
        )


for student in students:
    print(
        f"{student['name']} is from {student['home']} and lives on {student['house']}"
    )
