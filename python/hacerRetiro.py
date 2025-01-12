# Función para hacer un retiro
def hacerRetiro(saldo, nombre):
    while True:
        print(f"-> Hola {nombre}, estás en la sección de 'Hacer Retiros'.\n")

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
                print(f"-> {nombre}, solo aceptamos retiros de montos positivos.\n")
            elif retiro > saldo:
                print("-> No tienes suficiente dinero para realizar este retiro.")
                print(f"-> {nombre}, tu saldo actual es de ${saldo:.2f}.\n")
            else:
                saldo -= retiro
                print(
                    f"-> {nombre}, retiro exitoso. Tu nuevo saldo es de ${saldo:.2f}.\n"
                )
                return saldo

        except ValueError:
            print("-> Por favor, ingresa un valor numérico válido.\n")
