from inicioSesion import inicioSesion
from cryptography.fernet import Fernet

# Con esto estamos llamando la collection de datos que tenemos en mongo db
from connections.mongodb.connection import collection

# Para poder hacer las incriptaciones y desencriptaciones
key = Fernet.generate_key()

fernet = Fernet(key)


def crearCuenta():
    print(
        "\n\nBienvenido/a a nuestro sistema bancario Kalichhe. Estás en la sección de 'Crear cuenta'.\n"
    )
    while True:
        usuario_valido = True
        while usuario_valido:
            usuario = str(input("Ingresa un nombre de usuario: "))
            contrasena = str(input("Ingresa una contraseña: "))

            data = collection.find()

            usuario_no_existe = True
            for cliente in data:
                usuarioMongo = cliente["usuario"]

                if usuario == usuarioMongo:
                    print(
                        "\nEl nombre de usuario ya existen. Por favor, intenta con otros valores.\n"
                    )
                    usuario_no_existe = False
                    break

            if usuario_no_existe:
                usuario_valido = False

        nuevoUsuario = {
            "usuario": usuario,
            "contrasena": fernet.encrypt(contrasena.encode()),
            "saldo": 0,
            "key": key,
        }

        user = collection.insert_one(nuevoUsuario)

        print("\n¡Cuenta creada con éxito!")

        inicioSesion()
