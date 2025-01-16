# Con esto estamos llamando la collection de datos que tenemos en mongo db
from connections.mongodb.connection import collection, client
import sys  # Asegúrate de importar el módulo sys


def salir(nombre):

    data = collection.find()

    for cliente in data:
        usuarioJson = cliente["usuario"]
        saldoJson = cliente["saldo"]

        if nombre == usuarioJson:
            print(f"-> {nombre}, muchas gracias por usar nuestros servicios.")
            print(f"-> Tu saldo actual es de: ${saldoJson}")
            print("-> Hasta pronto, ¡que tengas un excelente día!\n")
            client.close()
            sys.exit()  # Sale de la aplicación de manera controlada
