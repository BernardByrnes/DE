def get_hint(guess, secret_number):
    if guess < secret_number:
        return "Too low Bro"
    elif guess > secret_number:
        return "Too high Bro"
    else:
        return "Correct"


def print_guess_history(guesses):
    print("")
    print("Guess History")
    print("-------------")

    for previous_guess in guesses:
        print(f"-{previous_guess}")


def print_summary(summary):
    print("")
    print("Game Summary")
    print("------------")
    print(f"Player: {summary['player_name']}")
    print(f"Secret number: {summary['secret_number']}")
    print(f"Attempts: {summary['attempts']}")
    print(
        f"Range: {summary['minimum_guess']} to {summary['maximum_guess']}"
    )
    print(f"Performance: {summary['performance']}")
    print(f"Result: {summary['result']}")


def main():
    secret_number = 7
    guess = 0
    attempts = 0
    minimum_guess = 1
    maximum_guess = 10
    guesses = []
    performance = ""
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

    if attempts <= 2:
        performance = "fast"
    elif attempts <= 4:
        performance = "steady"
    else:
        performance = "persistent"

    summary = {
        "player_name": player_name,
        "secret_number": secret_number,
        "attempts": attempts,
        "result": "won",
        "minimum_guess": minimum_guess,
        "maximum_guess": maximum_guess,
        "performance": performance,
    }
    print_guess_history(guesses)
    print_summary(summary)

    for previous_guess in guesses:
        print(f"- {previous_guess}")


if __name__ == "__main__":
    main()
