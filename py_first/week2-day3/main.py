def get_student():
    name = input("Student name: ")
    course = input("Course: ")
    grade = input("Grade: ")

    return {"name": name, "course": course, "grade": grade}


def main():
    student = get_student()
    print(student)


if __name__ == "__main__":
    main()
