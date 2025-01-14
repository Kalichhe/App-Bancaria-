# Transferir dinero
import json


def transferirDinero(nombre):
    with open("data/data.json", "r") as file:
        data = json.load(file)

    for cliente in data["clientes"]:
        usuarioJson = cliente["usuario"]
        saldoJson = cliente["saldo"]

        if nombre == usuarioJson:
            if saldoJson == 0:
                print(f"-> {nombre}, tu saldo actual es de ${saldoJson:.2f}.")
                print(
                    "-> No tienes fondos disponibles para realizar una transferencia.\n"
                )
                return saldoJson  # No es posible transferir si el saldo es 0

            print(f"-> {nombre}, tu saldo actual es de ${saldoJson:.2f}.")

            while True:
                try:
                    usuarioDestinatario = str(
                        input("Ingresa el usuario al que quieres enviar el dinero: ")
                    )
                    for clienteDesti in data["clientes"]:
                        usuarioJsonDesti = clienteDesti["usuario"]

                        if usuarioJsonDesti == nombre:
                            print("No puedes enviarte plata a ti mismo!\n")
                            break
                        elif usuarioDestinatario == usuarioJsonDesti:

                            cantidadDinero = int(
                                input("Ingresa la cantidad de dinero a enviar: ")
                            )
                            if cantidadDinero <= 0:
                                print(
                                    f"-> {nombre}, solo aceptamos transferencias de montos positivos.\n"
                                )
                                break
                            elif cantidadDinero > saldoJson:
                                print(
                                    "-> No tienes suficiente dinero para realizar esta transferencia."
                                )
                                print(
                                    f"-> {nombre}, tu saldo actual es de ${saldoJson:.2f}.\n"
                                )
                                break
                            else:
                                saldoJson -= cantidadDinero
                                print(
                                    f"-> {nombre}, transferencia exitosa. Tu nuevo saldo es de ${saldoJson:.2f}.\n"
                                )

                                # Con esto, modifico el saldo actual de dicho cliente
                                cliente["saldo"] = saldoJson

                                # Con esto enviamos el dinero al destinatario
                                clienteDesti["saldo"] += cantidadDinero

                                with open("data/data.json", "w") as file:
                                    json.dump(data, file, indent=4)
                                return

                    if usuarioDestinatario != usuarioJsonDesti:
                        print(
                            "Usuario destinatario, ¡no existe! Intenta con otro usuario.\n"
                        )

                except ValueError:
                    print("-> Por favor, ingresa un valor numérico válido.\n")
