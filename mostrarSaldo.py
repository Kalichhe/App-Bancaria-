import json


# Función para mostrar el saldo total
def mostrarSaldo(nombre):
    # Leer el archivo JSON para obtener la información de los usuarios
    with open("python/data/data.json", "r") as file:
        data = json.load(file)

    for cliente in data["clientes"]:
        usuarioJson = cliente["usuario"]
        saldoJson = cliente["saldo"]

        if nombre == usuarioJson:
            print(f"-> Hola {nombre}, estamos en la sección de Mostrar Saldo.")
            print(f"-> {nombre}, tu saldo actual es de: ${saldoJson}\n")
