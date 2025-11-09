import math
from entidades.fabrica_entidades import crear_bala, crear_fuego
from enumeracion.enumeracion_sonido import Sonido
from enumeracion.enumeracion_sprite import EnumeracionSprite


class SistemaDisparoEnemigo:
    def __init__(self, atlas, entidades, balas, sistema_sonido):
        self.atlas = atlas
        self.entidades = entidades
        self.balas = balas
        self.sistema_sonido = sistema_sonido

    def actualizar(self, enemigos_canon, jugador, delta_time):
        for canon in enemigos_canon:
            if not getattr(canon, "cuerpo_asociado", None):
                continue

            # Inicializar cooldown individual si no existe
            if not hasattr(canon, "tiempo_disparo"):
                canon.tiempo_disparo = 0
                canon.cooldown = 1.5  # segundos entre disparos

            # Incrementar timer individual
            canon.tiempo_disparo += delta_time

            # Verificar si puede disparar
            if canon.tiempo_disparo < canon.cooldown:
                continue

            canon.tiempo_disparo = 0  # reinicia timer después de disparar

            # --- Cálculos para disparo ---
            transform_canon = canon.ontener("transform")
            sprite_canon = canon.ontener("sprite")
            cuerpo = canon.cuerpo_asociado

            largo_canon = sprite_canon.alto
            rad = math.radians(transform_canon.rotacion - 90)
            punta_x = transform_canon.x + math.cos(rad) * largo_canon
            punta_y = transform_canon.y + math.sin(rad) * largo_canon

            # Ángulo hacia el jugador
            jugador_transform = jugador.ontener("transform")
            dx = jugador_transform.x - punta_x
            dy = jugador_transform.y - punta_y
            angulo_rad = math.atan2(dy, dx)
            angulo_deg = math.degrees(angulo_rad) + 90

            # Crear bala
            bala = crear_bala(self.atlas, punta_x, punta_y, angulo_deg, cuerpo)
            comp_bala = bala.ontener("bala")
            comp_bala.dx = math.cos(math.radians(angulo_deg - 90)) * comp_bala.velocidad
            comp_bala.dy = math.sin(math.radians(angulo_deg - 90)) * comp_bala.velocidad

            self.balas.append(bala)
            self.entidades.append(bala)

            # Reproducir sonido
            self.sistema_sonido.reproducir(Sonido.DISPARO)

            # Crear fuego en la punta del cañón
            fuego_info = self.atlas[EnumeracionSprite.DISPARO_NARANJA]
            offset_x = fuego_info["ancho"] // 2
            offset_y = fuego_info["alto"] // 2
            ajuste_punta = 15

            fuego = crear_fuego(
                self.atlas,
                punta_x - offset_x + math.cos(rad) * ajuste_punta,
                punta_y - offset_y + math.sin(rad) * ajuste_punta,
                rotacion=transform_canon.rotacion + 180
            )
            self.entidades.append(fuego)

            print(f"Enemigo {id(cuerpo)} dispara bala a ({punta_x:.2f}, {punta_y:.2f})")
