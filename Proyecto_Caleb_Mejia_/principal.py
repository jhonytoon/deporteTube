import tkinter as tk
from interfaz import DeportubeApp
from gestorApi import GestorApi

def main():
    # Inicializa la ventana principal de tkinter
    root = tk.Tk()
    # Crea una instancia de GestorApi con la URL base de la API
    gestorApi = GestorApi("https://v3.football.api-sports.io")
    # Crea una instancia de DeportubeApp y le pasa la ventana principal y el gestorApi
    app = DeportubeApp(root, gestorApi)
    # Inicia el bucle principal de la interfaz gráfica de usuario
    root.mainloop()

if __name__ == "__main__":
    main()
