import csv


def read_students(file_path):
    students = []

    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            students.append(row)

    return students


def print_students(students):
    print("")
    print("Students")
    print("----------")

    for student in students:
        print(
            f"my name is {student['name']} i am doing {student['course']}"
            f" i got {student['grade']}"
        )


def print_student_count(students):
    print(
        f"there are {len(students)} students in the class"
    )


def main():
    file_path = "students.csv"
    students = read_students(file_path)
    print_students(students)
    print_student_count(students)


if __name__ == "__main__":
    main()
