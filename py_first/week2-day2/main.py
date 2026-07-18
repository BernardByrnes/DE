def read_text(file_path="notes.txt"):
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()

    return text

def count_lines(text):
    lines = text.splitlines()
    return len(lines)

def

def main():
    summary = build_summary()

    print_summary(summary)


if __name__ == "__main__":
    main()
