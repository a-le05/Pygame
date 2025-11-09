class Temporal:
    def __init__(self, duracion):
        """
        componente que idica cuanto tienmpo debe existen una entidad antes de eliminarse
        :param duracion:
        """
        self.duracion = duracion  # cuanto tiempo debe existir la entidad que se crea
        self.tiempo_actual = 0  # lleva cuenta del tiempo transcurrido
