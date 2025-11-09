import pygame
from enumeracion.enumeracion_pantalla import EstadoJuego

class MenuPantalla:
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.fuente_titulo = pygame.font.SysFont("Arial", 90, bold=True)
        self.fuente_opcion = pygame.font.SysFont("Arial", 55, bold=True)
        self.opciones = ["Iniciar Juego", "Salir"]
        self.opcion_seleccionada = 0

        # 🔹 Cargar imagen de fondo
        self.fondo = pygame.image.load("assets/imagen_menu.png").convert()
        # Escalar para que ocupe toda la pantalla
        self.fondo = pygame.transform.scale(self.fondo, (self.pantalla.get_width(), self.pantalla.get_height()))

    def actualizar(self, eventos):
        for evento in eventos:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    self.opcion_seleccionada = (self.opcion_seleccionada - 1) % len(self.opciones)
                elif evento.key == pygame.K_DOWN:
                    self.opcion_seleccionada = (self.opcion_seleccionada + 1) % len(self.opciones)
                elif evento.key == pygame.K_RETURN:
                    if self.opcion_seleccionada == 0:
                        return EstadoJuego.JUEGO
                    elif self.opcion_seleccionada == 1:
                        pygame.quit()
                        exit()
        return EstadoJuego.MENU

    def dibujar(self):
        # 🔹 Dibujar el fondo
        self.pantalla.blit(self.fondo, (0, 0))

        # 🔹 Título
        #titulo = self.fuente_titulo.render("BATALLA DE TANQUES", True, (255, 255, 255))
        #self.pantalla.blit(titulo, (self.pantalla.get_width()//2 - titulo.get_width()//2, 100))

        # 🔹 Opciones del menú
        for i, texto in enumerate(self.opciones):
            color = (0, 0, 0) if i == self.opcion_seleccionada else (230, 230, 230)
            opcion = self.fuente_opcion.render(texto, True, color)
            self.pantalla.blit(opcion, (self.pantalla.get_width() // 2 - opcion.get_width() // 2, 350 + i * 80))

        pygame.display.flip()
