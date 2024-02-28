#!/usr/bin/python

import pygame
from pygame.locals import *
ANCHO_PANTALLA = 800
ALTO_PANTALLA = 600
VELOCIDAD_BARRA = 1
VELOCIDAD_PELOTA_X = 1
VELOCIDAD_PELOTA_Y = 1

def main():
    pygame.init()

    screen = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
    pygame.display.set_caption('barra')

    Pantalla = pygame.Surface(screen.get_size())
    Pantalla = Pantalla.convert()
    Pantalla.fill((173, 216, 230))

    # Posición inicial de la pelota
    pelota_x = ANCHO_PANTALLA // 2
    pelota_y = ALTO_PANTALLA // 2
    pelota_dx = VELOCIDAD_PELOTA_X
    pelota_dy = VELOCIDAD_PELOTA_Y

    # Posición inicial de la barra
    barra_x = ANCHO_PANTALLA // 2
    barra_y = ALTO_PANTALLA - 20

    font = pygame.font.Font(None, 72)
    text = font.render(" hola cara de picha", 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = Pantalla.get_rect().centerx
    Pantalla.blit(text, textpos)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()  # Cierra pygame
                return

        # Movimiento de la barra
        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            barra_x -= VELOCIDAD_BARRA
        if keys[K_RIGHT]:
            barra_x += VELOCIDAD_BARRA

        # Movimiento de la pelota
        pelota_x += pelota_dx
        pelota_y += pelota_dy

        # Rebote de la pelota en los bordes de la panta;;a
        if pelota_x <= 0 or pelota_x >= ANCHO_PANTALLA:
            pelota_dx *= -1
        if pelota_y <= 0 or pelota_y >= ALTO_PANTALLA:
            pelota_dy *= -1

        # Rebota de la pelota en la barro
        if pelota_y >= barra_y and pelota_x >= barra_x and pelota_x <= barra_x + 100:
            pelota_dy *= -1

        # pintoo la barra y la pelota
        Pantalla.fill((173, 216, 230))
        pygame.draw.rect(Pantalla, (0, 0, 0), (barra_x, barra_y, 100, 10))
        pygame.draw.circle(Pantalla, (255, 0, 0), (pelota_x, pelota_y), 10)

        screen.blit(Pantalla, (0, 0))
        pygame.display.flip()

if __name__ == "__main__":
    main()