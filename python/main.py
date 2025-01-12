from inicioSesion import inicioSesion
from crearCuenta import crearCuenta
import sys


def main():
    print("Bienvenido/a a nuestro sistema bancario Kalichhe\n")

    while True:
        try:
            print("Selecciona una opción:")
            print("     1) Iniciar sesión")
            print("     2) Crear una cuenta")
            print("     3) Salir")

            opcion = int(input("-> Ingresa el número de la opción deseada: "))

            if opcion == 1:
                inicioSesion()
            elif opcion == 2:
                crearCuenta()
            elif opcion == 3:
                print("\nGracias por usar el sistema bancario Kalichhe. ¡Hasta pronto!")
                sys.exit()
            else:
                print("\n-> Por favor, selecciona una opción válida (1, 2 o 3).\n")
        except ValueError:
            print("\n-> Entrada no válida. Por favor, ingresa un número (1, 2 o 3).\n")


main()
