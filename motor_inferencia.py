import sqlite3
import hashlib

# Establecer conexión con la base de datos
conn = sqlite3.connect('database.db')

def verificar_credenciales(email, password):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Usuario WHERE email = ?", (email,))
    resultado = cursor.fetchone()
    cursor.close()
    if resultado is None:
        return False
    stored_password = resultado[3]  # Obtener la contraseña almacenada en la base de datos
    salt = stored_password[:16]  # Obtener el salt de la contraseña almacenada
    password_hash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return stored_password == salt + password_hash


correo_ingresado = input("Ingrese su correo: ")
contrasena_ingresada = input("Ingrese su contraseña: ")

if verificar_credenciales(correo_ingresado, contrasena_ingresada):
    print("Inicio de sesión exitoso")
else:
    print("Credenciales inválidas. Intente nuevamente.")

# Cerrar la conexión a la base de datos
conn.close()
