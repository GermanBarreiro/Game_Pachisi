import pygame
import json

# Inicialización de Pygame
pygame.init()

# Creación de la ventana
ancho_ventana = 1366
alto_ventana = 768
ventana = pygame.display.set_mode((ancho_ventana, alto_ventana))

# Carga de la imagen de fondo
fondo = pygame.image.load('Mapa.png')

# Ajuste del tamaño de la imagen al de la ventana
fondo = pygame.transform.scale(fondo, (ancho_ventana, alto_ventana))

# Creación del panel
ancho_panel = 800
alto_panel = 770
panel = pygame.Surface((ancho_panel, alto_panel))

# Hacer el panel transparente
panel.set_alpha(0)

# Definir el color del borde
color_borde = (205, 133, 63)  # RGB para marrón claro (carmelita)

# Calcular la posición del panel para centrarlo
x_panel = (ancho_ventana - ancho_panel) / 2
y_panel = (alto_ventana - alto_panel) / 2

# Creación de los botones
boton_salir = pygame.Rect(x_panel + 50, y_panel + 110, 100, 50)  # Rectángulo que representa el botón de salir
color_boton = (255, 255, 255)  # RGB para blanco

# Crear una fuente y renderizar el texto para cada botón
fuente = pygame.font.Font(None, 24)  # Crea una fuente. None significa usar la fuente por defecto, y 24 es el tamaño de la fuente.
texto_salir = fuente.render("Salir", True, (0, 0, 0))  # Renderiza el texto para el botón de salir.

# Bucle principal del juego
run = True
while run:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            run = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if boton_salir.collidepoint(x, y):
                run = False

    # Dibujar la imagen de fondo
    ventana.blit(fondo, (0, 0))

    # Dibujar el panel en la posición deseada
    ventana.blit(panel, (x_panel, y_panel))

    # Dibujar el borde del panel
    pygame.draw.rect(ventana, color_borde, pygame.Rect(x_panel, y_panel, ancho_panel, alto_panel), 10)

    # Dibujar los botones
    pygame.draw.rect(ventana, color_boton, boton_salir)

    # Dibujar el texto en los botones
    ventana.blit(texto_salir, (boton_salir.x + 10, boton_salir.y + 10))  # Ajusta la posición del texto según sea necesario

    pygame.display.flip()

pygame.quit()
