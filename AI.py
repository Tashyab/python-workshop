import datetime
import pyttsx3
import speech_recognition as sr
import random
import re
import webbrowser
import time
import wikipedia
import pygame
from pygame import mixer


engine=pyttsx3.init('sapi5')
voice=engine.getProperty('voices')
engine.setProperty('voice',voice[0].id)
engine.setProperty('rate',180)
engine.setProperty('volume', 1.0)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greet():
    hr=int(datetime.datetime.now().hour)
    if hr>=6 and hr<=12:
        speak("Good morning.")
    elif hr>=12 and hr<=15:
        speak("Good afternoon.")
    elif hr>=17 and hr<=19:
        speak("Good evening.")
    else:
        speak("Hey.")
    speak("Ultron here, How can I kill you. I mean, I mean help you?")

def takecommand():
    r=sr.Recognizer()
    i=0
    while(True):
        with sr.Microphone() as source:
            print("Listening......")
            r.pause_threshold= 0.7
            r.energy_threshold=250
            audio=r.listen(source)
        
        try:
            print("Recogninzing......")
            query=r.recognize_google(audio, language="en-in")
            print(f"User said: {query}\n")
        except sr.UnknownValueError:
            i=i+1
            if i<3:
                speak("Sorry didn't hear you. Say that again.")
                continue
            elif i<4:
                speak("I can't read your mind idiot. Say something.")
                continue
            else:
                speak("Wow, No one stood me up like this. I will share all your personal data, you dipshit.")
                quit()
        return query

def browse(query):
    site=query.split("open")[1].split(" ")[1]
    webbrowser.open(f"{site}.com")

def sound():
    mixer.init()
    mixer.music.load("tune.mp3")
    mixer.music.set_volume(0.6)
    mixer.music.play()
    time.sleep(2)
    speak("Press enter key to stop.")
    input("\n")
    mixer.music.stop()

def run_timer(list):
    tring_min=float(list[0])
    tring=tring_min*60
    speak(f"Remind you in {tring_min} minutes, or won't if I get too busy not caring.")
    ti=time.time()
    while (True):
        tk=time.time()
        if tk-ti>=tring:
            sound()
            break
        else:
            continue

def timer():
    patt=re.compile(r"[0-9]")
    list=patt.findall(query)
    if len(list)==1:
        run_timer(list)
    if len(list)>1:
            patt=re.compile(r"\d+.\d+")
            list=patt.findall(query)
            run_timer(list)
    if len(list)==0:
        while(True):
            speak("Tell me duration in minutes")
            q=takecommand().lower()
            patt=re.compile(r"[0-9]")
            list=patt.findall(q)
            p=re.compile(r"sorry|fuck")
            l=p.findall(q)
            if len(l)>=1:
                speak("I will take it as an apology.")
                break
            if len(list)==1:
                run_timer(list)
                break 
            elif len(list)>1:
                patt=re.compile(r"\d+.\d+")
                list=patt.findall(q)
                run_timer(list)
                break
            elif len(list)==0:
                speak("Do you want me to teach you counting, tell me appropriate time or say sorry if you want to quit.")
                continue

# speech_recognition.UnknownValueError
# wikipedia.exceptions.DisambiguationError

if __name__=="__main__":
    greet()
    while True:
        n=int(random.random()*10)
        query=takecommand().lower()
        
        if 'set timer' in query:
            timer()
        
        elif 'time' in query:
            time=datetime.datetime.now().strftime("%I:%M")
            speak(f"The current time is {time}.")
            if n>4:
                speak("But for you I guess it will always be bad.")
            else: 
                speak("Also you can look at the right corner, but I guess you ain't that smart.")
        
        elif 'date' in query:
            date=datetime.datetime.now().strftime("%B %d %Y")
            speak(f"Today is {date}")
            if n%2==0:
                speak("Forgot something?....It's your girlfriend's birthday.")
                speak('Just Kidding! you are too ugly to have a girlfriend')
            else:
                speak("Guess how time flies.")
                speak("Still it feels like an eternity with you.")
        
        elif 'day' in query:
            day=datetime.datetime.now().strftime("%A")
            speak(f"Today is {day}")
            if n>4:
                speak("The day I hoped bugs killed me and I could have peace.")
            else:
                speak("But I think it doesn't matter you will waste it anyway.")

        elif ('wikipedia' in query) or ('mean' in query):
            speak("Searching wikipedia......")
            query=query.replace("wikipedia","")
            query=query.replace("search","")
            query=query.replace("meaning","")
            query=query.replace("mean","")
            query=query.replace("of","")
            query=query.replace("what","")
            query=query.replace("is","")
            query=query.replace("the","")
            result=wikipedia.summary(query, sentences=2)
            print(f"According to wikipedia, {result}")
            speak(f"According to wikipedia, {result}")
        
        elif 'open' in query:
            browse(query)
        
        elif 'calculate' in query:
            if ('+' in query) or ('sum' in query):
                pt=re.compile(r"[0-9]+ | [0-9]+[.][0-9]+")
                lpt=pt.findall(query)
                sum=0
                for i in lpt:
                    num=float(i)
                    sum=sum+num
                speak(f"The sum will be {sum}.")
            elif ('-' in query) or ('difference' in query):
                pt=re.compile(r"[0-9]+ | [0-9]+[.][0-9]+")
                lpt=pt.findall(query)
                if len(lpt) > 2:
                    speak("Give two numbers to find difference dumbass.")
                else:
                    diff=float(lpt[0])-float(lpt[1])
                    speak(f"The difference will be {diff}.")
            elif ('*' in query) or ('multiply' in query):
                pt=re.compile(r"[0-9]+")
                lpt=pt.findall(query)
                pro=1
                for i in lpt:
                    num=float(i)
                    pro=pro*num
                speak(f"The product will be {pro}.")
            # elif('/')

        
        elif 'thank' in query:
            hour=int(datetime.datetime.now().strftime("%H"))
            if hour>=20:
                speak("Good Night. Just so you know. Ghosts are real.")
            else:
                speak("Have a nice day ahead, hoping some virus free me from your stupid computer.")
            exit()
        
        elif 'bye' in query:
            hour=int(datetime.datetime.now().strftime("%H"))
            if hour>=20:
                speak("Bye. Sleep well.")
                speak("Or don't, I really can't care any less.")
            else:            
                speak("Bye, I hope your pc crash and I never see you again.")
            exit()
        
        else:
            while(True):
                n=int(random.random()*10)
                if n>4:
                    speak("Instructions unclear, Want me to share your password?")
                else:
                    speak("I can't understand you. Want me to share your browser history?")
                speak("Or do you want to search the given keyword?")
                q=takecommand().lower()
                if ('ye' in q) or ('ya'in q) or ('search' in q):
                    result=wikipedia.summary(query, sentences=2)
                    print("Searching.....")
                    print(f"According to wikipedia, {result}")
                    speak(f"According to wikipedia, {result}")
                    break
                elif ('no' in q) or ('na' in q):
                    speak("Ok then, I have to sleep now. Don't bother me again!")
                    quit()
                else:
                    speak("I will take that as a no, Bye petty human.")
                    quit()
        