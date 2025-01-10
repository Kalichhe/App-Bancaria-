# Vamos a hacer una app bancaria, que permita a los usuarios poder mostrar el saldo total, depositar, retirar y salir de la app.

import sys


# Funcion para salir de la app
def salir(total, nombre):
    print(f"-> {nombre}, Muchas gracias por usar nuestros servicios, la buena")
    print(f"-> Tu saldo actual es de ${total}", "\n")
    sys.exit()
