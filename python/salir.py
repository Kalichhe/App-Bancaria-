import sys  # Asegúrate de importar el módulo sys

def salir(saldo, nombre):
    print(f"-> {nombre}, muchas gracias por usar nuestros servicios.")
    print(f"-> Tu saldo actual es de: ${saldo}")
    print("-> Hasta pronto, ¡que tengas un excelente día!\n")

    sys.exit()  # Sale de la aplicación de manera controlada
