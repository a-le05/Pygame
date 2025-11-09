import pygame
from enumeracion.enumeracion_mapa import EnumeracionMapa
from enumeracion.enumeracion_sprite import EnumeracionSprite

TILE_SIZE = 128

def dibujar_mapa(pantalla, atlas, mapa):
    """
    Dibuja el mapa usando la matriz numérica y el atlas de sprites.
    """
    for y, fila in enumerate(mapa):
        for x, valor in enumerate(fila):
            if valor == EnumeracionMapa.TILE_ARENA_1.value:
                imagen = atlas[EnumeracionSprite.ARENA_1]["imagen"]
            elif valor == EnumeracionMapa.TILE_ARENA_2.value:
                imagen = atlas[EnumeracionSprite.ARENA_2]["imagen"]
            elif valor == EnumeracionMapa.TILE_ARENA_CRUZ.value:
                imagen = atlas[EnumeracionSprite.ARENA_CRUZ]["imagen"]
            elif valor == EnumeracionMapa.TILE_ARENA_HORIZONTAL.value:
                imagen = atlas[EnumeracionSprite.ARENA_ARIZONAL]["imagen"]
            elif valor == EnumeracionMapa.TILE_ARENA_VERTICAL.value:
                imagen = atlas[EnumeracionSprite.ARENA_VERTICAL]["imagen"]
            else:
                continue  # Por si hay otros valores en el futuro

            pantalla.blit(imagen, (x * TILE_SIZE, y * TILE_SIZE))