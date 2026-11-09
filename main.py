#!/usr/bin/env python3

import utils
import game

if __name__ == "__main__":
    continuar = True
    opcion = None

    partida = game.HangmanGame()

    utils.inicio()
    utils.reglas()

    while continuar:

        utils.user_interface(partida)

        opcion = utils.menu(partida)

        try:
            match opcion:
                case 1:
                    letter = utils.solicitar_letra(partida)
                    acierto = partida.process_guess(letter)
                    if acierto:
                        print("La letra ingresada es correcta")
                        utils.espera(2)
                        utils.limpiar_pantalla()
                    else:
                        print(f"La letra ingresada es incorrecta")
                        utils.espera(2)
                        utils.limpiar_pantalla()

                    if partida.is_won():
                        print("¡Victoria! ¡Adivinaste la palabra!")
                        continuar = False
                        utils.fin()

                    elif partida.is_lost():
                        print(f"Fin del juego. La palabra era: {partida.word}")
                        continuar = False
                        utils.fin()

                case 2:
                    utils.limpiar_pantalla()
                    utils.reglas()
                case 3:
                    utils.fin()
                    continuar = False
        except TypeError:
            print("Debe ingresar un numero entre 1 y 3")
            utils.limpiar_interfaz(partida)

        utils.limpiar_pantalla()
