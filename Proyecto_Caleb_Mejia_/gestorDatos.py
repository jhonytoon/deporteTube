import pandas as pd

class GestorDatos:
    def __init__(self, datos):
        self.datos = pd.DataFrame(datos)  # Convierte los datos proporcionados en un DataFrame de pandas

    def prepararDatos(self):
        if 'fixture' in self.datos.columns:
            self.datos['inicioTimestamp'] = pd.to_datetime(self.datos['fixture'].apply(lambda x: x['date']))  # Convierte la columna de fechas a formato datetime
        self.datos.fillna(0, inplace=True)  # Llena los valores nulos con 0
        return self.datos

    def resumirDatos(self):
        return self.datos.describe()  # Devuelve un resumen estadístico del DataFrame

# Ejemplo de uso:
# datos = [{'fixture': {'date': '2024-07-11T18:00:00Z'}, 'teams': {'home': 'Team A', 'away': 'Team B'}, 'league': 'League A', 'round': 'Round 1', 'goals': {'home': 2, 'away': 1}, 'score': {'fulltime': {'home': 2, 'away': 1}}}]
# gestor_datos = GestorDatos(datos)
# datos_preparados = gestor_datos.prepararDatos()
# resumen = gestor_datos.resumirDatos()
# print(datos_preparados)
# print(resumen)
