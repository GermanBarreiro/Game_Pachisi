from player import Player
from dado import tirar_dado
from map import Map
from turnos import Turno 
import random
import json

# Abre el archivo JSON y carga los datos
with open('clics.json', 'r') as f:
    clics = json.load(f)

class Juego:
    def __init__(self, jugadores):
        self.jugadores = jugadores
        self.tablero = Map()
        self.turno = Turno(1, jugadores)

    def fichas_en_meta(self, jugador):
        return all(ficha.on_finish for ficha in jugador.fichas)

    def mover_ficha(self, jugador, ficha, movimientos):
        # Encuentra la posición actual de la ficha
        current = self.tablero.cells.head
        while current.cell.indice != ficha.indice:  # Busca la ficha por su índice en lugar de por su color
            current = current.next

        # Calcula la nueva posición
        for _ in range(movimientos):
            current = current.next

        # Mueve la ficha a la nueva posición
        current.cell.indice = ficha.indice  # Actualiza el índice de la celda con el de la ficha

        # Actualiza la posición de la ficha en la imagen
        ficha.x, ficha.y = clics[current.cell.indice]  # Asume que 'clics' es una lista de coordenadas (x, y)

        print(f"La ficha {ficha.indice} del jugador {jugador.nombre} se ha movido a la celda {current.cell.indice}.")

    def check_ganador(self):
        # Este método verifica si hay un ganador
        ganador = [jugador for jugador in self.jugadores if self.fichas_en_meta(jugador)]
        if ganador:  # Si hay un ganador
            print(f"El ganador es {ganador[0].nombre}.")
            return True
        return False

    def jugar_turno(self):
        jugador_actual = self.turno.jugador_siguiente()
        print(f"Turno del jugador {jugador_actual.nombre}.")
    
        # Lanza los dados
        dado1 = tirar_dado()
        dado2 = tirar_dado()
        print(f"Los dados han caído en {dado1} y {dado2}.")
    
        # Si los dados son iguales o alguno es 5, saca una ficha
        if dado1 == dado2 or dado1 == 5 or dado2 == 5:
            if not jugador_actual.fichas_fuera():
                jugador_actual.sacar_ficha()
    
        # Elige una ficha al azar para mover
        fichas_fuera = [ficha for ficha in jugador_actual.fichas if ficha.out_of_start]
        if fichas_fuera:  # Si hay fichas fuera
            ficha_a_mover = random.choice(fichas_fuera)
            # Mueve la ficha
            self.mover_ficha(jugador_actual, ficha_a_mover, dado1 + dado2)
        else:
            print(f"El jugador {jugador_actual.nombre} no tiene fichas fuera para mover.")
    
        # Verifica si hay un ganador después de mover la ficha
        if self.check_ganador():
            print("El juego ha terminado.")
            return

        # Imprime el tablero después de cada turno
        self.tablero.imprimir_mapa()
