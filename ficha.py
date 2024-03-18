class Ficha:
    def __init__(self, color, indice):
        self.on_star = True
        self.on_finish=False
        self.color=color
        self.out_of_start = False
        self.indice = indice  # Añade un identificador único a cada ficha
