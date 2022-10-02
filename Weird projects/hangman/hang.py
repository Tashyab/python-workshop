import random
import os
import time
import pygame
# pygame.init()
from pygame import mixer
# import getpass

def sound():
    mixer.init()
    mixer.music.load("tune.mp3")
    mixer.music.set_volume(0.5)
    mixer.music.play()
    input("Press enter key to stop.")
    mixer.music.stop()

def timer():
    t=5*60
    ti=time.time()
    while (True):
        tk=time.time()
        if tk-ti>=t:
            sound()
            break
        else:
            continue


def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

def comp():
    with open (r"C:\Users\Acer\3D Objects\Projects\python-workshop\hangman\words10.txt") as f:
        word_list=f.read().splitlines()
    word=random.choice(word_list).lower()
    return word

if __name__=="__main__":
    game_ch=int(input("Enter 1 to play against computer and 2 play against a friend: "))
    if game_ch==1:
        word=comp()
    else:
        # word=getpass.getpass(prompt="Enter the word or phrase to be guessed: ")
        word=input("Enter the word or phrase to be guessed: ")
        os.system('cls')
    word=word.strip()
    uw=word
    guessed=[]
    unlist=[ch for ch in word]
    lives=6
    for ch in unlist:
        if ch.isalpha()==True:
            uw=uw.replace(ch,"-")
    print("This is a word or phrase, start guessing, you will get 6 tries.")

    while(lives!=0) and ('-' in uw):
        print("The word or phrase looks like: " + uw)
        guess=input("\nEnter your guess:")
        if guess.isalpha()==True:
            guess=guess.lower()
            if guess not in guessed:
                if guess in word:
                    print("Correct guess")
                    guessed.append(guess)
                    oclist=find(word, guess)
                    for oc in oclist:
                        uw=uw[:oc]+guess+uw[oc+1:]
                    print(f"{lives} more guesses remains.\n")
                else:
                    print("Incorrect guess")
                    lives=lives-1
                    guessed.append(guess)
                    print(f"{lives} more guesses remains.\n")
            else:
                print("Already guessed this letter.\n")
        else:
            print("Not a valid letter.")
    if(lives==0):
        print("Sorry, you lost.")
    else:
        print("Congrats you win.")
    if " " in word:
        print(f"The correct phrase is {word}")
    else:
        print(f"The correct word is {word}")

