import json
import sys  # Asegúrate de importar el módulo sys


def salir(nombre):
    with open("python/data/data.json", "r") as file:
        data = json.load(file)

    for cliente in data["clientes"]:
        usuarioJson = cliente["usuario"]
        saldoJson = cliente["saldo"]

        if nombre == usuarioJson:
            print(f"-> {nombre}, muchas gracias por usar nuestros servicios.")
            print(f"-> Tu saldo actual es de: ${saldoJson}")
            print("-> Hasta pronto, ¡que tengas un excelente día!\n")

            sys.exit()  # Sale de la aplicación de manera controlada
