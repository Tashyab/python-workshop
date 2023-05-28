import os
import sys
import time
import pygame
from pygame import mixer
from pygame import font
import random
pygame.init()
try:
    pygame.mixer.init()
    soundcheck = 1
except Exception:
    soundcheck = 0

# SCREEN
FPS = 60
SW = 1120
SH = 630
SC = pygame.display.set_mode((SW, SH))
pygame.display.set_caption("Rocketman")
BACK = pygame.image.load('assets/back3.jpg')
BACK = pygame.transform.scale(BACK, (SW, SH))
PLAYER = pygame.image.load('assets/char.png')
PLAYER_RED = pygame.image.load('assets/charR2.png')
PLAYER_BLUE = pygame.image.load('assets/charB2.png')
HIT_SOUND = pygame.mixer.Sound('assets/hit.wav')
POINT_SOUND = pygame.mixer.Sound('assets/point.wav')

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
GREY = (170, 169, 173)
ORANGE = (255, 165, 0)

FONT = pygame.font.SysFont('broadway', 50)
FONT_LARGE = pygame.font.SysFont('broadway', 100)
WALL = pygame.Rect(SW/2+5, 0, 10, SH)
UPWALL = pygame.Rect(0, 0, SW, 10)
DOWNWALL = pygame.Rect(0, SH-10, SW, 10)

# Ball
BD = 30
BALL = pygame.transform.scale(pygame.image.load("assets/ball.png"), (BD, BD))
BX = WALL.x-10
BY = SH/2
BV = 6

# Player
PH = 105
PW = 105
P1 = pygame.transform.scale(PLAYER_RED, (PW, PH))
P2 = pygame.transform.scale(pygame.transform.flip(PLAYER_BLUE, True, False), (PW, PH))
PV = 8


class Ball:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.rad = radius
        self.x_vel = BV
        self.y_vel = 0

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel

    def reset(self):
        self.x = BX
        self.y = BY
        self.x_vel *= -1
        self.y_vel = 0

def handle_collision(pl, pr, bo):
    if (bo.y + BD >= SH - 10 or bo.y - bo.rad <= 0):
        bo.y_vel *= -1
    
    if bo.x_vel < 0:
        if bo.y + bo.rad >=pl.y and bo.y + bo.rad <= pl.y + PH:
            if (bo.x - bo.rad + 15 <= pl.x + PW and bo.x - bo.rad + 15 >= pl.x + PW*0.9): # offset = 15
                bo.x_vel *= -1

                midy = pl.y + PH/2
                diffy = bo.y - midy
                red_fact = (PH/2)/BV
                bo.y_vel = diffy/red_fact
                if(soundcheck == 1):
                        HIT_SOUND.play()

    else:
        if bo.y +bo.rad >= pr.y and bo.y + bo.rad <= pr.y + PH:
            if (bo.x + bo.rad + 15 >= pr.x and bo.x + bo.rad + 15 <= pr.x + PW*0.1):
                bo.x_vel *= -1

                midy = pr.y + PH/2
                diffy = bo.y - midy
                red_fact = (PH/2)/BV
                bo.y_vel = diffy/red_fact
                if(soundcheck == 1):
                        HIT_SOUND.play()

def welcomeScreen():
    text = FONT.render("<Press spacebar to start>", 1, WHITE)
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif(event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
                return
            else:
                SC.blit(BACK, (0, 0))
                SC.blit(PLAYER, (50, SH/2-50))
                SC.blit(pygame.transform.flip(
                    PLAYER, True, False), (800, SH/2-50))
                SC.blit(text, (225, 50))
            pygame.display.update()
            clock.tick(FPS)


def score_update(plsc, prsc):
    plsc_text = FONT.render(f"{plsc}", 1, WHITE)
    prsc_text = FONT.render(f"{prsc}", 1, WHITE)
    SC.blit(plsc_text, (SW//4 - plsc_text.get_width()//2, 20))
    SC.blit(prsc_text, (SW-(SW//4 - prsc_text.get_width()//2), 20))

def draw_screen(pl, pr, bo, plsc, prsc ):
    SC.blit(BACK, (0, 0))
    score_update(plsc, prsc)
    pygame.draw.rect(SC, ORANGE, WALL)
    pygame.draw.rect(SC, ORANGE, UPWALL)
    pygame.draw.rect(SC, ORANGE, DOWNWALL)
    SC.blit(P1, (pl.x, pl.y))
    SC.blit(P2, (pr.x, pr.y))
    SC.blit(BALL, (bo.x, bo.y))
    pygame.display.update()

def game():
    clock = pygame.time.Clock()
    pl = pygame.Rect(100, SH/2-PH/2, PW, PH)
    pr = pygame.Rect(SW-100-PW, SH/2-PH/2, PW, PH)
    bo = Ball(BX, BY, BD//2)
    plsc = 0
    prsc = 0
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                run = False

        press = pygame.key.get_pressed()

        if press[pygame.K_w] and (pl.y > 10):
            pl.y -= PV
        if press[pygame.K_s] and (pl.y+PH < SH-10):
            pl.y += PV
        if press[pygame.K_a] and (pl.x+30 > 0):
            pl.x -= PV
        if press[pygame.K_d] and (pl.x+PW+5 < WALL.x):
            pl.x += PV

        if press[pygame.K_UP] and (pr.y > 10):
            pr.y -= PV
        if press[pygame.K_DOWN] and (pr.y+PH < SH-10):
            pr.y += PV
        if press[pygame.K_LEFT] and (pr.x > WALL.x+10):
            pr.x -= PV
        if press[pygame.K_RIGHT] and (pr.x+PW-30 < SW):
            pr.x += PV

        if(bo.x > SW): 
            plsc += 1
            if(soundcheck == 1):
                POINT_SOUND.play()
            bo.reset()         
        if(bo.x < 0): 
            prsc += 1
            if(soundcheck == 1):
                POINT_SOUND.play()
            bo.reset()
        
        win = False
        winscore = 3
        if(plsc >= winscore):
            win = True
            win_color = RED
            win_text = "Team Red Wins"
        
        if(prsc >= winscore):
            win = True
            win_color = BLUE
            win_text = "Team Blue Wins"
            
        if(win==True):
            score_update(plsc, prsc)
            pygame.display.update()
            time.sleep(0.5)
            ti = time.time()
            count = 0
            while(time.time() - ti <= 5):
                count += 1
                if(count % 2 == 0):
                    col = win_color
                else:
                    col = WHITE
                win_text_rend = FONT_LARGE.render(f"{win_text}", 1, col)
                SC.blit(win_text_rend, (SW//2 - win_text_rend.get_width()//2, SH//2))
                pygame.display.update()

            count = 0
            pl.x = 100
            pl.y = SH/2-PH/2
            pr.x = SW-100-PW
            pr.y = SH/2-PH/2
            prsc = 0
            plsc = 0
            bo.reset()

        bo.move()
        handle_collision(pl, pr, bo)
        draw_screen(pl, pr, bo, plsc, prsc)


if __name__ == "__main__":
    welcomeScreen()
    game()
