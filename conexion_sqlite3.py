import sqlite3
from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD

# para encriptado de contraseña
import hashlib
import os

# Conectar a la base de datos SQLite
def connect_to_database():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    return conn, cursor

# Obtener la conexión y el cursor
conn, cursor = connect_to_database()

# Tabla Usuario
cursor.execute('''CREATE TABLE IF NOT EXISTS Usuario (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT,
                    email TEXT,
                    password TEXT,
                    edad INTEGER)''')

# Tabla RecomendacionPelicula
cursor.execute('''CREATE TABLE IF NOT EXISTS RecomendacionPelicula (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    usuario_id INTEGER,
                    pelicula_id INTEGER,
                    FOREIGN KEY (usuario_id) REFERENCES Usuario (id),
                    FOREIGN KEY (pelicula_id) REFERENCES Pelicula (id))''')

# Tabla Calificacion
cursor.execute('''CREATE TABLE IF NOT EXISTS Calificacion (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    usuario_id INTEGER,
                    pelicula_id INTEGER,
                    descripcion TEXT,
                    FOREIGN KEY (usuario_id) REFERENCES Usuario (id),
                    FOREIGN KEY (pelicula_id) REFERENCES Pelicula (id))''')


# Tabla Pelicula
cursor.execute('''CREATE TABLE IF NOT EXISTS Pelicula (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    titulo TEXT,
                    director TEXT,
                    clasificacion_id INTEGER,
                    genero_id INTEGER,
                    FOREIGN KEY (clasificacion_id) REFERENCES Clasificacion (id),
                    FOREIGN KEY (genero_id) REFERENCES Genero (id))''')

# Tabla Clasificacion
cursor.execute('''CREATE TABLE IF NOT EXISTS Clasificacion (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT)''')

# Tabla Genero
cursor.execute('''CREATE TABLE IF NOT EXISTS Genero (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT)''')


# Cerrar conexión a la base de datos SQLite
def close_connection(conn):
    conn.close()


# Función para encriptar la contraseña
def encrypt_password(password):
    salt = os.urandom(16)  # Generar un salt aleatorio de 16 bytes
    password_hash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return salt.hex() + password_hash.hex()


# Ejemplo de recolección de datos y guardado en la base de datos

def collect_usuario_data():
    usuario_data = [
        ("Ayelen", "ayelenestevezs@gmail.com", encrypt_password("ayelen"), 22),
        ("Jherlin", "mandeporayerling@gmail.com", encrypt_password("jherlin"), 22),
        ("Neil", "neil20cuellar1@gmail.com", encrypt_password("neil"), 22),
        ("Susane", "susane@gmail.com", encrypt_password("susane"), 23),
        ("Carlos", "carlos@gmail.com", encrypt_password("carlos"), 27),
        # Agrega más datos de usuario aquí
    ]
    cursor.executemany('INSERT INTO Usuario (nombre, email, password, edad) VALUES (?, ?, ?, ?)', usuario_data)

def collect_calificacion_data():
    calificacion_data = [
        (1, 1, "Excelente"),
        (2, 2, "Malo"),
        (3, 3, "Neutro"),
        (4, 4, "Malo"),
        (5, 5, "Excelente"),
        # Agrega más datos de calificación aquí
    ]
    cursor.executemany('INSERT INTO Calificacion (usuario_id, pelicula_id, descripcion) VALUES (?, ?, ?)', calificacion_data)



def collect_recomendacion_data():
    recomendacion_data = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        # Agrega más datos de recomendación aquí
    ]
    cursor.executemany('INSERT INTO RecomendacionPelicula (usuario_id, pelicula_id) VALUES (?, ?)', recomendacion_data)





def collect_pelicula_data():
    pelicula_data = [
        ("Francotirador", "Clint Eastwood", 3, 1),
        ("Atraccion Peligrosa", "Ben Affleck", 3, 2),
        ("E.T", "Steven Spielberg", 1, 3),
        ("Corazonada", "Alejandro Montiel", 3, 4),
        ("Harry Potter", "Chris Columbus", 2, 5),
        # Agrega más datos de película aquí
    ]
    cursor.executemany('INSERT INTO Pelicula (titulo, director, clasificacion_id, genero_id) VALUES (?, ?, ?, ?)', pelicula_data)


