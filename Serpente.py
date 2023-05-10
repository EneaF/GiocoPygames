import pygame
from pygame.locals import *
from coda import coda

class Serpente():
    def __init__(self,pos,size,ultimo=False,T=False):
        self.coloreC=(80,122,218)
        self.image=pygame.Surface(size)
        self.pos=pos
        self.size=size
        self.rect=pygame.Rect((pos[0],pos[1]),(size[0],size[1]))
        self.T=T
        self.indicazioni=coda()
        self.indicazioniUltimo=coda()
        self.ultimaIndicazione=None
        self.ultimaPosizione=None
        self.ultimo=ultimo

        self.TestaUP=pygame.image.load("Testa_Su.png")
        self.TestaDOWN=pygame.image.load("Testa_Giu.png")
        self.TestaLEFT=pygame.image.load("Testa_Sinistra.png")
        self.TestaRIGHT=pygame.image.load("Testa_Destra.png")


    def draw(self,screen,size,pos,Testa=0):
        if self.T==True:
            rect=pygame.Rect((pos[0],pos[1]),(size[0],size[1]))
            screen.blit(Testa,rect)
        if self.T==False:
            rect=pygame.Rect((pos[0],pos[1]),(size[0],size[1]))
            self.image.fill(self.coloreC)
            screen.blit(self.image,rect)
    
    def muoviT(self,size,dir,screen):
        if dir==0:
            self.pos=(self.pos[0],self.pos[1]-size[1])
            self.draw(screen,size,self.pos,self.TestaUP)
        if dir==1:
            self.pos=(self.pos[0],self.pos[1]+size[1])
            self.draw(screen,size,self.pos,self.TestaDOWN)
        if dir==2:
            self.pos=(self.pos[0]-size[0],self.pos[1])
            self.draw(screen,size,self.pos,self.TestaLEFT)
        if dir==3:
            self.pos=(self.pos[0]+size[0],self.pos[1])
            self.draw(screen,size,self.pos,self.TestaRIGHT)
    
    def muoviC(self,size,dir,screen):

        if dir==0:
            self.indicazioni.push(dir)
            self.indicazioniUltimo.push(dir)
            dir=self.indicazioni.front()
            if self.ultimo==True:
                self.ultimaPosizione=self.pos
                self.ultimaIndicazione=dir
            self.indicazioni.pop()
            self.indicazioniUltimo.pop()
            self.muoviT(size,dir,screen)

        elif dir==1:
            self.indicazioni.push(dir)
            self.indicazioniUltimo.push(dir)
            dir=self.indicazioni.front()
            if self.ultimo==True:
                self.ultimaPosizione=self.pos
                self.ultimaIndicazione=dir
            self.indicazioni.pop()
            self.indicazioniUltimo.pop()
            self.muoviT(size,dir,screen)

        elif dir==2:
            self.indicazioni.push(dir)
            self.indicazioniUltimo.push(dir)
            dir=self.indicazioni.front()
            if self.ultimo==True:
                self.ultimaPosizione=self.pos
                self.ultimaIndicazione=dir
            self.indicazioni.pop()
            self.indicazioniUltimo.pop()
            self.muoviT(size,dir,screen)
            
        elif dir==3:
            self.indicazioni.push(dir)
            self.indicazioniUltimo.push(dir)
            dir=self.indicazioni.front()
            if self.ultimo==True:
                self.ultimaPosizione=self.pos
                self.ultimaIndicazione=dir
            self.indicazioni.pop()
            self.indicazioniUltimo.pop()
            self.muoviT(size,dir,screen)

