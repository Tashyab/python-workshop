import datetime
import pyttsx3
import speech_recognition as sr

engine=pyttsx3.init('sapi5')
voice=engine.getProperty('voices')
engine.setProperty('voice',voice[1].id)
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
    speak("Friday here, How can I assist you?")

def takecommand():
    reco=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        reco.pause_threshold=0.7
        reco.energy_threshold=400
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
    while True:
        query=takecommand().lower()

        if 'what time' in query:
            time=datetime.datetime.now().strftime("%I:%M")
            print(time)
            speak(f"The current time is {time}.")
        
        elif 'what date' in query:
            date=datetime.datetime.now().strftime("%B %d, %Y")
            print(date)
            speak(f"Today's date is {date}.")
        
        elif 'Thank you' in query:
            speak("Happy to help.")
            exit()
        