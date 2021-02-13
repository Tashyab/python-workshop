import datetime
import pyttsx3
import speech_recognition as sr
import random

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
    speak("Ultron here, How can I assist you?")

def takecommand():
    reco=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        reco.pause_threshold=0.7
        reco.energy_threshold=250
        audio=reco.listen(source)
    
    try:
        print("Recognizing.....")
        query=reco.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    
    except Exception:
        print("Say that again.....")
        return "None"
    return query

if __name__=="__main__":
    greet()
    n=int(random.random()*10)
    while True:
        query=takecommand().lower()

        if 'time' in query:
            time=datetime.datetime.now().strftime("%I:%M")
            speak(f"The current time is {time}.")
            if n>4:
                speak("But for you I guess it will always be bad.")
            else: 
                speak("Also you can look at the right corner, but I guess you ain't that smart.")
        
        elif 'date' in query:
            date=datetime.datetime.now().strftime("%B %d %Y")
            speak(f"Today is {date}")
            if n==0 or n==9:
                speak("Forgot something?....It's your girlfriend's birthday.")
                speak('Just Kidding! you are too ugly to have a girlfriend')
            else:
                speak("Guess how time flies.")
                speak("Still I feels like an eternity with you.")
        
        elif 'day' in query:
            day=datetime.datetime.now().strftime("%A")
            speak(f"Today is {day}")
            if n>4:
                speak("The day I hoped bugs killed me.")
            else:
                speak("But I think it doesn't matter you will waste it anyway.")

        elif 'thanks' in query:
            if n>4:
                speak("Bye, I hope your pc crash and I never see you again.")
            else:
                speak("Have a nice day, hope some virus free me from your stupid computer.")
            exit()



        