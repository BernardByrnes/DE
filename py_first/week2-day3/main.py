import csv


def get_student():
    name = input("Student name: ")
    course = input("Course: ")
    grade = input("Grade: ")

    return {"name": name, "course": course, "grade": grade}


def append_student(student):
    with open(
        "studentz.csv", "a", encoding="utf-8", newline=""
    ) as file:
        writer = csv.DictWriter(
            file, fieldnames=["name", "course", "grade"]
        )
        writer.writerow(student)


def read_students(file_path="students.csv"):
    students = []
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            students.append(row)
    return students


def print_students(students):
    print("")
    print("Students List")
    print("-------------------")

    for student in students:
        print(
            f"my name is{student['name']}, i am taking {student['name']}, i got {student['grade']}"
        )


def main():
    student = get_student()
    append_student(student)
    print("student saved")
    students = read_students("studentz.csv")
    print_students(students)


if __name__ == "__main__":
    main()
