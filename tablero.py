class Tablero:
    def __init__(self):
        self.casillas = [" "] * 9

    def mostrar(self):
        for i in range(0, 9, 3):
            print(f" {self.casillas[i]} | {self.casillas[i+1]} | {self.casillas[i+2]} ")
            if i < 6:
                print("---+---+---")

    def marcar(self, posicion, simbolo):
        if self.casillas[posicion] == " ":
            self.casillas[posicion] = simbolo
            return True
        return False

    def hay_ganador(self):
        combinaciones = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Filas
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columnas
            (0, 4, 8), (2, 4, 6)               # Diagonales
        ]
        for a, b, c in combinaciones:
            if self.casillas[a] == self.casillas[b] == self.casillas[c] != " ":
                return True
        return False

    def lleno(self):
        return " " not in self.casillas
