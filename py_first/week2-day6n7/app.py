import csv


def read_file(file_path="teachers.csv"):
    teachers = []
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            teachers.append(row)
    return teachers


def print_list(teachers):
    number_of_records = 0
    print(" ")
    print("teachers")
    print("----------------------")

    for teacher in teachers:
        number_of_records = number_of_records + 1
        print(
            f"my name is {teacher['name']}, i teach {teacher['subject']}, i have {teacher['students']} students in my class"
        )
    print(
        f"there is a total of {number_of_records} teachers"
    )


def main():
    teachers = read_file("teachers.csv")
    print_list(teachers)


if __name__ == "__main__":
    main()
