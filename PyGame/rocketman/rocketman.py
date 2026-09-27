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
GAME_SURFACE = pygame.Surface((SW, SH))
SC = pygame.display.set_mode((SW, SH), pygame.RESIZABLE)
pygame.display.set_caption("Rocketman")
fullscreen = False

def update_display():
    window_width, window_height = pygame.display.get_window_size()

    scale = min(window_width / SW, window_height / SH)

    scaled_width = max(1, int(SW * scale))
    scaled_height = max(1, int(SH * scale))

    scaled_surface = pygame.transform.smoothscale(
        GAME_SURFACE,
        (scaled_width, scaled_height)
    )

    SC.fill(BLACK)

    x = (window_width - scaled_width) // 2
    y = (window_height - scaled_height) // 2

    SC.blit(scaled_surface, (x, y))
    pygame.display.flip()

def toggle_fullscreen():
    global SC, fullscreen

    fullscreen = not fullscreen

    if fullscreen:
        SC = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    else:
        SC = pygame.display.set_mode((SW, SH), pygame.RESIZABLE)

ROOT = 'D:/Projects/python-workshop/PyGame/rocketman/assets/'
BACK = pygame.image.load(f'{ROOT}back3.jpg')
BACK = pygame.transform.scale(BACK, (SW, SH))
PLAYER = pygame.image.load(f'{ROOT}char.png')
PLAYER_RED = pygame.image.load(f'{ROOT}charR2.png')
PLAYER_BLUE = pygame.image.load(f'{ROOT}charB2.png')
HIT_SOUND = pygame.mixer.Sound(f'{ROOT}hit.wav')
POINT_SOUND = pygame.mixer.Sound(f'{ROOT}point.wav')
WIN_SOUND = pygame.mixer.Sound(f'{ROOT}sci-fi.wav')

pygame.mixer.music.load(f'{ROOT}welcome.mp3')

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

# MIDWALL = pygame.transform.scale(pygame.image.load(f"{ROOT}wall.png"), (10, SH))
# BOUNDARY = pygame.transform.scale(pygame.transform.rotate(pygame.image.load(f"{ROOT}wall.png"), 90), (SW, 10))

# Ball
BD = 30
BALL = pygame.transform.scale(pygame.image.load(f'{ROOT}ball.png'), (BD, BD))
BX = 555
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

    def reset(self, wy):
        self.x = BX
        self.y = wy
        self.x_vel *= -1
        self.y_vel = 0

def handle_collision(pl, pr, bo):
    cpu_target_y = None

    if (bo.y + BD >= SH - 10 or bo.y - bo.rad <= 0):
        bo.y_vel *= -1
    
    if bo.x_vel < 0:
        if bo.y + bo.rad >= pl.y and bo.y + bo.rad <= pl.y + PH:
            if (bo.x - bo.rad + 15 <= pl.x + PW and bo.x - bo.rad + 15 >= pl.x + PW * 0.9):
                bo.x_vel *= -1

                midy = pl.y + PH / 2
                diffy = bo.y - midy
                red_fact = (PH / 2) / BV
                bo.y_vel = diffy / red_fact

                cpu_target_y = predict_cpu_target(bo)

                if soundcheck == 1:
                    HIT_SOUND.play()

    else:
        if bo.y + bo.rad >= pr.y and bo.y + bo.rad <= pr.y + PH:
            if (bo.x + bo.rad + 15 >= pr.x and bo.x + bo.rad + 15 <= pr.x + PW * 0.1):
                bo.x_vel *= -1

                midy = pr.y + PH / 2
                diffy = bo.y - midy
                red_fact = (PH / 2) / BV
                bo.y_vel = diffy / red_fact

                if soundcheck == 1:
                    HIT_SOUND.play()

    return cpu_target_y

