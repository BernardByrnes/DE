import csv

# students = []

# with open("students.csv", "r", encoding="utf-8") as file:
#     reader = csv.DictReader(file)

#     for row in reader:
#         students.append(row)

# print(students)

# for student in students:
#     print(
#         f"{student['name']} is learning {student['course']}."
#     )

# ================================================
# def main():
#     with open(
#         "students.csv", "r", encoding="utf-8"
#     ) as file:
#         contents = file.read()

#     print(contents)


# if __name__ == "__main__":
#     main()
# ================================================
def main():
    with open(
        "students.csv", "r", encoding="utf-8"
    ) as file:
        contents = csv.DictReader(file)

        for row in contents:
            print(row)


if __name__ == "__main__":
    main()
