import sys
import pygame
from pygame.locals import *
import random
import pyttsx3
try:
    pygame.mixer.init()
    soundcheck=1
except Exception:
    soundcheck=0
pygame.font.init()

engine=pyttsx3.init('sapi5')
voice=engine.getProperty('voices')
engine.setProperty('voice',voice[0].id)
engine.setProperty('rate',160)
engine.setProperty('volume', 1.0)
FPS=38
SC_H=630
SC_W=1120
SC=pygame.display.set_mode((SC_W,SC_H))
GROUNDY=SC_H*0.8
GAME_SPRITES={}
GAME_SOUNDS={}
PLAYER="equip/sprites/jet_char.png"
OBSTACLE="equip/sprites/pilliar.png"
BASE = 'equip/sprites/lava.png'
BACK="equip/sprites/well3.png"
FONT=pygame.font.SysFont('Algerian', 20)
FONT2 = pygame.font.SysFont('Algerian', 60)
FONT3 = pygame.font.SysFont('Algerian', 25)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
pygame.mixer.music.load("equip/sounds/muse.mp3")

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def welcomeScreen(hslist):
    blink_interval = 400
    last_blink_time = 0
    is_text_visible = True
    scores1 = FONT3.render(f"1. {hslist[0][0]}:   {hslist[0][1]}                2. {hslist[1][0]}:   {hslist[1][1]}                3. {hslist[2][0]}:   {hslist[2][1]}",
                           True, RED)
    scores2 = FONT3.render(f"1. {hslist[0][0]}:   {hslist[0][1]}                2. {hslist[1][0]}:   {hslist[1][1]}                3. {hslist[2][0]}:   {hslist[2][1]}",
                           True, BLUE)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                return
        
        if(not pygame.mixer.music.get_busy()): 
            pygame.mixer.music.play()
        current_time = pygame.time.get_ticks()
        if current_time - last_blink_time >= blink_interval:
            last_blink_time = current_time
            is_text_visible = not is_text_visible

        SC.blit(GAME_SPRITES['message'], (0, 0))
        SC.blit(scores2, ((SC_W-scores2.get_width())//2, 45))

        text_surface = FONT2.render("<Press spacebar to start>", True, WHITE)
        text_rect = text_surface.get_rect(center=(SC_W // 2, SC_H // 2)) 
        if is_text_visible:
            SC.blit(text_surface, text_rect)
            SC.blit(scores1, ((SC_W-scores1.get_width())//2, 45))

        pygame.display.update()
        fpsclock.tick(FPS)

def mainGame(hs, hslist):
    pygame.mixer.music.rewind()

    score=0
    playerx=int(SC_W/4)
    playery=int(SC_H/2)
    basex=0

    newpipe1=getRandomPipe()
    newpipe2=getRandomPipe()

    upperpipes= [
        {'x':SC_W+100,'y':newpipe1[0]['y']},
        {'x':SC_W+100+(SC_W/2),'y':newpipe2[0]['y']}
    ]
    lowerpipes= [
        {'x':SC_W+100,'y':newpipe1[1]['y']}, 
        {'x':SC_W+100+(SC_W/2),'y':newpipe2[1]['y']}
    ]
    pipevelx= -5
    playervely= -9
    playermaxvely=10
    playerminvely= -8
    playeraccy=1

    playerflapvel= -14
    playerflapped=False

    bgx = 0

    while(True):
        for event in pygame.event.get():
            if event.type == QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and (event.key==K_SPACE or event.key==K_UP):
                if playery>0:
                    playervely= playerflapvel
                    playerflapped= True
                    try:
                        GAME_SOUNDS['swoosh'].play()
                    except Exception:
                        pass
        
        if(not pygame.mixer.music.get_busy()): 
            pygame.mixer.music.play()
        crashTest=Collide(playerx, playery, upperpipes, lowerpipes, score, hslist)
        if crashTest:
            return True

        playermidpos= playerx + GAME_SPRITES['player'].get_width()/2
        for pipe in upperpipes:
            pipemidpos=pipe['x'] + GAME_SPRITES['obstacle'][0].get_width()/2
            if pipemidpos <= playermidpos < pipemidpos+4:
                score+=1
                try:
                    GAME_SOUNDS['score'].play()
                except Exception:
                    pass
        
        if playervely < playermaxvely and not playerflapped:
            playervely+= playeraccy
        
        if playerflapped:
            playerflapped=False
        
        playerh= GAME_SPRITES['player'].get_height()
        playery = playery + playervely

        for upperpipe, lowerpipe in zip(upperpipes,lowerpipes):
            upperpipe['x']+= pipevelx
            lowerpipe['x']+= pipevelx

        if 0<upperpipes[0]['x'] <10:
            newpipe=getRandomPipe()
            upperpipes.append(newpipe[0])
            lowerpipes.append(newpipe[1])

        if upperpipes[0]['x'] + GAME_SPRITES['obstacle'][0].get_width() + 10 < 0 :
            upperpipes.pop(0)
            lowerpipes.pop(0)
    
        bgx -= 2
        if bgx < -GAME_SPRITES['background'][0].get_width():
            bgx = 0
        screen(hs, score, bgx)
        
        for upperpipe,lowerpipe in zip(upperpipes,lowerpipes):
            SC.blit(GAME_SPRITES['obstacle'][0], (upperpipe['x'], upperpipe['y']))
            SC.blit(GAME_SPRITES['obstacle'][1], (lowerpipe['x'], lowerpipe['y']))
        
        SC.blit(GAME_SPRITES['base'], (basex-60,GROUNDY-50))
        SC.blit(GAME_SPRITES['player'], (playerx,playery))
        
        mydigits= [int(x) for x in list(str(score))]
        width = 0
        for digit in mydigits: 
            width+=GAME_SPRITES['numbers'][digit].get_width()
        xoffset=SC_W-300
        for digit in mydigits:
            SC.blit(GAME_SPRITES['numbers'][digit],(xoffset, 20))
            xoffset+=GAME_SPRITES['numbers'][digit].get_width() - 20
        
        pygame.display.update()
        fpsclock.tick(FPS)

def screen(hs, score, bgx):
    if score>hs:
        sc = score
    else:
        sc = hs

    SC.blit(GAME_SPRITES['background'][0], (bgx, 0))
    SC.blit(GAME_SPRITES['background'][0], (bgx + GAME_SPRITES['background'][0].get_width(), 0))
    text=FONT.render(f"High Score: {sc}", 1, BLACK)
    SC.blit(text,(20,20))
        
def player():
    # Set up input box
    input_box = pygame.Rect(SC_W//2-135, SC_H//2-100, 200, 40)
    color_inactive = (255, 255, 0)
    color_active = GREEN
    color = color_inactive
    text = ''
    font = pygame.font.SysFont("Georgia", 24)
    text_surface = font.render(text, True, BLACK, WHITE)
    width = max(200, text_surface.get_width()+10)

    active = False
    input_box.w = width

    clock = pygame.time.Clock()
    is_flashing_text = True
    blank_interval = 400
    last_blink_time = 0

    pl = pygame.image.load('equip/sprites/jetpack.png')
    pl = pygame.transform.scale(pl, (pl.get_width()//10, pl.get_height()//10))
    pl_rect = pl.get_rect()
    pl_rect.x = -pl.get_width()//2
    pl_rect.y = SC_H-100

    while True:
        if(not pygame.mixer.music.get_busy()): 
            pygame.mixer.music.play()
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        return text
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    elif(len(text)<=20 and event.unicode != ' '):
                        text += event.unicode
                    width = max(200, font.size(text)[0]+10)
                    input_box.w = width
                    text_surface = font.render(text, True, BLACK, WHITE)

        current_time = pygame.time.get_ticks()
        if(current_time-last_blink_time >= blank_interval):
            last_blink_time = current_time
            is_flashing_text = not is_flashing_text
            pl_rect.x+=100
            pl_rect.y-=100
                
        congrats1 = FONT3.render("CONGRATULATIONS! Enter Your Name.", True, RED)
        congrats2 = FONT3.render("CONGRATULATIONS! Enter Your Name.", True, BLUE)
        
        SC.blit(GAME_SPRITES['message'], (0, 0))
        SC.blit(congrats2, (SC_W//2-congrats1.get_width()//2, 120))
        if(pl_rect.x>SC_W):
            pl_rect.x = -pl.get_width()//2
        if(pl_rect.y<0):
            pl_rect.y = SC_H-random.choice([i for i in range(0, SC_H, 10)])
    
        SC.blit(pl, (pl_rect.x, pl_rect.y))

        if is_flashing_text:
            SC.blit(congrats1, (SC_W//2-congrats1.get_width()//2, 120))

        pygame.draw.rect(SC, color, input_box, 2)
        pygame.draw.rect(SC, WHITE, (input_box.x + 3, input_box.y + 3, width - 6, 36))
        SC.blit(text_surface, (input_box.x+7, input_box.y+7))
        input_box.w = max(200, text_surface.get_width()+10)
        pygame.display.flip()
        clock.tick(30)

def highScore(score, hslist):
    if score > hslist[0][1]:
        hslist[0][1] = score
        hslist[0][0] = player()
    elif score > hslist[1][1]:
        hslist[1][1] = score
        hslist[1][0] = player()
    elif score > hslist[2][1]:
        hslist[2][1] = score
        hslist[2][0] = player()
    with open("HS.txt", "w") as f:
        f.write(f"{hslist[0][0]} {hslist[0][1]}\n{hslist[1][0]} {hslist[1][1]}\n{hslist[2][0]} {hslist[2][1]}")

def Collide(playerx, playery, upperpipes, lowerpipes, score, hslist):
    playerh=GAME_SPRITES['player'].get_height()
    pipeh=GAME_SPRITES['obstacle'][0].get_height()
    pipeh=GAME_SPRITES['obstacle'][0].get_height()
    if (playery > (GROUNDY - GAME_SPRITES['player'].get_height())):
        try:
            GAME_SOUNDS['crash'].play()
        except Exception:
            pass
        highScore(score, hslist)
        return True
    
    if (playery < 0):
        try:
            GAME_SOUNDS['explosion'].play()
        except Exception:
            pass
        highScore(score, hslist)
        return True
    
    for pipe in upperpipes:
        if (playery < (pipe['y']+pipeh) and abs(playerx - pipe['x']) < GAME_SPRITES['obstacle'][0].get_width()):
            try:
                GAME_SOUNDS['explosion'].play()
            except Exception:
                pass
            highScore(score, hslist)
            return True 
    for pipe in lowerpipes:
        if ((playery+pipeh > pipe['y']+GAME_SPRITES['base'].get_height()+playerh) and abs(playerx - pipe['x']) < GAME_SPRITES['obstacle'][0].get_width()):
            try:
                GAME_SOUNDS['explosion'].play()
            except Exception:
                pass
            highScore(score, hslist)
            return True

def getRandomPipe():
    pipeh= GAME_SPRITES['obstacle'][0].get_height()
    offset= SC_W/5
    y2= offset+ random.randrange(0, int(SC_H - GAME_SPRITES['base'].get_height()-offset))
    pipex= SC_W + 10
    y1= pipeh - y2 + offset
    pipe=[
        {'x':pipex, 'y':-y1},  #upper pipe
        {'x':pipex, 'y':y2}    #lower pipe 
    ]
    return pipe

if __name__=="__main__":
    pygame.init()
    fpsclock=pygame.time.Clock()
    pygame.display.set_caption("JETPACK JOYRIDE")
    pygame.mixer.music.play()
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
    ) # (62, 69)

    GAME_SPRITES['background']=(
        pygame.transform.scale(pygame.image.load('equip/sprites/well3.png'), (SC_W*1.5,SC_H*1.2)),
        pygame.transform.scale(pygame.image.load('equip/sprites/well.png'), (SC_W, SC_H)),
    )

    GAME_SPRITES['message']=GAME_SPRITES['background'][0].convert_alpha()
    GAME_SPRITES['base']=pygame.image.load(BASE).convert_alpha() # (1120, 229)
    
    GAME_SPRITES['obstacle']=(
        pygame.image.load(OBSTACLE).convert_alpha(), 
        pygame.transform.rotate(pygame.image.load(OBSTACLE).convert_alpha(), 180)
    ) # (66, 382)
    try:
        GAME_SOUNDS['swoosh']=pygame.mixer.Sound('equip/sounds/swoosh.wav')
        GAME_SOUNDS['crash']=pygame.mixer.Sound('equip/sounds/crash.wav')
        GAME_SOUNDS['score']=pygame.mixer.Sound('equip/sounds/score.wav')
        GAME_SOUNDS['explosion']=pygame.mixer.Sound('equip/sounds/explosion.wav')
    except Exception:
        pass
    
    GAME_SPRITES['player']=pygame.image.load(PLAYER).convert_alpha() # (83, 77)

    with open("HS.txt") as f:
        hsfile = f.read()
        hsfile = hsfile.split('\n')
        keys = [i.split()[0] for i in hsfile]
        values = list(map(int, [i.split()[-1] for i in hsfile]))
        hslist = [[keys[i], values[i]] for i in range(3)]
        hs = hslist[0][1]

    while(True):
        welcomeScreen(hslist)
        mainGame(hs, hslist)