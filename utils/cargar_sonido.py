# sistemas/sistema_sonido.py
import pygame
from enumeracion.enumeracion_sonido import Sonido

class SistemaSonido:
    def __init__(self):
        pygame.mixer.init()
        self.sonidos = {}
        for s in Sonido:
            self.sonidos[s] = pygame.mixer.Sound(s.value)

        # Estados de reproducción
        self.sonido_moviendose_reproduciendose = False
        self.sonido_quieto_reproduciendose = False

    def reproducir(self, tipo: Sonido):
        #  Si se reproduce movimiento, asegurarse de detener el sonido quieto
        if tipo == Sonido.TANQUE_MOVIENDOSE:
            if not self.sonido_moviendose_reproduciendose:
                self.detener_quieto()
                self.sonidos[tipo].play(-1)  # loop infinito
                self.sonido_moviendose_reproduciendose = True

        #  Si se reproduce el sonido de quieto, detener el de movimiento
        elif tipo == Sonido.TANQUE_QUIETO:
            if not self.sonido_quieto_reproduciendose:
                self.detener_movimiento()
                self.sonidos[tipo].play(-1)  # también en loop, mientras esté quieto
                self.sonido_quieto_reproduciendose = True
        #  Sonido de disparo (una sola vez)
        elif tipo == Sonido.DISPARO:
            # Se reproduce sin loop
            self.sonidos[tipo].play()
        #  Sonido de explosión
        elif tipo == Sonido.EXPLOSION:
            self.sonidos[tipo].play()
        #  En caso de que agregues otros sonidos (explosión, daño, etc.)
        else:
            self.sonidos[tipo].play()

    def detener_movimiento(self):
        if self.sonido_moviendose_reproduciendose:
            self.sonidos[Sonido.TANQUE_MOVIENDOSE].stop()
            self.sonido_moviendose_reproduciendose = False

    def detener_quieto(self):
        if self.sonido_quieto_reproduciendose:
            self.sonidos[Sonido.TANQUE_QUIETO].stop()
            self.sonido_quieto_reproduciendose = False

