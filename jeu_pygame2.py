import pygame
from pygame.locals import *

pygame.init()
#présentation de la fenêtre
w=600
h=400
screen=pygame.display.set_mode((w,h))
pygame.display.set_caption('Un jeu de lignes')


#les couleurs
blanc=(255,255,255)
noir=(0,0,0)
rouge=(190,180,50)
vert=(0,255,0)
blue=(0,0,255)
jaune=(255,255,0)

#Affichage
screen.fill(rouge)

pygame.draw.rect(screen,noir,[50,150,100,200],2)
#insérer un texte avec une certaine police
police1=pygame.font.SysFont('arial',30)
texte=police1.render("bonjour Mr le lundi!",True,blue)
screen.blit(texte,(300,100))
#faire apparître les objets
pygame.display.update()

#parcourir la boucle d'affichage
parcour=True
while parcour:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            parcour=False

pygame.quit()

