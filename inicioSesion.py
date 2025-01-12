from menu import menu
import json


def inicioSesion():
    from crearCuenta import crearCuenta

    print(
        "\n\nBienvenido/a a nuestro sistema bancario Kalichhe. Estás en la sección de 'Iniciar Sesión'."
    )

    while True:
        # Leer el archivo JSON para obtener la información de los usuarios
        with open("python/data/data.json", "r") as file:
            data = json.load(file)

        usuario = str(input("\n-> Ingresa tu usuario: "))
        contrasena = str(input("-> Ingresa tu contraseña: "))

        # Verificar credenciales
        usuario_encontrado = False
        for cliente in data["clientes"]:
            usuarioJson = cliente["usuario"]
            contrasenaJson = cliente["contrasena"]

            if usuario == usuarioJson and contrasena == contrasenaJson:
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
