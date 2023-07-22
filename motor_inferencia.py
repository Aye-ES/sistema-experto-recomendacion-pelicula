import sqlite3
import hashlib


def verificar_credenciales(email, password):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM Usuario WHERE email = ?', (email,))
    resultado = cursor.fetchone()

    cursor.close()
    conn.close()

    if resultado is None:
        return None

    stored_password = bytes.fromhex(resultado[3])  # Convertir el valor hexadecimal a bytes
    salt = stored_password[:16]  # Obtener el salt de la contraseña almacenada
    password_hash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    if stored_password == salt + password_hash:
        return resultado[1]  # Retorna el nombre del usuario si las credenciales son válidas
    else:
        return None
