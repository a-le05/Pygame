import pygame

from componentes.animacion import Animacion
from componentes.bala import Bala
from componentes.dano import Dano
from componentes.enemigo import Enemigo
from componentes.movimiento import Movimiento
from componentes.temporal import Temporal
from componentes.vida import Vida
from enumeracion.enumeracion_sprite import EnumeracionSprite
from componentes.transform import Transform
from componentes.sprite import Sprite
from componentes.colision import Colision
from componentes.player import Jugador


class Entidad:
    """
    Entidad básica ECS (solo agrupa componentes en un dict).
    componentes → un diccionario donde la clave es el tipo de componente
    (por ejemplo "vida", "sprite") y el valor es el objeto componente (rápido y dinámico).
    """

    def __init__(self):
        self.componentes = {}

    def agregar_componentes(self, tipo, componente):
        """Método para agregar un componente a la entidad."""
        self.componentes[tipo] = componente

    def ontener(self, tipo):
        """Método para recuperar un componente de la entidad, Devuelve None si la entidad no tiene ese componente."""
        return self.componentes.get(tipo)


def crear_jugador(atlas, x=100, y=100):
    """
    Crea la entidad jugador
    """
    entidad = Entidad()  # Creamos la entidad base donde se almacenarán todos los componentes.

    # Cuerpo del tanque (verde)
    sprite_info = atlas[EnumeracionSprite.TANQUE_VERDE]  # Toma del atlas de sprites la información del tanque verde

    transform = Transform(x, y)  # posicion inicial
    sprite = Sprite(sprite_info["imagen"], sprite_info["ancho"], sprite_info["alto"])  # apariencia visual del tanque
    colision = Colision(sprite_info["ancho"], sprite_info["alto"])  # rectángulo de colisión para detectar impactos.
    player = Jugador()  # marcador que indica que esta entidad es controlable por el usuario
    movimiento = Movimiento(velocidad=6, velocidad_rotacion=3)  # controla velocidad lineal y de rotación
    vida = Vida(100)  # indica cuánta salud tiene el tanque

    entidad.agregar_componentes("transform", transform)
    entidad.agregar_componentes("sprite", sprite)
    entidad.agregar_componentes("colision", colision)
    entidad.agregar_componentes("jugador", player)
    entidad.agregar_componentes("movimiento", movimiento)
    entidad.agregar_componentes("vida", vida)

    return entidad

def crear_canon_verde(atlas, tanque):
    """Crea la entidad del cañón verde, vinculada al tanque."""
    canon = Entidad()
    sprite_info = atlas[EnumeracionSprite.CANON_VERDE_TIPO_1]

    # Inicialmente colocamos el cañón en (0,0) — el sistema lo actualizará
    transform = Transform(0, 0, rotacion=0)
    sprite = Sprite(sprite_info["imagen"], sprite_info["ancho"], sprite_info["alto"])

    # Corregir orientación del sprite
    sprite.imagen = pygame.transform.rotate(sprite.imagen, 180)  # gira 180 grados

    canon.agregar_componentes("transform", transform)
    canon.agregar_componentes("sprite", sprite)

    # --- Campos útiles directamente en la entidad para facilitar integración ---
    # Marca para que los sistemas sepan que esto es un cañón
    canon.es_canon = True
    # Referencia al cuerpo del tanque (objeto Entidad)
    canon.cuerpo_asociado = tanque
    # --- Vinculación automática ---
    if not hasattr(tanque, "vinculos"):
        tanque.vinculos = []
    tanque.vinculos.append(canon)
    return canon


def crear_caja_metal(atlas, x=0, y=0):
    entidad = Entidad()

    sprite_info = atlas[EnumeracionSprite.CAJA_METAL]

    transform = Transform(x, y)
    sprite = Sprite(sprite_info["imagen"], sprite_info["ancho"], sprite_info["alto"])
    colision = Colision(sprite_info["ancho"], sprite_info["alto"])

    entidad.agregar_componentes("transform", transform)
    entidad.agregar_componentes("sprite", sprite)
    entidad.agregar_componentes("colision", colision)

    return entidad




#----------------------------BALA GENERICA----------------------------
def crear_bala(atlas, x, y, angulo, owner):
    entidad = Entidad()
    sprite_info = atlas[EnumeracionSprite.BALA_NEGRO_TIPO_1]  # agrega esta entrada en tu atlas

    transform = Transform(x, y, rotacion=angulo)
    sprite = Sprite(sprite_info["imagen"], sprite_info["ancho"], sprite_info["alto"])
    colision = Colision(sprite_info["ancho"], sprite_info["alto"])
    bala = Bala(velocidad=5, angulo=angulo, owner=owner)
    dano = Dano(20)

    entidad.agregar_componentes("transform", transform)
    entidad.agregar_componentes("sprite", sprite)
    entidad.agregar_componentes("colision", colision)
    entidad.agregar_componentes("bala", bala)
    entidad.agregar_componentes("dano", dano)
    return entidad

