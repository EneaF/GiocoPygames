import pygame
from pygame.locals import *

class Mela():
    def __init__(self,pos,size):
        self.pos=pos
        self.image=pygame.Surface(size)
        self.rect=pygame.Rect((pos[0],pos[1]),(size[0],size[1]))
        self.Immagine=pygame.image.load("Mela.png")
    
    def draw(self,screen,pos,size):
        rect=pygame.Rect((pos[0],pos[1]),(size[0],size[1]))
        screen.blit(self.Immagine,rect)