def welcomeScreen():
    if(not pygame.mixer.music.get_busy()):
        pygame.mixer.music.play()
    text1 = FONT.render("Press <SPACE>  Player vs Player", 1, WHITE)
    text2 = FONT.render("Press <CTRL + SPACE>  Player vs CPU", 1, WHITE)
    clock = pygame.time.Clock()
    blink_interval = 400
    last_blink_time = 0
    is_text_visible = True

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_F11:
                    toggle_fullscreen()
                elif event.key == pygame.K_RETURN and pygame.key.get_mods() & pygame.KMOD_ALT:
                    toggle_fullscreen()
                elif event.key == pygame.K_SPACE:
                    if pygame.key.get_mods() & pygame.KMOD_CTRL:
                        return True
                    return False

        # Blinking logic
        current_time = pygame.time.get_ticks()
        if current_time - last_blink_time >= blink_interval:
            last_blink_time = current_time
            is_text_visible = not is_text_visible

        GAME_SURFACE.blit(BACK, (0, 0))
        GAME_SURFACE.blit(PLAYER_RED, (50, SH/2-50))
        GAME_SURFACE.blit(pygame.transform.flip(PLAYER_BLUE, True, False), (800, SH/2-50))

        # Blinking
        if is_text_visible:
            GAME_SURFACE.blit(text1, (SW//2 - text1.get_width()//2, 50))
            GAME_SURFACE.blit(text2, (SW//2 - text2.get_width()//2, 110))
            GAME_SURFACE.blit(PLAYER_BLUE, (50, SH/2-50))
            GAME_SURFACE.blit(pygame.transform.flip(PLAYER_RED, True, False), (800, SH/2-50))

        update_display()
        clock.tick(FPS)

def score_update(plsc, prsc):
    plsc_text = FONT.render(f"{plsc}", 1, WHITE)
    prsc_text = FONT.render(f"{prsc}", 1, WHITE)
    GAME_SURFACE.blit(plsc_text, (SW//4 - plsc_text.get_width()//2, 20))
    GAME_SURFACE.blit(prsc_text, (SW-(SW//4 - prsc_text.get_width()//2), 20))

def draw_screen(pl, pr, bo, plsc, prsc ):
    GAME_SURFACE.blit(BACK, (0, 0))
    score_update(plsc, prsc)
    pygame.draw.rect(GAME_SURFACE, (244,140,6), WALL)
    pygame.draw.rect(GAME_SURFACE, (244,140,6), UPWALL)
    pygame.draw.rect(GAME_SURFACE, (244,140,6), DOWNWALL)
    GAME_SURFACE.blit(P1, (pl.x, pl.y))
    GAME_SURFACE.blit(P2, (pr.x, pr.y))
    GAME_SURFACE.blit(BALL, (bo.x, bo.y))
    update_display()

def predict_cpu_target(bo):
    target_x = SW - 100 - PW
    distance = target_x - bo.x

    if bo.x_vel > 0 and distance > 0:
        time_to_reach = distance / bo.x_vel
        predicted_y = bo.y + bo.y_vel * time_to_reach

        height = SH - BD
        predicted_y %= height * 2

        if predicted_y > height:
            predicted_y = height * 2 - predicted_y

        return predicted_y

    return SH / 2

def cpu_move(pr, cpu_target_y, cpu_target_x):
    cpu_speed = 5
    dead_zone = 20

    if pr.centerx < cpu_target_x - 10:
        pr.x += cpu_speed
    elif pr.centerx > cpu_target_x + 10:
        pr.x -= cpu_speed

    if pr.centery < cpu_target_y - dead_zone:
        pr.y += cpu_speed
    elif pr.centery > cpu_target_y + dead_zone:
        pr.y -= cpu_speed

    pr.x = max(WALL.x + 10, min(pr.x, SW - PW - 30))
    pr.y = max(10, min(pr.y, SH - PH - 10))

def game(cpu=False):
    pygame.mixer.music.rewind()
    clock = pygame.time.Clock()
    pl = pygame.Rect(100, SH/2-PH/2, PW, PH)
    pr = pygame.Rect(SW-100-PW, SH/2-PH/2, PW, PH)
    bo = Ball(BX, BY, BD//2)
    plsc = 0
    prsc = 0
    cpu_target_y = SH / 2
    cpu_target_x = SW - 100 - PW
    run = True
    while run:
        if(not pygame.mixer.music.get_busy()):
            pygame.mixer.music.play()
        clock.tick(FPS)

        if cpu and random.randint(1, 45) == 1:
            cpu_target_x = random.randint(SW - 100 - PW - 100, SW - 100 - PW + 60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                elif event.key == pygame.K_F11:
                    toggle_fullscreen()
                elif event.key == pygame.K_RETURN and pygame.key.get_mods() & pygame.KMOD_ALT:
                    toggle_fullscreen()

        press = pygame.key.get_pressed()

        if press[pygame.K_w] and (pl.y > 10):
            pl.y -= PV
        if press[pygame.K_s] and (pl.y+PH < SH-10):
            pl.y += PV
        if press[pygame.K_a] and (pl.x+30 > 0):
            pl.x -= PV
        if press[pygame.K_d] and (pl.x+PW+5 < WALL.x):
            pl.x += PV

        if cpu:
            cpu_move(pr, cpu_target_y, cpu_target_x)
        else:
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
            bo.reset(pl.y + PH / 2 - BD / 2)

        if(bo.x < -80): 
            prsc += 1
            if(soundcheck == 1):
                POINT_SOUND.play()
            bo.reset(pr.y + PH / 2 - BD / 2)
        
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
            update_display()
            pygame.time.delay(500)
            ti = time.time()
            count = 0
            while(time.time() - ti <= 5):
                count += 1
                if(count % 2 == 0):
                    col = win_color
                else:
                    col = WHITE
                win_text_rend = FONT_LARGE.render(f"{win_text}", 1, col)
                GAME_SURFACE.blit(win_text_rend, (SW//2 - win_text_rend.get_width()//2, SH//2))
                if soundcheck == 1:
                    WIN_SOUND.play()
                update_display()
            return

        bo.move()
        new_target = handle_collision(pl, pr, bo)

        if new_target is not None:
            cpu_target_y = new_target
        draw_screen(pl, pr, bo, plsc, prsc)


if __name__ == "__main__":
    pygame.mixer.music.play()
    while(True):
        cpu = welcomeScreen()
        game(cpu)