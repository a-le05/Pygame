import pygame


class Sprite:
    """
    componente que contiene la información grafica necesaria para dibujar uan entidad en patanlla
    la imagen (pygame.Surface) y su dimensiones (ancho, alto).
    """

    def __init__(self, imagen: pygame.Surface, ancho: int, alto: int):
        self.imagen = imagen  # una superficie ya cargada
        self.ancho = ancho  # tamaño de sprite ancho
        self.alto = alto  # tamaño de sprite alto

    def dibujar(self, pantalla, x, y):
        "dibujar muestra la imagen en la pantalla (pygame.Surface), en la posicion (x, y)"
        pantalla.blit(self.imagen, (x, y))
