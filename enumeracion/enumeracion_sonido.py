# enumeracion/enumeracion_sonidos.py
from enum import Enum


class Sonido(Enum):
    TANQUE_QUIETO = "assets/sonidos/quieto.wav"
    TANQUE_MOVIENDOSE = "assets/sonidos/moviendo.wav"
    DISPARO = "assets/sonidos/disparo.wav"
    EXPLOSION = "assets/sonidos/explosion.wav"
