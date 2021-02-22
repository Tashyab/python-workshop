import sys
import pygame
from pygame.locals import *
import random

FPS=32
SC_H=630
SC_W=1120
SC=pygame.display.set_mode((SC_W,SC_H))
GROUNDY=SC_H*0.8
GAME_SPRITES={}
GAME_SOUNDS={}
PLAYER="equip/sprites/char.png"
BACK="equip/sprites/back2.png"
OBSTACLE="equip/sprites/obstacle.png"

def welcomeScreen():
    playerx=int(SC_W/2)
    playery=int((SC_H - GAME_SPRITES['player'].get_width())/2)
    w1=GAME_SPRITES['intback'][0].get_width()
    w2=GAME_SPRITES['intback'][1].get_width()
    w3=GAME_SPRITES['intback'][2].get_width()
    w4=GAME_SPRITES['intback'][3].get_width()
    while(True):
        for event in pygame.event.get():
            if event.type == QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and (event.key==K_SPACE or event.key==K_UP):
                return
            else:
                SC.blit(GAME_SPRITES['message'],(0,0))
                SC.blit(GAME_SPRITES['intgr'],(playerx+100,playery-100))
                SC.blit(GAME_SPRITES['player'],(playerx+40, playery-100))
                SC.blit(GAME_SPRITES['intback'][0],(-10, GROUNDY-20))
                SC.blit(GAME_SPRITES['intback'][1],(w1-40, GROUNDY-20))
                SC.blit(GAME_SPRITES['intback'][2],(w1+w2-80, GROUNDY-20))
                SC.blit(GAME_SPRITES['intback'][3],(w1+w2+w3-140, GROUNDY-20))
                SC.blit(GAME_SPRITES['intback'][4],(w1+w2+w3+w4-180, GROUNDY-20))
                pygame.display.update()
                fpsclock.tick(FPS)

def mainGame():
    pass    

if __name__=="__main__":
    pygame.init()
    fpsclock=pygame.time.Clock()
    pygame.display.set_caption("Jetpack by Tashyab's ultron")
    GAME_SPRITES['numbers']=(
        pygame.image.load('equip/sprites/0.png').convert_alpha(),
        pygame.image.load('equip/sprites/1.png').convert_alpha(),
        pygame.image.load('equip/sprites/2.png').convert_alpha(),
        pygame.image.load('equip/sprites/3.png').convert_alpha(),
        pygame.image.load('equip/sprites/4.png').convert_alpha(),
        pygame.image.load('equip/sprites/5.png').convert_alpha(),
        pygame.image.load('equip/sprites/6.png').convert_alpha(),
        pygame.image.load('equip/sprites/7.png').convert_alpha(),
        pygame.image.load('equip/sprites/8.png').convert_alpha(),
        pygame.image.load('equip/sprites/9.png').convert_alpha()
    )
    GAME_SPRITES['message']=pygame.image.load('equip/sprites/welcome.png').convert_alpha()
    GAME_SPRITES['base']=pygame.image.load('equip/sprites/ground.png').convert_alpha()
    GAME_SPRITES['obstacle']=(
        pygame.image.load(OBSTACLE).convert_alpha(), 
        pygame.transform.rotate(pygame.image.load(OBSTACLE).convert_alpha(), 180)
    )
    GAME_SOUNDS['die']=pygame.mixer.Sound('equip/sounds/die.wav')
    GAME_SOUNDS['hit']=pygame.mixer.Sound('equip/sounds/hit.wav')
    GAME_SOUNDS['point']=pygame.mixer.Sound('equip/sounds/point.wav')
    GAME_SOUNDS['swoosh']=pygame.mixer.Sound('equip/sounds/swoosh.wav')
    GAME_SOUNDS['bell']=pygame.mixer.Sound('equip/sounds/bell.wav')
    GAME_SPRITES['intgr']=pygame.image.load('equip/sprites/gr.png')
    GAME_SPRITES['intback']=(
        pygame.image.load('equip/sprites/back1.png'),
        pygame.image.load('equip/sprites/back2.png'),
        pygame.image.load('equip/sprites/back3.png'),
        pygame.image.load('equip/sprites/back4.png'),
        pygame.image.load('equip/sprites/back5.png')
    )
    GAME_SPRITES['background']=pygame.image.load(BACK).convert()
    GAME_SPRITES['player']=pygame.image.load(PLAYER).convert_alpha()

    while(True):
        welcomeScreen()
        mainGame()
