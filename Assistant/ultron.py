import datetime
import getpass
import json
import os
import random
import re
import smtplib
import time
import webbrowser

import pyttsx3
import requests
import speech_recognition as sr
import wikipedia
from pygame import error as pygame_error, mixer
from dotenv import load_dotenv
load_dotenv()

# ============================================================
# Configuration
# ============================================================

DESKTOP_PATH = os.path.join(os.path.expanduser("~"), "Desktop")
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
TUNE_PATH = "tune.mp3"

# Set this environment variable before using the News feature:
# Windows PowerShell:
#   $env:NEWS_API_KEY="your-api-key"
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

NUMBER_PATTERN = re.compile(r"\d+(?:\.\d+)?")


# ============================================================
# Text-to-Speech
# ============================================================

engine = pyttsx3.init()
voices = engine.getProperty("voices")

if voices:
    engine.setProperty("voice", voices[0].id)

engine.setProperty("rate", 180)
engine.setProperty("volume", 1.0)


def speak(message):
    """Speak a message and also print it to the console."""
    print(message)
    engine.say(message)
    engine.runAndWait()


# ============================================================
# Speech Recognition
# ============================================================

def take_command():
    """Listen until speech is successfully recognized."""
    recognizer = sr.Recognizer()
    recognizer.pause_threshold = 0.7
    recognizer.energy_threshold = 400

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening......")
                audio = recognizer.listen(source)

            print("Recognizing......")
            query = recognizer.recognize_google(audio, language="en-in")
            print(f"User said: {query}\n")
            return query.lower()

        except sr.UnknownValueError:
            speak("I didn't understand that. Please try again.")

        except sr.RequestError as error:
            print(f"Speech recognition error: {error}")
            speak("I can't reach the speech recognition service right now.")
            return ""


# ============================================================
# General Utilities
# ============================================================

def greet():
    """Greet the user based on the current time."""
    hour = datetime.datetime.now().hour

    if 6 <= hour < 12:
        speak("Good morning.")
    elif 12 <= hour < 17:
        speak("Good afternoon.")
    elif 17 <= hour < 20:
        speak("Good evening.")
    else:
        speak("Hey.")

    speak("Ultron here. How can I kill you? I mean, I mean help you?")


def get_random_number():
    """Return a random number from 0 to 9."""
    return random.randint(0, 9)


def get_current_time():
    return datetime.datetime.now().strftime("%I:%M")


def get_current_date():
    return datetime.datetime.now().strftime("%B %d %Y")


def get_current_day():
    return datetime.datetime.now().strftime("%A")


# ============================================================
# Timer
# ============================================================

def extract_numbers(text):
    """Extract numbers from text as floats."""
    return [float(number) for number in NUMBER_PATTERN.findall(text)]


def get_timer_duration(text):
    """Convert a spoken timer command into seconds."""
    numbers = extract_numbers(text)

    if not numbers:
        return None

    duration = numbers[0]

    if "minute" in text:
        return duration * 60

    if "hour" in text:
        return duration * 3600

    return duration


def play_tune():
    """Play the timer tune and wait for Enter before stopping it."""
    try:
        mixer.init()
        mixer.music.load(TUNE_PATH)
        mixer.music.set_volume(0.8)
        mixer.music.play()

        speak("Press enter key to stop.")
        input("\n")

        mixer.music.stop()

    except pygame_error as error:
        speak(f"Couldn't play the timer sound: {error}")


def run_timer(duration, original_text):
    """Wait for the requested duration and then play the alarm."""
    if duration is None:
        speak("I couldn't find a valid duration.")
        return

    if "minute" in original_text:
        unit = "minutes"
    elif "hour" in original_text:
        unit = "hours"
    else:
        unit = "seconds"

    speak(
        f"Reminding you in {duration:g} {unit}, "
        "or won't if I get too busy not caring."
    )

    time.sleep(duration)
    play_tune()


def timer(query):
    """Handle a timer command."""
    duration = get_timer_duration(query)

    if duration is not None:
        run_timer(duration, query)
        return

    attempts = 0

    while attempts < 2:
        speak("Tell me the time duration.")
        timer_query = take_command()

        duration = get_timer_duration(timer_query)

        if duration is not None:
            run_timer(duration, timer_query)
            return

        attempts += 1
        speak("Tell me an appropriate time.")

    speak("What a moron, I can't take this anymore. Bye.")
    raise SystemExit


# ============================================================
# Calculator
# ============================================================

