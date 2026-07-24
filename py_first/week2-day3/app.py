import csv

student = {"name": "Tiny", "course": "Rust", "grade": "99"}

with open(
    "students.csv", "a", encoding="utf-8", newline=""
) as file:
    writer = csv.DictWriter(
        file, fieldnames=["name", "course", "grade"]
    )
    writer.writerow(student)
