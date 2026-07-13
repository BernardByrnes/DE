import csv

students = []

with open("students.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        students.append(row)


print(students[1]["name"])
