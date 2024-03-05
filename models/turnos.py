import random
from Player import Player


class Turno:
    def __init__(self, num, Players):
        self.num = num  # número de ronda
        self.Players = Players  # lista con cada uno jugadores

    def quien_empieza(self):
        jugador = random.choice(self.Players)
        print(f'El jugador seleccionado aleatoriamente para empezar es : {jugador.nombre}')

player_1=Player("German","asd","Azul",100,100)            
player_2=Player("juan","123","Amarillo",100,100) 
player_3=Player("pedro","546","Rojo",100,100) 
player_4=Player("alberto","8790","Verde",100,100) 

jugadores = [player_1, player_2, player_3, player_4]


turno = Turno(1, jugadores)


turno.quien_empieza()
