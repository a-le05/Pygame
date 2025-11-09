class Bala:
    def __init__(self, velocidad=5, angulo=0, owner=None):
        """
        bala es un componente de identidad, define el comportamiento base de un proyectil.
        guarda toda la informacion esencial de una bala
        """
        self.velocidad = velocidad  # cuánto se moverá cada frame.
        self.angulo = angulo  # direccion en la que se dispara
        self.owner = owner  # guarda una referencia a la entidad que disparo la bala
