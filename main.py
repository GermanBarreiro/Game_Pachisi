 # importar las miles 
import sys,pygame
  # inicializar el game 
pygame.init()

#la ventana en que vamos a jugar  
size =800,600 
screen =pygame.display.set_mode(size)
pygame.display.set_caption("Parchi")

#ciclo infinito para  que solo se cierre si se preciona el cerrar
run=True
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:run=False

pygame.quit       
