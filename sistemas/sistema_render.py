# sistemas/sistema_render.py
import math
import pygame

class SistemaRender:
    def __init__(self, pantalla):
        self.pantalla = pantalla

    def rotar_desde_base(self, image, angle, base_pos):
        """
        Rota una imagen alrededor de su base.
        base_pos: posición (x, y) donde estará la base del cañón.
        Devuelve (rotated_image, rect) listos para blit.
        """
        # Notar: en tu ejemplo rotabas con -angle al llamar a transform.rotate,
        # así que mantenemos la misma convención:
        rotated_image = pygame.transform.rotate(image, -angle)
        rect = rotated_image.get_rect()

        w, h = image.get_size()
        # Pivote por defecto: borde izquierdo, centro vertical (ajustá si hace falta)
        pivot = pygame.math.Vector2(0, h / 2)
        # pivot_rotated = pivot.rotate(angle)  # rotate usa grados, convención positiva antihorario
        pivot_rotated = pivot.rotate(angle)

        # Ajustar rect para que la base quede en base_pos
        rect.center = (base_pos[0] - pivot_rotated.x, base_pos[1] - pivot_rotated.y)
        return rotated_image, rect

    def dibujar(self, entidades):

        for e in entidades:
            sprite = e.ontener("sprite")
            transform = e.ontener("transform")
            if not sprite or not transform:
                continue

            # Para otros sprites (tanque, cajas) usamos el centro como antes
            # Para cañones: usa la función especial para mantener el pivote en la base.
            # Para otros sprites: rota desde el centro del sprite (tanque, bala, caja, etc.).
            if getattr(e, "es_canon", False):
                # En nuestro SistemaCanon ya pusimos transform.x/y = base_pos (centro del tanque)
                base_pos = (transform.x, transform.y)
                imagen_rotada, rect = self.rotar_desde_base(sprite.imagen, transform.rotacion, base_pos)
                self.pantalla.blit(imagen_rotada, rect.topleft)
            else:
                # Rotación normal desde el centro del sprite
                imagen_rotada = pygame.transform.rotate(sprite.imagen, -transform.rotacion)
                rect = imagen_rotada.get_rect(center=(transform.x + sprite.ancho // 2,
                                                      transform.y + sprite.alto // 2))
                self.pantalla.blit(imagen_rotada, rect.topleft)
                # Para ver dónde está la base del cañón
                #pygame.draw.circle(self.pantalla, (255, 0, 0), (int(transform.x), int(transform.y)), 3)

