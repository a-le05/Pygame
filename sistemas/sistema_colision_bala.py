import pygame

class SistemaColisionBala:
    def __init__(self, ancho_pantalla, alto_pantalla):
        self.ancho = ancho_pantalla
        self.alto = alto_pantalla

    def actualizar(self, balas, entidades):
        for bala in balas[:]:  # Itera sobre una copia de la lista de balas para poder eliminar elementos dentro del bucle.
            # Verificamos que la bala tenga transform, colisión y componente bala antes de procesarla.
            transform_b = bala.ontener("transform")
            col_b = bala.ontener("colision")
            bala_comp = bala.ontener("bala")
            if not col_b or not transform_b or not bala_comp:
                continue

            # Actualiza el rectángulo de colisión con la posición actual de la bala
            col_b.actualizar_posicion(transform_b.x, transform_b.y)

            # Flag para saber si la bala debe ser eliminada en este frame.
            eliminada = False

            # Ignora la bala misma y al dueño de la bala (no se dispara a sí misma).
            for target in entidades:
                if target is bala or target is bala_comp.owner:
                    continue

                # Sincroniza la posición del rectángulo de colisión del objetivo
                col_t = target.ontener("colision")
                if not col_t:
                    continue

                trans_t = target.ontener("transform")
                col_t.actualizar_posicion(trans_t.x, trans_t.y)

                # Verifica si hay intersección entre rectángulos.
                if col_b.rect.colliderect(col_t.rect):
                    print(f"Bala {id(bala)} colisionó con {id(target)}")
                    # Aplica el daño de la bala a la entidad que recibió el impacto.
                    if target.ontener("jugador") or target.ontener("enemigo"):
                        vida_objetivo = target.ontener("vida")
                        dano_bala = bala.ontener("dano")

                        if vida_objetivo and dano_bala:
                            vida_objetivo.recibir_danio(dano_bala.cantidad)

                        # Elimina la bala de listas de balas y entidades.
                        if bala in balas:
                            balas.remove(bala)
                        if bala in entidades:
                            entidades.remove(bala)
                        # Marca eliminada = True y rompe el loop de colisiones (ya no hace más rebotes).
                        eliminada = True
                        break


                    # Impacto con caja u obstáculo → rebote
                    else:
                        # Compara distancia en X y Y para decidir hacia qué eje rebota la bala.
                        # Invierte la dirección (dx o dy) para simular el rebote.
                        centro_b_x = col_b.rect.centerx
                        centro_b_y = col_b.rect.centery
                        centro_t_x = col_t.rect.centerx
                        centro_t_y = col_t.rect.centery

                        diff_x = centro_b_x - centro_t_x
                        diff_y = centro_b_y - centro_t_y

                        if abs(diff_x) > abs(diff_y):
                            bala_comp.dx *= -1
                        else:
                            bala_comp.dy *= -1

                        # Mueve la bala fuera del obstáculo para evitar quedarse “atascada”.
                        transform_b.x += bala_comp.dx
                        transform_b.y += bala_comp.dy
                        break  # un rebote por frame

            # Movimiento y límites de pantalla
            if eliminada:
                continue

            # Actualiza la posición de la bala según su velocidad.
            transform_b.x += bala_comp.dx
            transform_b.y += bala_comp.dy

            # Si sale de los límites de la pantalla, se elimina automáticamente.
            if (transform_b.x < 0 or transform_b.x > self.ancho or
                transform_b.y < 0 or transform_b.y > self.alto):
                if bala in balas:
                    balas.remove(bala)
                if bala in entidades:
                    entidades.remove(bala)
