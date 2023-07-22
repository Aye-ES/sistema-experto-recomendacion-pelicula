# interfaz_usuario.py
import tkinter as tk
import sqlite3
from motor_inferencia import verificar_credenciales
from base_conocimiento import recomendar_pelicula
from tkinter import ttk


genero_var = None
clasificacion_var = None
#titulo_pelicula_recomendada = None
#director_pelicula_recomendada = None
main_window = None

###############################
def obtener_recomendacion():
    genero_seleccionado = genero_var.get()
    clasificacion_seleccionada = clasificacion_var.get()

    # Llamar a la función para obtener la recomendación de película
    pelicula_recomendada = recomendar_pelicula(genero_seleccionado, clasificacion_seleccionada)

    if pelicula_recomendada:
        # Obtener el título y el director de la película recomendada
        titulo_pelicula_recomendada = pelicula_recomendada["titulo"]
        director_pelicula_recomendada = pelicula_recomendada["director"]

        # Mostrar la recomendación en la interfaz gráfica
        recomendacion_label = tk.Label(main_window, text=f"Película recomendada: {titulo_pelicula_recomendada} (Director: {director_pelicula_recomendada})", font=("Arial", 12))
        recomendacion_label.pack(pady=10)
    else:
        # Si no hay recomendación, mostrar un mensaje
        recomendacion_label = tk.Label(main_window, text="No se encontró una película recomendada para los criterios seleccionados.", font=("Arial", 12))
        recomendacion_label.pack(pady=10)
        #####################################333

def login():
    email = email_var.get()
    password = password_var.get()

    nombre_usuario = verificar_credenciales(email, password)
    if nombre_usuario:
        show_main_window(nombre_usuario)
    else:
        error_label = tk.Label(login_window, text="Credenciales incorrectas", fg="red")
        error_label.place(relx=0.5, rely=0.9, anchor="center")
        login_window.after(2000, error_label.destroy)

def show_main_window(nombre_usuario):
    global main_window, genero_var, clasificacion_var  # Agregamos las variables globales aquí

    main_window = tk.Tk()
    main_window.title("Sistema de Películas")
    main_window.geometry("600x400")

    # Crear un estilo personalizado para los menús desplegables
    style = ttk.Style()
    style.theme_use("clam")  # Puedes cambiar el tema aquí ("clam", "alt", "default", etc.)

    # Estilo para el menú desplegable de género
    style.configure("TMenubutton", background="lightblue", borderwidth=2, relief="flat", font=("Arial", 12))

    # Estilo para el menú desplegable de clasificación
    style.configure("TCombobox", background="lightgreen", borderwidth=2, relief="flat", font=("Arial", 12))

    # Bienvenida
    welcome_label = tk.Label(main_window, text=f"Bienvenido, {nombre_usuario}!", font=("Arial", 16))
    welcome_label.pack(pady=20)

    # Primera sección
    frame_seccion1 = tk.Frame(main_window)
    frame_seccion1.pack(pady=20)

    pelicula_label = tk.Label(frame_seccion1, text="Película Favorita:")
    pelicula_label.pack(side=tk.LEFT, padx=10)

    pelicula_var = tk.StringVar()
    pelicula_entry = tk.Entry(frame_seccion1, textvariable=pelicula_var)
    pelicula_entry.pack(side=tk.LEFT, padx=10)

    # Segunda sección
    frame_seccion2 = tk.Frame(main_window)
    frame_seccion2.pack(pady=20)

      # Menú desplegable de género
    generos = obtener_generos()  # Obtener los géneros de la base de datos
    genero_var = tk.StringVar()
    genero_var.set(generos[0])  # Establecer el valor inicial del menú al primer género
    genero_menu = ttk.OptionMenu(frame_seccion2, genero_var, *generos)
    genero_menu["menu"].configure(bg="lightblue")  # Establecer el color de fondo del menú desplegable
    genero_menu.pack(side=tk.LEFT, padx=10)



    # Menú desplegable de clasificación
    clasificaciones = obtener_clasificaciones()  # Obtener las clasificaciones de la base de datos
    clasificacion_var = tk.StringVar()
    clasificacion_var.set(clasificaciones[0])  # Establecer el valor inicial del menú a la primera clasificación
    clasificacion_menu = ttk.OptionMenu(frame_seccion2, clasificacion_var, *clasificaciones)
    clasificacion_menu["menu"].configure(bg="lightgreen")  # Establecer el color de fondo del menú desplegable
    clasificacion_menu.pack(side=tk.LEFT, padx=10)
   ###############3
    recomendar_button = tk.Button(main_window, text="Recomendar Película", command=obtener_recomendacion)
    recomendar_button.pack(pady=10)
############################

    main_window.mainloop()



def obtener_generos():
    # Función para obtener los géneros desde la base de datos
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT nombre FROM Genero')
    generos = [row[0] for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return generos

def obtener_clasificaciones():
    # Función para obtener las clasificaciones desde la base de datos
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT nombre FROM Clasificacion')
    clasificaciones = [row[0] for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return clasificaciones

def show_login_window():
    global email_var, password_var, login_window

    login_window = tk.Tk()
    login_window.title("Inicio de sesión")
    login_window.configure(bg="lightgray")

    screen_width = login_window.winfo_screenwidth()
    screen_height = login_window.winfo_screenheight()
    window_width = 400
    window_height = 300
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    login_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    email_var = tk.StringVar()
    password_var = tk.StringVar()

    email_label = tk.Label(login_window, text="Correo electrónico:")
    email_label.place(relx=0.5, rely=0.35, anchor="center")
    email_entry = tk.Entry(login_window, textvariable=email_var)
    email_entry.place(relx=0.5, rely=0.4, anchor="center")

    password_label = tk.Label(login_window, text="Contraseña:")
    password_label.place(relx=0.5, rely=0.55, anchor="center")
    password_entry = tk.Entry(login_window, show="*", textvariable=password_var)
    password_entry.place(relx=0.5, rely=0.6, anchor="center")

    login_button = tk.Button(login_window, text="Iniciar sesión", command=login)
    login_button.place(relx=0.5, rely=0.75, anchor="center")

    login_window.mainloop()

def main():
    show_login_window()

if __name__ == "__main__":
    main()
