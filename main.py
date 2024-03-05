import pygame
from models import Map
from models import Turno
from models import Dado
from models import Cell

class Juego:
    def __init__(self, jugadores):
        self.jugadores = jugadores
        self.tablero = Map()
        self.turno = Turno(1, jugadores)
        self.screen = pygame.display.set_mode((800, 600))  # Define el tamaño de la ventana
        self.font = pygame.font.Font(None, 24)  # Define la fuente para renderizar el texto

    def imprimir_en_pantalla(self, texto):
        text_surface = self.font.render(texto, True, (255, 255, 255))  # Crea una superficie con el texto
        self.screen.blit(text_surface, (0, 0))  # Dibuja la superficie en la pantalla

    def jugar(self):
        jugadores_en_meta = 0
        running = True
        while running and jugadores_en_meta < 3:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Cierra el juego si el usuario cierra la ventana
                    running = False
            for jugador in self.jugadores:
                self.turno.jugador_actual = jugador
                self.jugar_turno(jugador)
                if self.jugador_en_meta(jugador):
                    jugadores_en_meta += 1
                    if jugadores_en_meta == 3:
                        break
            pygame.display.flip()  # Actualiza la pantalla

    def jugar_turno(self, jugador):
        dado1 = Dado.tirar_dado()
        dado2 = Dado.tirar_dado()
        if dado1 == dado2 or dado1 == 5 or dado2 == 5:
        # El jugador mueve una ficha desde el inicio
            self.mover_ficha_desde_inicio(jugador)
        else:
        # El jugador mueve una ficha en el tablero
            self.mover_ficha_en_tablero(jugador, dado1 + dado2)
            self.tablero.imprimir_Mapa()

    def mover_ficha_desde_inicio(self, jugador):
    # Encuentra una ficha en el inicio y muévela al tablero
        for ficha in jugador.fichas:
            if ficha.en_inicio():
            # Mueve la ficha a la celda de inicio correcta según su color
                ficha.mover_a_tablero(self.tablero.punto_inicio(jugador.color))
                break


    def mover_ficha_en_tablero(self, jugador, pasos):
    # Encuentra una ficha en el tablero y muévela
        for ficha in jugador.fichas:
            if ficha.en_tablero():
                ficha.mover(pasos)
                break


pygame.init()
# Crear jugadores y añadirlos a la lista de jugadores
jugadores = []
juego = Juego(jugadores)
juego.jugar()
pygame.quit()