def collect_clasificacion_data():
    clasificacion_data = [
        ("APT",),
        ("Personas menores de 15 años",),
        ("Personas mayores de 15 años",),
        # Agrega más datos de clasificación aquí
    ]
    cursor.executemany('INSERT INTO Clasificacion (nombre) VALUES (?)', clasificacion_data)


def collect_genero_data():
    genero_data = [
        ("Acción",),
        ("Suspenso",),
        ("Ciencia Ficción",),
        ("Suspenso",),
        ("Fantasía",),
        # Agrega más datos de género aquí
    ]
    cursor.executemany('INSERT INTO Genero (nombre) VALUES (?)', genero_data)


# Ejecutar las funciones de recolección de datos
collect_usuario_data()
collect_recomendacion_data()
collect_calificacion_data()
collect_pelicula_data()
collect_clasificacion_data()
collect_genero_data()


# Guardar los cambios en la base de datos
conn.commit()

# Consulta para mostrar los nombres en lugar de IDs en la tabla RecomendacionPelicula
cursor.execute('''
    SELECT Usuario.nombre, Pelicula.titulo
    FROM RecomendacionPelicula
    JOIN Usuario ON RecomendacionPelicula.usuario_id = Usuario.id
    JOIN Pelicula ON RecomendacionPelicula.pelicula_id = Pelicula.id
''')
recomendaciones = cursor.fetchall()
print("Recomendaciones:")
for recomendacion in recomendaciones:
    print(f"Usuario: {recomendacion[0]}, Película: {recomendacion[1]}")


# Consulta para mostrar los nombres en lugar de IDs en la tabla Usuario
cursor.execute('SELECT nombre, email, password, edad FROM Usuario')
usuarios = cursor.fetchall()
print("\nTabla Usuario:")
for usuario in usuarios:
    print(f"Nombre: {usuario[0]}, Email: {usuario[1]}, Password: {usuario[2]}, Edad: {usuario[3]}")

# Consulta para mostrar los nombres en lugar de IDs en la tabla Pelicula
cursor.execute('''
    SELECT titulo, director, Clasificacion.nombre, Genero.nombre
    FROM Pelicula
    JOIN Clasificacion ON Pelicula.clasificacion_id = Clasificacion.id
    JOIN Genero ON Pelicula.genero_id = Genero.id
''')
peliculas = cursor.fetchall()
print("\nTabla Pelicula:")
for pelicula in peliculas:
    print(f"Título: {pelicula[0]}, Director: {pelicula[1]}, Clasificación: {pelicula[2]}, Género: {pelicula[3]}")

# Consulta para mostrar los nombres en lugar de IDs en la tabla Clasificacion
cursor.execute('SELECT nombre FROM Clasificacion')
clasificaciones = cursor.fetchall()
print("\nTabla Clasificacion:")
for clasificacion in clasificaciones:
    print(f"Nombre: {clasificacion[0]}")

# Consulta para mostrar los nombres en lugar de IDs en la tabla Genero
cursor.execute('SELECT nombre FROM Genero')
generos = cursor.fetchall()
print("\nTabla Genero:")
for genero in generos:
    print(f"Nombre: {genero[0]}")


# Consulta para mostrar los nombres en lugar de IDs en la tabla Calificacion
cursor.execute('''
    SELECT Usuario.nombre, Pelicula.titulo, Calificacion.descripcion
    FROM Calificacion
    JOIN Usuario ON Calificacion.usuario_id = Usuario.id
    JOIN Pelicula ON Calificacion.pelicula_id = Pelicula.id
''')
calificaciones = cursor.fetchall()
print("\nCalificaciones:")
for calificacion in calificaciones:
    print(f"Usuario: {calificacion[0]}, Película: {calificacion[1]}, Descripción: {calificacion[2]}")


# Cerrar la conexión a la base de datos
close_connection(conn)
