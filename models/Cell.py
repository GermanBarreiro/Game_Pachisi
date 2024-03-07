import typing
class Cell:
    def __init__(self, indice, color, inicio, fin, proteccion):
        self.indice : int  = indice #numeros
        self.color :str = color #string
        self.inicio :bool= inicio #buleano
        self.fin :bool= fin #buleano
        self.proteccion :bool = proteccion #buleano
