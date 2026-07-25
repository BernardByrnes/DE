import csv


def get_student():
    name = input("what is your name?: ")
    course = input("what course are u doing?: ")
    grade = input("what grade did u get?: ")

    return {"name": name, "course": course, "grade": grade}


def append_student(student):
    with open(
        "student2.csv", "a", encoding="utf-8", newline=""
    ) as file:
        writer = csv.Dictwriter(
            file, fieldnames=["name", "course", "grade"]
        )
        writer.writerow(student)


def read_students(file_path="students2.csv"):
    students = []
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            students.append(row)
    return students


def main():
    student = get_student()

    print(student)


if __name__ == "__main__":
    main()
