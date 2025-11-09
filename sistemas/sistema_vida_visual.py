import pygame


class SistemaVidaVisual:
    def __init__(self, pantalla):
        self.pantalla = pantalla

    def actualizar(self, entidades):
        for e in entidades:
            vida = e.ontener("vida")
            transform = e.ontener("transform")
            sprite = e.ontener("sprite")
            if vida and transform and sprite:
                # Calcula la posición de la barra de vida.
                ancho_barra = sprite.ancho
                alto_barra = 6
                x = transform.x - ancho_barra // 2
                y = transform.y - sprite.alto // 2   # 10 pixeles arriba del tanque

                # Dibuja el fondo gris de la barra, que representa la vida total.
                pygame.draw.rect(self.pantalla, (50, 50, 50), (x, y, ancho_barra, alto_barra))

                # Calcula la proporción de vida actual, Dibuja la barra verde
                largo_vida = int(ancho_barra * (vida.actual / vida.max))
                pygame.draw.rect(self.pantalla, (0, 255, 0), (x, y, largo_vida, alto_barra))

                # Dibuja un borde negro alrededor de la barra para que se vea mejor.
                pygame.draw.rect(self.pantalla, (0, 0, 0), (x, y, ancho_barra, alto_barra), 1)
                #print(f"Vida de {e}: {vida.actual}/{vida.max} en posición ({x},{y})")
