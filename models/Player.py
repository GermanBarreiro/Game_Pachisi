from Ficha import Ficha

class Player:
    def __init__(self, nombre, nick ,color, vida , mana ):
        self.nombre = nombre
        self.nick = nick
        self.color = color
        self.vida = vida
        self.mana = mana
        self.fichas = [Ficha( color) for _ in range(4)]

    
player_1=Player("German","asd","Azul",100,100)            
player_2=Player("juan","123","Amarillo",100,100) 
player_3=Player("pedro","546","Rojo",100,100) 
player_4=Player("alberto","8790","Verde",100,100) 

jugadores = [player_1, player_2, player_3, player_4]