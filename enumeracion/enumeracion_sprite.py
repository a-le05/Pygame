# enumeracion/enumeracion_sprite
from enum import Enum, auto


class EnumeracionSprite(Enum):
    # Cuerpo del tanque
    TANQUE_VERDE = auto()
    TANQUE_NEGRO = auto()
    TANQUE_AZUL = auto()
    TANQUE_ROJO = auto()
    TANQUE_AMARILLO = auto()

    # Huellas de tanque
    HUELLA_TANQUE = auto

    # Cañon de tanques
    CANON_NEGRO_TIPO_1 = auto()
    CANON_NEGRO_TIPO_2 = auto()
    CANON_NEGRO_TIPO_3 = auto()

    CANON_VERDE_TIPO_1 = auto()
    CANON_VERDE_TIPO_2 = auto()
    CANON_VERDE_TIPO_3 = auto()

    CANON_AZUL_TIPO_1 = auto()
    CANON_AZUL_TIPO_2 = auto()
    CANON_AZUL_TIPO_3 = auto()

    CANON_ROJO_TIPO_1 = auto()
    CANON_ROJO_TIPO_2 = auto()
    CANON_ROJO_TIPO_3 = auto()

    CANON_AMARILO_TIPO_1 = auto()
    CANON_AMARILO_TIPO_2 = auto()
    CANON_AMARILO_TIPO_3 = auto()

    # Cuerpo de tanques especiales
    TANQUE_GRANDE_ROJO = auto()
    TANQUE_ENORME = auto()
    TANQUE_GRANDE_OSCURO = auto()

    # Huella de tanque especial
    HUELLA_TANQUE_ESPECIAL = auto()

    # Cañon de tanque especial
    CANON_ESPECIAL_TIPO_1 = auto()
    CANON_ESPECIAL_TIPO_2 = auto()
    CANON_ESPECIAL_TIPO_3 = auto()
    CANON_ESPECIAL_TIPO_4 = auto()
    CANON_ESPECIAL_TIPO_5 = auto()
    CANON_ESPECIAL_TIPO_6 = auto()
    CANON_ESPECIAL_TIPO_7 = auto()

    # Balas de cañon
    BALA_NEGRO_TIPO_1 = auto()
    BALA_NEGRO_TIPO_2 = auto()
    BALA_NEGRO_TIPO_3 = auto()

    BALA_VERDE_TIPO_1 = auto()
    BALA_VERDE_TIPO_2 = auto()
    BALA_VERDE_TIPO_3 = auto()

    BALA_AZUL_TIPO_1 = auto()
    BALA_AZUL_TIPO_2 = auto()
    BALA_AZUL_TIPO_3 = auto()

    BALA_ROJO_TIPO_1 = auto()
    BALA_ROJO_TIPO_2 = auto()
    BALA_ROJO_TIPO_3 = auto()

    BALA_AMARILLO_TIPO_1 = auto()
    BALA_AMARILLO_TIPO_2 = auto()
    BALA_AMARILLO_TIPO_3 = auto()

    # Explosión
    EXPLOCION_1 = auto()
    EXPLOCION_2 = auto()
    EXPLOCION_3 = auto()
    EXPLOCION_4 = auto()
    EXPLOCION_5 = auto()

    # Explosión con humo
    EXPLOCION_HUMO_1 = auto()
    EXPLOCION_HUMO_2 = auto()
    EXPLOCION_HUMO_3 = auto()
    EXPLOCION_HUMO_4 = auto()
    EXPLOCION_HUMO_5 = auto()

    # Efecto al disparo
    DISPARO_GRANDE = auto()
    DISPARO_NARANJA = auto()
    DISPARO_ROJO = auto()
    DISPARO_FINO = auto()

    # Terreno de desierto
    ARENA_1 = auto()
    ARENA_2 = auto()
    ARENA_CRUZ = auto()
    ARENA_ARIZONAL = auto()
    ARENA_VERTICAL = auto()

    # Terreno de cesped
    CESPED_1 = auto()
    CESPED_2 = auto()

    # Obstaculos de colisión
    ARBOL_VERDE = auto
    ARBOL_NARANJA = auto()
    CAJA_METAL = auto()

    # Base metralladora automatica
    BASE = auto()

    # Trampa
    TRAMPA = auto()

    # Objeto
    BARRIL_GASOLINA = auto()
