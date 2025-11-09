import math
import random

class SistemaMovimientoEnemigo:
    def __init__(self):
        # Esto evita que el enemigo cambie de comportamiento a cada frame
        self.tiempo_reaccion = 0

    def actualizar(self, enemigos, jugador, delta_time):
        for e in enemigos:
            transform = e.ontener("transform")
            mov = e.ontener("movimiento")
            enemigo = e.ontener("enemigo")

            if not (transform and mov and enemigo):
                continue

            # --- Guardar posición previa ---
            e.prev_pos = (transform.x, transform.y)

            # --- Calcular dirección hacia el jugador ---
            jugador_transform = jugador.ontener("transform")
            dx = jugador_transform.x - transform.x
            dy = jugador_transform.y - transform.y
            distancia = math.hypot(dx, dy)

            # Ángulo hacia el jugador
            angulo_objetivo = math.degrees(math.atan2(dx, -dy))  # mismo eje que el jugador
            diferencia = (angulo_objetivo - transform.rotacion + 540) % 360 - 180

            # --- Rotación hacia el jugador ---
            if abs(diferencia) > 5:
                if diferencia > 0:
                    transform.rotacion += mov.velocidad_rotacion_max
                else:
                    transform.rotacion -= mov.velocidad_rotacion_max

            # --- Movimiento hacia el jugador ---
            # Solo avanza si está más lejos de 200 px
            if distancia > 200:
                mov.velocidad_actual += mov.aceleracion
            else:
                # Se frena cerca del jugador
                mov.velocidad_actual *= (1 - mov.friccion * 2)

            # Limitar velocidad
            mov.velocidad_actual = max(-mov.velocidad_max, min(mov.velocidad_actual, mov.velocidad_max))

            # --- Aplicar movimiento según rotación ---
            rad = math.radians(transform.rotacion)
            transform.x += math.sin(rad) * mov.velocidad_actual
            transform.y -= math.cos(rad) * mov.velocidad_actual

