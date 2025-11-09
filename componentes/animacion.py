class Animacion:
    def __init__(self, frames, velocidad=0.1, loop=False):
        """
        Animacion es un componente de indentidad que guarda los datos necesarios apra manejar
        una animacion cuadro a cuaro(frames) de un sprite o efecto visual
        frames: lista de cuadros o imagenes que forma la animacion
        velocidad: el tiempo en segundo que dura cada frame antes de apra al siguiente
        loop: si es True, la animacion se repite (ideal para animaciones continuas)
              si es False, se reproduce una sola vez (como una explosion)
        """
        self.frames = frames  # Guarda lista de frames de la animacion
        self.velocidad = velocidad  # cuanto tarde en cambiar a la siguiente imagen
        self.loop = loop  # indicamos si la animación se repite o se detiene
        self.index = 0  # indice del frame actual
        self.timer = 0  # acumula el tiempo desde el ultimo frame
        self.terminada = False  # marcamos si la animacion a terminado
