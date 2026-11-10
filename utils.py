#!/usr/bin/env python3

import random
import time
import os

def limpiar_pantalla():
    os.system("clear")

def espera(tiempo):
    time.sleep(tiempo)

def inicio():
    print(
        """
 _    _          _   _  _____ __  __          _   _
| |  | |   /\   | \ | |/ ____|  \/  |   /\   | \ | |
| |__| |  /  \  |  \| | |  __| \  / |  /  \  |  \| |
|  __  | / /\ \ | . ` | | |_ | |\/| | / /\ \ | . ` |
| |  | |/ ____ \| |\  | |__| | |  | |/ ____ \| |\  |
|_|  |_/_/    \_\_| \_|\_____|_|  |_/_/    \_\_| \_|

             =========================
                  H A N G M A N
             =========================
        """
    )
    input("         [ PRESIONE ENTER PARA INICIAR ]")
    limpiar_pantalla()

def fin():
    print(""" _____ _____ _   _ 
|  ___|_   _| \ | |
| |_    | | |  \| |
|  _|   | | | . ` |
| |    _| |_| |\  |
\_|    \___/\_| \_/
    """)
    espera(3)

def menu(partida):
    while True:
        try:
            opcion = int(input("""Ingrese la opción deseada:
1- Ingresar letra
2- Reglas
3- salir
"""))

            if  1 <= opcion <= 3:
                return opcion

            print("Debe ingresar un valor entre 1 y 3")
            espera(1)
            limpiar_interfaz(partida)

        except ValueError:
            print("Debe ingresar un número entero.")
            espera(1)
            limpiar_interfaz(partida)

def reglas():
    print("""Reglas Del Juego:
    - El jugador debe adivinar la palabra oculta letra por letra.
    - Solo se aceptan letras como entrada válida.
    - Cada intento incorrecto aumenta el contador de errores.
    - La partida concluira luego de adivinar la palabra o al realizar 6 intentos incorrectos.""")
    espera(3)
    limpiar_pantalla()

def get_random_word():
    try:
        with open("wordlist.txt", "r") as file:
            palabras = file.readlines()

        if len(palabras) < 1:
            raise ValueError("El archivo seleccionado se encuentra vacío")
        else:
            palabra = random.choice(palabras)
            return palabra
        
    except FileNotFoundError:
        print("El archivo indicado no existe.")

def solicitar_letra(partida):
    continuar = True
    while continuar:
        limpiar_interfaz(partida)
        letter = input("Ingrese una letra: ")

        if letter.isalpha() == False or len(letter) != 1:
            print("Debe ingresar una entrada válida.")
            espera(1.5)
        else:
            if letter in partida.guessed_letters or letter in partida.incorrect_letters:
                print("La letra ingresada ya se utilizó.")
                espera(1.5)
            else:
                return letter

def user_interface(partida):
    partida.mostrar_intentos()
    partida.mostrar_palabra()
    partida.mostrar_intentos_restantes()
    partida.mostrar_ahorcado()
    print("="*40)

def limpiar_interfaz(partida):
    limpiar_pantalla()
    user_interface(partida)

def obtener_partida():
    pass

def guardar_partida():
    pass