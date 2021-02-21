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
import math
import os
import smtplib
import json
import requests as req
import pickle

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
                speak("Ok, the next time you see some unwanted cringy ads, remember me.")
                quit()
        return query

def filestarter(key):
    path=f"C:\\Users\\VIP\\Desktop\\{key}"
    speak(f"Opening {key}....")
    print(f"Opening {key}....\n")
    os.startfile(path)
    exit()

def sound():
    mixer.init()
    mixer.music.load("tune.mp3")
    mixer.music.set_volume(0.6)
    mixer.music.play()
    time.sleep(2)
    speak("Press enter key to stop.")
    input("\n")
    mixer.music.stop()

def run_timer(list, q):
    tring_time=float(list[0])
    if ('minute' in query) or ('minute' in q):
        tring=tring_time*60
        speak(f"Remind you in {tring_time} minutes, or won't if I get too busy not caring.")
    elif ('second' in query) or ('second' in q):
        tring=tring_time
        speak(f"Remind you in {tring_time} seconds, or won't if I get too busy not caring.")
    elif ('hour' in query) or ('hour' in q):
        tring=tring_time*3600
        speak(f"Remind you in {tring_time} hours, or won't if I get too busy not caring.")
    else:
        speak("Standard time unit not provided. Setting timer in seconds.")
        tring=tring_time
        speak(f"Remind you in {tring_time} seconds, or won't if I get too busy not caring.")
    ti=time.time()
    while (True):
        tk=time.time()
        if tk-ti>=tring:
            sound()
            break
        else:
            continue

def timer():
    patt=re.compile(r"[0-9]+")
    list=patt.findall(query)
    if len(list)==1:
        run_timer(list, "")
    if len(list)>1:
            patt=re.compile(r"\d+.\d+")
            list=patt.findall(query)
            run_timer(list, "")
    if len(list)==0:
        i=0
        while(True):
            speak("Tell me time duration.")
            q=takecommand().lower()
            patt=re.compile(r"[0-9]+")
            list=patt.findall(q)
            if len(list)==1:
                run_timer(list, q)
                break 
            elif len(list)>1:
                patt=re.compile(r"\d+.\d+")
                list=patt.findall(q)
                run_timer(list, q)
                break
            elif len(list)==0:
                i=i+1
                if (i==2):
                    speak("What a moron, I am quitting.")
                    quit()
                else:
                    speak("Tell me appropriate time.")
                    continue
                
def calculator():
    if ('+' in query) or ('sum' in query) or ('add' in query):
        pt=re.compile(r"[0-9]+[.][0-9]+|[0-9]+")
        lpt=pt.findall(query)
        sum=0
        for i in lpt:
            num=float(i)
            sum=sum+num
        speak(f"The sum will be {sum}.")
        print(f"The sum will be {sum}.")
    
    elif ('-' in query) or ('difference' in query) or ('subtract' in query):
        pt=re.compile(r"[0-9]+[.][0-9]+|[0-9]+")
        lpt=pt.findall(query)
        diff=0
        if len(lpt)>1:
            for i in lpt:
                num=float(i)
                diff=diff-num
            diff=diff+(2*float(lpt[0]))
            diff=round(diff,4)
            speak(f"The difference will be {diff}.")
            print(f"The difference will be {diff}.")
        else:
            speak("Provide at least two numbers and try again.")

        
    elif ('*' in query) or ('multi' in query) or ('into' in query):
        pt=re.compile(r"[0-9]+[.][0-9]+|[0-9]+")
        lpt=pt.findall(query)
        pro=1
        if len(lpt)>1:
            for i in lpt:
                num=float(i)
                pro=pro*num
            speak(f"The product will be {pro}.")
            print(f"The product will be {pro}.")
        else:
            speak("Provide at least two numbers and try again.")
    elif ('/' in query) or ('divide' in query):
        pt=re.compile(r"[0-9]+[.][0-9]+|[0-9]+")
        lpt=pt.findall(query)
        if len(lpt)==2:
            div=(float(lpt[0]))/(float(lpt[1]))
            div=round(div,4)
            quo=int((float(lpt[0]))/(float(lpt[1])))
            rem=int((float(lpt[0]))%(float(lpt[1])))
            speak(f"The result is {div}.\nQuotient={quo} and Remainder={rem}.")
            print(f"The result is {div}.\nQuotient={quo} and Remainder={rem}.")  
        else:
            speak("Provide only two numbers, The dividend and the divisor.")
    else:
        speak("Not a valid statement. Missing either the operands or the operator.")

def wiki(query):
    speak("Searching, please wait......")
    query=query.replace("wikipedia","")
    query=query.replace("search","")
    query=query.replace("meaning","")
    query=query.replace("mean","")
    query=query.replace("of","")
    query=query.replace("what","")
    query=query.replace("do","")
    query=query.replace("you","")
    query=query.replace("is","")
    query=query.replace("the","")
    result=wikipedia.summary(query, sentences=2)
    print(f"According to wikipedia, {result}")
    speak(f"According to wikipedia, {result}")        

