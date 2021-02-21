import time
import pygame
# pygame.init()
from pygame import mixer


def sound():
    mixer.init()
    mixer.music.load("tune.mp3")
    mixer.music.set_volume(0.5)
    mixer.music.play()
    input("Press enter key to stop.")
    mixer.music.stop()

t=float(input("Enter time in minutes:"))
print(f"Remind you in {t} minutes")
t=t*60
ti=time.time()
while (True):
    tk=time.time()
    if tk-ti>=t:
        sound()
        break
    else:
        continue
print("Thank you")

