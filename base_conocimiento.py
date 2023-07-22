import random

# Lista de películas ficticias (puedes agregar más)
peliculas = [
    {"titulo": "Francotirador", "director": "Clint Eastwood", "genero": "Acción", "clasificacion": "Personas mayores de 15 años"},
    {"titulo": "Atraccion Peligrosa", "director": "Ben Affleck", "genero": "Suspenso", "clasificacion": "Personas mayores de 15 años"},
    {"titulo": "E.T", "director": "Steven Spielberg", "genero": "Ciencia Ficción", "clasificacion": "Personas menores de 15 años"},
    {"titulo": "Corazonada", "director": "Alejandro Montiel", "genero": "Suspenso", "clasificacion": "Personas mayores de 15 años"},
    {"titulo": "Harry Potter", "director": "Chris Columbus", "genero": "Fantasía", "clasificacion": "Personas mayores de 15 años"},
]

def recomendar_pelicula(genero_seleccionado, clasificacion_seleccionada):
    # Filtrar películas que coincidan con el género y clasificación seleccionados
    peliculas_filtradas = [pelicula for pelicula in peliculas if pelicula["genero"] == genero_seleccionado and pelicula["clasificacion"] == clasificacion_seleccionada]

    if not peliculas_filtradas:
        return None  # No hay películas que cumplan con los criterios seleccionados

    # Elegir una película al azar de las películas filtradas
    pelicula_recomendada = random.choice(peliculas_filtradas)
    return pelicula_recomendada
