import pygame
from cell import Cell

class Node:
    def __init__(self, cell):
        self.cell = cell
        self.next = None

class CircularLinkedList:
    def __init__(self, cells):
        self.head = None
        self.tail = None
        for cell in cells:
            self.append(cell)

    def append(self, cell):
        node = Node(cell)
        if not self.head:
            self.head = node
            self.tail = node
            self.tail.next = self.head
        else:
            self.tail.next = node
            self.tail = node
            self.tail.next = self.head

class Map:
    def __init__(self):
        cells = [Cell(i,"Blanco",False,False,False) for i in range(68)]
        cells[4] = Cell(5, "Amarillo", True, False,True)
        cells[67] = Cell(68, "Amarillo", False, True,True)
        cells[21] = Cell(22, "Azul", True, False,True)
        cells[16] = Cell(17, "Azul", False, True,True)
        cells[38] = Cell(39, "Rojo", True, False,True)
        cells[33] = Cell(34, "Rojo", False, True,True)
        cells[55] = Cell(56, "Verde", True, False,True)
        cells[50] = Cell(51, "Verde", False, True,True)
        self.cells = CircularLinkedList(cells)

    def imprimir_mapa(self):
        current = self.cells.head
        while True:
            cell = current.cell
            print(f"Celda {cell.indice}: Color {cell.color}, Inicio: {cell.inicio}, Fin: {cell.fin}, Protección: {cell.proteccion}")
            current = current.next
            if current == self.cells.head:
                break
    
    def draw_map(self, ventana, x_panel, y_panel):
        current = self.cells.head
        cell_width = 38  # Ancho de la celda en píxeles
        cell_height = 76  # Alto de la celda en píxeles
        colores = {
            "Amarillo": (231, 150, 71),  # e79647
            "Verde": (45, 204, 112),  # 2dcc70
            "Rojo": (215, 152, 101),  # d79865
            "Azul": (236, 220, 184)  # ecdcb8
        }
        while True:
            cell = current.cell
            x = x_panel + (cell.indice % 8) * cell_width
            y = y_panel + (cell.indice // 8) * cell_height
            color = (255, 255, 255)  # blanco por defecto
            if cell.color in colores:
                color = colores[cell.color]
            pygame.draw.rect(ventana, color, pygame.Rect(x, y, cell_width, cell_height))
            current = current.next
            if current == self.cells.head:
                break