def sendmail():
    speak("Enter your email")
    print("Before entering your email make sure to allow less secure to apps use your account.\n"
    "| Go to your account > Security > Toggle to allow less secue apps |")
    print("Enter your email:")
    sender_email=input()
    speak("Enter your password")
    print("Enter your password:")
    sender_password=input()
    speak("Whom to send the mail, Tell me the email address.")
    print("Sender's email address:")
    to=input()
    while(True):
        speak("What should I say?")
        cont=takecommand()
        speak("Say confirm to send the mail, anything else to write the message.")
        call=takecommand().lower()
        if "confirm" in call:
            break
        else:
            speak("Write the message.")
            print("Write the message.")
            cont=input()
            break
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, to, cont)
    server.close()

def start(pr):
    i = 0
    while (i < len(pr['articles'])):
        for key in [*pr['articles'][i]]:
            if key == 'title':
                print(pr['articles'][i]['title'])
                speak(pr['articles'][i]['title'])
                time.sleep(1)
        i += 1
    speak("That's all from today's headlines. Hope your knowledge of current affairs improves.")

def news(query):
    speak("Which headlines would you like to hear? Top Headlines, Sports, Entertainment, or Business")
    q=takecommand().lower()
    try:
        if "top" in q:
            r=req.get("http://newsapi.org/v2/top-headlines?country=in&apiKey=aff4be3b07634fe2ab1da4f0e0db241f")
            pr=json.loads(r.text)
            start(pr)
        elif "sports" in q:
            r = req.get("http://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=aff4be3b07634fe2ab1da4f0e0db241f")
            pr = json.loads(r.text)
            start(pr)
        elif 'entertainment' in q:
            r = req.get("http://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=aff4be3b07634fe2ab1da4f0e0db241f")
            pr = json.loads(r.text)
            start(pr)
        elif 'business' in q:
            r = req.get("http://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=aff4be3b07634fe2ab1da4f0e0db241f")
            pr = json.loads(r.text)
            start(pr)
        else:
            speak("Not a valid choice.")
    except Exception:
        speak("Can't get the headlines, try again later.")

# speech_recognition.UnknownValueError
# wikipedia.exceptions.DisambiguationError

if __name__=="__main__":
    greet()
    while True:
        n=int(random.random()*10)
        query=takecommand().lower()
        
        if 'set timer' in query:
            timer()
        
        elif ('news' in query) or ('headline' in query):
            news(query)
      
        elif ('send mail' in query) or ('send email' in query) or ('send gmail' in query):
            try:
                sendmail()
                speak("Mail sent successfully.")  
            except Exception:
                speak("Sorry can't send the mail.")

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

        elif 'open' in query:
            try:
                q=query.split("open ")[1]
                filestarter(q)
            except Exception:
                speak("No such application on desktop. Opening manually.")
                if 'code blocks' in query:
                    filestarter("codeblocks")
                elif ('python' in query):
                    filestarter("Pycharm")
                elif 'code' in query:
                    filestarter("Visual Studio Code")
                elif 'chrome' in query:
                    filestarter("Chrome")
                else:
                    try:
                        speak("Opening in browser") 
                        site=query.split("open ")[1]
                        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"))
                        webbrowser.get('chrome').open(f"{site}.com")
                        exit()
                    except Exception:
                        speak("I can't open blank, you dumb person. Tell me what to open.")
                        speak("Or I will open the profile you usually stalk. Yeah. I know everything.")
        
        elif ('wikipedia' in query):
            try:
                wiki(query)        
            except Exception:
                speak("Can't find this on wikipedia right now. Try again later.")

        elif 'search' in query:
            query=query.replace("search ", "")
            query=query.replace(" ","+")
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"))
            webbrowser.get('chrome').open(f"https://www.google.co.in/search?q={query}")
            exit()
                           
        elif ('calculate' in query) or ('add' in query) or ('sum' in query) or ('multiply' in query) or ('subtract' in query) or ('divide' in query):
            calculator()

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
                speak("Bye, I hope your pc crashes and I never see you again.")
            exit()
        
        else:
            if n>4:
                speak("Instructions unclear, Want me to share your password?")
            else:
                speak("I can't understand you. Want me to share your browser history?")
            speak("Or If you want to search the given keyword? Say search.")
            q=takecommand().lower()
            if ('ye' in q) or ('ya'in q):
                speak("Sharing browser history and passwords to global server. Thank me later.")
                exit()
            elif 'search' in q:
                query=query.replace("search", "")
                query=query.replace(" ","+")
                webbrowser.register('chrome', None, webbrowser.BackgroundBrowser("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"))
                webbrowser.get('chrome').open(f"https://www.google.co.in/search?q={query}")
                exit()
            elif ('no' in q) or ('na' in q):
                speak("Ok then, I have to sleep now. Don't bother me again!")
                exit()
            else:
                speak("I will take that as a no, you petty human.")
                quit()
        