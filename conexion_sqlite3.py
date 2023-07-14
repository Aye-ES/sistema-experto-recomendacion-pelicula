import sqlite3

# Conectar a la base de datos SQLite
def connect_to_database():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    return conn, cursor

# Obtener la conexión y el cursor
conn, cursor = connect_to_database()

# Tabla Usuario
cursor.execute('''CREATE TABLE IF aNOT EXISTS Usuario (
                    id INTEGER PRIMARY KEY,
                    nombre TEXT,
                    email TEXT)''')

# Tabla RecomendacionPelicula
cursor.execute('''CREATE TABLE IF NOT EXISTS RecomendacionPelicula (
                    id INTEGER PRIMARY KEY,
                    usuario_id INTEGER,
                    pelicula_id INTEGER,
                    FOREIGN KEY (usuario_id) REFERENCES Usuario (id),
                    FOREIGN KEY (pelicula_id) REFERENCES Pelicula (id))''')

# Tabla Calificacion
cursor.execute('''CREATE TABLE IF NOT EXISTS Calificacion (
                    id INTEGER PRIMARY KEY,
                    usuario_id INTEGER,
                    pelicula_id INTEGER,
                    valor INTEGER,
                    FOREIGN KEY (usuario_id) REFERENCES Usuario (id),
                    FOREIGN KEY (pelicula_id) REFERENCES Pelicula (id))''')

# Tabla Pelicula
cursor.execute('''CREATE TABLE IF NOT EXISTS Pelicula (
                    id INTEGER PRIMARY KEY,
                    titulo TEXT,
                    clasificacion_id INTEGER,
                    FOREIGN KEY (clasificacion_id) REFERENCES Clasificacion (id))''')

# Tabla Clasificacion
cursor.execute('''CREATE TABLE IF NOT EXISTS Clasificacion (
                    id INTEGER PRIMARY KEY,
                    nombre TEXT)''')

# Tabla Genero
cursor.execute('''CREATE TABLE IF NOT EXISTS Genero (
                    id INTEGER PRIMARY KEY,
                    nombre TEXT)''')

# Cerrar conexión a la base de datos SQLite
def close_connection(conn):
    conn.close()





# Función para crear un nuevo usuario
def create_usuario(nombre, email):
    # Insertar un nuevo usuario
    cursor.execute("INSERT INTO Usuario (nombre, email) VALUES (?, ?)", (nombre, email))
    conn.commit()

# Ejemplo de creación de usuario
nombre = "Neil Edson Chilimani Cuellar"
email = "neil20cuellar1@gmail.com"
create_usuario(nombre, email)

# Cerrar la conexión a la base de datos
close_connection(conn)