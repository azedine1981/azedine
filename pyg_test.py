# importation du module et des constantes locales
import pygame
from pygame.locals import *
# initialisation (à ne pas oublier!)
pygame.init()
# creation de la surface "fenêtre"
dimensions = (largeur, hauteur) = (200, 300)
fenetre = pygame.display.set_mode(dimensions)
# dessin dans la surface fenêtre
jaune = (255, 255, 0) # le code RGB de la couleur jaune
fenetre.fill(jaune)
# affichage
pygame.event.get()# pas necessaire, en theorie...
pygame.time.wait(5000)
pygame.quit()
