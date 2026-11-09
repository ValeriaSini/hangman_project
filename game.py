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
            print("La lista proporcionada se encuentra vacía")

    def process_guess(self, letter):
        if letter in self.word:
            self.guessed_letters.append(letter)
            return True
        else:
            self.errors += 1
            self.incorrect_letters.append(letter)
            print("La letra ingresada es incorrecta")
            return False

    def mostrar_intentos(self):
        letras_ingresadas = (
            self.guessed_letters + self.incorrect_letters
        )
        print(f"Letras ingresadas: {', '.join(letras_ingresadas)}")

    def mostrar_palabra(self):
        progreso = []

        for letra in self.word:
            if letra in self.guessed_letters:
                progreso.append(letra)
            else:
                progreso.append("_")

        print(f"Palabra: {' '.join(progreso)}")

    def mostrar_intentos_restantes(self):
        intentos_restantes = self.max_errors - self.errors
        print(f"Intentos restantes: {intentos_restantes}")

if __name__ == "__main__":
    prueba = HangmanGame()

    prueba.display_progress(prueba.word)