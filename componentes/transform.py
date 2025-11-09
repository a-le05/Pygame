class Transform:
    """
    Componente que define la posición, rotación y escala de una entidad.
    """
    def __init__(self, x: float = 0, y: float = 0, rotacion: float = 0, escala: float = 1):
        self.x = x  # coordenadas del mundo x
        self.y = y  # coordenadas del mundo y
        self.rotacion = rotacion  # ángulo de rotacion en grados
        self.escala = escala  # tamaño para renderizado o colisiones

    @property
    def posicion(self):
        """
        Muy útil para pasar directamente a funciones de Pygame o sistemas que esperan coordenadas en tuplas
        pantalla.blit(sprite.imagen, transform.posicion)
        """
        return (self.x, self.y)