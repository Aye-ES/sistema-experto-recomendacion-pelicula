from pgmpy.inference import VariableElimination

# Realizar inferencias utilizando el motor de inferencia
def perform_inference(modelo_bayesiano):
    # Crear un objeto de VariableElimination para realizar inferencias
    inferencia = VariableElimination(modelo_bayesiano)

    # Realizar una inferencia específica
    resultado = inferencia.query(variables=["RecomendacionPelicula"], evidence={"Usuario": 1})
    print(resultado)
