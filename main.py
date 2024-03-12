import pygame
from Game_Pachisi.models import Juego

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))  # Define el tamaño de la ventana
    font = pygame.font.Font(None, 24)  # Define la fuente para renderizar el texto

    # Crear jugadores y añadirlos a la lista de jugadores
    jugadores = []
    juego = Juego.Juego(jugadores, screen, font)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Cierra el juego si el usuario cierra la ventana
                running = False
        juego.jugar()
        pygame.display.flip()  # Actualiza la pantalla

    pygame.quit()

if __name__ == "__main__":
    main()
