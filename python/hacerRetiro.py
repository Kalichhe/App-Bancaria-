# Vamos a hacer una app bancaria, que permita a los usuarios poder mostrar el saldo total, depositar, retirar y salir de la app.


# Funcion para hacer un retiro
def hacerRetiro(total, nombre):
    while True:
        print(f"-> Hola {nombre}, estamos en la seccion de hacer retiros")
        if total == 0:
            print(f"-> {nombre}, Tu saldo actual es de ${total}")
            print("-> No tienes dinero para hacer un retiro\n")
        else:
            print(f"-> {nombre}, Tu saldo actual es de ${total}", "\n")
            retiro = float(input("-> Ingresa la cantidad de dinero a retirar: $"))
            if retiro > total:
                print("-> No tienes dinero para hacer un retiro")
                print(f"-> {nombre}, Tu saldo actual es de ${total}\n")
                return total
            elif retiro < 0:
                print(f"-> {nombre}, Solo aceptamos retiros de numeros positivos\n")
            else:
                total -= retiro
                print(f"-> {nombre}, Tu saldo actual es de ${total}", "\n")
                return total
