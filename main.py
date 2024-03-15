import pygame
import Map

pygame.init()

# Define las dimensiones de la ventana
ancho_ventana = 1366
alto_ventana = 768

# Crea la ventana
ventana = pygame.display.set_mode((ancho_ventana, alto_ventana))

# Crea el mapa
mapa = Map()
# Bucle principal del juego
Run = True
while Run:
    # Rellena la ventana con blanco
    ventana.fill((255, 255, 255))
    
    mapa.draw_map(ventana, ancho_ventana, alto_ventana)

    
    # Actualiza la ventana
    pygame.display.update()
    
    # Manejo de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            Run = False

pygame.quit()