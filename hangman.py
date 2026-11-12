import random

WORDS = ("python", "computer", "science", "programming", "developer")
MAX_INCORRECT_GUESSES = 6


def choose_word() -> str:
    return random.choice(WORDS)


def display_word(secret_word: str, guessed_letters: set[str]) -> str:
    return " ".join(
        letter if letter in guessed_letters else "_"
        for letter in secret_word
    )


def is_valid_guess(guess: str) -> bool:
    # Allows single letters and whole-word guesses (ASCII letters only)
    return guess.isascii() and guess.isalpha()


def play_game(secret_word: str) -> bool:
    if not secret_word.isascii() or not secret_word.isalpha():
        raise ValueError("The secret word must contain letters only.")

    secret_word = secret_word.lower()
    guessed_letters: set[str] = set()
    guessed_words: set[str] = set()
    attempts_remaining = MAX_INCORRECT_GUESSES

    print("\nGuess the hidden word, one letter at a time (or guess the whole word)!")

    while attempts_remaining > 0 and not all(
        letter in guessed_letters for letter in secret_word
    ):
        print(f"\nWord: {display_word(secret_word, guessed_letters)}")
        print(f"Incorrect attempts remaining: {attempts_remaining}")

        if guessed_letters:
            print("Guessed letters: " + ", ".join(sorted(guessed_letters)))
        if guessed_words:
            print("Wrong words tried: " + ", ".join(sorted(guessed_words)))

        guess = input("Enter a letter or word: ").strip().lower()

        if not is_valid_guess(guess):
            print("Invalid input. Enter letters only.")
            continue

        if len(guess) == 1:
            if guess in guessed_letters:
                print("You already guessed that letter. Try another one.")
                continue

            guessed_letters.add(guess)

            if guess in secret_word:
                print("Correct guess!")
            else:
                attempts_remaining -= 1
                print("Sorry, that letter is not in the word.")
        else:
            if guess in guessed_words:
                print("You already tried that word. Try another one.")
                continue

            if guess == secret_word:
                guessed_letters.update(secret_word)
                print("Correct word guess!")
            else:
                guessed_words.add(guess)
                attempts_remaining -= 1
                print(f"Sorry, '{guess}' is not the correct word.")

    if all(letter in guessed_letters for letter in secret_word):
        print(f"\nYou win! The word was '{secret_word}'.")
        return True

    print(f"\nGame over! The word was '{secret_word}'.")
    return False


def ask_play_again() -> bool:
    while True:
        answer = input("\nWould you like to play again? (y/n): ").strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Please enter y or n.")


def main() -> None:
    print("========== HANGMAN GAME ==========")
    try:
        while True:
            play_game(choose_word())
            if not ask_play_again():
                break
    except (KeyboardInterrupt, EOFError):
        print()
    print("Thanks for playing!")


if __name__ == "__main__":
    main()