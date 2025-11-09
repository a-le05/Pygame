import pygame

class SistemaTemporal:
    def actualizar(self, entidades, dt):
        eliminar = []
        for e in entidades:
            # Obtiene el componente Temporal de la entidad.
            temporal = e.componentes.get("temporal")
            if temporal:
                # Incrementa el tiempo que la entidad ha estado activa.
                temporal.tiempo_actual += dt
                # Si supera su duración, se añade a la lista de eliminación.
                if temporal.tiempo_actual >= temporal.duracion:
                    eliminar.append(e)
        # Elimina finalmente todas las entidades que ya cumplieron su tiempo de vida.
        for e in eliminar:
            entidades.remove(e)
            #print(f"Eliminando entidad temporal: {e}")