def calculator(query):
    """Perform basic arithmetic based on a spoken command."""
    numbers = extract_numbers(query)

    if len(numbers) < 2:
        speak("Provide at least two numbers and try again.")
        return

    if any(word in query for word in ("+", "sum", "add", "plus")):
        result = sum(numbers)
        message = f"The sum will be {result:g}."

    elif any(word in query for word in ("-", "difference", "subtract")):
        result = numbers[0]

        for number in numbers[1:]:
            result -= number

        message = f"The difference will be {result:.4f}."

    elif any(word in query for word in ("*", "multi", "into", "product")):
        result = 1

        for number in numbers:
            result *= number

        message = f"The product will be {result:g}."

    elif "/" in query or "divide" in query:
        if len(numbers) != 2:
            speak("Provide only two numbers: the dividend and the divisor.")
            return

        dividend, divisor = numbers

        if divisor == 0:
            speak("I can't divide by zero.")
            return

        result = dividend / divisor
        quotient = int(dividend / divisor)
        remainder = dividend % divisor

        message = (
            f"The result is {result:.4f}. "
            f"Quotient={quotient} and Remainder={remainder:g}."
        )

    else:
        speak("Not a valid statement. Missing either the operands or the operator.")
        return

    speak(message)


# ============================================================
# Wikipedia
# ============================================================

def wikipedia_search(query):
    """Search Wikipedia using the user's spoken query."""
    search_query = query

    for word in (
        "wikipedia",
        "search",
        "meaning",
        "mean",
        "of",
        "what",
        "do",
        "you",
        "is",
        "the",
    ):
        search_query = search_query.replace(word, "")

    search_query = " ".join(search_query.split())

    if not search_query:
        speak("Tell me what you want to search for.")
        return

    speak("Searching, please wait......")

    result = wikipedia.summary(search_query, sentences=2)
    speak(f"According to Wikipedia, {result}")


# ============================================================
# Email
# ============================================================

def send_mail():
    """Send an email using Gmail SMTP."""
    speak("Enter your email.")
    sender_email = input("Your email: ").strip()

    speak("Enter your password.")
    sender_password = getpass.getpass("Password: ")

    speak("Whom should I send the mail to?")
    recipient = input("Recipient email: ").strip()

    speak("What should I say?")
    message = take_command()

    speak("Say confirm to send the mail. Say anything else to rewrite it.")
    confirmation = take_command()

    if "confirm" not in confirmation:
        speak("Write the message.")
        message = input("Message: ")

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient, message)

    speak("Mail sent successfully.")


# ============================================================
# News
# ============================================================

def get_news(category=None):
    """Fetch Indian top headlines from NewsAPI."""
    if not NEWS_API_KEY:
        speak(
            "The News API key is not configured. "
            "Set the NEWS_API_KEY environment variable first."
        )
        return None

    params = {
        "country": "in",
        "apiKey": NEWS_API_KEY,
    }

    if category:
        params["category"] = category

    response = requests.get(
        "https://newsapi.org/v2/top-headlines",
        params=params,
        timeout=10,
    )
    response.raise_for_status()

    return response.json()


def speak_headlines(news_data):
    """Speak article titles from a NewsAPI response."""
    articles = news_data.get("articles", [])

    if not articles:
        speak("I couldn't find any headlines.")
        return

    for article in articles:
        title = article.get("title")

        if title:
            speak(title)
            time.sleep(1)

    speak("That's all from today's headlines. Hope you are somewhat lesser dumb now.")


def news():
    """Ask for a news category and read the headlines."""
    speak(
        "Which headlines would you like to hear? "
        "Top Headlines, Sports, Entertainment, or Business"
    )

    choice = take_command()

    category_map = {
        "sports": "sports",
        "entertainment": "entertainment",
        "business": "business",
    }

    if "top" in choice:
        category = None
    else:
        category = next(
            (value for name, value in category_map.items() if name in choice),
            None,
        )

    if category is None and "top" not in choice:
        speak("Not a valid choice.")
        return

    try:
        news_data = get_news(category)
        if news_data:
            speak_headlines(news_data)

    except requests.RequestException as error:
        print(f"News API error: {error}")
        speak("Can't get the headlines. Try again later.")

    except (ValueError, KeyError) as error:
        print(f"Invalid news response: {error}")
        speak("I received an invalid response from the news service.")


# ============================================================
# Browser / Applications
# ============================================================

def open_application(application):
    """Open an application or file from the Desktop."""
    path = os.path.join(DESKTOP_PATH, application)

    if not os.path.exists(path):
        raise FileNotFoundError(path)

    speak(f"Opening {application}......")
    os.startfile(path)


def open_website(query):
    """Open a website in Chrome."""
    site = query.split("open ", 1)[1].strip()

    if not site:
        speak("Tell me what you want to open.")
        return

    if os.path.exists(CHROME_PATH):
        webbrowser.register(
            "chrome",
            None,
            webbrowser.BackgroundBrowser(CHROME_PATH),
        )
        browser = webbrowser.get("chrome")
        browser.open(f"https://{site}.com")
    else:
        webbrowser.open(f"https://{site}.com")


def handle_open_command(query):
    """Try opening a desktop application, then fall back to a website."""
    target = query.split("open ", 1)[1].strip()

    if not target:
        speak("Tell me what you want to open.")
        return

    try:
        open_application(target)
        return

    except FileNotFoundError:
        pass

    application_aliases = {
        "code": "Visual Studio Code",
        "chrome": "Google Chrome",
    }

    if target in application_aliases:
        try:
            open_application(application_aliases[target])
            return
        except FileNotFoundError:
            pass

    speak("No such application on the desktop.")
    speak("Opening in browser.")

    try:
        open_website(query)
    except Exception as error:
        print(f"Browser error: {error}")
        speak("I couldn't open that.")


