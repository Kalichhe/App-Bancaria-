# Importando las funciones necesarias
from mostrarSaldo import mostrarSaldo
from hacerDeposito import hacerDeposito
from hacerRetiro import hacerRetiro
from transferirDinero import transferirDinero
from salir import salir


# Menú principal
def menu(usuario):
    while True:
        # Diseño del menú
        longitud_usuario = len(usuario)
        print("\n " + "-" * (38 + longitud_usuario))
        print(f"| Bienvenido/a a tu sistema bancario, {usuario} |")
        print(" " + "-" * (38 + longitud_usuario))
        print("| 1. Mostrar saldo total" + " " * (15 + longitud_usuario) + "|")
        print("| 2. Hacer un depósito" + " " * (17 + longitud_usuario) + "|")
        print("| 3. Hacer un retiro" + " " * (19 + longitud_usuario) + "|")
        print("| 4. Hacer una transferencia" + " " * (11 + longitud_usuario) + "|")
        print("| 5. Salir de la aplicación" + " " * (12 + longitud_usuario) + "|")
        print(" " + "-" * (38 + longitud_usuario))
        print("")

        # Solicitar la opción al usuario
        number = input("-> Selecciona una opción: ")
        print("")

        # Opciones del menú
        if number == "1":
            mostrarSaldo(usuario)  # Muestra el saldo actual
        elif number == "2":
            hacerDeposito(usuario)  # Realiza un depósito y suma al saldo
        elif number == "3":
            hacerRetiro(usuario)  # Realiza un retiro y actualiza el saldo
        elif number == "4":
            transferirDinero(usuario)  # Realiza transferencia a un usuario en especifico
        elif number == "5":
            salir(usuario)  # Sale de la aplicación
        else:
            # Manejo de opciones inválidas
            print("-> Opción no válida. Por favor, selecciona una opción entre 1 y 5.")
            print("")
