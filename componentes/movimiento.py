class Movimiento:
    """
    movimiento es un componente de datos fisicos y cinematicos.
    tiene valores de como una entidad puede moverse
    velocidad máxima de desplazamiento lineal (adelante o atrás)
    velociddd máxima de rotación (giro sobre su eje)
    """

    def __init__(self, velocidad=0, velocidad_rotacion=0):
        self.velocidad_actual = 0  # guarada la velocidad
        self.velocidad_rotacion_actual = 0  # guarda velocidad de toracion
        self.velocidad_max = velocidad  # velocidad maxima que puede alcanzar
        self.velocidad_rotacion_max = velocidad_rotacion  # velocidad maxima en grados por frame (que tan rapido gira)
        self.aceleracion = 0.1  # define la tasa de aceleracion lineal (pixels/frame²)
        self.friccion = 0.05  # resistencia al movimiento (la velocidad se reduce )
