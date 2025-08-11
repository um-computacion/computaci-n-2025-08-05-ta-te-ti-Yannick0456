from jugador import Jugador
from tateti import Tateti

def main():
    print("=== Ta-Te-Ti ===")
    nombre1 = input("Nombre del jugador 1 (X): ")
    nombre2 = input("Nombre del jugador 2 (O): ")

    jugador1 = Jugador(nombre1, "X")
    jugador2 = Jugador(nombre2, "O")
    juego = Tateti(jugador1, jugador2)

    while True:
        juego.tablero.mostrar()
        jugador = juego.jugadores[juego.turno]
        try:
            pos = int(input(f"{jugador.nombre}, elige posición (1-9): ")) - 1
            if pos < 0 or pos > 8:
                print("Posición inválida.")
                continue
        except ValueError:
            print("Debes ingresar un número.")
            continue

        resultado = juego.jugar_turno(pos)
        if resultado:
            juego.tablero.mostrar()
            print(resultado)
            break

if __name__ == "__main__":
    main()
