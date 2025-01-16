# Con esto estamos llamando la collection de datos que tenemos en mongo db
from connections.mongodb.connection import collection


# Función para hacer un depósito
def hacerDeposito(nombre):
    while True:

        data = collection.find()

        for cliente in data:
            usuario = cliente["usuario"]
            saldoJson = cliente["saldo"]

            if nombre == usuario:
                print(
                    f"-> Hola {nombre}, estás en la sección de 'Hacer un Depósito'.\n"
                )
                deposito = float(input("-> Ingresa el monto que deseas depositar: $"))

                # Validar que el depósito sea un número positivo
                if not deposito.is_integer():
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
                    query_filter = {"usuario": usuario}
                    update_operation = {"$set": {"saldo":nuevo_saldo}}
                    user = collection.update_one(query_filter,update_operation)
                    return
