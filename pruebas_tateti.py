import unittest
from jugador import Jugador
from tateti import Tateti

class TestTateti(unittest.TestCase):
    def setUp(self):
        self.j1 = Jugador("Jugador1", "X")
        self.j2 = Jugador("Jugador2", "O")
        self.juego = Tateti(self.j1, self.j2)

    def test_gana_fila(self):
        self.juego.tablero.casillas = ["X", "X", "X", " ", " ", " ", " ", " ", " "]
        self.assertTrue(self.juego.tablero.hay_ganador())

    def test_empate(self):
        self.juego.tablero.casillas = ["X", "O", "X", "X", "O", "O", "O", "X", "X"]
        self.assertTrue(self.juego.tablero.lleno())

if __name__ == "__main__":
    unittest.main()
