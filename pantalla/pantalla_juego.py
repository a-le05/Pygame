import pygame
import os
from enumeracion.enumeracion_pantalla import EstadoJuego
from mapa.nivel_1 import MAPA_NIVEL_1
from sistemas.sistema_animacion import SistemaAnimacion
from sistemas.sistema_canon import SistemaCanon
from sistemas.sistema_canon_enemigo import SistemaCanonEnemigo
from sistemas.sistema_colision import SistemaColision
from sistemas.sistema_colision_bala import SistemaColisionBala
from sistemas.sistema_disparo import SistemaDisparo
from sistemas.sistema_disparo_enemigo import SistemaDisparoEnemigo
from sistemas.sistema_mapa import dibujar_mapa
from enumeracion.enumeracion_sprite import EnumeracionSprite
from entidades.fabrica_entidades import *
from sistemas import *
from sistemas.sistema_movimiento import SistemaMovimientoTanque
from sistemas.sistema_movimiento_bala import SistemaMovimientoBala
from sistemas.sistema_movimiento_enemigo import SistemaMovimientoEnemigo
from sistemas.sistema_puntuacion import SistemaPuntuacion
from sistemas.sistema_render import SistemaRender
from sistemas.sistema_temporal import SistemaTemporal
from sistemas.sistema_vida import SistemaVida
from sistemas.sistema_vida_visual import SistemaVidaVisual
from sistemas.sistemna_spawn_enemigos import SistemaSpawnEnemigos
from utils.cargar_atlas import cargar_atlas
from utils.cargar_sonido import SistemaSonido


