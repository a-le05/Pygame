from enum import Enum, auto

class EstadoJuego(Enum):
    MENU = auto()
    JUEGO = auto()
    GAME_OVER = auto()