from inicioSesion import inicioSesion

# Importamos json para gestionar la información de los usuarios
import json


def crearCuenta():
    print(
        "\n\nBienvenido/a a nuestro sistema bancario Kalichhe. Estás en la sección de 'Crear cuenta'.\n"
    )
    while True:
        usuario_valido = True
        while usuario_valido:
            usuario = str(input("Ingresa un nombre de usuario: "))
            contrasena = str(input("Ingresa una contraseña: "))

            # Leer el archivo JSON para agregar más información
            with open("data/data.json", "r") as file:
                data = json.load(file)

            usuario_no_existe = True
            for cliente in data["clientes"]:
                usuarioJson = cliente["usuario"]

                if usuario == usuarioJson:
                    print(
                        "\nEl nombre de usuario o la cédula ya existen. Por favor, intenta con otros valores.\n"
                    )
                    usuario_no_existe = False
                    break

            if usuario_no_existe:
                usuario_valido = False

        nuevoUsuario = {
            "usuario": usuario,
            "contrasena": contrasena,
            "saldo": 0,
        }
        data["clientes"].append(nuevoUsuario)

        with open("data/data.json", "w") as file:
            json.dump(data, file, indent=4)

        print("\n¡Cuenta creada con éxito!")

        inicioSesion()
