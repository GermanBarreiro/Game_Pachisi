# importar las miles 
import pygame
# inicializar el game 
pygame.init()
x=0
FPS=60
Reloj=pygame.time.Clock()
#la ventana en que vamos a jugar  
W,H =800,600 
Pantalla=pygame.display.set_mode((W,H))
wallpaper=pygame.image.load("data/fondo_2.png").convert()
x=0
Pantalla.blit(wallpaper, (x,0))

run=True
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:run=False
    x_aux= x % Pantalla.get_rect().width   
    Pantalla.blit(wallpaper, (x_aux-Pantalla.get_rect().width,0))
    if x_aux< W :
        Pantalla.blit(wallpaper,(x_aux,0))


    x-=1    
    pygame.display.flip()
    Reloj.tick(FPS)    

pygame.quit
