# importar las miles 
import pygame
# inicializar el game 
pygame.init()
x=0
#la ventana en que vamos a jugar  
size =800,600 
Pantalla=pygame.display.set_mode(size)
wallpaper=pygame.image.load("data/fondo_2.png").convert()
Pantalla.blit(wallpaper, (x,0))

run=True
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:run=False
    Pantalla.blit(wallpaper, (x,0))
    pygame.display.flip()    

pygame.quit