#------------------------ ENEMIGO ROJO ----------------------------
def crear_enemigo_test(atlas, x=100, y=100):
    """
    creamos enemigo de prueba
    """
    entidad = Entidad()
    sprite_info = atlas[EnumeracionSprite.TANQUE_ROJO]

    transform = Transform(x, y)
    sprite = Sprite(sprite_info["imagen"], sprite_info["ancho"], sprite_info["alto"])
    colision = Colision(sprite_info["ancho"], sprite_info["alto"])
    movimiento = Movimiento(velocidad=5, velocidad_rotacion=3)
    vida = Vida(100)

    entidad.agregar_componentes("transform", transform)
    entidad.agregar_componentes("sprite", sprite)
    entidad.agregar_componentes("colision", colision)
    entidad.agregar_componentes("enemigo", Enemigo())
    entidad.agregar_componentes("movimiento", movimiento)
    entidad.agregar_componentes("vida", vida)
    return entidad


def crear_canon_rojo(atlas, tanque):
    """Crea la entidad del cañón rojo, vinculada al tanque."""
    canon = Entidad()
    sprite_info = atlas[EnumeracionSprite.CANON_ROJO_TIPO_1]

    # Inicialmente colocamos el cañón en (0,0) — el sistema lo actualizará
    transform = Transform(0, 0, rotacion=0)
    sprite = Sprite(sprite_info["imagen"], sprite_info["ancho"], sprite_info["alto"])

    # Corregir orientación del sprite
    sprite.imagen = pygame.transform.rotate(sprite.imagen, 180)  # gira 180 grados

    canon.agregar_componentes("transform", transform)
    canon.agregar_componentes("sprite", sprite)

    # --- Campos útiles directamente en la entidad para facilitar integración ---
    # Marca para que los sistemas sepan que esto es un cañón
    # Referencia al cuerpo del tanque (objeto Entidad)
    canon.es_canon = True
    canon.cuerpo_asociado = tanque

    # --- Vinculación automática ---
    if not hasattr(tanque, "vinculos"):
        tanque.vinculos = []
    tanque.vinculos.append(canon)
    return canon

# ---------------------------------- ENEMIGO AZUL -------------------------------------
def crear_enemigo_azul(atlas, x=100, y=100):
    """
    creamos enemigo de prueba
    """
    entidad = Entidad()
    sprite_info = atlas[EnumeracionSprite.TANQUE_AZUL]

    transform = Transform(x, y)
    sprite = Sprite(sprite_info["imagen"], sprite_info["ancho"], sprite_info["alto"])
    colision = Colision(sprite_info["ancho"], sprite_info["alto"])
    movimiento = Movimiento(velocidad=5, velocidad_rotacion=3)
    vida = Vida(100)

    entidad.agregar_componentes("transform", transform)
    entidad.agregar_componentes("sprite", sprite)
    entidad.agregar_componentes("colision", colision)
    entidad.agregar_componentes("enemigo", Enemigo())
    entidad.agregar_componentes("movimiento", movimiento)
    entidad.agregar_componentes("vida", vida)
    return entidad


def crear_canon_azul(atlas, tanque):
    """Crea la entidad del cañón rojo, vinculada al tanque."""
    canon = Entidad()
    sprite_info = atlas[EnumeracionSprite.CANON_AZUL_TIPO_1]

    # Inicialmente colocamos el cañón en (0,0) — el sistema lo actualizará
    transform = Transform(0, 0, rotacion=0)
    sprite = Sprite(sprite_info["imagen"], sprite_info["ancho"], sprite_info["alto"])

    # Corregir orientación del sprite
    sprite.imagen = pygame.transform.rotate(sprite.imagen, 180)  # gira 180 grados

    canon.agregar_componentes("transform", transform)
    canon.agregar_componentes("sprite", sprite)

    # --- Campos útiles directamente en la entidad para facilitar integración ---
    # Marca para que los sistemas sepan que esto es un cañón
    # Referencia al cuerpo del tanque (objeto Entidad)
    canon.es_canon = True
    canon.cuerpo_asociado = tanque

    # --- Vinculación automática ---
    if not hasattr(tanque, "vinculos"):
        tanque.vinculos = []
    tanque.vinculos.append(canon)
    return canon

# ---------------------------------- ENEMIGO NEGRO ----------------------
def crear_enemigo_negro(atlas, x=100, y=100):
    """
    creamos enemigo de prueba
    """
    entidad = Entidad()
    sprite_info = atlas[EnumeracionSprite.TANQUE_NEGRO]

    transform = Transform(x, y)
    sprite = Sprite(sprite_info["imagen"], sprite_info["ancho"], sprite_info["alto"])
    colision = Colision(sprite_info["ancho"], sprite_info["alto"])
    movimiento = Movimiento(velocidad=5, velocidad_rotacion=3)
    vida = Vida(100)

    entidad.agregar_componentes("transform", transform)
    entidad.agregar_componentes("sprite", sprite)
    entidad.agregar_componentes("colision", colision)
    entidad.agregar_componentes("enemigo", Enemigo())
    entidad.agregar_componentes("movimiento", movimiento)
    entidad.agregar_componentes("vida", vida)
    return entidad


