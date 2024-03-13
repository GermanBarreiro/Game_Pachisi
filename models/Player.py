from ficha import Ficha

class Player:
    def __init__(self, nombre, nick ,color, vida , mana ):
        self.nombre = nombre
        self.nick = nick
        self.color = color
        self.vida = vida
        self.mana = mana
        self.fichas = [Ficha(color) for _ in range(4)]

    def fichas_fuera(self):
        # Este método devuelve True si el jugador tiene al menos una ficha fuera
        return any(ficha.out_of_start for ficha in self.fichas)

    def sacar_ficha(self):
        # Este método saca una ficha del jugador
        for ficha in self.fichas:
            if not ficha.out_of_start:
                ficha.out_of_start = True
                print(f"La ficha {ficha.color} del jugador {self.nombre} ha sido sacada.")
                break
