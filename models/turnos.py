import random
from Player import Player

class Turno:
    def __init__(self, num, Players):
        self.num = num  # número de ronda
        self.Players = Players  # lista con cada uno jugadores
        self.actual_player = 0  # índice del jugador actual

    def quien_empieza(self):
        jugador_inicial = random.choice(self.Players)
        print(f'El jugador seleccionado aleatoriamente para empezar es : {jugador_inicial.nombre}')

        self.actual_player = self.Players.index(jugador_inicial)
        self.Players = self.Players[self.actual_player:] + self.Players[:self.actual_player]
        return jugador_inicial

    def jugador_siguiente(self):
        jugador_que_toca=self.actual_player = (self.actual_player + 1) % len(self.Players)
        print(f'Le toca a {self.Players[self.actual_player].nombre}')
        return jugador_que_toca


player_1=Player("German","asd","Azul",100,100)            
player_2=Player("juan","123","Amarillo",100,100) 
player_3=Player("pedro","546","Rojo",100,100) 
player_4=Player("alberto","8790","Verde",100,100) 
jugadores = [player_1, player_2, player_3, player_4]

turno = Turno(1, jugadores)
turno.quien_empieza()
turno.jugador_siguiente()
turno.jugador_siguiente()
turno.jugador_siguiente()
turno.jugador_siguiente()
turno.jugador_siguiente()
