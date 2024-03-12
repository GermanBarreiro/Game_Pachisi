from player import Player
from dado import tirar_dado
from map import Map
from turnos import Turno 
import random

class Juego:
    def __init__(self, jugadores):
        self.jugadores = jugadores
        self.tablero = Map()
        self.turno = Turno(1, jugadores)

    def fichas_en_meta(self, jugador):
        return all(ficha.on_finish for ficha in jugador.fichas)

    def mover_ficha(self, jugador, ficha, movimientos):
        # Encuentra la posición actual de la ficha
        for i, celda in enumerate(self.tablero.cells):
            if celda.color == ficha.color:
                posicion_actual = i
                break

        # Calcula la nueva posición
        nueva_posicion = (posicion_actual + movimientos) % len(self.tablero.cells)

        # Mueve la ficha a la nueva posición
        self.tablero.cells[posicion_actual].color = "Blanco"
        self.tablero.cells[nueva_posicion].color = ficha.color
        print(f"La ficha {ficha.color} del jugador {jugador.nombre} se ha movido a la celda {nueva_posicion}.")

    def check_ganador(self):
        # Este método verifica si hay un ganador
        ganadores = [jugador for jugador in self.jugadores if self.fichas_en_meta(jugador)]
        if len(ganadores) == 3:
            perdedor = [jugador for jugador in self.jugadores if jugador not in ganadores][0]
            print(f"Los ganadores son {ganadores[0].nombre}, {ganadores[1].nombre} y {ganadores[2].nombre}. El último lugar es para {perdedor.nombre}.")
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
