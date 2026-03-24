"""
Módulo nave.py
Representa un barco del juego Hundir la Flota.
"""


class Nave:
    """
    Representa una nave del juego con nombre, tipo y vida.

    La vida equivale al número de casillas que ocupa en el tablero.
    Cada disparo que recibe reduce su vida en 1.
    Cuando la vida llega a 0, la nave queda hundida.

    Atributos de clase (constantes compartidas por todos los objetos):
        TOCADO  (int): código de retorno cuando la nave sigue viva → 1
        HUNDIDO (int): código de retorno cuando la nave queda destruida → 2

    Atributos de instancia:
        nombre  (str):  nombre único de la nave, p.ej. "Bismarck"
        tipo    (str):  categoría: "submarino", "fragata" o "portaaviones"
        vida    (int):  casillas de vida restantes
        hundido (bool): True si la nave ha sido destruida completamente
    """

    # Constantes de clase: como el mismo nombre implica, mantiene constancia en valores que no se tienen que cambiar.
    TOCADO  = 1
    HUNDIDO = 2

    def __init__(self, nombre, tipo, vida):
        """
        Constructor. Crea una nave lista para el combate.

        Args:
            nombre (str): nombre de la nave
            tipo   (str): tipo de nave (submarino, fragata, portaaviones)
            vida   (int): número de casillas que ocupa (= vida inicial)
        """
        self.nombre  = nombre
        self.tipo    = tipo
        self.vida    = vida
        self.hundido = False    # Al crearse, ninguna nave está hundida

    def recibir_disparo(self):
        """
        Procesa un impacto sobre la nave.

        Reduce la vida en 1. Si llega a 0, marca la nave como hundida.
        Si la nave ya estaba hundida, devuelve HUNDIDO sin hacer nada más.

        Returns:
            int: TOCADO (1) si la nave sigue viva,
                 HUNDIDO (2) si la nave queda o ya estaba destruida.
        """
        # Si ya estaba hundida, no hay que hacer nada adicional
        if self.hundido:
            return self.HUNDIDO

        # Descontar una vida por el impacto
        self.vida -= 1

        # Comprobar si la nave queda destruida
        if self.vida <= 0:
            self.vida    = 0       # Evitar valores negativos
            self.hundido = True
            print(f"{self.nombre} hundido")
            return self.HUNDIDO
        else:
            print(f"{self.nombre} tocado. Vida restante: {self.vida}")
            return self.TOCADO