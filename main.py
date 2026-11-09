#!/usr/bin/env python3

import utils
import game

if __name__ == "__main__":
    continuar = True
    opcion = None

    partida = game.HangmanGame()

    while continuar:
        opcion = utils.menu()
        
        match opcion:
            case 1:
                letter = utils.solicitar_letra(partida)
                acierto = partida.process_guess(letter)
                if acierto:
                    print("La letra ingresada es correcta")
                else:
                    print(f"La letra ingresada es incorrecta")

                partida.mostrar_intentos()
                partida.mostrar_palabra()
                partida.mostrar_intentos_restantes()
                partida.mostrar_ahorcado()

                if partida.is_won():
                    print("¡Victoria! ¡Adivinaste la palabra!")
                    continuar = False

                elif partida.is_lost():
                    print(f"Fin del juego. La palabra era: {partida.word}")
                    continuar = False

            case 2:
                pass
            case 3:
                pass
            case 4:
                continuar = False
