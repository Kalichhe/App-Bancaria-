# Con esto estamos llamando la collection de datos que tenemos en mongo db
from connections.mongodb.connection import collection


# Función para mostrar el saldo total
def mostrarSaldo(nombre):

    data = collection.find()

    for cliente in data:
        usuarioJson = cliente["usuario"]
        saldoJson = cliente["saldo"]

        if nombre == usuarioJson:
            print(f"-> Hola {nombre}, estamos en la sección de Mostrar Saldo.")
            print(f"-> {nombre}, tu saldo actual es de: ${saldoJson}\n")
