# Función para hacer un depósito
def hacerDeposito(saldo, nombre):
    while True:
        print(f"-> Hola {nombre}, estás en la sección de 'Hacer un Depósito'.\n")
        deposito = input("-> Ingresa el monto que deseas depositar: $")

        # Validar que el depósito sea un número positivo
        if not deposito.isdecimal():
            print(f"-> {nombre}, solo aceptamos depósitos con valores numéricos positivos.\n")
        elif float(deposito) <= 0:
            print(f"-> {nombre}, el monto a depositar debe ser mayor a $0.\n")
        else:
            nuevo_saldo = saldo + float(deposito)
            print(f"-> {nombre}, tu depósito de ${float(deposito):.2f} fue exitoso.")
            print(f"-> Tu nuevo saldo es de ${nuevo_saldo:.2f}.\n")
            return float(deposito)
