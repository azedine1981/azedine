import pygame
pygame.init()
#présentation de la fenêtre
w=700
h=500
screen=pygame.display.set_mode((w,h))
pygame.display.set_caption('Un jeu primitif')
horloge=pygame.time.Clock()
FPS=60

#les couleurs
blanc=(255,255,255)
noir=(0,0,0)
rouge=(190,180,50)
vert=(0,255,0)
blue=(0,0,255)
jaune=(255,255,200)

#remplissage de la fenêtre
screen.fill(rouge)


#tracer des formes géométriques
cercle=pygame.draw.circle(screen,blue,(100,100),50,4)
rectangle=pygame.draw.rect(screen,jaune,[200,200,100,100],1)
ligne=pygame.draw.line(screen,(100,100,255),(200,40),(500,100),4)

#dessiner des lignes discontinues

#chargement d'une image
image=pygame.image.load('jeu.png')
imagex=400
imagey=100
direction='left'
screen.blit(image,(imagex,imagey))


surf=pygame.Surface((100,100))
surf.fill(blanc)
screen.blit(surf,rectangle)
#faire afficher un texte


#faire apparître les objets
pygame.display.flip()

#parcourir la boucle d'affichage
parcour=True
while parcour:
    horloge.tick(FPS)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            parcour=False

pygame.quit()
