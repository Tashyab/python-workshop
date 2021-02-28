import sys
import pygame
from pygame.locals import *
import random
import time
import pyttsx3
try:
    pygame.mixer.init()
except Exception:
    pass
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
PLAYER="equip/sprites/char.png"
BACK="equip/sprites/background.png"
OBSTACLE="equip/sprites/obstacle.png"
FONT=pygame.font.SysFont('impact', 30)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

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
                SC.blit(GAME_SPRITES['intch'],(playerx+220, 0))
                SC.blit(GAME_SPRITES['intgr'],(playerx+40,playery-90))
                SC.blit(GAME_SPRITES['intback'][0],(-10, GROUNDY-20))
                SC.blit(GAME_SPRITES['intback'][1],(w1-40, GROUNDY-20))
                SC.blit(GAME_SPRITES['intback'][2],(w1+w2-80, GROUNDY-20))
                SC.blit(GAME_SPRITES['intback'][3],(w1+w2+w3-140, GROUNDY-20))
                SC.blit(GAME_SPRITES['intback'][4],(w1+w2+w3+w4-180, GROUNDY-20))
                pygame.display.update()
                fpsclock.tick(FPS)

def mainGame():
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
            
        crashTest=Collide(playerx, playery, upperpipes, lowerpipes)
        if crashTest:
            print("Your score is", score)
            return True

        playermidpos= playerx + GAME_SPRITES['player'].get_width()/2
        for pipe in upperpipes:
            pipemidpos=pipe['x'] + GAME_SPRITES['obstacle'][0].get_width()/2
            if pipemidpos <= playermidpos < pipemidpos+4:
                score+=1
                try:
                    GAME_SOUNDS['point'].play()
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
        
        screen(score)
        if score==2:
            # speak("Congrats. You won. Ultron is now your servant. You get two bonus point.")
            speak("All hail Tashyab, The creator.")
            speak("Enjoy the fast wind.")
            pipevelx=-15
            score+=2
        for upperpipe,lowerpipe in zip(upperpipes,lowerpipes):
            SC.blit(GAME_SPRITES['obstacle'][0], (upperpipe['x'], upperpipe['y']))
            SC.blit(GAME_SPRITES['obstacle'][1], (lowerpipe['x'], lowerpipe['y']))
        
        SC.blit(GAME_SPRITES['base'], (basex,GROUNDY))
        
        SC.blit(GAME_SPRITES['player'], (playerx,playery))
        
        mydigits= [int(x) for x in list(str(score))]
        width = 0
        for digit in mydigits: 
            width+=GAME_SPRITES['numbers'][digit].get_width()
        xoffset=SC_W-300
        for digit in mydigits:
            SC.blit(GAME_SPRITES['numbers'][digit],(xoffset, 40))
            xoffset+=GAME_SPRITES['numbers'][digit].get_width()
        
        pygame.display.update()
        fpsclock.tick(FPS)

def screen(score):
    text=FONT.render("Reach 18 points to win", 1, (255,0,0))
    text_win=FONT.render("Congrats, You win. Enjoy.", 1, (0,0,255))
    text_hail=FONT.render("All hail Tashyab, The creator.", 1, (255,0,0))
    if 0<=score and score<3:
        SC.blit((GAME_SPRITES['background'][0]), (0,0))
        SC.blit(text,(20,20))
    elif 3<=score and score<6:
        SC.blit((GAME_SPRITES['background'][1]), (0,0))
        SC.blit(text,(20,20))
    elif 6<=score and score<9:
        SC.blit((GAME_SPRITES['background'][2]), (0,0))
        SC.blit(text,(20,20))
    elif 9<=score and score<12:
        SC.blit((GAME_SPRITES['background'][3]), (0,0))
        SC.blit(text,(20,20))
    elif 12<=score and score<15:
        SC.blit((GAME_SPRITES['background'][4]), (0,0))
        SC.blit(text,(20,20))
    elif 15<=score and score<18:
        SC.blit((GAME_SPRITES['background'][5]), (0,0))
        SC.blit(text,(20,20))
    if score>=18:
        SC.blit((GAME_SPRITES['background'][0]), (0,0))
        SC.blit(text_win,(20,20))
        SC.blit(text_hail, (20, SC_H-20))
    
def Collide(playerx, playery, upperpipes, lowerpipes):
    playerh=GAME_SPRITES['player'].get_height()
    pipeh=GAME_SPRITES['obstacle'][0].get_height()
    pipeh=GAME_SPRITES['obstacle'][0].get_height()
    if (playery > (GROUNDY - GAME_SPRITES['player'].get_height())) or (playery < 0):
        try:
            GAME_SOUNDS['hit'].play()
        except Exception:
            pass
        return True

    for pipe in upperpipes:
        if (playery < (pipe['y']+pipeh) and abs(playerx - pipe['x']) < GAME_SPRITES['obstacle'][0].get_width()):
            try:
                GAME_SOUNDS['hit'].play()
            except Exception:
                pass
            return True 
    for pipe in lowerpipes:
        if ((playery+pipeh > pipe['y']+GAME_SPRITES['base'].get_height()+playerh) and abs(playerx - pipe['x']) < GAME_SPRITES['obstacle'][0].get_width()):
            try:
                GAME_SOUNDS['hit'].play()
            except Exception:
                pass
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
    pygame.display.set_caption("JETPACK PENGUIN")
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
    try:
        GAME_SOUNDS['die']=pygame.mixer.Sound('equip/sounds/die.wav')
        GAME_SOUNDS['hit']=pygame.mixer.Sound('equip/sounds/hit.wav')
        GAME_SOUNDS['point']=pygame.mixer.Sound('equip/sounds/point.wav')
        GAME_SOUNDS['swoosh']=pygame.mixer.Sound('equip/sounds/swoosh.wav')
        GAME_SOUNDS['bell']=pygame.mixer.Sound('equip/sounds/bell.wav')
    except Exception:
        pass

    GAME_SPRITES['intgr']=pygame.image.load('equip/sprites/gr.png')
    GAME_SPRITES['intch']=pygame.image.load('equip/sprites/chint.png')
    GAME_SPRITES['intback']=(
        pygame.image.load('equip/sprites/back1.png'),
        pygame.image.load('equip/sprites/back2.png'),
        pygame.image.load('equip/sprites/back3.png'),
        pygame.image.load('equip/sprites/back4.png'),
        pygame.image.load('equip/sprites/back5.png')
    )
    
    GAME_SPRITES['background']=(
        pygame.image.load(BACK).convert(),
        pygame.transform.scale(pygame.image.load('equip/sprites/back1.png'), (SC_W,SC_H)), 
        pygame.transform.scale(pygame.image.load('equip/sprites/back2.png'), (SC_W,SC_H)),
        pygame.transform.scale(pygame.image.load('equip/sprites/back3.png'), (SC_W,SC_H)),
        pygame.transform.scale(pygame.image.load('equip/sprites/back4.png'), (SC_W,SC_H)),
        pygame.transform.scale(pygame.image.load('equip/sprites/back5.png'), (SC_W,SC_H))
        
    )
    GAME_SPRITES['player']=pygame.image.load(PLAYER).convert_alpha()

    while(True):
        welcomeScreen()
        mainGame()