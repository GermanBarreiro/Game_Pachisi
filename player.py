from ficha import Ficha  
class Player:
    def __init__(self, nombre, nick ,color, vida , mana ):
        self.nombre = nombre
        self.nick = nick
        self.color = color
        self.vida = vida
        self.mana = mana
        self.fichas = [Ficha(color, i) for i in range(4)]  # Crea las fichas con un identificador único
