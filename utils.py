#!/usr/bin/env python3

import random
import time
import os


def menu():
    return int(input("""
    Ingrese la opción deseada:
    1- ingresar letra
    2- ver cantidad de intentos restantes
    3- ver cantidad de errores
    4- salir
    """))

def get_random_word():
    try:
        with open("wordlist.txt", "r") as file:
            palabras = file.readlines()

        if len(palabras) < 1:
            raise ValueError("El archivo seleccionado se encuentra vacío")
        else:
            palabra = random.choice(palabras)
            return palabra
        
    except FileNotFoundError():
        print("El archivo indicado no existe.")

def solicitar_letra(partida):
    continuar = True
    print(partida.word)
    while continuar:
        letter = input("Ingrese una letra: ")

        if letter.isalpha() == False or len(letter) != 1:
            print("Debe ingresar una entrada válida.")
            time.sleep(1.5)
            os.system("clear")
        else:
            if letter in partida.guessed_letters or letter in partida.incorrect_letters:
                print("La letra ingresada ya se utilizó.")
            else:
                return letter
            continuar = False

def opciones():
    opcion = menu

    if opcion > 3:
        return False
    else: 
        return True


if __name__ == "__main__":
    pass