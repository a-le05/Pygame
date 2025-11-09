import pygame
class Colision:
    """
    Es un componente de datos que define el área de colisión de uan entidad mediante un
    rectangulo (pygame.Rect)
    """
    def __init__(self, ancho: int, alto: int, offset_x: int = 0, offset_y: int = 0):
        self.rect = pygame.Rect(0, 0, ancho, alto)  # Crea rectangulo que define el area de colision
        self.offset_x = offset_x  # ajusta el el rectangulo dentro del sprite en x
        self.offset_y = offset_y  # ajusta el rectangulo dentro del sprite en y

    def actualizar_posicion(self, x, y):
        """
        Sincroniza el rectángulo de colisión con la posición del Transform.
        si la entidad se mueve o gira, el area de colision se mantiene alineada a su posicion.
        """
        self.rect.topleft = (x + self.offset_x, y + self.offset_y)
