from pyknow import *
from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD

# Definición de clases
class Usuario(Fact):
    pass

class RecomendacionPelicula(Fact):
    pass

class Calificacion(Fact):
    pass

class Pelicula(Fact):
    pass

class Clasificacion(Fact):
    pass

class Genero(Fact):
    pass

# Definir la base de conocimiento utilizando redes bayesianas
def create_bayesian_model():
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

    # Definir las distribuciones de probabilidad condicional (CPDs) de las variables

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

    return modelo_bayesiano
