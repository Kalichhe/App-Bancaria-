from connections.mongodb.connection import collection


def transferirDinero(nombre):
    usuarioEmisor = collection.find_one({"usuario": nombre})
    if not usuarioEmisor:
        print(f"-> El usuario {nombre} no existe en la base de datos.\n")
        return

    usuario = usuarioEmisor["usuario"]
    saldo = usuarioEmisor["saldo"]

    if saldo == 0:
        print(f"-> {nombre}, tu saldo actual es de ${saldo:.2f}.")
        print("-> No tienes fondos disponibles para realizar una transferencia.\n")
        return saldo  # No es posible transferir si el saldo es 0

    print(f"-> {usuario}, tu saldo actual es de ${saldo:.2f}.")

    usuarioReceptor = list(collection.find())  # Convertimos el cursor en una lista para reusarlo
    while True:
        try:
            nombreUsuario = input("Ingresa el usuario al que quieres enviar el dinero: ").strip()

            if nombre == nombreUsuario:
                print("No puedes enviarte dinero a ti mismo!\n")
                continue

            clienteDestino = next(
                (cliente for cliente in usuarioReceptor if cliente["usuario"] == nombreUsuario), None
            )

            if not clienteDestino:
                print("Usuario destinatario no existe. Intenta con otro usuario.\n")
                continue

            cantidadDinero = float(input("Ingresa la cantidad de dinero a enviar: "))
            if cantidadDinero <= 0:
                print(f"-> {nombre}, solo aceptamos transferencias de montos positivos.\n")
                continue

            if cantidadDinero > saldo:
                print("-> No tienes suficiente dinero para realizar esta transferencia.")
                print(f"-> {nombre}, tu saldo actual es de ${saldo:.2f}.\n")
                continue

            # Actualizar el saldo del emisor
            saldoEmisor = saldo - cantidadDinero
            collection.update_one({"usuario": usuario}, {"$set": {"saldo": saldoEmisor}})

            # Actualizar el saldo del receptor
            saldoReceptor = clienteDestino["saldo"] + cantidadDinero
            collection.update_one({"usuario": nombreUsuario}, {"$set": {"saldo": saldoReceptor}})

            print(f"-> {nombre}, transferencia exitosa. Tu nuevo saldo es de ${saldoEmisor:.2f}.\n")
            return

        except ValueError:
            print("-> Por favor, ingresa un valor numérico válido.\n")
