import pygame
import pygame.gfxdraw
from sys import exit

pygame.init()
#tracer une fenêtre
larg=600
long=500
c=(0,255,0)
screen=pygame.display.set_mode((larg,long))
screen=pygame.display.set_caption("un jeu test")

screen.fill((255,0,0))


horloge=pygame.time.Clock()



#la boucle d'événement

while True:
    for event in pygame.event.get():
        if event .type == pygame .QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
    horloge.tick(60)
    