class JuegoPantalla:
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.ancho, self.alto = pantalla.get_size()
        self.atlas = cargar_atlas("assets/allSprites_retina.png")

        # --- Contadores de tiempo ---
        self.tiempo_total = 0.0
        self.tiempo_muerte = 0.0

        # --- Mejor tiempo cargado desde archivo ---
        self.archivo_mejor = "mejor_tiempo.txt"
        self.mejor_tiempo = self.cargar_mejor_tiempo()
        self.fuente_tiempo = pygame.font.SysFont("Arial", 30)

        # --- Entidades principales ---
        self.jugador = crear_jugador(self.atlas, x=200, y=200)
        # self.caja = crear_caja_metal(self.atlas, x=400, y=300)
        self.canon = crear_canon_verde(self.atlas, self.jugador)
        self.balas = []
        self.entidades = [self.jugador, self.canon] + self.balas

        # --- Sistemas ---
        self.sistema_colision = SistemaColision()
        self.sistema_colision_bala = SistemaColisionBala(self.ancho, self.alto)
        self.sistema_sonido = SistemaSonido()
        self.sistema_movimiento = SistemaMovimientoTanque(self.sistema_sonido)
        self.sistema_canon = SistemaCanon()
        self.sistema_movimiento_bala = SistemaMovimientoBala()
        self.sistema_disparo = SistemaDisparo(self.atlas, self.entidades, self.balas, self.sistema_sonido)
        self.sistema_movimiento_enemigo = SistemaMovimientoEnemigo()
        self.sistema_canon_enemigo = SistemaCanonEnemigo()
        self.sistema_disparo_enemigo = SistemaDisparoEnemigo(self.atlas, self.entidades, self.balas, self.sistema_sonido)
        self.sistema_temporal = SistemaTemporal()

        self.enemigos = []
        self.canones_enemigos = []

        self.sistema_spawn = SistemaSpawnEnemigos(
            self.atlas, self.entidades, self.jugador,
            modelos_enemigos=[(crear_enemigo_test, crear_canon_rojo),
                              (crear_enemigo_azul, crear_canon_azul),
                              (crear_enemigo_negro, crear_canon_negro),
                              (crear_enemigo_amarillo, crear_canon_amarillo)],
            enemigos_lista=self.enemigos,
            canones_lista=self.canones_enemigos,
            max_enemigos=6,
            tiempo_spawn=4.0,
            sistema_colision=self.sistema_colision
        )

        frames_explosion = [
            self.atlas[EnumeracionSprite.EXPLOCION_1],
            self.atlas[EnumeracionSprite.EXPLOCION_2],
            self.atlas[EnumeracionSprite.EXPLOCION_3],
            self.atlas[EnumeracionSprite.EXPLOCION_4],
            self.atlas[EnumeracionSprite.EXPLOCION_5],
        ]
        self.sistema_vida = SistemaVida(frames_explosion, self.sistema_colision, sistema_sonido=self.sistema_sonido)
        self.sistema_animacion = SistemaAnimacion()
        self.sistema_vida_visual = SistemaVidaVisual(pantalla)
        self.render = SistemaRender(pantalla)

        self.fuente = pygame.font.SysFont("Arial", 30)
        self.sistema_puntuacion = SistemaPuntuacion(self.fuente)

        for e in [self.jugador]:
            self.sistema_colision.agregar_entidad(e)

        # --- Estado de juego ---
        self.puede_jugar = True

    # --- Mejor tiempo ---
    def cargar_mejor_tiempo(self):
        if os.path.exists(self.archivo_mejor):
            try:
                with open(self.archivo_mejor, "r") as f:
                    return float(f.read())
            except:
                return 0.0
        return 0.0

    def guardar_mejor_tiempo(self):
        try:
            with open(self.archivo_mejor, "w") as f:
                f.write(str(self.mejor_tiempo))
        except:
            print("Error guardando mejor tiempo.")

    # --- Reiniciar tiempo al iniciar nueva partida ---
    def reiniciar_tiempo(self):
        self.tiempo_total = 0.0
        self.tiempo_muerte = 0.0

    def actualizar(self, eventos, delta_time):
        # --- Contador general ---
        self.tiempo_total += delta_time

        for evento in eventos:
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                return EstadoJuego.MENU

        # --- Sistemas de juego ---
        self.sistema_disparo.procesar_eventos(eventos, self.jugador, self.canon)
        self.sistema_movimiento.actualizar([self.jugador])
        self.sistema_canon.actualizar([self.canon])
        self.sistema_movimiento_bala.actualizar(self.balas)
        self.sistema_movimiento_enemigo.actualizar(self.enemigos, self.jugador, delta_time)
        self.sistema_canon_enemigo.actualizar(self.canones_enemigos, self.jugador)
        self.sistema_disparo_enemigo.actualizar(self.canones_enemigos, self.jugador, delta_time)
        self.sistema_spawn.actualizar(delta_time)
        self.sistema_vida.actualizar(self.entidades, delta_time, self.sistema_puntuacion)
        self.sistema_animacion.actualizar(self.entidades, delta_time)
        self.sistema_colision.actualizar()
        self.sistema_colision_bala.actualizar(self.balas, self.entidades)
        self.sistema_temporal.actualizar(self.entidades, delta_time)

        # --- Verificar muerte ---
        vida_jugador = self.jugador.componentes["vida"]
        if vida_jugador.actual <= 0:
            self.sistema_sonido.detener_movimiento()
            self.sistema_sonido.detener_quieto()

            self.tiempo_muerte += delta_time

            if self.tiempo_muerte >= 2.0:
                self.tiempo_muerte = 0
                self.puede_jugar = True

                # --- Mejor tiempo ---
                if self.tiempo_total > self.mejor_tiempo:
                    self.mejor_tiempo = self.tiempo_total
                    self.guardar_mejor_tiempo()

                return EstadoJuego.GAME_OVER
            return EstadoJuego.JUEGO

        return EstadoJuego.JUEGO

    def dibujar(self):
        self.pantalla.fill((0, 0, 0))
        dibujar_mapa(self.pantalla, self.atlas, MAPA_NIVEL_1)
        self.render.dibujar(self.entidades)
        self.sistema_vida_visual.actualizar(self.entidades)
        self.sistema_puntuacion.dibujar(self.pantalla)

        # --- Mostrar tiempo ---
        texto_tiempo = self.fuente_tiempo.render(
            f"Tiempo: {int(self.tiempo_total)}s", True, (255, 255, 255)
        )
        self.pantalla.blit(texto_tiempo, (10, 50))

        # --- Mostrar mejor tiempo ---
        texto_mejor = self.fuente_tiempo.render(
            f"Mejor: {int(self.mejor_tiempo)}s", True, (255, 255, 0)
        )
        self.pantalla.blit(texto_mejor, (10, 90))

        pygame.display.flip()