import requests

class GestorApi:
    def __init__(self, urlBase):
        # URL base de la API
        self.urlBase = urlBase

    def obtenerEventosEnVivo(self):
        # Construye la URL completa para obtener eventos en vivo en una fecha específica
        url = f"{self.urlBase}/fixtures?date=2024-07-15"
        # Encabezados de la solicitud, incluyendo la llave de acceso a la API
        headers = {
            "x-apisports-key": "86d8ea63f1540917c5e894e5b2f66532"
        }
        try:
            # Realiza una solicitud GET a la API
            respuesta = requests.get(url, headers=headers)
            # Lanza una excepción si la respuesta contiene un código de error HTTP
            respuesta.raise_for_status()
            # Devuelve la respuesta en formato JSON
            return respuesta.json()
        except requests.RequestException as e:
            # Imprime un mensaje de error si ocurre una excepción y devuelve None
            print(f"Error al obtener eventos en vivo: {e}")
            return None
