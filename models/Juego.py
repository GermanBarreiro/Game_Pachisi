from Map import Map
from Game_Pachisi.models.Turno import Turno
from Dado import tirar_dado

class Juego:
    def __init__(self, jugadores):
        self.jugadores = jugadores
        self.tablero = Map()
        self.turno = Turno(1, jugadores)

    def jugar(self):
        jugadores_en_meta = 0
        while jugadores_en_meta < 3:
            for jugador in self.jugadores:
                self.turno.jugador_actual = jugador
                self.jugar_turno(jugador)
                if self.jugador_en_meta(jugador):
                    jugadores_en_meta += 1
                    if jugadores_en_meta == 3:
                        break

    def jugar_turno(self, jugador):
        dado1 = tirar_dado()
        dado2 = tirar_dado()
        if dado1 == dado2 or dado1 == 5 or dado2 == 5:
        # El jugador mueve una ficha desde el inicio
            self.mover_ficha_desde_inicio(jugador)
        else:
        # El jugador mueve una ficha en el tablero
            self.mover_ficha_en_tablero(jugador, dado1 + dado2)
            self.tablero.imprimir_Mapa()

    def mover_ficha_desde_inicio(self, jugador):
    # Encuentra una ficha en el inicio y muévela al tablero
        for ficha in jugador.fichas:
            if ficha.en_inicio():
            # Mueve la ficha a la celda de inicio correcta según su color
                ficha.mover_a_tablero(self.tablero.punto_inicio(jugador.color))
                break


    def mover_ficha_en_tablero(self, jugador, pasos):
    # Encuentra una ficha en el tablero y muévela
        for ficha in jugador.fichas:
            if ficha.en_tablero():
                ficha.mover(pasos)
                break

