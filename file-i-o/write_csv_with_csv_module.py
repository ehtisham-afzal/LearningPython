import csv

name = input("Whats your name ")
home = input("Where's your home ")

with open("names_and_home.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})
