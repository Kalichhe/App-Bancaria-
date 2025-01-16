# Con esto estamos llamando la collection de datos que tenemos en mongo db
from connections.mongodb.connection import collection


# Función para hacer un retiro
def hacerRetiro(nombre):
    while True:
        # Leer el archivo JSON para obtener la información de los usuarios
        print(f"-> Hola {nombre}, estás en la sección de 'Hacer Retiros'.\n")

        data = collection.find()
        for cliente in data:
            usuario = cliente["usuario"]
            saldo = cliente["saldo"]

            if nombre == usuario:
                if saldo == 0:
                    print(f"-> {nombre}, tu saldo actual es de ${saldo:.2f}.")
                    print("-> No tienes fondos disponibles para realizar un retiro.\n")
                    return saldo  # No es posible retirar si el saldo es 0

                print(f"-> {nombre}, tu saldo actual es de ${saldo:.2f}.")

                try:
                    retiro = float(
                        input("-> Ingresa la cantidad de dinero que deseas retirar: $")
                    )

                    if retiro <= 0:
                        print(
                            f"-> {nombre}, solo aceptamos retiros de montos positivos.\n"
                        )
                    elif retiro > saldo:
                        print(
                            "-> No tienes suficiente dinero para realizar este retiro."
                        )
                        print(f"-> {nombre}, tu saldo actual es de ${saldo:.2f}.\n")
                    else:
                        saldo -= retiro
                        print(
                            f"-> {nombre}, retiro exitoso. Tu nuevo saldo es de ${saldo:.2f}.\n"
                        )

                        # Con esto, modifico el saldo actual de dicho cliente
                        query_filter = {"usuario": usuario}
                        update_operation = {"$set": {"saldo":saldo}}
                        user = collection.update_one(query_filter,update_operation)
                        return

                except ValueError:
                    print("-> Por favor, ingresa un valor numérico válido.\n")
