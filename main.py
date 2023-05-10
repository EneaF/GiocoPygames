import pygame, sys, os, random
from pygame.locals import *
from Campo import Campo
from Serpente import Serpente
from Mela import Mela
from coda import coda
from Riquadri import RiqScritto

print("Gioco programmato da Enea Fascilla 3P")

pygame.init()

WINDOW_SIZE=(1000,700)
screen = pygame.display.set_mode(WINDOW_SIZE)
screen.fill((172,213,83))
pygame.display.set_caption("Snake")

clock=pygame.time.Clock()
fps=7
campo = Campo(14,20,WINDOW_SIZE)
# campo.draw(screen)

Dim=(50,50)

posMela=((650,350))
mela = Mela(posMela,Dim)

posPunti=(755,5)
sizePunti=(190,40)

posBest=(55,5)
sizeBest=(190,40)

posRestart=(355,655)
sizeRestart=(290,40)

posStart=(355,600)
sizeStart=(290,90)

posResetBest=(695,600)
sizeResetBest=(240,70)

posQuit=(75,600)
sizeQuit=(240,70)

punti = RiqScritto(screen, posPunti, sizePunti, "Punti:")
best = RiqScritto(screen, posBest, sizeBest, "Best:")
restart= RiqScritto(screen, posRestart, sizeRestart, "Restart")

Start = RiqScritto(screen, posStart, sizeStart, "START")
ResetBest = RiqScritto(screen, posResetBest, sizeResetBest, "Reset Best")
QuitButton = RiqScritto(screen, posQuit, sizeQuit, "Quit")

menu=pygame.image.load("Menu.png")
Schermo=pygame.Rect((0,0),WINDOW_SIZE)

with open("salvaBest.txt","r",encoding="utf-8") as f:
    if os.stat("salvaBest.txt").st_size == 0:
        bestScore=0
    for riga in f:
        bestScore=int(riga)

def FunzRestartTesta(Dim):
    testa=Serpente((200,350), (Dim),False,True)
    return testa

def FunzRestartCorpo(Dim):
    corpo=[Serpente((150,350),(Dim))]
    corpo[0].indicazioni.push(3)
    corpo[0].indicazioniUltimo.push(3)

    corpo.append(Serpente((100,350),(Dim)))
    corpo[1].indicazioni.push(3)
    corpo[1].indicazioni.push(3)
    corpo[1].indicazioniUltimo.push(3)
    corpo[1].indicazioniUltimo.push(3)

    corpo.append(Serpente((50,350),(Dim),True))
    corpo[2].indicazioni.push(3)
    corpo[2].indicazioni.push(3)
    corpo[2].indicazioni.push(3)
    corpo[2].indicazioniUltimo.push(3)
    corpo[2].indicazioniUltimo.push(3)
    corpo[2].indicazioniUltimo.push(3)

    return corpo

def collisioneBordi(testa,campo):
    if testa.pos in campo.Killer:
        return True
    else:
        return False

def collisioneCorpo(testa,corpo):
    for pezzo in corpo:
        if pezzo.pos==testa.pos:
            return True
    return False

def collisioneMela(testa,mela):
    if mela.pos == testa.pos:
        return True
    else:
        return False

def disegnaMela(mela,pos):
    mela.draw(screen,pos,(50,50))

def SpawnaMela(campo,testa,corpo):
    NoBene=[]
    while True:
        esci=1
        posXEstr=random.randint(1,18)*50
        posYEstr=random.randint(1,13)*50
        CoordEstr=(posXEstr,posYEstr)
        if CoordEstr in NoBene:
            esci=0
        elif testa.pos==(CoordEstr):
            NoBene.append(CoordEstr)
            esci=0
        elif CoordEstr in campo.Killer:
            NoBene.append(CoordEstr)
            esci=0
        else:
            
            for pezzo in corpo:
                if pezzo.pos==CoordEstr:
                    esci=0
                    NoBene.append(CoordEstr)
        if esci==1:
            break
        
    return CoordEstr

def Allunga(corpo):
    for pezzo in corpo:
        if pezzo.ultimo==True:
            corpo.append(Serpente(pezzo.ultimaPosizione,(50,50),True))
            corpo[-1].indicazioni.push(pezzo.ultimaIndicazione)
            corpo[-1].indicazioniUltimo.push(pezzo.ultimaIndicazione)
            while not pezzo.indicazioniUltimo.empty():
                corpo[-1].indicazioni.push(pezzo.indicazioniUltimo.front())
                corpo[-1].indicazioniUltimo.push(pezzo.indicazioniUltimo.front())
                pezzo.indicazioniUltimo.pop()
            pezzo.ultimo=False
            break

def disegnaTutto(screen,mela,posMela,posPunti,sizePunti,nPunti,bestScore):
    campo.draw(screen)
    disegnaMela(mela,posMela)
    punti.draw(1,str(nPunti))
    best.draw(1,str(bestScore))

