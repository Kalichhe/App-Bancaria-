# Vamos a hacer una app bancaria, que permita a los usuarios poder mostrar el saldo total, depositar, retirar y salir de la app.


# Funcion para hacer un deposito


def hacerDeposito(total, nombre):
    while True:
        print(f"-> Hola {nombre}, estamos en la seccion de hacer un deposito")
        deposito = input("-> Ingresa el valor a depositar: $")
        if not deposito.isdecimal():
            print(f"-> {nombre}, Solo aceptamos depositos de numeros positivos\n")
        elif float(deposito) < 0:
            print(f"-> {nombre}, Solo aceptamos depositos de numeros positivos\n")
            return 0
        else:
            print(f"-> {nombre}, Tu saldo actual es de ${total + float(deposito)}\n")
            return float(deposito)
