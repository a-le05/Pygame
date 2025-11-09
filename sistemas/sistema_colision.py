class SistemaColision:
    """Mantiene una lista de entidades con componente Colision."""
    # Inicializa la lista de entidades que tienen colisión.
    def __init__(self):
        self.entidades_colision = []

    # Solo agrega entidades que tengan componente Colision.
    def agregar_entidad(self, e):
        if e.ontener("colision"):
            self.entidades_colision.append(e)

    # Permite quitar entidades del sistema (por ejemplo si mueren o desaparecen).
    def eliminar_entidad(self, e):
        if e in self.entidades_colision:
            self.entidades_colision.remove(e)

    # Para cada entidad a, sincroniza el rectángulo de colisión con la posición actual de la entidad (Transform).
    def actualizar(self):
        for a in self.entidades_colision:
            col_a = a.ontener("colision")
            trans_a = a.ontener("transform")
            if not col_a or not trans_a:
                continue

            col_a.actualizar_posicion(trans_a.x, trans_a.y)

            for b in self.entidades_colision:  # Compara a con todas las demás entidades (b) excepto consigo misma.
                if a is b:
                    continue
                col_b = b.ontener("colision")
                trans_b = b.ontener("transform")
                if not col_b or not trans_b:  # Sincroniza también la posición de b.
                    continue

                col_b.actualizar_posicion(trans_b.x, trans_b.y)

                if col_a.rect.colliderect(col_b.rect):  # colliderect → función de Pygame que retorna True si dos rectángulos se superponen.
                    print(f"Colisión entre {id(a)} y {id(b)}")
                    if hasattr(a, "prev_pos"):  # Si la entidad a tiene un atributo prev_pos (pos anterior antes del movimiento):
                        trans_a.x, trans_a.y = a.prev_pos  # Se regresa a a la posición anterior
                        col_a.actualizar_posicion(trans_a.x, trans_a.y)  # Se actualiza el rectángulo de colisión, Esto evita que a atraviese b.