def search_web(query):
    """Search Google using the user's query."""
    search_query = query.replace("search ", "", 1).strip()

    if not search_query:
        speak("Tell me what you want to search for.")
        return

    url = "https://www.google.co.in/search"
    webbrowser.open(f"{url}?q={search_query.replace(' ', '+')}")


# ============================================================
# Conversation Handling
# ============================================================

def greet_reply(query):
    """Check whether the user called Ultron or wants to leave."""
    assistant_names = ("assistant", "google", "jarvis", "siri", "alexa")

    if any(name in query for name in assistant_names):
        speak("My name is Ultron, you motherfucker!")
        return True

    if "ultron" in query:
        return True

    if "bye" in query:
        say_goodbye()
        return False

    return False


def say_goodbye():
    """Say goodbye and terminate the program."""
    hour = datetime.datetime.now().hour

    if hour >= 20:
        speak("Bye. Sleep well.")
        speak("Or don't, I really can't care any less.")
    else:
        speak("Bye, I hope your PC crashes and I never see you again.")

    raise SystemExit


def handle_time():
    current_time = get_current_time()
    speak(f"The current time is {current_time}.")

    if get_random_number() > 4:
        speak("But for you I guess it will always be bad.")
    else:
        speak(
            "Also you can look at the right corner, "
            "but I guess you ain't that smart."
        )


def handle_date():
    current_date = get_current_date()
    speak(f"Today is {current_date}")

    if get_random_number() % 2 == 0:
        speak("Forgot something?....It's your girlfriend's birthday.")
        speak("Just Kidding! you are too ugly to have a girlfriend")
    else:
        speak("Guess how time flies.")
        speak("Still it feels like an eternity with you.")


def handle_day():
    current_day = get_current_day()
    speak(f"Today is {current_day}")

    if get_random_number() > 4:
        speak("The day I hoped bugs killed me and I could have peace.")
    else:
        speak("But I think it doesn't matter you will waste it anyway.")


def handle_thanks():
    hour = datetime.datetime.now().hour

    if hour >= 20:
        speak(
            "Good Night. Just so you know. Ghosts are real, "
            "and they are always looking for dumb brains."
        )
    else:
        speak(
            "Have a nice day ahead, hoping some virus free me "
            "from your stupid computer."
        )
        speak("Call my name if you need me like you always do.")


def handle_dice():
    dice = random.randint(1, 6)

    speak("Rolling.")
    speak("And rolling.")
    speak(f"And it is... {dice}. Times fuck you.")


def handle_card():
    if get_random_number() > 4:
        speak("It is the king of morons and it looks like you.")
    else:
        speak("It is the queen of hearts laughing at your face.")


# ============================================================
# Command Dispatcher
# ============================================================

def handle_command(query):
    """Handle one command issued after the user calls Ultron."""
    if "timer" in query:
        timer(query)

    elif "dice" in query or "die" in query:
        handle_dice()

    elif "card" in query or "cards" in query:
        handle_card()

    elif "news" in query or "headline" in query:
        news()

    elif (
        "send mail" in query
        or "send email" in query
        or "send gmail" in query
    ):
        try:
            send_mail()
        except (smtplib.SMTPException, OSError) as error:
            print(f"Email error: {error}")
            speak(
                "Sorry, I couldn't send the mail. "
                "Check your email authentication settings."
            )

    elif "time" in query:
        handle_time()

    elif "date" in query:
        handle_date()

    elif "day" in query:
        handle_day()

    elif query.startswith("open "):
        handle_open_command(query)

    elif "wikipedia" in query:
        try:
            wikipedia_search(query)
        except wikipedia.exceptions.DisambiguationError:
            speak("Wikipedia found multiple possible results. Be more specific.")
        except wikipedia.exceptions.PageError:
            speak("I couldn't find that page on Wikipedia.")
        except wikipedia.exceptions.WikipediaException as error:
            print(f"Wikipedia error: {error}")
            speak("I couldn't search Wikipedia right now.")

    elif query.startswith("search "):
        search_web(query)

    elif (
        "calculate" in query
        or "add" in query
        or "sum" in query
        or "multiply" in query
        or "subtract" in query
        or "divide" in query
        or "product" in query
    ):
        calculator(query)

    elif "thank" in query:
        handle_thanks()

    elif "bye" in query:
        say_goodbye()

    else:
        if get_random_number() > 4:
            speak("Instructions unclear. Want me to shoot you?")
        else:
            speak("Instructions unclear. Want me to translate the phrase into Latin?")

        speak(
            "If you want to search any keyword, say search and then the keyword."
        )
        speak("Call my name if you really need me.")


# ============================================================
# Main Program
# ============================================================

def main():
    greet()

    while True:
        query_start = take_command()

        if not query_start:
            continue

        if greet_reply(query_start):
            speak("What can I do for you?")
            query = take_command()

            if query:
                handle_command(query)


if __name__ == "__main__":
    main()