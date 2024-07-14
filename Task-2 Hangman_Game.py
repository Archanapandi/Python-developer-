# hangman_game.py

import random

# Predefined words and phrases for the game
WORDS = [
    "python",
    "hangman",
    "game",
    "development",
    "fun",
    " coding",
    "challenge",
    "adventure"
]

# Hangman visual representation
HANGMAN_PICS = [
    """
    +---+
    |   |
            |
            |
            |
            |
    =========""",
    """
    +---+
    |   |
    O   |
            |
            |
            |
    =========""",
    """
    +---+
    |   |
    O   |
    |   |
            |
            |
    =========""",
    """
    +---+
    |   |
    O   |
   /|   |
            |
            |
    =========""",
    """
    +---+
    |   |
    O   |
   /|\  |
            |
            |
    =========""",
    """
    +---+
    |   |
    O   |
   /|\  |
   /    |
            |
    =========""",
    """
    +---+
    |   |
    O   |
   /|\  |
   / \  |
            |
    ========="""
]

class HangmanGame:
    def __init__(self):
        self.word = random.choice(WORDS)
        self.guessed_letters = []
        self.incorrect_guesses = 0
        self.max_attempts = len(HANGMAN_PICS) - 1

    def display_word(self):
        word_display = ""
        for letter in self.word:
            if letter in self.guessed_letters:
                word_display += letter
            else:
                word_display += "_"
        return word_display

    def guess_letter(self, letter):
        if letter in self.guessed_letters:
            print("You already guessed this letter!")
            return
        self.guessed_letters.append(letter)
        if letter not in self.word:
            self.incorrect_guesses += 1
            print("Incorrect guess!")
        else:
            print("Correct guess!")

    def display_hangman(self):
        print(HANGMAN_PICS[self.incorrect_guesses])

    def play(self):
        print("Welcome to Hangman!")
        while self.incorrect_guesses < self.max_attempts:
            print(self.display_word())
            self.display_hangman()
            print(f"Remaining attempts: {self.max_attempts - self.incorrect_guesses}")
            guess = input("Guess a letter: ").lower()
            if len(guess) != 1:
                print("Invalid input! Please enter a single letter.")
                continue
            self.guess_letter(guess)
            if all(letter in self.guessed_letters for letter in self.word):
                print("Congratulations! You won!")
                return
        print("Game over! The word was " + self.word)

if __name__ == "__main__":
    game = HangmanGame()
    game.play()