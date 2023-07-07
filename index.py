import sqlite3
from pyknow import *

from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination


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


# Definir la estructura de la red bayesiana

# Crear el objeto de la red bayesiana
modelo_bayesiano = BayesianModel()

# Definir las variables
variables = ["Usuario", "Genero", "Calificacion", "RecomendacionPelicula"]

# Agregar las variables al modelo
modelo_bayesiano.add_nodes_from(variables)

# Definir las relaciones entre las variables
modelo_bayesiano.add_edges_from([
    ("Usuario", "Calificacion"),
    ("Genero", "RecomendacionPelicula"),
    ("Calificacion", "RecomendacionPelicula")
])


# Definir las distribuciones de probabilidad condicional (CPDs) de las siguientes variables:

# Definir CPD para la variable "Usuario"
cpd_usuario = TabularCPD(variable="Usuario", variable_card=2, values=[[0.6, 0.4]])

# Definir CPD para la variable "Genero"
cpd_genero = TabularCPD(variable="Genero", variable_card=2, values=[[0.5, 0.5]])

# Definir CPD para la variable "Calificacion"
cpd_calificacion = TabularCPD(variable="Calificacion", variable_card=2,
                             values=[[0.2, 0.8], [0.7, 0.3]],
                             evidence=["Usuario"], evidence_card=[2])

# Definir CPD para la variable "RecomendacionPelicula"
cpd_recomendacion = TabularCPD(variable="RecomendacionPelicula", variable_card=2,
                              values=[[0.3, 0.6, 0.1, 0.9], [0.7, 0.4, 0.9, 0.1]],
                              evidence=["Genero", "Calificacion"],
                              evidence_card=[2, 2])

# Asociar los CPDs al modelo
modelo_bayesiano.add_cpds(cpd_usuario, cpd_genero, cpd_calificacion, cpd_recomendacion)



# Realizar inferencias utilizando el motor de inferencia:
# Crear un objeto de VariableElimination para realizar inferencias
inferencia = VariableElimination(modelo_bayesiano)

# Realizar una inferencia específica
resultado = inferencia.query(variables=["RecomendacionPelicula"], evidence={"Usuario": 1})
print(resultado)
