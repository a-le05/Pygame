import pygame

class SistemaPuntuacion:
    def __init__(self, fuente, color=(255, 255, 255)):
        self.puntos = 0  # contador de la puntuación.
        self.fuente = fuente  # objeto pygame.font.Font para renderizar texto.
        self.color = color  # color del texto (por defecto blanco).

    def sumar_puntos(self, cantidad):
        self.puntos += cantidad  # Incrementa los puntos actuales.

    def dibujar(self, pantalla):
        texto = self.fuente.render(f"Puntuación: {self.puntos}", True, self.color)  # Renderiza un texto con la puntuación.
        pantalla.blit(texto, (20, 20))  # Lo dibuja en la esquina superior izquierda de la pantalla.