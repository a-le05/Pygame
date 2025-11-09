import random


class SistemaSpawnEnemigos:
    def __init__(self, atlas, entidades, jugador, modelos_enemigos,
                 enemigos_lista, canones_lista, max_enemigos=6, tiempo_spawn=4.0,
                 sistema_colision=None):
        self.atlas = atlas
        self.entidades = entidades
        self.jugador = jugador
        self.modelos_enemigos = modelos_enemigos
        self.enemigos_lista = enemigos_lista
        self.canones_lista = canones_lista
        self.max_enemigos = max_enemigos
        self.tiempo_spawn = tiempo_spawn
        self.timer = 0
        self.sistema_colision = sistema_colision

        self.spawn_area = {"x_min": 100, "x_max": 1180, "y_min": 100, "y_max": 620}

    def actualizar(self, delta_time):
        # Incrementa el tiempo transcurrido desde el último spawn.
        self.timer += delta_time

        # Limpiar listas de enemigos y cañones que ya fueron destruidos.
        self.enemigos_lista[:] = [e for e in self.enemigos_lista if e in self.entidades]
        self.canones_lista[:] = [c for c in self.canones_lista if c in self.entidades]
        # Si ha pasado suficiente tiempo, reinicia el timer y empieza el proceso de spawn.
        if self.timer >= self.tiempo_spawn:
            self.timer = 0
            # Escoge aleatoriamente un modelo de enemigo y su cañón.
            if len(self.enemigos_lista) < self.max_enemigos:
                modelo_enemigo, modelo_canon = random.choice(self.modelos_enemigos)
                x = random.randint(self.spawn_area["x_min"], self.spawn_area["x_max"])
                y = random.randint(self.spawn_area["y_min"], self.spawn_area["y_max"])
                # Llama a las funciones de fábrica para crear el enemigo y su cañón, vinculándolos.
                nuevo_enemigo = modelo_enemigo(self.atlas, x, y)
                nuevo_canon = modelo_canon(self.atlas, nuevo_enemigo)

                # Agrega las entidades al ECS y a las listas de seguimiento.
                self.entidades.append(nuevo_enemigo)
                self.entidades.append(nuevo_canon)
                self.enemigos_lista.append(nuevo_enemigo)
                self.canones_lista.append(nuevo_canon)

                # Registrar colisión solo si el sistema existe
                if self.sistema_colision:
                    self.sistema_colision.agregar_entidad(nuevo_enemigo)
                    print(f"Spawn enemigo en ({x}, {y})")