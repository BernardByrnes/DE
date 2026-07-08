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
    guesses = []
    player_name = input("What is your name? ")

    print("Number Guessing Game")
    print("-------------------------")
    print("Guess a number between 1 and 10")

    while guess != secret_number:
        guess_text = input("Enter Your Guess: ")
        guess = int(guess_text)
        guesses.append(guess)
        attempts = attempts + 1
        hint = get_hint(guess, secret_number)
        print(hint)
    summary = {
        "player_name": player_name,
        "secret_number": secret_number,
        "attempts": attempts,
        "result": "won",
    }
    print(f"You guessed the number in {attempts} attempts.")
    print("Guess History")

    for previous_guess in guesses:
        print(f"- {previous_guess}")


if __name__ == "__main__":
    main()
