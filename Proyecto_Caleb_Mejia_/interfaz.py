import tkinter as tk
from tkinter import ttk, PhotoImage, messagebox
from filtros import GestorFiltros
import visualizacion

class DeportubeApp:
    def __init__(self, root, gestorApi):
        """
        Inicializa la interfaz de la aplicación Deportube.
        root: Ventana raíz de tkinter.
        gestorApi: Instancia de GestorApi para manejar las solicitudes a la API.
        """
        self.root = root
        self.gestorApi = gestorApi
        self.filtros = GestorFiltros(self)  # Instancia de GestorFiltros
        self.root.title("Deportube")
        self.root.geometry("800x900")
        self.root.configure(bg="#ADD8E6")

        # Lista para almacenar los eventos deportivos en vivo
        self.eventosEnVivo = []

        # Variables tkinter StringVar para almacenar las selecciones del usuario
        self.ligaVar = tk.StringVar(value="Sin selección")
        self.paisVar = tk.StringVar(value="Sin selección")
        self.equipoVar = tk.StringVar(value="Sin selección")

        # Listas para almacenar las opciones originales de ligas, países y equipos
        self.lista_original_liga = []
        self.lista_original_pais = []
        self.lista_original_equipo = []

        self.crearInterfaz()

    def crearInterfaz(self):
        """
        Crea y organiza los elementos de la interfaz gráfica.
        """
        try:
            # Cargar la imagen del balón de fútbol
            self.imagenBalon = PhotoImage(file="balon.png")
        except Exception as e:
            print(f"Error al cargar la imagen: {e}")
            self.imagenBalon = None

        # Botón para cargar eventos en vivo
        self.botonEventosEnVivo = tk.Button(
            self.root, text="Cargar eventos",
            command=lambda: self.filtros.obtenerEventosEnVivo(self.gestorApi),
            bg="light gray", image=self.imagenBalon, compound="bottom",width=300, height=200
        )
        self.botonEventosEnVivo.pack(pady=10)

        # Etiqueta de título
        self.label = tk.Label(self.root, text="Eventos Deportivos", bg="#ADD8E6")
        self.label.pack(pady=10)

        # Etiqueta y lista desplegable para Liga
        self.ligaLabel = tk.Label(self.root, text="Liga", bg="#ADD8E6")
        self.ligaLabel.pack()
        self.ligaMenu = self.crear_combobox(self.ligaVar, self.filtros.actualizarEquipos)
        self.ligaMenu.pack(pady=5, ipadx=30)

        # Etiqueta y lista desplegable para País
        self.paisLabel = tk.Label(self.root, text="País", bg="#ADD8E6")
        self.paisLabel.pack()
        self.paisMenu = self.crear_combobox(self.paisVar, self.filtros.actualizarEquipos)
        self.paisMenu.pack(pady=5, ipadx=30)

        # Etiqueta y lista desplegable para Equipo
        self.equipoLabel = tk.Label(self.root, text="Equipo", bg="#ADD8E6")
        self.equipoLabel.pack()
        self.equipoMenu = self.crear_combobox(self.equipoVar, lambda event: None)
        self.equipoMenu.pack(pady=5, ipadx=30)

        # Botón para filtrar y mostrar eventos
        self.botonFiltrarEventos = tk.Button(
            self.root, text="Mostrar Todos los Eventos",
            command=lambda: self.filtros.filtrarEventos(),
            bg="light gray"
        )
        self.botonFiltrarEventos.pack(pady=10)

        # Treeview para mostrar los eventos filtrados
        self.tree = ttk.Treeview(self.root, columns=("Equipo local", "Equipo visitante", "Estado", "Marcador"), show="headings")
        self.tree.heading("Equipo local", text="Equipo local")
        self.tree.heading("Equipo visitante", text="Equipo visitante")
        self.tree.heading("Estado", text="Estado")
        self.tree.heading("Marcador", text="Marcador")
        self.tree.column("Equipo local", anchor="center")
        self.tree.column("Equipo visitante", anchor="center")
        self.tree.column("Estado", anchor="center")
        self.tree.column("Marcador", anchor="center")
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Botón para ejecutar la visualización
        self.botonVisualizacion = tk.Button(
            self.root, text="Visualizar estado de partidos",
            command=self.visualizarResultados,
            bg="light gray"
        )
        self.botonVisualizacion.pack(pady=10)

    def crear_combobox(self, variable, command):
        """
        Crea un combobox con una variable y un comando específico.
        variable: command:
        """
        combobox = ttk.Combobox(self.root, textvariable=variable, state='readonly')
        combobox.bind("<<ComboboxSelected>>", command)
        return combobox

    def mostrarEventosFiltrados(self, eventosFiltrados):
        """
        Muestra los eventos filtrados en el Treeview.
        con sus estados y marcadores.
        """
        for row in self.tree.get_children():
            self.tree.delete(row)

        for evento, estado, marcador in eventosFiltrados:
            self.tree.insert("", "end", values=(evento["teams"]["home"]["name"], evento["teams"]["away"]["name"], estado, marcador))

    def visualizarResultados(self):
        """
        Ejecuta la visualización de los resultados.
        """
        visualizacion.graficarResultadosPorEstado(self.eventosEnVivo)
