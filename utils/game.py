import random


class Hangman:

    possible_words = ["becode", "learning", "mathematics", "sessions"]

    def __init__(self):
        self.word = random.choice(Hangman.possible_words)
        self.word_to_find = list(self.word)
        self.word_to_find_upper = [letter_l.upper() for letter_l in self.word_to_find]
        self.lives = 5
        self.correctly_guessed_letters = ['_'] * len(self.word_to_find)
        self.wrongly_guessed_letters = []
        self.turn_count = 0
        self.error_count = 0

    def play(self):
        print(self.correctly_guessed_letters)
        print("Enter a letter please")
        letter = input()
        self.turn_count += 1
        if letter.isalpha() and len(letter) == 1:
            if letter in self.word_to_find:
                for i, character in list(enumerate(self.word_to_find, 0)):
                    if character == letter:
                        self.correctly_guessed_letters[i] = letter.upper()
                        print(f"Correct! This is letter number {i}")
            else:
                self.wrongly_guessed_letters.append(letter)
                self.error_count += 1
                self.lives -= 1
                print("Incorrect letter!")

    def game_over(self):
        print("Game over...")

    def well_played(self):
        print(f"You find the wold: {self.word}")

    def start_game(self):

        while True:
            self.play()
            print("________________________________")
            print(f"You chose incorrect letters: {self.wrongly_guessed_letters}")
            print(f"Your have turn_count: {self.turn_count}")
            print(f"Your have error: {self.error_count}")
            print(f"Your have lives: {self.lives}")
            print("________________________________________________________________")
            if self.lives == 0: 
                self.game_over()
                break
            if self.correctly_guessed_letters == self.word_to_find_upper:
                self.well_played() 
                break
