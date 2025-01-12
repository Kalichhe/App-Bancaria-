import json


# Función para hacer un depósito
def hacerDeposito(nombre):
    while True:

        with open("python/data/data.json", "r") as file:
            data = json.load(file)

        for cliente in data["clientes"]:
            usuario = cliente["usuario"]
            saldoJson = cliente["saldo"]

            if nombre == usuario:
                print(
                    f"-> Hola {nombre}, estás en la sección de 'Hacer un Depósito'.\n"
                )
                deposito = input("-> Ingresa el monto que deseas depositar: $")

                # Validar que el depósito sea un número positivo
                if not deposito.isdecimal():
                    print(
                        f"-> {nombre}, solo aceptamos depósitos con valores numéricos positivos.\n"
                    )
                elif float(deposito) <= 0:
                    print(f"-> {nombre}, el monto a depositar debe ser mayor a $0.\n")
                else:
                    nuevo_saldo = saldoJson + float(deposito)
                    print(
                        f"-> {nombre}, tu depósito de ${float(deposito):.2f} fue exitoso."
                    )
                    print(f"-> Tu nuevo saldo es de ${nuevo_saldo:.2f}.\n")

                    # Con esto, modifico el saldo actual de dicho cliente
                    cliente["saldo"] = nuevo_saldo

                    with open("python/data/data.json", "w") as file:
                        json.dump(data, file, indent=4)
                    return
