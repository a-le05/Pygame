# sistemas/sistema_canon_enemigo.py
import math

class SistemaCanonEnemigo:
    def actualizar(self, cañones_enemigo, jugador):
        """
        cañones_enemigo: lista de entidades cañón de enemigos
        jugador: entidad jugador para apuntar
        """
        for e in cañones_enemigo:  # Itera sobre las entidades cañón y omite las que no son cañones.
            if not getattr(e, "es_canon", False):
                continue

            cuerpo = getattr(e, "cuerpo_asociado", None)  # Obtiene el tanque asociado a ese cañón.
            if cuerpo is None:  # Si no tiene tanque, lo ignora.
                continue

            # Verifica que el tanque tenga sprite y transform para calcular la posición del cañón.
            sprite_cuerpo = cuerpo.ontener("sprite")
            transform_cuerpo = cuerpo.ontener("transform")
            if not sprite_cuerpo or not transform_cuerpo:
                continue

            # Posición base del cañón: centro del tanque enemigo
            base_x = transform_cuerpo.x + sprite_cuerpo.ancho // 2
            base_y = transform_cuerpo.y + sprite_cuerpo.alto // 2
            e.ontener("transform").x = base_x
            e.ontener("transform").y = base_y

            # Calcula el vector desde el cañón hacia el jugador
            jugador_transform = jugador.ontener("transform")
            dx = jugador_transform.x - base_x
            dy = jugador_transform.y - base_y


            # Ajuste según orientación del sprite
            # Convierte el vector en ángulo en grados y lo asigna al transform
            angulo = math.degrees(math.atan2(dy, dx)) + 90
            e.ontener("transform").rotacion = angulo
            #print(f"Cañón enemigo apuntando a jugador → ángulo={angulo:.2f}")