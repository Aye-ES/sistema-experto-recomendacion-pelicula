import sqlite3
from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD

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
                    email TEXT)''')

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
                    valor INTEGER,
                    FOREIGN KEY (usuario_id) REFERENCES Usuario (id),
                    FOREIGN KEY (pelicula_id) REFERENCES Pelicula (id))''')

# Tabla Pelicula
cursor.execute('''CREATE TABLE IF NOT EXISTS Pelicula (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    titulo TEXT,
                    clasificacion_id INTEGER,
                    FOREIGN KEY (clasificacion_id) REFERENCES Clasificacion (id))''')

# Tabla Clasificacion
cursor.execute('''CREATE TABLE IF NOT EXISTS Clasificacion (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT)''')
#Tabla Genero
cursor.execute('''CREATE TABLE IF NOT EXISTS Genero (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT,
                    pelicula_id INTEGER,
                    FOREIGN KEY (pelicula_id) REFERENCES Pelicula (id))''')


# Cerrar conexión a la base de datos SQLite
def close_connection(conn):
    conn.close()




# Ejemplo de recolección de datos y guardado en la base de datos

def collect_usuario_data():
    usuario_data = [
        #("Leandro", "leandro@gmail.com"),
        # Agrega más datos de usuario aquí
    ]
    cursor.executemany('INSERT INTO Usuario (nombre, email) VALUES (?, ?)', usuario_data)

def collect_recomendacion_data():
    recomendacion_data = [
        # (1, 1),
        # Agrega más datos de recomendación aquí
    ]
    cursor.executemany('INSERT INTO RecomendacionPelicula (usuario_id, pelicula_id) VALUES (?, ?)', recomendacion_data)

def collect_calificacion_data():
    calificacion_data = [
        # (1, 1, 5),
        # Agrega más datos de calificación aquí
    ]
    cursor.executemany('INSERT INTO Calificacion (usuario_id, pelicula_id, valor) VALUES (?, ?, ?)', calificacion_data)

def collect_pelicula_data():
    pelicula_data = [
        # ("Pelicula1", 1),
        # Agrega más datos de película aquí
    ]
    cursor.executemany('INSERT INTO Pelicula (titulo, clasificacion_id) VALUES (?, ?)', pelicula_data)

def collect_clasificacion_data():
    clasificacion_data = [
        # ("Clasificacion1"),
        # Agrega más datos de clasificación aquí
    ]
    cursor.executemany('INSERT INTO Clasificacion (nombre) VALUES (?)', clasificacion_data)

def collect_genero_data():
    genero_data = [
        # ("Genero1", 1),
        # Agrega más datos de género aquí
    ]
    cursor.executemany('INSERT INTO Genero (nombre, pelicula_id) VALUES (?, ?)', genero_data)

# Ejecutar las funciones de recolección de datos
collect_usuario_data()
collect_recomendacion_data()
collect_calificacion_data()
collect_pelicula_data()
collect_clasificacion_data()
collect_genero_data()

# Guardar los cambios en la base de datos
conn.commit()

# Cerrar la conexión a la base de datos
close_connection(conn)