def aggiornaBest(NewBest):
    with open("salvaBest.txt","w",encoding="utf-8") as f:
        f.write(str(NewBest))




fase=3
while True:
    
    if fase==3:
        screen.blit(menu,Schermo)
        Start.draw(0,"",1)
        ResetBest.draw(0,"",1)
        QuitButton.draw(0,"",1)
        pos = pygame.mouse.get_pos()
        if Start.rect.collidepoint(pos):
            Start.draw()
        if ResetBest.rect.collidepoint(pos):
            ResetBest.draw()
        if QuitButton.rect.collidepoint(pos):
            QuitButton.draw()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if Start.rect.collidepoint(pos):
                    fase=1
                    testa=FunzRestartTesta(Dim)
                    corpo=FunzRestartCorpo(Dim)
                    posMela=((650,350))
                    mela = Mela(posMela,Dim)
                    nPunti=0
                    direz=3
                    mangia=0
                
                if ResetBest.rect.collidepoint(pos):
                    aggiornaBest(0)
                    bestScore=0
                
                if QuitButton.rect.collidepoint(pos):
                    pygame.quit()
                    sys.exit()
                
            if event.type == KEYDOWN:
                if event.key==pygame.K_s:
                    fase=1
                    testa=FunzRestartTesta(Dim)
                    corpo=FunzRestartCorpo(Dim)
                    posMela=((650,350))
                    mela = Mela(posMela,Dim)
                    nPunti=0
                    direz=3
                    mangia=0

        

    if fase==1:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if event.key== pygame.K_UP or event.key==pygame.K_w and direz!=1:
                    direz=0
                    
                if event.key==pygame.K_DOWN or event.key==pygame.K_s and direz!=0:
                    direz=1
                    
                if event.key==pygame.K_LEFT or event.key==pygame.K_a and direz!=3:
                    direz=2
                    
                if event.key==pygame.K_RIGHT or event.key==pygame.K_d and direz!=2:
                    direz=3
                
                if event.key==pygame.K_ESCAPE:
                    fase=3

                if event.key==pygame.K_r:
                    testa=FunzRestartTesta(Dim)
                    corpo=FunzRestartCorpo(Dim)
                    posMela=((650,350))
                    mela = Mela(posMela,Dim)
                    direz=3
                    mangia=0
                    nPunti=0
                    fase=1
                    
        if direz==0:
            disegnaTutto(screen,mela,posMela,posPunti,sizePunti,nPunti,bestScore)
            
            for pezzo in corpo:
                pezzo.muoviC(Dim,direz,screen)
            testa.muoviT(Dim, direz,screen)

        if direz==1:
            disegnaTutto(screen,mela,posMela,posPunti,sizePunti,nPunti,bestScore)
            
            for pezzo in corpo:
                pezzo.muoviC(Dim,direz,screen)
            testa.muoviT(Dim, direz, screen)

        if direz==2:
            disegnaTutto(screen,mela,posMela,posPunti,sizePunti,nPunti,bestScore)
        
            for pezzo in corpo:
                pezzo.muoviC(Dim,direz,screen)
            testa.muoviT(Dim, direz, screen)

        if direz==3:
            disegnaTutto(screen,mela,posMela,posPunti,sizePunti,nPunti,bestScore)
            
            for pezzo in corpo:
                pezzo.muoviC(Dim,direz,screen)
            testa.muoviT(Dim, direz, screen)
        
        if collisioneBordi(testa, campo):
            fase=2
        if collisioneCorpo(testa, corpo):
            fase=2
        if collisioneMela(testa,mela):
            mangia=1
        
        if mangia==1:
            posMela=SpawnaMela(campo, testa, corpo)
            mela.pos=posMela
            mangia=0
            nPunti+=1
            Allunga(corpo)
        
    if fase==2:
        restart.draw(1)
        if nPunti>bestScore:
            aggiornaBest(nPunti)
            bestScore=nPunti
        nPunti=0
        pos = pygame.mouse.get_pos()
        if restart.rect.collidepoint(pos):
            restart.draw(1,"",1)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN and event.button ==1:
                pos = pygame.mouse.get_pos()

                if restart.rect.collidepoint(pos):
                    testa=FunzRestartTesta(Dim)
                    corpo=FunzRestartCorpo(Dim)
                    posMela=((650,350))
                    mela = Mela(posMela,Dim)
                    direz=3
                    mangia=0
                    fase=1
            
            if event.type == KEYDOWN:
                if event.key==pygame.K_r:
                    testa=FunzRestartTesta(Dim)
                    corpo=FunzRestartCorpo(Dim)
                    posMela=((650,350))
                    mela = Mela(posMela,Dim)
                    direz=3
                    mangia=0
                    nPunti=0
                    fase=1
                if event.key==pygame.K_ESCAPE:
                    fase=3

    pygame.display.update()
    clock.tick(fps)