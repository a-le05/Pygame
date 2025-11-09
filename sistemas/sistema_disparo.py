# sistema_disparo.py
import math

import pygame

from entidades.fabrica_entidades import crear_bala, crear_fuego
from enumeracion.enumeracion_sonido import Sonido
from enumeracion.enumeracion_sprite import EnumeracionSprite


class SistemaDisparo:
    def __init__(self, atlas, entidades, balas, sistema_sonido):
        self.atlas = atlas
        self.entidades = entidades
        self.balas = balas
        self.sistema_sonido = sistema_sonido  # 👈 igual que haces con el tanque

    def procesar_eventos(self, eventos, jugador, canon):
        # Evitar disparar si el cañón no está vinculado a un tanque
        if getattr(canon, "cuerpo_asociado", None) is None:
            return

        # Detecta click izquierdo del mouse.
        for evento in eventos:
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                # Obtiene la rotación y tamaño del cañón.
                # Convierte a radianes para cálculos trigonométricos.
                transform_canon = canon.ontener("transform")
                sprite_canon = canon.ontener("sprite")
                largo_canon = sprite_canon.alto
                rad = math.radians(transform_canon.rotacion - 90)

                # Calcula la posición de la punta del cañón, desde donde sale la bala.
                punta_x = transform_canon.x + math.cos(rad) * largo_canon
                punta_y = transform_canon.y + math.sin(rad) * largo_canon

                # Calcula el ángulo hacia el mouse usando atan2.
                mx, my = pygame.mouse.get_pos()
                angulo_rad = math.atan2(my - punta_y, mx - punta_x)

                # Crea la entidad bala con la posición inicial, ángulo y dueño (jugador).
                bala_nueva = crear_bala(
                    self.atlas,
                    punta_x,
                    punta_y,
                    math.degrees(angulo_rad) + 90,
                    jugador
                )

                # Calcula la velocidad de la bala en X e Y según el ángulo.
                bala_comp = bala_nueva.ontener("bala")
                bala_comp.dx = math.cos(angulo_rad) * bala_comp.velocidad
                bala_comp.dy = math.sin(angulo_rad) * bala_comp.velocidad

                # Agrega la bala a las listas que el juego usa para actualizar y dibujar.
                self.balas.append(bala_nueva)
                self.entidades.append(bala_nueva)

                # Reproduce el efecto de sonido cuando se dispara.
                self.sistema_sonido.reproducir(Sonido.DISPARO)

                # --- Crear fuego temporal en la punta del cañón ---
                # Calcula la posición para que el fuego aparezca delante de la punta del cañón.
                fuego_sprite_info = self.atlas[EnumeracionSprite.DISPARO_NARANJA]
                offset_x = fuego_sprite_info["ancho"] // 2
                offset_y = fuego_sprite_info["alto"] // 2

                # Desplazamiento extra para que el fuego quede más adelante
                desplazamiento_punta = 15  # píxeles hacia adelante

                fuego_x = punta_x + math.cos(rad) * desplazamiento_punta
                fuego_y = punta_y + math.sin(rad) * desplazamiento_punta

                # Crea la entidad de fuego y la agrega a las entidades.
                fuego = crear_fuego(
                    self.atlas,
                    fuego_x - offset_x,
                    fuego_y - offset_y,
                    rotacion=transform_canon.rotacion + 180
                )
                # Este fuego puede tener animación temporal para desaparecer después.
                self.entidades.append(fuego)
                print(
                    f"Disparo: bala creada en ({punta_x:.2f}, {punta_y:.2f}) con ángulo {math.degrees(angulo_rad):.2f}")