class Vida:
    """
    componente vida  alamacena el estado de salud de uan entidad
    cuanto daño recibe antes de ser destruida
    """
    def __init__(self, max_vida):
        self.max = max_vida  # vida maxima de entidad
        self.actual = max_vida  # vida actual que ira disminnuyendo

    def recibir_danio(self, cantidad):
        """
        cantidad normalmente proviene del componente Dano de otra entidad (ej. bala).
        """
        self.actual -= cantidad
        if self.actual < 0:  # nos aseguramos que actual nunca sea negativo.
            self.actual = 0

    def esta_muerto(self):
        """
        Método que devuelve True si la entidad ya no tiene vida.
        """
        return self.actual <= 0
