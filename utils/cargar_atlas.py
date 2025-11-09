import pygame

from enumeracion.enumeracion_sprite import EnumeracionSprite


def cargar_atlas(ruta):
    """
    Diccionario con sprite recortados
    """
    atlas = pygame.image.load(ruta).convert_alpha()

    sprite = {
        # TANQUE VERDE + CAÑON + BALA
        EnumeracionSprite.TANQUE_VERDE: {"imagen": atlas.subsurface((874, 1032, 84, 80)), "ancho": 84, "alto": 128},
        EnumeracionSprite.CANON_VERDE_TIPO_1: {"imagen": atlas.subsurface((1086, 897, 24, 60)), "ancho": 24,
                                               "alto": 60},
        EnumeracionSprite.CANON_VERDE_TIPO_2: {"imagen": atlas.subsurface((1028, 857, 32, 60)), "ancho": 32,
                                               "alto": 60},
        EnumeracionSprite.CANON_VERDE_TIPO_3: {"imagen": atlas.subsurface((1086, 1009, 24, 60)), "ancho": 24,
                                               "alto": 60},
        EnumeracionSprite.BALA_VERDE_TIPO_1: {"imagen": atlas.subsurface((1066, 1069, 24, 32)), "ancho": 24,
                                              "alto": 32},

        # TANQUE ROJO + CAÑON Y BALA
        EnumeracionSprite.TANQUE_ROJO: {"imagen": atlas.subsurface((952, 569, 76, 80)), "ancho": 76, "alto": 80},
        EnumeracionSprite.CANON_ROJO_TIPO_1: {"imagen": atlas.subsurface((1085, 542, 24, 60)), "ancho": 24, "alto": 60},
        EnumeracionSprite.CANON_ROJO_TIPO_2: {"imagen": atlas.subsurface((1026, 362, 32, 60)), "ancho": 32, "alto": 60},
        EnumeracionSprite.CANON_ROJO_TIPO_3: {"imagen": atlas.subsurface((1088, 686, 24, 60)), "ancho": 24, "alto": 60},
        EnumeracionSprite.BALA_ROJO_TIPO_1: {"imagen": atlas.subsurface((1061, 654, 24, 32)), "ancho": 24, "alto": 32},

        # TANQUE AZUL + CAÑON
        EnumeracionSprite.TANQUE_AZUL: {"imagen": atlas.subsurface((868, 620, 84, 84)), "ancho": 84, "alto": 84},
        EnumeracionSprite.CANON_AZUL_TIPO_1: {"imagen": atlas.subsurface(1058, 422, 32, 60), "ancho": 32, "alto": 60},

        # TANQUE NEGRO + CAÑON
        EnumeracionSprite.TANQUE_NEGRO: {"imagen": atlas.subsurface((868, 704, 84, 80)), "ancho": 84, "alto": 80},
        EnumeracionSprite.CANON_NEGRO_TIPO_1: {"imagen": atlas.subsurface(1056, 705, 32, 60), "ancho": 32, "alto": 60},

        # TANQUE AMARILLO + CANON
        EnumeracionSprite.TANQUE_AMARILLO: {"imagen": atlas.subsurface((876, 784, 84, 80)), "ancho": 84, "alto": 80},
        EnumeracionSprite.CANON_AMARILO_TIPO_1: {"imagen": atlas.subsurface((1058, 482, 32, 60)), "ancho": 32,
                                                 "alto": 60},

        # TANQUE JEFE TEST
        EnumeracionSprite.TANQUE_GRANDE_ROJO: {"imagen": atlas.subsurface((420, 1024, 104, 104)), "ancho": 104,
                                               "alto": 104},
        EnumeracionSprite.CANON_ESPECIAL_TIPO_5: {"imagen": atlas.subsurface((1058, 362, 32, 60)), "ancho": 32,
                                                  "alto": 60},

        # BALA GENERAL
        EnumeracionSprite.BALA_NEGRO_TIPO_1: {"imagen": atlas.subsurface((1085, 654, 24, 32)), "ancho": 24, "alto": 32},

        EnumeracionSprite.HUELLA_TANQUE: {"imagen": atlas.subsurface((951, 186, 82, 104)), "ancho": 82, "alto": 104},

        # EFECTO DE DISPARO
        EnumeracionSprite.DISPARO_FINO: {"imagen": atlas.subsurface((1106, 440, 16, 52)), "ancho": 16, "alto": 52},
        EnumeracionSprite.DISPARO_NARANJA: {"imagen": atlas.subsurface((1033, 214, 32, 56)), "ancho": 32, "alto": 56},
        EnumeracionSprite.DISPARO_GRANDE: {"imagen": atlas.subsurface((1024, 56, 40, 50)), "ancho": 40, "alto": 50},
        EnumeracionSprite.DISPARO_ROJO: {"imagen": atlas.subsurface((1016, 434, 42, 76)), "ancho": 42, "alto": 76},

        # ANIMACION DE EXPLISION
        EnumeracionSprite.EXPLOCION_1: {"imagen": atlas.subsurface((640, 804, 120, 120)), "ancho": 120, "alto": 120},
        EnumeracionSprite.EXPLOCION_2: {"imagen": atlas.subsurface((764, 508, 114, 112)), "ancho": 114, "alto": 112},
        EnumeracionSprite.EXPLOCION_3: {"imagen": atlas.subsurface((640, 256, 127, 126)), "ancho": 127, "alto": 126},
        EnumeracionSprite.EXPLOCION_4: {"imagen": atlas.subsurface((860, 96, 92, 90)), "ancho": 92, "alto": 90},
        EnumeracionSprite.EXPLOCION_5: {"imagen": atlas.subsurface((0, 1024, 106, 104)), "ancho": 106, "alto": 104},

        # PARA DIBUJAR MAPAS
        EnumeracionSprite.ARENA_1: {"imagen": atlas.subsurface((256, 128, 128, 128)), "ancho": 128, "alto": 128},
        EnumeracionSprite.ARENA_2: {"imagen": atlas.subsurface((256, 0, 128, 128)), "ancho": 128, "alto": 128},
        EnumeracionSprite.ARENA_CRUZ: {"imagen": atlas.subsurface((384, 128, 128, 128)), "ancho": 128, "alto": 128},
        EnumeracionSprite.ARENA_ARIZONAL: {"imagen": atlas.subsurface((256, 896, 128, 128)), "ancho": 128, "alto": 128},
        EnumeracionSprite.ARENA_VERTICAL: {"imagen": atlas.subsurface((256, 768, 128, 128)), "ancho": 128, "alto": 128},

        # OBSTACULO PARA PROBAR COLISIONES
        EnumeracionSprite.CAJA_METAL: {"imagen": atlas.subsurface((958, 992, 56, 56)), "ancho": 56, "alto": 56}

    }

    return sprite
