from Cell import Cell
from Player import Player
from Ficha import Ficha
from Map import Map
from turnos import Turno
from Dado import tirar_dado

class Juego:
      
   
   
   
   
   
   
   
   
   
   """ def __init__(self, jugadores, screen, font):
        self.jugadores = jugadores
        self.tablero = Map()
        self.turno = Turno(1, jugadores)
        self.screen = screen
        self.font = font

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
            self.mover_ficha_desde_inicio(jugador)
        else:
            self.mover_ficha_en_tablero(jugador, dado1 + dado2)
        self.tablero.imprimir_Mapa()

    def mover_ficha_desde_inicio(self, jugador):
        for ficha in jugador.fichas:
            if ficha.en_inicio():
                ficha.mover_a_tablero(self.tablero.punto_inicio(jugador.color))
                break

    def mover_ficha_en_tablero(self, jugador, pasos):
        for ficha in jugador.fichas:
            if ficha.en_tablero():
                ficha.mover(pasos)
                break """
