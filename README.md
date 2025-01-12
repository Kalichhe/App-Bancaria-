# Funcionamiento de la Aplicación: Sistema Bancario Kalichhe

## Descripción:

El Sistema Bancario Kalichhe es una aplicación de terminal que simula el funcionamiento de un banco. Esta aplicación no tiene una interfaz gráfica, por lo que toda la interacción se realiza a través de la línea de comandos.

**Características principales:**
- **Almacenamiento en archivo JSON:** Todos los datos relacionados con las cuentas bancarias y transacciones se guardan en un archivo JSON.
- **Ubicación del archivo de datos:** El archivo JSON se encuentra dentro de una carpeta llamada [`data`](https://github.com/Kalichhe/App-Bancaria-/tree/main/data).

## Zona de Registro y Inicio de Sesión:

El sistema cuenta con una **zona de registro y inicio de sesión** para permitir a los usuarios crear una cuenta y acceder al sistema de manera segura. El usuario que se registra será el mismo que utilizará sus credenciales para acceder posteriormente.

### Proceso de Registro:
1. **Ingreso de datos:** El usuario debe proporcionar los siguientes datos:
   - **Usuario:** Un nombre de usuario único.
   - **Cédula:** Un número de identificación único.
   - **Contraseña:** Una contraseña segura.
2. **Almacenamiento en el archivo JSON:** Los datos del nuevo usuario (usuario, cédula y contraseña) se almacenan en el archivo JSON dentro de la carpeta [`data`](https://github.com/Kalichhe/App-Bancaria-/tree/main/data), creando una entrada única para cada cuenta de usuario.

### Proceso de Inicio de Sesión:
1. **Ingreso de credenciales:** El usuario deberá ingresar el **usuario (nombre de usuario)** y la **contraseña** que utilizó durante el proceso de registro.
2. **Verificación:** El sistema verifica las credenciales proporcionadas comparándolas con los datos almacenados en el archivo JSON.
3. **Acceso al sistema:** Si las credenciales son correctas, el usuario obtiene acceso a su cuenta bancaria dentro del sistema y puede realizar diversas operaciones, como consultas de saldo y transacciones.
