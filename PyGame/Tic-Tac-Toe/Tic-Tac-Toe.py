import pygame
from pygame import font
from pygame import mixer
import sys
import time

pygame.init()
try:
    pygame.mixer.init()
    soundcheck = 1
except:
    soundcheck = 0


# SCREEN
FPS = 60
SH, SW = 340, 340
SC = pygame.display.set_mode((SW, SH))
pygame.display.set_caption("Tic-Tac-Toe")
BOX = pygame.Rect(0, 0, SW, SH)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
GREY = (170, 169, 173)
ORANGE = (255, 165, 0)


FONT = pygame.font.SysFont('broadway', 20)


def welcomescreen():
    text_white = FONT.render("<Press Spacebar to start>", 1, WHITE)
    text_black = FONT.render("<Press Spacebar to start>", 1, BLACK)
    # text_o = FONT.render(
    #     "O   O   O   O   O   O   O   O   O   O   O   O   O   O   O   O   O", 1, WHITE)
    # text_x = FONT.render(
    #     "  X   X   X   X   X   X   X   X   X   X   X   X   X   X   X   X", 1, WHITE)
    clock = pygame.time.Clock()
    flash = 0
    SC.fill(BLACK)
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif ((event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE) or (event.type == pygame.MOUSEBUTTONDOWN)):
                return
            else:
                flash += 1
                if(flash % 2 != 0):
                    SC.blit(text_white, (SW//2 - text_white.get_width() //
                                         2, SH//2-text_white.get_height()//2))
                    # SC.blit(text_o, (0, SH//5))
                    # SC.blit(text_x, (0, 4*SH//5))

                else:
                    SC.blit(text_black, (SW//2 - text_black.get_width() //
                                         2, SH//2-text_black.get_height()//2))
                    # SC.blit(text_x, (0, SH//5))
                    # SC.blit(text_o, (0, 4*SH//5))

            pygame.display.update()
            clock.tick(FPS)


def drawscreen(turn, x, y):
    SC.fill(BLACK)
    pygame.draw.rect(SC, WHITE, BOX, width=10)
    pygame.draw.line(SC, WHITE, (110, 0), (110, SH), 10)
    pygame.draw.line(SC, WHITE, (220, 0), (220, SH), 10)
    pygame.draw.line(SC, WHITE, (0, 110), (SW, 110), 10)
    pygame.draw.line(SC, WHITE, (0, 220), (SW, 220), 10)
    if turn == 1:
        pygame.draw.circle(SC, WHITE, (x, y), 40, width=10)
    if turn == -1:
        pygame.draw.line(SC, WHITE, (x-40, y-40), (x+40, y+40), width=10)
        pygame.draw.line(SC, WHITE, (x+40, y-40), (x-40, y+40), width=10)
    pygame.display.update()


def game():
    clock = pygame.time.Clock()
    run = True
    turn = -1

    while(run == True):
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                run = False

        x, y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
                turn *= -1
                print(turn)
        
        drawscreen(turn, x, y)


if __name__ == "__main__":
    welcomescreen()
    game()
