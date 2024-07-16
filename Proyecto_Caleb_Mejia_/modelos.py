class Pais:
    def __init__(self, alpha2, alpha3, nombre):
        self.alpha2 = alpha2  # Código de país de 2 letras (ISO 3166-1 alpha-2)
        self.alpha3 = alpha3  # Código de país de 3 letras (ISO 3166-1 alpha-3)
        self.nombre = nombre  # Nombre completo del país

class ColoresEquipo:
    def __init__(self, primario, secundario, texto):
        self.primario = primario  # Color primario del equipo
        self.secundario = secundario  # Color secundario del equipo
        self.texto = texto  # Color del texto (usado en uniformes)

class Equipo:
    def __init__(self, nombre, slug, nombreCorto, id, pais, colores):
        self.nombre = nombre  # Nombre completo del equipo
        self.slug = slug  # Identificador único del equipo en formato de texto
        self.nombreCorto = nombreCorto  # Nombre corto o abreviado del equipo
        self.id = id  # Identificador único del equipo
        self.pais = pais  # Objeto de la clase Pais asociado al equipo
        self.colores = colores  # Objeto de la clase ColoresEquipo que describe los colores del equipo

class EstadoPartido:
    def __init__(self, codigo, descripcion, tipo):
        self.codigo = codigo  # Código del estado del partido
        self.descripcion = descripcion  # Descripción del estado del partido
        self.tipo = tipo  # Tipo de estado del partido (ej. finalizado, en vivo)

class Ronda:
    def __init__(self, ronda, nombre, slug, tipoCopa):
        self.ronda = ronda  # Número de la ronda en el torneo
        self.nombre = nombre  # Nombre de la ronda
        self.slug = slug  # Identificador único de la ronda en formato de texto
        self.tipoCopa = tipoCopa  # Tipo de copa o torneo

class Temporada:
    def __init__(self, nombre, year, id):
        self.nombre = nombre  # Nombre de la temporada
        self.year = year  # Año de la temporada
        self.id = id  # Identificador único de la temporada

class Torneo:
    def __init__(self, nombre, slug, categoria, deporte, id, temporada, estado, equipoLocal, equipoVisitante, inicioTimestamp, soloResultadoFinal, ronda):
        self.nombre = nombre  # Nombre del torneo
        self.slug = slug  # Identificador único del torneo en formato de texto
        self.categoria = categoria  # Categoría del torneo (ej. juvenil, profesional)
        self.deporte = deporte  # Tipo de deporte (ej. fútbol, baloncesto)
        self.id = id  # Identificador único del torneo
        self.temporada = temporada  # Objeto de la clase Temporada asociado al torneo
        self.estado = estado  # Objeto de la clase EstadoPartido que describe el estado del torneo
        self.equipoLocal = equipoLocal  # Objeto de la clase Equipo que representa al equipo local
        self.equipoVisitante = equipoVisitante  # Objeto de la clase Equipo que representa al equipo visitante
        self.inicioTimestamp = inicioTimestamp  # Fecha y hora de inicio del torneo
        self.soloResultadoFinal = soloResultadoFinal  # Indica si solo se muestra el resultado final del torneo
        self.ronda = ronda  # Objeto de la clase Ronda que describe la ronda del torneo

    def __str__(self):
        return f"Torneo: {self.nombre}, Categoría: {self.categoria}, Deporte: {self.deporte}"
