def get_hint(guess, secret_number):
    if guess < secret_number:
        return "Too low Bro"
    elif guess > secret_number:
        return "Too high Bro"
    else:
        return "Correct"


def main():
    secret_number = 7

    guess_text = input("Guess a number between 1 and 10: ")
    guess = int(guess_text)

    hint = get_hint(guess, secret_number)
    print(hint)


if __name__ == "__main__":
    main()
