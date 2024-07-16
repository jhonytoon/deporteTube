import tkinter as tk
from tkinter import messagebox
from gestorApi import GestorApi

class GestorFiltros:
    def __init__(self, app):
        # Referencia a la instancia de la aplicación principal
        self.app = app

    def obtenerEventosEnVivo(self, gestorApi):
        # Obtiene eventos en vivo desde la API y actualiza la interfaz con ligas y países únicos
        eventos = gestorApi.obtenerEventosEnVivo()
        if eventos:
            self.app.eventosEnVivo = eventos["response"]
            ligas = ["Sin selección"] + sorted(set(evento["league"]["name"] for evento in self.app.eventosEnVivo))
            paises = ["Sin selección"] + sorted(set(evento["league"]["country"] for evento in self.app.eventosEnVivo))
            self.app.ligaMenu['values'] = ligas
            self.app.paisMenu['values'] = paises
            self.actualizarEquipos()
        else:
            messagebox.showerror("Error", "No se pudieron obtener eventos en vivo.")

    def actualizarEquipos(self, event=None):
        # Actualiza la lista de equipos basada en la selección de liga y país
        liga = self.app.ligaVar.get()
        pais = self.app.paisVar.get()

        equipos_filtrados = set()
        for evento in self.app.eventosEnVivo:
            if (liga == "Sin selección" or evento["league"]["name"] == liga) and (pais == "Sin selección" or evento["league"]["country"] == pais):
                equipos_filtrados.add(evento["teams"]["home"]["name"])
                equipos_filtrados.add(evento["teams"]["away"]["name"])

        equipos = ["Sin selección"] + sorted(equipos_filtrados)
        self.app.equipoMenu['values'] = equipos

    def filtrarEventos(self):
        # Filtra los eventos deportivos basados en los criterios seleccionados y actualiza la interfaz
        liga = self.app.ligaVar.get()
        pais = self.app.paisVar.get()
        equipo = self.app.equipoVar.get()

        eventosFiltrados = []
        for evento in self.app.eventosEnVivo:
            estado_corto = evento["fixture"]["status"]["short"]
            estado_legible = self.get_estado_legible(estado_corto)

            if liga != "Sin selección" and equipo != "Sin selección":
                if evento["league"]["name"] == liga and (evento["teams"]["home"]["name"] == equipo or evento["teams"]["away"]["name"] == equipo):
                    marcador = self.get_marcador(evento, estado_corto)
                    eventosFiltrados.append((evento, estado_legible, marcador))
            elif pais != "Sin selección" and equipo != "Sin selección":
                if evento["league"]["country"] == pais and (evento["teams"]["home"]["name"] == equipo or evento["teams"]["away"]["name"] == equipo):
                    marcador = self.get_marcador(evento, estado_corto)
                    eventosFiltrados.append((evento, estado_legible, marcador))
            elif liga != "Sin selección":
                if evento["league"]["name"] == liga:
                    marcador = self.get_marcador(evento, estado_corto)
                    eventosFiltrados.append((evento, estado_legible, marcador))
            elif pais != "Sin selección":
                if evento["league"]["country"] == pais:
                    marcador = self.get_marcador(evento, estado_corto)
                    eventosFiltrados.append((evento, estado_legible, marcador))
            elif equipo != "Sin selección":
                if evento["teams"]["home"]["name"] == equipo or evento["teams"]["away"]["name"] == equipo:
                    marcador = self.get_marcador(evento, estado_corto)
                    eventosFiltrados.append((evento, estado_legible, marcador))

        self.app.mostrarEventosFiltrados(eventosFiltrados)

    def get_estado_legible(self, estado_corto):
        # Convierte los códigos de estado cortos en etiquetas legibles
        estados = {
            "TBD": "Sin fecha",
            "FT": "Finalizado",
            "NS": "Proximamente",
            "2H": "En vivo",
            "1H": "En vivo",
            "PEN": "Finalizado-penales",
            "ET": "Tiempo extra"
        }
        return estados.get(estado_corto, "Desconocido")

    def get_marcador(self, evento, estado_corto):
        # Determina el marcador correcto basado en el estado del evento
        if estado_corto in ["1H", "2H", "ET"]:
            return f"{evento['goals']['home']} - {evento['goals']['away']}"
        elif estado_corto == "FT":
            return f"{evento['score']['fulltime']['home']} - {evento['score']['fulltime']['away']}"
        elif estado_corto == "NS":
            return "--"
        elif estado_corto == "PEN":
            return f"Penales: {evento['score']['penalty']['home']} - {evento['score']['penalty']['away']}"
        else:
            return ""
