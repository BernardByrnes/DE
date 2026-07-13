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
    print("--------")

    for student in students:
        print(
            f"{student['name']} is learning {student['course']}"
            f"and has grade {student['grade']}"
        )


def print_record_count(students):
    print(f"Records read: {len(students)}")


def main():
    file_path = "students.csv"
    students = read_students(file_path)
    print_record_count(students)
    print_students(students)


if __name__ == "__main__":
    main()
