import csv


def read_file(file_path="teachers.csv"):
    teachers = []
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            teachers.append(row)
    return teachers


def print_list(teachers):
    print(" ")
    print("teachers")
    print("----------------------")

    for teacher in teachers:
        print(
            f"my name is {teacher['name']}, i teach {teacher['subject']}, i have {teacher['students']} students in my class"
        )


def main():
    teachers = read_file("teachers.csv")
    print_list(teachers)


if __name__ == "__main__":
    main()
