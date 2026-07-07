def main():
    secret_number = 7
    guess_text = input("Guess a number between 1 and 10: ")
    guess = int(guess_text)
    print(f"You guessed {guess}")

if __name__ == "__main__":
    main()
