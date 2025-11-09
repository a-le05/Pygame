import pygame
from enumeracion.enumeracion_pantalla import EstadoJuego

class GameOverPantalla:
    def __init__(self, pantalla):
        self.pantalla = pantalla
        #self.fuente_titulo = pygame.font.SysFont("Arial", 80, bold=True)
        self.fuente_opcion = pygame.font.SysFont("Arial", 40, bold=True)

        # 🔹 Cargar imagen de fondo de derrota
        self.fondo = pygame.image.load("assets/imagen_game_over.png").convert()
        self.fondo = pygame.transform.scale(self.fondo, (1792, 896))  # tu resolución exacta

    def actualizar(self, eventos):
        for evento in eventos:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    return EstadoJuego.MENU
        return EstadoJuego.GAME_OVER

    def dibujar(self):
        # 🔹 Dibujar fondo de pantalla completa
        self.pantalla.blit(self.fondo, (0, 0))

        # 🔹 Texto "GAME OVER"
        #titulo = self.fuente_titulo.render("GAME OVER", True, (255, 0, 0))
        #self.pantalla.blit(titulo, (self.pantalla.get_width()//2 - titulo.get_width()//2, 100))

        # 🔹 Texto de instrucción
        instruccion = self.fuente_opcion.render("Presiona ENTER para volver al menú", True, (255, 255, 255))
        self.pantalla.blit(instruccion, (self.pantalla.get_width()//2 - instruccion.get_width()//2, 750))

        pygame.display.flip()

