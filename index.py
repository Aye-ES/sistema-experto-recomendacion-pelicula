import sqlite3
from pyknow import *

# Definición de clases
class Usuario(Fact):
    pass

class RecomendacionPelicula(Fact):
    pass

class Calificacion(Fact):
    pass

class Sistema:
    def __init__(self):
        self.conn = sqlite3.connect('database.db')
        self.cursor = self.conn.cursor()

    def obtener_recomendaciones(self, usuario):
        # Lógica para obtener recomendaciones
        pass

class Pelicula(Fact):
    pass

class Clasificacion(Fact):
    pass

class Genero(Fact):
    pass




conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Tabla Usuario
cursor.execute('''CREATE TABLE IF NOT EXISTS Usuario (
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

# Guardar cambios y cerrar conexión
conn.commit()
conn.close()




