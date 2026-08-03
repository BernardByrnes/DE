import csv


def read_file(file_path="teachers.csv"):
    teachers = []
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            teachers.append(row)
    return teachers


def main():
    teachers = read_file("teachers.csv")
    print(teachers)


if __name__ == "__main__":
    main()
