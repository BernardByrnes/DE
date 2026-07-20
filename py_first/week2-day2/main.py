def read_text(file_path="notes.txt"):
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()

    return text


def count_lines(text):
    lines = text.splitlines()
    return len(lines)


def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    return len(text)


def build_summary(file_path="notes.txt"):
    text = read_text(file_path)

    return {
        "file_path": file_path,
        "line_count": count_lines(text),
        "word_count": count_words(text),
        "character_count": count_characters(text),
    }


def print_summary(summary):
    print("")
    print("Word Counter Summary")
    print("--------------------")
    print(f"File: {summary['file_path']}")
    print(f"Lines: {summary['line_count']}")
    print(f"Words: {summary['word_count']}")
    print(f"Characters: {summary['character_count']}")


def main():
    summary = build_summary()
    hey = 3

    print_summary(summary)


if __name__ == "__main__":
    main()
