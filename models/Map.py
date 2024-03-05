from Cell import Cell


class Map:
    def __init__(self):
        self.cells = [None] * 68  

        # Crear las celdas específicas según tus indicaciones
        self.cells[4] = Cell(5, "Amarillo", True, None,True)  # Punto de inicio para el jugador amarillo
        self.cells[67] = Cell(68, "Amarillo", None, False,True)  # Fin del recorrido para el jugador amarillo

        self.cells[21] = Cell(22, "Azul", True, None,True)  
        self.cells[16] = Cell(17, "Azul", None, False,True) 

        self.cells[38] = Cell(39, "Rojo", True, None,True)  
        self.cells[33] = Cell(34, "Rojo", None, False,True)  

        self.cells[55] = Cell(56, "Verde", True, None,True)  
        self.cells[50] = Cell(51, "Verde", None, False,True) 


    def imprimir_Mapa(self):
        for cell in self.cells:
            if cell:
                print(f"Celda {cell.indice}: Color {cell.color}, Inicio: {cell.inicio}, Fin: {cell.fin}, Protección: {cell.proteccion}")
            else:
                print(f"Celda vacía")

# Crear el tablero
parchis_tablero = Map()
parchis_tablero.imprimir_Mapa()