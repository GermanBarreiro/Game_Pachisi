from player import Player
import random

class Turno:
    def __init__(self, num, players):
        self.num = num  # número de ronda
        self.players = players  # lista con cada uno jugadores
        self.actual_player = 0  # índice del jugador actual

    def quien_empieza(self):
        jugador_inicial = random.choice(self.players)
        print(f'El jugador seleccionado aleatoriamente para empezar es : {jugador_inicial.nombre}')

        self.actual_player = self.players.index(jugador_inicial)
        self.players = self.players[self.actual_player:] + self.players[:self.actual_player]
        return jugador_inicial

    def jugador_siguiente(self):
        jugador_que_toca = self.players[self.actual_player]
        print(f"Turno {self.num}. Le toca a {jugador_que_toca.nombre}")
        self.actual_player = (self.actual_player + 1) % len(self.players)
        if self.actual_player == 0:  # Si es el turno del primer jugador
            self.num += 1  # Incrementa el número de turno
        return jugador_que_toca
