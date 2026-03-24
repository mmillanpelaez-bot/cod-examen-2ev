"""
Módulo juego.py
Controlador principal del juego Hundir la Flota.
"""

from tablero import Tablero


class Juego:
    """
    Controlador principal del juego.

    Coordina la partida: recibe los ataques del usuario, los delega
    al Tablero y muestra el resultado por pantalla.

    El Tablero se crea una única vez en el constructor para que la
    memoria de casillas visitadas se mantenga durante toda la partida.

    Atributos:
        tablero (Tablero): el tablero de juego con las naves colocadas
    """

    def __init__(self):
        """
        Constructor. Inicializa el juego creando el tablero.
        El tablero se crea aquí (una sola vez) para que persista
        entre ataques y las casillas guarden su estado.
        """
        self.tablero = Tablero()

    def mostrar_resultado(self, resultado):
        """
        Traduce el código de resultado a un mensaje legible para el usuario.

        Args:
            resultado (int | None): código devuelto por el tablero
                None → casilla ya disparada
                0    → agua
                1    → tocado
                2    → hundido
        """
        if resultado is None:
            print("Ya disparaste aquí")
        elif resultado == 0:
            print("Agua")
        elif resultado == 1:
            print("Tocado")
        elif resultado == 2:
            print("Hundido")

    def lanzar_ataque(self, x, y):
        """
        Ejecuta un disparo en las coordenadas indicadas.

        Delega en el Tablero la comprobación del impacto y luego
        muestra el resultado por pantalla.

        Args:
            x (int): fila del disparo (0-9)
            y (int): columna del disparo (0-9)
        """
        print(f"\nAtaque en ({x}, {y})")
        resultado = self.tablero.comprobar_impacto(x, y)
        self.mostrar_resultado(resultado)

    def jugar_demo(self):
        """
        Secuencia de prueba que demuestra todos los casos posibles:
        agua, tocado, hundido y casilla ya visitada.
        """
        # Caso 1: disparo a agua
        self.lanzar_ataque(0, 0)

        # Caso 2: tocado al portaaviones (tiene 5 de vida, no se hunde)
        self.lanzar_ataque(1, 1)

        # Caso 3: repetir la misma casilla → "Ya disparaste aquí"
        self.lanzar_ataque(1, 1)

        # Caso 4: hundir el submarino U-47 (solo tiene 1 de vida)
        self.lanzar_ataque(4, 6)


if __name__ == "__main__":
    juego = Juego()
    juego.jugar_demo()