from cell import Cell
class Map:
    def __init__(self):
        self.cells = [Cell(i,"Blanco",False,False,False) for i in range(68) ]    

        self.cells[4] = Cell(5, "Amarillo", True, False,True)  # Punto de inicio para el jugador amarillo
        self.cells[67] = Cell(68, "Amarillo", False, True,True)  # Fin del recorrido para el jugador amarillo

        self.cells[21] = Cell(22, "Azul", True, False,True)  
        self.cells[16] = Cell(17, "Azul", False, True,True) 

        self.cells[38] = Cell(39, "Rojo", True, False,True)  
        self.cells[33] = Cell(34, "Rojo", False, True,True)  

        self.cells[55] = Cell(56, "Verde", True, False,True)  
        self.cells[50] = Cell(51, "Verde", False, True,True) 


    def imprimir_mapa(self):
        for cell in self.cells:
            print(f"Celda {cell.indice}: Color {cell.color}, Inicio: {cell.inicio}, Fin: {cell.fin}, Protección: {cell.proteccion}")
            

# Crear el tablero
parchis_tablero = Map()
parchis_tablero.imprimir_mapa()