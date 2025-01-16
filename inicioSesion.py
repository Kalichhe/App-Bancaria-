from menu import menu
from cryptography.fernet import Fernet


# Con esto estamos llamando la collection de datos que tenemos en mongo db
from connections.mongodb.connection import collection


def inicioSesion():
    from crearCuenta import crearCuenta

    print(
        "\n\nBienvenido/a a nuestro sistema bancario Kalichhe. Estás en la sección de 'Iniciar Sesión'."
    )

    while True:

        data = collection.find()

        usuario = str(input("\n-> Ingresa tu usuario: "))
        contrasena = str(input("-> Ingresa tu contraseña: "))

        # Verificar credenciales
        usuario_encontrado = False
        for cliente in data:
            usuarioMongo = cliente["usuario"]
            contrasenaMongo = cliente["contrasena"]
            key = cliente["key"]
            fernet = Fernet(key)

            if usuario == usuarioMongo and contrasena == fernet.decrypt(contrasenaMongo).decode():
                usuario_encontrado = True
                print(
                    f"\n-> Bienvenido/a, {usuario}! Accediendo al menú principal...\n"
                )
                menu(usuario)  # Llama al menú principal con el nombre de usuario
                return  # Termina la función después de acceder al menú

        if not usuario_encontrado:
            print(
                "\n-> Usuario o contraseña incorrectos. Por favor, inténtalo nuevamente.\n"
            )

        # Preguntar si el usuario tiene una cuenta o quiere crear una
        print("¿Tienes ya una cuenta?")
        print("1) Sí")
        print("2) No")
        desicion = int(input("-> Selecciona una opción: "))

        if desicion == 1:
            continue  # Volver a intentar iniciar sesión
        elif desicion == 2:
            crearCuenta()  # Crear una nueva cuenta
            break  # Salir del ciclo si el usuario decide crear una cuenta
        else:
            print("-> Opción no válida. Por favor, selecciona 1 o 2.\n")
