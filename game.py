#!/usr/bin/env python3

from utils import get_random_word

class HangmanGame():
    
    def __init__(self):
        self.word = get_random_word()
        self.guessed_letters = []
        self.incorrect_letters = []
        self.max_errors = 6
        self.errors = 0

    @property
    def word(self):
        return self.__word
    
    @word.setter
    def word(self, word):
        self.__word = word

    @property
    def guessed_letters(self):
        return self.__guessed_letters
    
    @guessed_letters.setter
    def guessed_letters(self, guessed_letters):
        self.__guessed_letters = guessed_letters

    @property
    def max_errors(self):
        return self.__max_errors

    @max_errors.setter
    def max_errors(self, max_errors):
        self.__max_errors = max_errors

    @property
    def errors(self):
        return self.__errors
    
    @errors.setter
    def errors(self, errors):
        self.__errors = errors

    def display_progress(self, progress):

        try:
            for letter in progress:
                print(letter, end=" ")
            print()

        except IndexError:
            print("La lista proporcionada se encuentra vacia")

    def process_guess(self, letter):
        if letter in self.word:
            self.guessed_letters.append(letter)
            return True
        else:
            self.errors += 1
            self.incorrect_letters.append(letter)
            print("La letra ingresada es incorrecta")
            return False

if __name__ == "__main__":
    prueba = HangmanGame()

    prueba.display_progress(prueba.word)