def crear_canon_negro(atlas, tanque):
    """Crea la entidad del cañón rojo, vinculada al tanque."""
    canon = Entidad()
    sprite_info = atlas[EnumeracionSprite.CANON_NEGRO_TIPO_1]

    # Inicialmente colocamos el cañón en (0,0) — el sistema lo actualizará
    transform = Transform(0, 0, rotacion=0)
    sprite = Sprite(sprite_info["imagen"], sprite_info["ancho"], sprite_info["alto"])

    # Corregir orientación del sprite
    sprite.imagen = pygame.transform.rotate(sprite.imagen, 180)  # gira 180 grados

    canon.agregar_componentes("transform", transform)
    canon.agregar_componentes("sprite", sprite)

    # --- Campos útiles directamente en la entidad para facilitar integración ---
    # Marca para que los sistemas sepan que esto es un cañón
    # Referencia al cuerpo del tanque (objeto Entidad)
    canon.es_canon = True
    canon.cuerpo_asociado = tanque

    # --- Vinculación automática ---
    if not hasattr(tanque, "vinculos"):
        tanque.vinculos = []
    tanque.vinculos.append(canon)
    return canon

# -----------------------------ENEMIGO AMARILLO ---------------------
def crear_enemigo_amarillo(atlas, x=100, y=100):
    """
    creamos enemigo de prueba
    """
    entidad = Entidad()
    sprite_info = atlas[EnumeracionSprite.TANQUE_AMARILLO]

    transform = Transform(x, y)
    sprite = Sprite(sprite_info["imagen"], sprite_info["ancho"], sprite_info["alto"])
    colision = Colision(sprite_info["ancho"], sprite_info["alto"])
    movimiento = Movimiento(velocidad=5, velocidad_rotacion=3)
    vida = Vida(100)

    entidad.agregar_componentes("transform", transform)
    entidad.agregar_componentes("sprite", sprite)
    entidad.agregar_componentes("colision", colision)
    entidad.agregar_componentes("enemigo", Enemigo())
    entidad.agregar_componentes("movimiento", movimiento)
    entidad.agregar_componentes("vida", vida)
    return entidad


def crear_canon_amarillo(atlas, tanque):
    """Crea la entidad del cañón rojo, vinculada al tanque."""
    canon = Entidad()
    sprite_info = atlas[EnumeracionSprite.CANON_AMARILO_TIPO_1]

    # Inicialmente colocamos el cañón en (0,0) — el sistema lo actualizará
    transform = Transform(0, 0, rotacion=0)
    sprite = Sprite(sprite_info["imagen"], sprite_info["ancho"], sprite_info["alto"])

    # Corregir orientación del sprite
    sprite.imagen = pygame.transform.rotate(sprite.imagen, 180)  # gira 180 grados

    canon.agregar_componentes("transform", transform)
    canon.agregar_componentes("sprite", sprite)

    # --- Campos útiles directamente en la entidad para facilitar integración ---
    # Marca para que los sistemas sepan que esto es un cañón
    # Referencia al cuerpo del tanque (objeto Entidad)
    canon.es_canon = True
    canon.cuerpo_asociado = tanque

    # --- Vinculación automática ---
    if not hasattr(tanque, "vinculos"):
        tanque.vinculos = []
    tanque.vinculos.append(canon)
    return canon

# ---------------------------- CREAR EXPLOSION ---------------------------------
def crear_explosion(frames, x, y):
    """
    Crea una entidad de explosión en (x, y) usando la lista de frames.
    """
    expl = Entidad()

    # Transform
    expl.agregar_componentes("transform", Transform(x, y))
    # Sprite inicial
    primer_frame = frames[0]
    expl.agregar_componentes("sprite", Sprite(primer_frame["imagen"], primer_frame["ancho"], primer_frame["alto"]))
    # Animación (no loop)
    anim = Animacion(frames, velocidad=0.1, loop=False)
    expl.agregar_componentes("animacion", anim)

    return expl


# -------------------------------------- EFECTO DE DISPARO ---------------------------
def crear_fuego(atlas, x, y, rotacion=0):
    entidad = Entidad()

    sprite_info = atlas[EnumeracionSprite.DISPARO_NARANJA]
    transform = Transform(x, y, rotacion=rotacion)  # <-- rotación asignada aquí
    sprite = Sprite(sprite_info["imagen"], sprite_info["ancho"], sprite_info["alto"])
    temporal = Temporal(0.2)  # dura 1 segundo

    entidad.agregar_componentes("transform", transform)
    entidad.agregar_componentes("sprite", sprite)
    entidad.agregar_componentes("temporal", temporal)

    return entidad
