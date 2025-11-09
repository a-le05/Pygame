# sistemas/sistema_canon.py
import math
import pygame

class SistemaCanon:
    def actualizar(self, entidades_canon):
        """
        entidades_canon: lista de entidades que son cañones (puede ser [canon] o varios).
        Cada entidad debe tener:
            - es_canon == True
            - cuerpo_asociado: referencia a la entidad tanque
            - transform (con x, y, rotacion)
        """
        mx, my = pygame.mouse.get_pos()  # Obtiene la posición actual del mouse en la ventana, en píxeles.

        for e in entidades_canon:  # Itera sobre las entidades y ignora las que no sean cañones.
            if not getattr(e, "es_canon", False):
                continue

            cuerpo = getattr(e, "cuerpo_asociado", None)  # Cada cañón tiene un atributo cuerpo_asociado que referencia la entidad tanque a la que pertenece.
            if cuerpo is None:  # Si no tiene cuerpo asociado, se salta.
                continue

            # La base del cañón sigue el centro del cuerpo (ajusta si querés otro punto)
            # Verifica que el cuerpo tenga sprite y transform para poder calcular la posición del cañón.
            sprite_cuerpo = cuerpo.ontener("sprite")
            transform_cuerpo = cuerpo.ontener("transform")
            if not sprite_cuerpo or not transform_cuerpo:
                continue

            # Calcula el centro del tanque como punto base para posicionar el cañón.
            base_x = transform_cuerpo.x + sprite_cuerpo.ancho // 2
            base_y = transform_cuerpo.y + sprite_cuerpo.alto // 2

            # Colocar la posición del transform del cañón en ese punto base
            # (el render se encargará de usar esa posición como base de rotación)
            e.ontener("transform").x = base_x
            e.ontener("transform").y = base_y

            # Calcula el vector que va desde el cañón hacia el mouse.
            dx = mx - base_x
            dy = my - base_y

            # Lo multiplica por -1 porque la imagen del cañón apunta hacia arriba en tu atlas (ajuste de orientación).
            dx *= -1
            dy *= -1

            # Rotación apuntando al mouse; -90 porque la imagen apunta hacia arriba en el atlas
            angulo = math.degrees(math.atan2(dy, dx)) - 90  # Se resta 90° para alinear la imagen del cañón con la dirección correcta.
            e.ontener("transform").rotacion = angulo  # Se asigna al transform del cañón, de manera que cuando se dibuje, gire apuntando al mouse.
            #print(f"Cañón apuntando a {mx},{my} → ángulo={angulo:.2f}")