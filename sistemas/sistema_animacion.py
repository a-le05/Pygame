class SistemaAnimacion:
    def actualizar(self, entidades, delta_time):
        """
        Actualiza todas las animaciones de las entidades
        Se encarga de actualizar las animaciones de todas las entidades que
        tengan un componente Animacion y un Sprite.
        """
        for e in entidades[:]:  # Itera sobre una copia de la lista de entidades ([:]) para poder eliminar entidades dentro del bucle
            anim = e.ontener("animacion")  # obtenemos compoentes animacion
            sprite = e.ontener("sprite")  # obtenemos componente sprite
            if not anim or not sprite or anim.terminada:
                continue

            # Actualiza el frame según el tiempo transcurrido.
            anim.timer += delta_time  # tiempo que pasó desde el último frame
            if anim.timer >= anim.velocidad:
                anim.timer = 0  # indica que es hora de avanzar al siguiente frame
                anim.index += 1  # Resetea timer y aumenta index para cambiar de frame

                if anim.index >= len(anim.frames):  # Si se llegó al último frame
                    if anim.loop:
                        anim.index = 0
                    else:
                        anim.index = len(anim.frames) - 1
                        anim.terminada = True  # vuelve al primer frame si es False se queda en el último frame y marca la animación como terminada

                # Actualizar el sprite con la imagen y dimensiones del frame actual
                frame_info = anim.frames[anim.index]
                sprite.imagen = frame_info["imagen"]
                sprite.ancho = frame_info["ancho"]
                sprite.alto = frame_info["alto"]

            # Si la animación terminó y no es loop, eliminar la entidad
            if anim.terminada and not anim.loop:
                print(f"Animación terminada, eliminando entidad id={id(e)}")
                if e in entidades:
                    entidades.remove(e)

# Esto le da a la explosión un ciclo de vida automático:
# se crea, se reproduce, y se borra sola al terminar.
