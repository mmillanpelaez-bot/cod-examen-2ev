"""
Módulo tablero.py
Representa el tablero de juego de 10x10 casillas.
"""

from nave import Nave
from casilla import Casilla


class Tablero:
    """
    Gestiona el tablero de juego: una matriz de 10x10 objetos Casilla.

    Cada posición del tablero es un objeto Casilla que puede contener
    una nave o estar vacía. El Tablero no resuelve el disparo directamente,
    sino que delega esa responsabilidad en la Casilla correspondiente.

    Atributos de clase (constantes de resultado):
        AGUA    (int): 0 → el disparo cayó en agua
        TOCADO  (int): 1 → el disparo impactó una nave que sigue viva
        HUNDIDO (int): 2 → el disparo destruyó completamente una nave

    Atributos de instancia:
        casillero (list[list[Casilla]]): matriz 10x10 de objetos Casilla
    """

    AGUA    = 0
    TOCADO  = 1
    HUNDIDO = 2

    def __init__(self):
        """
        Constructor. Crea la matriz de Casillas y coloca las naves en el tablero.
        """

        # ── Crear las naves
        por1 = Nave("Enterprise",      "portaaviones", 5)

        fra1 = Nave("Bismarck",        "fragata", 3)
        fra2 = Nave("Prince of Wales", "fragata", 3)
        fra3 = Nave("Graf Spee",       "fragata", 3)

        sub1 = Nave("U-47",  "submarino", 1)
        sub2 = Nave("U-96",  "submarino", 1)
        sub3 = Nave("U-505", "submarino", 1)
        sub4 = Nave("U-534", "submarino", 1)

        # Crear la matriz 10x10 de objetos Casilla
        # Comprensión de lista: genera 10 filas, cada una con 10 Casillas nuevas
        self.casillero = [[Casilla() for _ in range(10)] for _ in range(10)]

        # Colocar naves: asignar cada nave a las casillas que ocupa

        # Enterprise (portaaviones) — fila 1, columnas 1 a 5 (horizontal)
        self.casillero[1][1].nave = por1
        self.casillero[1][2].nave = por1
        self.casillero[1][3].nave = por1
        self.casillero[1][4].nave = por1
        self.casillero[1][5].nave = por1

        # Bismarck (fragata) — columna 3, filas 3 a 5 (vertical)
        self.casillero[3][3].nave = fra1
        self.casillero[4][3].nave = fra1
        self.casillero[5][3].nave = fra1

        # Prince of Wales (fragata) — fila 7, columnas 1 a 3 (horizontal)
        self.casillero[7][1].nave = fra2
        self.casillero[7][2].nave = fra2
        self.casillero[7][3].nave = fra2

        # Graf Spee (fragata) — fila 9, columnas 1 a 3 (horizontal)
        self.casillero[9][1].nave = fra3
        self.casillero[9][2].nave = fra3
        self.casillero[9][3].nave = fra3

        # Submarinos (1 casilla cada uno)
        self.casillero[4][6].nave = sub1
        self.casillero[9][9].nave = sub2
        self.casillero[7][6].nave = sub3
        self.casillero[9][5].nave = sub4

    def comprobar_impacto(self, x, y):
        """
        Recibe las coordenadas de un disparo y delega en la Casilla correspondiente.

        No resuelve el disparo directamente: es la Casilla quien decide
        si ya fue visitada, si hay nave, y qué devolver.

        Args:
            x (int): fila del disparo (0-9)
            y (int): columna del disparo (0-9)

        Returns:
            int | None: resultado devuelto por la Casilla
                None → ya disparada
                0    → agua
                1    → tocado
                2    → hundido
        """
        return self.casillero[x][y].disparar()