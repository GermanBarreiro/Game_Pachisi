from Ficha import Ficha
class Player:
    def __init__(self, nombre, nick ,color, vida , mana ):
            self.nombre = nombre #string
            self.nick = nick #string
            self.color = color #string
            self.vida = vida #num -defecto-100
            self.mana = mana #num -defecto-100
            #self.personaje=personaje #el personaje elegido


            self.fichas = [Ficha(i+1, i+2, i+3, i+4, self) for i in range(4)]