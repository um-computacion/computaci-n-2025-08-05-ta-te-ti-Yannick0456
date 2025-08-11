from jugador import Jugador
from tablero import Tablero

class Tateti:
    def __init__(self, jugador1, jugador2):
        self.tablero = Tablero()
        self.jugadores = [jugador1, jugador2]
        self.turno = 0

    def jugar_turno(self, posicion):
        jugador = self.jugadores[self.turno]
        if self.tablero.marcar(posicion, jugador.simbolo):
            if self.tablero.hay_ganador():
                return f"¡{jugador.nombre} ha ganado!"
            elif self.tablero.lleno():
                return "Empate"
            else:
                self.turno = 1 - self.turno
                return None
        else:
            return "Casilla ocupada"
