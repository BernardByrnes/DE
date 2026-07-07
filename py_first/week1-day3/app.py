def get_hint(guess, secret_number):
    if guess < secret_number:
        return "Too low Bro"
    elif guess > secret_number:
        return "Too high Bro"
    else:
        return "Correct"


def main():
    secret_number = 7
    guess = 0
    attempts = 0

    print("Number Guessing Game")
    print("-------------------------")
    print("Guess a number between 1 and 10")

    while guess != secret_number:
        guess_text = input("Enter Your Guess: ")
        guess = int(guess_text)
        attempts = attempts + 1
        hint = get_hint(guess, secret_number)
        print(hint)


if __name__ == "__main__":
    main()
