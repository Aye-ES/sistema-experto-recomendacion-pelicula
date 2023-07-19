import tkinter as tk
import sqlite3


# Función para iniciar sesión
def login():
    # Obtener los valores de correo electrónico y contraseña ingresados por el usuario
    email = email_var.get()
    password = password_var.get()

    # Realizar la lógica de autenticación y validación de datos
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Verificar si el correo electrónico y la contraseña coinciden en la base de datos
    cursor.execute('SELECT * FROM Usuario WHERE email = ? AND password = ?', (email, password))
    user = cursor.fetchone()

    if user:
        # Cerrar la conexión a la base de datos
        conn.close()
        login_window.destroy()  # Cerrar la ventana de inicio de sesión

        # Mostrar mensaje de éxito
        success_label = tk.Label(login_window, text="Inicio de sesión exitoso", fg="green")
        success_label.place(relx=0.5, rely=0.9, anchor="center")

        # Aquí puedes continuar con la lógica de tu programa, como mostrar la ventana principal, realizar recomendaciones, etc.
        show_main_window()
    else:
        # Cerrar la conexión a la base de datos
        conn.close()

        # Mostrar mensaje de error
        error_label = tk.Label(login_window, text="Credenciales incorrectas", fg="red")
        error_label.place(relx=0.5, rely=0.9, anchor="center")

    # Cerrar la ventana de inicio de sesión después de verificar las credenciales
    login_window.after(2000, login_window.destroy)


# Ventana de inicio de sesión
def show_login_window():
    global email_var, password_var, login_window  # Definir las variables como globales

    login_window = tk.Tk()

    # Configurar la ventana de inicio de sesión
    login_window.title("Inicio de sesión")
    login_window.configure(bg="lightgray")  # Establecer el color de fondo

    # Obtener el tamaño de la pantalla
    screen_width = login_window.winfo_screenwidth()
    screen_height = login_window.winfo_screenheight()

    # Calcular las coordenadas para centrar la ventana en la pantalla
    window_width = 400
    window_height = 300
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)

    # Establecer la geometría de la ventana
    login_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Variables de control para los campos de correo electrónico y contraseña
    email_var = tk.StringVar()
    password_var = tk.StringVar()

    # Crear etiqueta y campo de entrada para correo electrónico
    email_label = tk.Label(login_window, text="Correo electrónico:")
    email_label.place(relx=0.5, rely=0.35, anchor="center")
    email_entry = tk.Entry(login_window, textvariable=email_var)
    email_entry.place(relx=0.5, rely=0.4, anchor="center")

    # Crear etiqueta y campo de entrada para contraseña
    password_label = tk.Label(login_window, text="Contraseña:")
    password_label.place(relx=0.5, rely=0.55, anchor="center")
    password_entry = tk.Entry(login_window, show="*", textvariable=password_var)
    password_entry.place(relx=0.5, rely=0.6, anchor="center")

    # Crear botón de inicio de sesión
    login_button = tk.Button(login_window, text="Iniciar sesión", command=login)
    login_button.place(relx=0.5, rely=0.75, anchor="center")

    # Ejecutar el bucle principal de la ventana de inicio de sesión
    login_window.mainloop()
    #############################################





    
# Ventana de registro de usuario
def show_register_window():
    register_window = tk.Tk()
    # Configurar la ventana de registro de usuario
    # ...
    register_window.mainloop()

# Ventana principal
def show_main_window():
    main_window = tk.Tk()
    # Configurar la ventana principal
    # ...
    main_window.mainloop()





# Función principal
def main():
    # Lógica principal del programa
    show_login_window()

# Punto de entrada del programa
if __name__ == "__main__":
    main()
