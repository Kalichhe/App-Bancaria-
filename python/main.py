# Vamos a hacer una app bancaria, que permita a los usuarios poder mostrar el saldo total, depositar, retirar y salir de la app.

# Haciendo importaciones de las funciones
from mostrarSaldo import mostrarSaldo
from hacerDeposito import hacerDeposito
from hacerRetiro import hacerRetiro
from salir import salir

# Menu
def menu():
    while True:
        print(" --------------------------------")
        print("|Bienvenid@ a tu sistema bancario|")
        print(" --------------------------------")
        print("|1. Mostrar saldo total          |")
        print(" --------------------------------")
        print("|2. Hacer un deposito            |")
        print(" --------------------------------")
        print("|3. Hacer un retiro              |")
        print(" --------------------------------")
        print("|4. Salir de la aplicacion       |")
        print(" --------------------------------")
        print("")
        number = input("Selecciona una opcion: ")
        print("")

        if number in {"1", "2", "3", "4"}:
            {
                "1": lambda: mostrarSaldo(),
                "2": lambda: hacerDeposito(),
                "3": lambda: hacerRetiro(),
                "4": lambda: salir(),
            }[number]()
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")
            print("")

menu()