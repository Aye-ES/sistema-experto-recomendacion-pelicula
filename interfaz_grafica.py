from tkinter import Tk, Button

from base_conocimiento import create_bayesian_model
from motor_inferencia import perform_inference
from conexion_sqlite3 import connect_to_database, close_connection

# Crear instancia de la base de conocimiento utilizando redes bayesianas
modelo_bayesiano = create_bayesian_model()

# Crear ventana
ventana = Tk()

# Función para mostrar las recomendaciones
def mostrar_recomendaciones():
    # Conectar a la base de datos
    conn, cursor = connect_to_database()

    # Realizar inferencia y mostrar recomendaciones
    perform_inference(modelo_bayesiano)

    # Cerrar conexión a la base de datos
    close_connection(conn)

# Botón para obtener recomendaciones
btn_recomendaciones = Button(ventana, text="Obtener Recomendaciones", command=mostrar_recomendaciones)
btn_recomendaciones.pack()

# Ejecutar ventana
ventana.mainloop()
