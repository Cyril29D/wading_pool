import pygame
from pygame.locals import *
import pendu

# réfrence pour les textes : https://stackoverflow.com/questions/20842801/how-to-display-text-in-pygame
pygame.init()

fenetre = pygame.display.set_mode((600, 600))

img1 = "img/pendu.jpg"
fond = pygame.image.load(img1)
fond = pygame.transform.scale(fond, (600, 600))
fenetre.blit(fond, (0, 0))

pygame.font.init()
my_font = pygame.font.SysFont("Comic Sans MS", 50)
text_surface = my_font.render("Le jeu du Pendu :)", False, (255, 255, 255))
fenetre.blit(text_surface, (0, 0))


continuer = True
while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False
    pygame.display.update()


pygame.quit()
