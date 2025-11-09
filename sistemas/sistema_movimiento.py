import math
import pygame
from enumeracion.enumeracion_sonido import Sonido

class SistemaMovimientoTanque:
    def __init__(self, sistema_sonido):
        self.sistema_sonido = sistema_sonido

    def actualizar(self, entidades):
        keys = pygame.key.get_pressed()  # lista de teclas presionadas.
        tanque_en_movimiento = False  # Para detectar si se está moviendo

        for e in entidades:
            transform = e.ontener("transform")
            mov = e.ontener("movimiento")
            jugador = e.ontener("jugador")

            if transform and jugador and mov:
                # --- Guardar posición previa ---
                e.prev_pos = (transform.x, transform.y)

                # --- Rotación tipo tanque ---
                if keys[pygame.K_a]:  # girar izquierda
                    transform.rotacion -= mov.velocidad_rotacion_max
                    tanque_en_movimiento = True
                if keys[pygame.K_d]:  # girar derecha
                    transform.rotacion += mov.velocidad_rotacion_max
                    tanque_en_movimiento = True

                # --- Movimiento lineal ---
                if keys[pygame.K_w]:
                    mov.velocidad_actual += mov.aceleracion
                    tanque_en_movimiento = True
                elif keys[pygame.K_s]:
                    mov.velocidad_actual -= mov.aceleracion
                    tanque_en_movimiento = True
                else:
                    mov.velocidad_actual *= (1 - mov.friccion)

                # Limitar velocidad
                mov.velocidad_actual = max(-mov.velocidad_max, min(mov.velocidad_actual, mov.velocidad_max))

                # --- Aplicar movimiento según rotación ---
                rad = math.radians(transform.rotacion)
                transform.x += math.sin(rad) * mov.velocidad_actual
                transform.y -= math.cos(rad) * mov.velocidad_actual

        # --- Control de sonido según movimiento ---
        if tanque_en_movimiento:
            self.sistema_sonido.reproducir(Sonido.TANQUE_MOVIENDOSE)
        else:
            self.sistema_sonido.reproducir(Sonido.TANQUE_QUIETO)
