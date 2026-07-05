def build_greeting(name, background):
    return f"hello, {name}. i bet you are an amazing {background}."


def main():
    name = input("What is your name?")
    background = input("what is your profession?")
    greeting = build_greeting(name, background)
    print(greeting)


if __name__ == "__main__":
    main()
