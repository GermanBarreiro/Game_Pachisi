import pygame
from pygame.locals import *
    
pygame.init()





screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Roll battel")

run = True
while run:
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False

        # Actualizar la pantalla
        pygame.display.flip()

pygame.quit()  
