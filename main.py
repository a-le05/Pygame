import pygame
from enumeracion.enumeracion_pantalla import EstadoJuego
from pantalla.pantalla_menu import MenuPantalla
from pantalla.pantalla_juego import JuegoPantalla
from pantalla.pantalla_gameover import GameOverPantalla

pygame.init()
ANCHO, ALTO = 14 * 128, 7 * 128  # 1792 x 896
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("BATALLAS DE TANQUES")


reloj = pygame.time.Clock()
estado_actual = EstadoJuego.MENU

menu = MenuPantalla(pantalla)
juego = None
game_over = GameOverPantalla(pantalla)

corriendo = True
while corriendo:
    delta_time = reloj.get_time() / 1000
    eventos = pygame.event.get()
    for e in eventos:
        if e.type == pygame.QUIT:
            corriendo = False

    # # --- Estados ---
    if estado_actual == EstadoJuego.MENU:
        estado_actual = menu.actualizar(eventos)
        menu.dibujar()
        # Cuando el menú devuelve "JUEGO", creamos un juego nuevo
        if estado_actual == EstadoJuego.JUEGO:
            juego = JuegoPantalla(pantalla)

    elif estado_actual == EstadoJuego.JUEGO:
        estado_actual = juego.actualizar(eventos, delta_time)
        juego.dibujar()

    elif estado_actual == EstadoJuego.GAME_OVER:
        estado_actual = game_over.actualizar(eventos)
        game_over.dibujar()
        # 🔹 Si volvemos al menú desde Game Over, recreamos el menú
        if estado_actual == EstadoJuego.MENU:
            menu = MenuPantalla(pantalla)

    reloj.tick(60)

pygame.quit()
