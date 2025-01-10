# Vamos a hacer una app bancaria, que permita a los usuarios poder mostrar el saldo total, depositar, retirar y salir de la app.

# Haciendo importaciones de las funciones
from mostrarSaldo import mostrarSaldo
from hacerDeposito import hacerDeposito
from hacerRetiro import hacerRetiro
from salir import salir


# Menu
def menu():
    total = 0
    nombre = str(input("Ingresa el nombre del titular de la cuenta: "))
    while True:
        print(" ---------------------------------" + len(nombre) * "-")
        print(f"|Bienvenid@ a tu sistema bancario {nombre}|")
        print(" ---------------------------------" + len(nombre) * "-")
        print("|1. Mostrar saldo total           " + len(nombre) * " " + "|")
        print(" ---------------------------------" + len(nombre) * "-")
        print("|2. Hacer un deposito             " + len(nombre) * " " + "|")
        print(" ---------------------------------" + len(nombre) * "-")
        print("|3. Hacer un retiro               " + len(nombre) * " " + "|")
        print(" ---------------------------------" + len(nombre) * "-")
        print("|4. Salir de la aplicacion        " + len(nombre) * " " + "|")
        print(" ---------------------------------" + len(nombre) * "-")
        print("")
        number = input("-> Selecciona una opcion: ")
        print("")

        if number == "1":
            mostrarSaldo(total, nombre)
        elif number == "2":
            total += hacerDeposito(total, nombre)
        elif number == "3":
            total = hacerRetiro(total, nombre)
        elif number == "4":
            salir(total, nombre)
        else:
            print("-> Opción no válida. Por favor, intenta de nuevo.")
            print("")


menu()
