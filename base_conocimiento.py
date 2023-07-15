from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD

def create_bayesian_model():
    # Crear el objeto de la red bayesiana
    modelo_bayesiano = BayesianModel()

    # Definir las variables
    variables = ["Usuario", "RecomendacionPelicula", "Calificacion", "Pelicula", "Clasificacion", "Genero"]

    # Agregar las variables al modelo
    modelo_bayesiano.add_nodes_from(variables)

    # Definir las relaciones entre las variables
    modelo_bayesiano.add_edges_from([
        ("Usuario", "RecomendacionPelicula"),
        ("Usuario", "Calificacion"),
        ("Pelicula", "RecomendacionPelicula"),
        ("Pelicula", "Calificacion"),
        ("Clasificacion", "Pelicula"),
        ("Genero", "Pelicula")
    ])

    # Definir las distribuciones de probabilidad condicional (CPDs) de las variables

     # Definir CPD para la variable "Usuario"
    cpd_usuario = TabularCPD(variable="Usuario", variable_card=2, values=[[0.6, 0.4]])

    # Definir CPD para la variable "RecomendacionPelicula"
    cpd_recomendacion = TabularCPD(variable="RecomendacionPelicula", variable_card=2,
                                   values=[[0.3, 0.6, 0.1, 0.9], [0.7, 0.4, 0.9, 0.1]],
                                   evidence=["Usuario", "Pelicula"],
                                   evidence_card=[2, 2])

    # Definir CPD para la variable "Calificacion"
    cpd_calificacion = TabularCPD(variable="Calificacion", variable_card=2,
                                  values=[[0.2, 0.8], [0.7, 0.3]],
                                  evidence=["Usuario", "Pelicula"],
                                  evidence_card=[2, 2])

    # Definir CPD para la variable "Pelicula"
    cpd_pelicula = TabularCPD(variable="Pelicula", variable_card=2,
                              values=[[0.3, 0.7], [0.6, 0.4], [0.8, 0.2], [0.1, 0.9]],
                              evidence=["Clasificacion", "Genero"],
                              evidence_card=[2, 2])

    # Definir CPD para la variable "Clasificacion"
    cpd_clasificacion = TabularCPD(variable="Clasificacion", variable_card=2, values=[[0.5, 0.5]])

    # Definir CPD para la variable "Genero"
    cpd_genero = TabularCPD(variable="Genero", variable_card=2, values=[[0.5, 0.5]])

    # Asociar los CPDs al modelo
    modelo_bayesiano.add_cpds(cpd_usuario, cpd_recomendacion, cpd_calificacion, cpd_pelicula, cpd_clasificacion,
                              cpd_genero)

    return modelo_bayesiano


# Crear la base de conocimiento utilizando el modelo bayesiano
base_conocimiento = create_bayesian_model()
