import pygame
from pygame.locals import *

class Campo():

    def __init__(self,nrighe,ncolonne,size,Killer=None):

        self.nrighe=nrighe
        self.ncolonne=ncolonne
        self.width=size[0]
        self.height=size[1]
        self.size=size
        self.verdeC=(162,210,75)
        self.verdeS=(86,138,53)
        self.verdeSf=(172,213,83)
        if Killer==None:
            self.Killer=[]
        else:
            self.Killer=Killer

    def dimRighe(self):
        dim=self.height//self.nrighe
        return dim
    
    def dimColonne(self):
        dim = self.width//self.ncolonne
        return dim



    def draw(self,screen):
        Drighe=self.dimColonne()
        Dcolonne=self.dimRighe()
        i1=0
        j1=0
        for i in range(0,self.width,Drighe):
            for j in range(0,self.height,Dcolonne):
                if i1==0 or j1==0 or j+Dcolonne*2>self.height or i+Drighe*2>self.width:
                    q1=pygame.Rect((i,j),(Drighe,Dcolonne))
                    q1Dim=pygame.surface.Surface((Drighe,Dcolonne))
                    q1Dim.fill(self.verdeS)
                    screen.blit(q1Dim,q1)
                    self.Killer.append((i,j))

                elif (i1+j1)%2==0:
                    q1=pygame.Rect((i,j),(Drighe,Dcolonne))
                    q1Dim=pygame.surface.Surface((Drighe,Dcolonne))
                    q1Dim.fill(self.verdeC)
                    screen.blit(q1Dim,q1)
                else:
                    q1=pygame.Rect((i,j),(Drighe,Dcolonne))
                    q1Dim=pygame.surface.Surface((Drighe,Dcolonne))
                    q1Dim.fill(self.verdeSf)
                    screen.blit(q1Dim,q1)
                j1=j1+1
            j1=0
            i1=i1+1


