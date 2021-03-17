import os
import sys
import pygame
from pygame import mixer
from pygame import font
import random
pygame.init()
try:
    pygame.mixer.init()
except Exception:
    pass
#SCREEN
FPS=45
SW=1120
SH=630
SC=pygame.display.set_mode((SW, SH))
pygame.display.set_caption("Rocketman")
BACK= pygame.image.load('assets/back3.jpg')
BACK= pygame.transform.scale(BACK,(SW,SH))
PLAYER= pygame.image.load('assets/char.png')
PLAYER_RED= pygame.image.load('assets/charR2.png')
PLAYER_BLUE= pygame.image.load('assets/charB2.png')
WHITE= (255,255,255)
BLACK= (0,0,0)
RED= (255,0,0)
BLUE= (0,0,255)
GREEN= (0,255,0)
GREY=(170, 169, 173)
ORANGE=(255,165,0)

FONT=pygame.font.SysFont('broadway', 50)
WALL=pygame.Rect(SW/2+5, 0, 10, SH)

#Ball
BD= 30 
BALL= pygame.transform.scale(pygame.image.load("assets/ball.png"), (BD, BD))
BX=WALL.x-10
BY=SH/2

#Player
PH=105
PW=105
P1=pygame.transform.scale(PLAYER_RED, (PW, PH))
P2=pygame.transform.scale(pygame.transform.flip(PLAYER_BLUE, True, False), (PW, PH))
PV=10

def welcomeScreen():
    text=FONT.render("<Press spacebar to start>", 1, WHITE)
    clock=pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif(event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE):
                return
            else:
                SC.blit(BACK,(0,0))
                SC.blit(PLAYER, (50, SH/2-50))
                SC.blit(pygame.transform.flip(PLAYER, True, False), (800, SH/2-50))
                SC.blit(text, (225,50))
            pygame.display.update()
            clock.tick(FPS)

def draw_screen(pl,pr,bo):
    SC.blit(BACK,(0,0))
    pygame.draw.rect(SC, ORANGE, WALL)
    SC.blit(P1, (pl.x, pl.y))
    SC.blit(P2, (pr.x, pr.y))
    SC.blit(BALL, (bo.x,bo.y))
    pygame.display.update()
        
def game():
    clock=pygame.time.Clock()
    pl=pygame.Rect(100, SH/2-PH/2, PW, PH)
    pr=pygame.Rect(SW-100-PW, SH/2-PH/2, PW, PH)
    bo=pygame.Rect(BX, BY, BD, BD)
    
    bvx=5
    bvy=0
    
    run= True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type==pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE):
                run=False
        
        press=pygame.key.get_pressed()
        
        if press[pygame.K_UP] and (pr.y>0):
            pr.y-=PV
        if press[pygame.K_DOWN] and (pr.y+PH<SH):
            pr.y+=PV
        if press[pygame.K_LEFT] and (pr.x>WALL.x+10):
            pr.x-=PV
        if press[pygame.K_RIGHT] and (pr.x+PW-30<SW):
            pr.x+=PV
        
        if press[pygame.K_w] and (pl.y>0):
            pl.y-=PV
        if press[pygame.K_s] and (pl.y+PH<SH):
            pl.y+=PV
        if press[pygame.K_a] and (pl.x+30>0):
            pl.x-=PV
        if press[pygame.K_d]and (pl.x+PW+5<WALL.x):
            pl.x+=PV         
        
        draw_screen(pl, pr, bo)
        

if __name__=="__main__":
    welcomeScreen()
    game()