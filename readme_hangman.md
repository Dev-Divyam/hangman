# CodeAlpha Project: Hangman Game

A beginner-friendly, text-based Hangman game built with Python's standard library.

## Features

- Selects a random word from five predefined words.
- Accepts one English letter per guess.
- Allows up to six incorrect guesses.
- Shows correctly guessed letters and previously guessed letters.
- Rejects empty input, numbers, multiple letters, and repeated guesses without using an attempt.
- Announces a win or loss and reveals the word when the round ends.

## Requirements

- Python 3.9 or newer.

## Run the game

From this folder, run:

```bash
python hangman.py
```

On some systems, use `python3 hangman.py` instead.

## Run the tests

```bash
python -m unittest discover -s tests -v
```

The tests cover word selection, masked display, input validation, winning, losing, and invalid/repeated guesses.
