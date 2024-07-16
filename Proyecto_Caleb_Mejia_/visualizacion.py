import matplotlib.pyplot as plt
import pandas as pd

# Diccionario de estados
estados = {
    "TBD": "Sin fecha",
    "FT": "Finalizado",
    "NS": "Proximamente",
    "2H": "En vivo",
    "1H": "En vivo",
    "PEN": "Finalizado-penales",
    "ET": "Tiempo extra"
}

def graficarDatos(datos, titulo="Datos Deportivos"):
    # Grafica los datos proporcionados en un DataFrame de pandas
    if datos.empty:
        print("No hay datos para visualizar.")
        return

    plt.figure(figsize=(10, 5))
    for columna in datos.columns:
        if columna not in ['inicioTimestamp', 'teams', 'league', 'round', 'goals', 'score']:
            plt.plot(datos['inicioTimestamp'], datos[columna], marker='o', label=columna)
    plt.title(titulo)
    plt.xlabel('Fecha')
    plt.ylabel('Valores')
    plt.grid(True)
    plt.legend()
    plt.show()

def graficarResultadosPorEstado(eventos):
    # Grafica la cantidad de eventos por cada estado
    if not eventos:
        print("No hay eventos para visualizar.")
        return

    conteo_estados = {estado: 0 for estado in estados.values()}
    for evento in eventos:
        estado_corto = evento["fixture"]["status"]["short"]
        estado_legible = estados.get(estado_corto, "Desconocido")
        if estado_legible in conteo_estados:
            conteo_estados[estado_legible] += 1

    conteo_estados = {k: v for k, v in conteo_estados.items() if v > 0}

    plt.figure(figsize=(10, 5))
    plt.bar(conteo_estados.keys(), conteo_estados.values(), color='blue')
    plt.title('Cantidad de Eventos por Estado')
    plt.xlabel('Estado')
    plt.ylabel('Cantidad de Eventos')
    plt.grid(True)
    plt.show()
