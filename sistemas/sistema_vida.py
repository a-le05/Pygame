from entidades.fabrica_entidades import crear_explosion
from enumeracion.enumeracion_sonido import Sonido


class SistemaVida:
    def __init__(self, frames_explosion, sistema_colision=None, sistema_sonido=None):
        self.frames_explosion = frames_explosion
        self.sistema_colision = sistema_colision
        self.sistema_sonido = sistema_sonido  # Guardamos referencia al sistema de sonido

    def actualizar(self, entidades, delta_time, sistema_puntuacion=None):
        for e in entidades[:]:
            vida = e.ontener("vida")  # Revisa si la entidad tiene Vida.
            if vida and vida.actual <= 0:  # Si la vida es 0 o menor, procede a manejar su muerte.
                # Si la entidad tiene transform, crea una explosión visual en su posición.
                transform = e.ontener("transform")

                if transform:
                    expl = crear_explosion(self.frames_explosion, transform.x, transform.y)
                    entidades.append(expl)
                    # Reproducir sonido de explosión si tenemos el sistema de sonido
                    if self.sistema_sonido:
                        self.sistema_sonido.reproducir(Sonido.EXPLOSION)

                # Si la entidad tiene cañones u otras entidades vinculadas (vinculos), los elimina y desvincula.
                if hasattr(e, "vinculos"):
                    for vinculo in e.vinculos:
                        vinculo.cuerpo_asociado = None
                        if self.sistema_colision:
                            self.sistema_colision.eliminar_entidad(vinculo)
                        if vinculo in entidades:
                            entidades.remove(vinculo)
                    e.vinculos.clear()

                # Quita la entidad del sistema de colisiones y del ECS.
                if self.sistema_colision:
                    self.sistema_colision.eliminar_entidad(e)
                # Eliminar del ECS
                if e in entidades:
                    entidades.remove(e)

                # Suma puntos al sistema de puntuación si la entidad era un enemigo.
                if sistema_puntuacion and e.ontener("enemigo"):
                    sistema_puntuacion.sumar_puntos(100)  # cada enemigo vale 100 puntos
                    # print(f"Entidad eliminada: {e}, puntos sumados si es enemigo")