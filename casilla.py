"""
Módulo casilla.py
Representa una posición individual del tablero de juego.
"""


class Casilla:
    """
    Representa una casilla del tablero de 10x10.

    Cada casilla puede estar vacía (agua) u ocupada por una nave.
    Además, guarda memoria de si ya ha recibido un disparo,
    evitando que se pueda disparar dos veces al mismo lugar.

    Atributos:
        nave (Nave | None): referencia a la nave que ocupa esta casilla,
                            o None si es agua.
        visitada (bool):    True si esta casilla ya ha sido disparada,
                            False si todavía no.
    """

    def __init__(self):
        """
        Constructor. Inicializa la casilla vacía y sin disparar.
        """
        self.nave = None        # Por defecto, la casilla es agua
        self.visitada = False   # Por defecto, no ha sido disparada

    def disparar(self):
        """
        Procesa un disparo sobre esta casilla.

        Si la casilla ya fue disparada anteriormente, informa y no hace nada.
        Si es la primera vez, la marca como visitada y comprueba si hay nave:
            - Sin nave  → devuelve 0 (AGUA)
            - Con nave  → delega en la nave y devuelve 1 (TOCADO) o 2 (HUNDIDO)

        Returns:
            None  → casilla ya disparada anteriormente
            0     → AGUA, no había nave
            1     → TOCADO, hay nave y sigue viva
            2     → HUNDIDO, la nave se ha quedado sin vida
        """
        # Si ya se disparó aquí, no hacer nada
        if self.visitada:
            print("Ya disparaste aquí")
            return None

        # Marcar como visitada para que no se pueda volver a disparar
        self.visitada = True

        # Si no hay nave, es agua
        if self.nave is None:
            print("Agua")
            return 0

        # Si hay nave, delegarle el disparo y devolver su resultado
        return self.nave.recibir_disparo()