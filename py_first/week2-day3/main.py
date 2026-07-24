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


def main():
    student = get_student()
    append_student(student)
    print("student saved")


if __name__ == "__main__":
    main()
