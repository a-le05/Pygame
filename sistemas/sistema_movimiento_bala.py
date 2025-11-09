class SistemaMovimientoBala:
    def actualizar(self, balas):
        # Se asegura de que la entidad tenga ambos componentes.
        for e in balas:
            bala = e.ontener("bala")
            transform = e.ontener("transform")
            if not bala or not transform:
                continue

            # Actualiza la posición de la bala sumando el vector de desplazamiento.
            transform.x += bala.dx
            transform.y += bala.dy

