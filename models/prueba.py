from player import Player
from juego import Juego

# Crear los jugadores
player_1 = Player("German", "asd", "Azul", 100, 100)            
player_2 = Player("Juan", "123", "Amarillo", 100, 100) 
player_3 = Player("Pedro", "546", "Rojo", 100, 100) 
player_4 = Player("Alberto", "8790", "Verde", 100, 100) 

# Añadir los jugadores a una lista
jugadores = [player_1, player_2, player_3, player_4]

# Crear el juego
juego = Juego(jugadores)

# Comenzar el juego
juego.turno.quien_empieza()

# Jugar 20 turnos como ejemplo
for _ in range(20):
    juego.jugar_turno()
