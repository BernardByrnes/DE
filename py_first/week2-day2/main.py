def read_text(file_path="notes.txt"):
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()

    return text


def main():
    text = read_text()

    print(text)


if __name__ == "__main__":
    main()
