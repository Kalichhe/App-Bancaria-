import json


# Función para hacer un retiro
def hacerRetiro(nombre):
    while True:
        # Leer el archivo JSON para obtener la información de los usuarios
        print(f"-> Hola {nombre}, estás en la sección de 'Hacer Retiros'.\n")

        with open("python/data/data.json", "r") as file:
            data = json.load(file)

        for cliente in data["clientes"]:
            usuarioJson = cliente["usuario"]
            saldoJson = cliente["saldo"]

            if nombre == usuarioJson:
                if saldoJson == 0:
                    print(f"-> {nombre}, tu saldo actual es de ${saldoJson:.2f}.")
                    print("-> No tienes fondos disponibles para realizar un retiro.\n")
                    return saldoJson  # No es posible retirar si el saldo es 0

                print(f"-> {nombre}, tu saldo actual es de ${saldoJson:.2f}.")

                try:
                    retiro = float(
                        input("-> Ingresa la cantidad de dinero que deseas retirar: $")
                    )

                    if retiro <= 0:
                        print(
                            f"-> {nombre}, solo aceptamos retiros de montos positivos.\n"
                        )
                    elif retiro > saldoJson:
                        print(
                            "-> No tienes suficiente dinero para realizar este retiro."
                        )
                        print(f"-> {nombre}, tu saldo actual es de ${saldoJson:.2f}.\n")
                    else:
                        saldoJson -= retiro
                        print(
                            f"-> {nombre}, retiro exitoso. Tu nuevo saldo es de ${saldoJson:.2f}.\n"
                        )

                        # Con esto, modifico el saldo actual de dicho cliente
                        cliente["saldo"] = saldoJson

                        with open("python/data/data.json", "w") as file:
                            json.dump(data, file, indent=4)
                        return

                except ValueError:
                    print("-> Por favor, ingresa un valor numérico válido.\n")
